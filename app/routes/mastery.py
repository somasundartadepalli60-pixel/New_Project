from datetime import datetime, timezone
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_required, current_user
from sqlalchemy import desc
from ..extensions import db
from ..models import ConceptMastery, MasteryResponse, Topic, ReviewSchedule, LearningPreference
from ..content.mastery_questions import QUESTIONS, BY_KEY
from ..services.mastery_engine import update_mastery, recommendation_for
from ..services.spaced_repetition import schedule_next_review, RATINGS

mastery_bp = Blueprint("mastery", __name__)

def _now():
    return datetime.now(timezone.utc)

def _record_for(question):
    record = ConceptMastery.query.filter_by(user_id=current_user.id, concept_key=question["concept"]).first()
    if record is None:
        topic = Topic.query.filter_by(slug=question["concept"]).first()
        record = ConceptMastery(
            user_id=current_user.id, concept_key=question["concept"],
            concept_title=topic.title if topic else question["title"],
            unit_number=question["unit"], attempts=0, correct_count=0,
            consecutive_correct=0, mastery_score=0, last_seen_at=_now(), next_review_at=_now()
        )
        db.session.add(record)
        db.session.flush()
    return record

@mastery_bp.get("/")
@login_required
def index():
    records = ConceptMastery.query.filter_by(user_id=current_user.id).order_by(ConceptMastery.mastery_score.asc()).all()
    by_key = {record.concept_key: record for record in records}
    summaries = []
    for question in QUESTIONS:
        record = by_key.get(question["concept"])
        if record and any(item["concept"] == question["concept"] for item in QUESTIONS):
            if not any(item["concept_key"] == question["concept"] for item in summaries):
                recommendation = recommendation_for(record) if record else {"label":"Start here","reason":"No practice evidence has been recorded yet.","priority":1}
                summaries.append({"concept_key":question["concept"], "title":record.concept_title if record else question["title"], "unit":question["unit"], "attempts":record.attempts if record else 0, "score":record.mastery_score if record else 0, "accuracy":record.accuracy if record else 0, "recommendation":recommendation})
        elif not any(item["concept_key"] == question["concept"] for item in summaries):
            summaries.append({"concept_key":question["concept"], "title":question["title"], "unit":question["unit"], "attempts":0, "score":0, "accuracy":0, "recommendation":{"label":"Start here","reason":"No practice evidence has been recorded yet.","priority":1}})
    summaries.sort(key=lambda item:(item["recommendation"]["priority"], item["score"], item["unit"]))
    mistakes = MasteryResponse.query.filter_by(user_id=current_user.id, is_correct=False, reviewed=False).order_by(desc(MasteryResponse.created_at)).limit(10).all()
    overall_attempts = sum(record.attempts for record in records)
    overall_correct = sum(record.correct_count for record in records)
    overall_accuracy = round(overall_correct / overall_attempts * 100) if overall_attempts else 0
    return render_template("mastery/index.html", summaries=summaries, mistakes=mistakes, overall_attempts=overall_attempts, overall_accuracy=overall_accuracy)



def _revision_rank(question, records, now):
    """Rank a question for revision using only the learner's recorded evidence."""
    record = records.get(question["concept"])
    if record is None or record.attempts == 0:
        return (0, 0, question["unit"], question["key"])
    next_review = record.next_review_at
    if next_review is not None and next_review.tzinfo is None:
        next_review = next_review.replace(tzinfo=timezone.utc)
    due = next_review is None or next_review <= now
    # Due concepts come first, then weak mastery, then healthy concepts due later.
    if due:
        return (1, record.mastery_score, question["unit"], question["key"])
    return (2, record.mastery_score, question["unit"], question["key"])

@mastery_bp.get("/revision")
@login_required
def revision():
    """Show a transparent queue of concepts due or recommended for revision."""
    now = _now()
    records = {r.concept_key: r for r in ConceptMastery.query.filter_by(user_id=current_user.id).all()}
    queue = []
    seen = set()
    for question in sorted(QUESTIONS, key=lambda q: _revision_rank(q, records, now)):
        concept = question["concept"]
        if concept in seen:
            continue
        seen.add(concept)
        record = records.get(concept)
        next_review = record.next_review_at if record else None
        if next_review is not None and next_review.tzinfo is None:
            next_review = next_review.replace(tzinfo=timezone.utc)
        due = record is None or record.attempts == 0 or next_review is None or next_review <= now
        if record is None or record.attempts == 0:
            label, reason = "Not practised", "Start with a baseline question so the app can personalise later reviews."
        elif record.mastery_score < 55:
            label, reason = "Needs reinforcement", "Your recorded mastery score is below 55%; revisit the lesson and practise again."
        elif due:
            label, reason = "Due now", "The scheduled spaced-review date has arrived."
        else:
            label, reason = "Upcoming", "This concept is not due yet, but it can be included in mixed practice."
        queue.append({"question": question, "record": record, "label": label, "reason": reason, "due": due})
    due_count = sum(1 for item in queue if item["due"])
    open_mistakes = MasteryResponse.query.filter_by(user_id=current_user.id, is_correct=False, reviewed=False).count()
    recent = MasteryResponse.query.filter_by(user_id=current_user.id).order_by(desc(MasteryResponse.created_at)).limit(20).all()
    recent_accuracy = round(sum(1 for r in recent if r.is_correct) / len(recent) * 100) if recent else 0
    return render_template("mastery/revision.html", queue=queue, due_count=due_count,
                           open_mistakes=open_mistakes, recent_count=len(recent),
                           recent_accuracy=recent_accuracy)

@mastery_bp.post("/revision/start")
@login_required
def start_revision():
    now = _now()
    records = {r.concept_key: r for r in ConceptMastery.query.filter_by(user_id=current_user.id).all()}
    ranked = sorted(QUESTIONS, key=lambda q: _revision_rank(q, records, now))
    selected, concepts = [], set()
    # A short, mixed-unit set prioritises due/weak/unseen concepts and avoids repeats.
    for question in ranked:
        if question["concept"] in concepts:
            continue
        selected.append(question)
        concepts.add(question["concept"])
        if len(selected) >= 5:
            break
    session["mastery_question_keys"] = [q["key"] for q in selected]
    session["mastery_session_mode"] = "revision"
    return render_template("mastery/session.html", questions=selected, revision_mode=True)

@mastery_bp.post("/start")
@login_required
def start():
    # Prioritize weaker concepts, while rotating among the bank to avoid one fixed test.
    records = {record.concept_key: record for record in ConceptMastery.query.filter_by(user_id=current_user.id).all()}
    def rank(question):
        record = records.get(question["concept"])
        if record is None or record.attempts == 0:
            return (0, 0, question["key"])
        return (1, record.mastery_score, question["key"])
    # First choose one low-evidence concept from each unit, then fill any remaining
    # slots with the weakest distinct concepts. This keeps the short session mixed-unit.
    chosen = []
    used_concepts = set()
    for unit_number in range(1, 6):
        candidates = sorted((q for q in QUESTIONS if q["unit"] == unit_number), key=rank)
        candidate = next((q for q in candidates if q["concept"] not in used_concepts), None)
        if candidate is not None:
            chosen.append(candidate)
            used_concepts.add(candidate["concept"])
    if len(chosen) < 5:
        for question in sorted(QUESTIONS, key=rank):
            if question["concept"] not in used_concepts:
                chosen.append(question)
                used_concepts.add(question["concept"])
            if len(chosen) == 5:
                break
    chosen = chosen[:5]
    session["mastery_question_keys"] = [item["key"] for item in chosen]
    return render_template("mastery/session.html", questions=chosen)

@mastery_bp.post("/submit")
@login_required
def submit():
    keys = session.pop("mastery_question_keys", [])
    if not keys:
        flash("Start a mastery session before submitting answers.", "error")
        return redirect(url_for("mastery.index"))
    questions = [BY_KEY[key] for key in keys if key in BY_KEY]
    results = []
    score = 0
    for index, question in enumerate(questions):
        raw = request.form.get(f"q{index}", "")
        try:
            selected = int(raw)
        except (TypeError, ValueError):
            selected = -1
        if selected < -1 or selected >= len(question["choices"]):
            selected = -1
        is_correct = selected == question["answer"]
        if is_correct:
            score += 1
        record = _record_for(question)
        update_mastery(record, is_correct, _now())
        response = MasteryResponse(
            user_id=current_user.id, question_key=question["key"],
            concept_key=question["concept"], unit_number=question["unit"],
            selected_index=selected, correct_index=question["answer"],
            is_correct=is_correct,
            selected_text=question["choices"][selected] if selected >= 0 else "Not answered",
            misconception="" if is_correct else question["misconception"],
            explanation=question["explanation"], reviewed=False
        )
        db.session.add(response)
        results.append({"question":question, "selected":selected, "correct":is_correct, "response":response})
    db.session.commit()
    return render_template("mastery/results.html", results=results, score=score, total=len(questions))

@mastery_bp.post("/review/<int:response_id>")
@login_required
def mark_reviewed(response_id):
    response = MasteryResponse.query.filter_by(id=response_id, user_id=current_user.id).first_or_404()
    response.reviewed = True
    db.session.commit()
    flash("Mistake marked as reviewed.", "success")
    return redirect(url_for("mastery.index"))


@mastery_bp.get("/flashcards")
@login_required
def flashcards():
    """Show due and new lesson-derived cards with explicit source content."""
    now = _now()
    all_topics = Topic.query.order_by(Topic.unit_number, Topic.title).all()
    schedules = {item.topic_id: item for item in ReviewSchedule.query.filter_by(user_id=current_user.id).all()}
    preference = LearningPreference.query.filter_by(user_id=current_user.id).first()
    preferred_unit = preference.preferred_unit if preference else 0

    def card_rank(topic):
        schedule = schedules.get(topic.id)
        if schedule is None:
            rank = (0, 0)
        else:
            due_at = schedule.due_at
            if due_at and due_at.tzinfo is None:
                due_at = due_at.replace(tzinfo=timezone.utc)
            rank = (1 if due_at and due_at <= now else 2, due_at.timestamp() if due_at else 0)
        return (0 if preferred_unit and topic.unit_number == preferred_unit else 1, *rank, topic.unit_number, topic.title.lower())

    ordered = sorted(all_topics, key=card_rank)
    due_topic_ids = {topic.id for topic in all_topics if topic.id not in schedules or _as_utc(schedules[topic.id].due_at) <= now}
    due_count = len(due_topic_ids)
    return render_template("mastery/flashcards.html", topics=ordered, schedules=schedules,
                           due_count=due_count, due_topic_ids=due_topic_ids, now=now, preference=preference)

def _as_utc(value):
    if value is None:
        return None
    return value.replace(tzinfo=timezone.utc) if value.tzinfo is None else value

@mastery_bp.post("/flashcards/<int:topic_id>/grade")
@login_required
def grade_flashcard(topic_id):
    topic = Topic.query.filter_by(id=topic_id).first_or_404()
    rating = request.form.get("rating", "")
    if rating not in RATINGS:
        abort(400, description="Choose Again, Hard, Good, or Easy.")
    schedule = ReviewSchedule.query.filter_by(user_id=current_user.id, topic_id=topic.id).first()
    if schedule is None:
        schedule = ReviewSchedule(user_id=current_user.id, topic_id=topic.id)
        db.session.add(schedule)
        db.session.flush()
    decision = schedule_next_review(rating, schedule.repetitions, schedule.interval_days,
                                    schedule.ease_factor, _now())
    schedule.repetitions = decision.repetitions
    schedule.interval_days = decision.interval_days
    schedule.ease_factor = decision.ease_factor
    schedule.due_at = decision.due_at
    schedule.last_rating = rating
    schedule.review_count += 1
    db.session.commit()
    flash(f"{topic.title}: {decision.message} Next review in {decision.interval_days} day(s).", "success")
    return redirect(url_for("mastery.flashcards"))

@mastery_bp.route("/preferences", methods=["GET", "POST"])
@login_required
def learning_preferences():
    preference = LearningPreference.query.filter_by(user_id=current_user.id).first()
    if preference is None:
        preference = LearningPreference(user_id=current_user.id)
        db.session.add(preference)
        db.session.commit()
    if request.method == "POST":
        try:
            daily_goal = int(request.form.get("daily_goal_minutes", "30"))
            session_minutes = int(request.form.get("preferred_session_minutes", "15"))
            preferred_unit = int(request.form.get("preferred_unit", "0"))
        except (TypeError, ValueError):
            flash("Enter valid numeric study preferences.", "error")
            return redirect(url_for("mastery.learning_preferences"))
        if not 5 <= daily_goal <= 480 or not 5 <= session_minutes <= 120 or preferred_unit not in range(0, 6):
            flash("Daily goal must be 5–480 minutes, session length 5–120 minutes, and unit 0–5.", "error")
            return redirect(url_for("mastery.learning_preferences"))
        reminder_style = request.form.get("reminder_style", "gentle")
        if reminder_style not in {"gentle", "focused", "minimal"}:
            reminder_style = "gentle"
        preference.daily_goal_minutes = daily_goal
        preference.preferred_session_minutes = session_minutes
        preference.preferred_unit = preferred_unit
        preference.reminder_style = reminder_style
        db.session.commit()
        flash("Your study preferences have been saved.", "success")
        return redirect(url_for("mastery.flashcards"))
    return render_template("mastery/preferences.html", preference=preference)
