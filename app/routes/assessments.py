"""Question-bank browser and server-timed mock assessments using reviewed local questions."""
from datetime import datetime, timezone
import random
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_required, current_user
from ..extensions import db
from ..models import QuizAttempt
from ..content.mastery_questions import QUESTIONS, BY_KEY

assessments_bp = Blueprint("assessments", __name__)


def _question_view(question):
    return {key: question[key] for key in ("key", "unit", "concept", "title", "q", "choices", "explanation")}


@assessments_bp.get("/question-bank")
def question_bank():
    unit = request.args.get("unit", type=int)
    query = request.args.get("q", "").strip().lower()[:100]
    selected = [q for q in QUESTIONS if (not unit or q["unit"] == unit)]
    if query:
        selected = [q for q in selected if query in q["title"].lower() or query in q["q"].lower() or query in q["concept"].lower()]
    return render_template("assessments/question_bank.html", questions=selected, unit=unit, query=query,
                           total=len(QUESTIONS), unit_counts={n: sum(1 for q in QUESTIONS if q["unit"] == n) for n in range(1, 6)})


@assessments_bp.get("/mock")
@login_required
def mock_landing():
    attempts = QuizAttempt.query.filter_by(user_id=current_user.id).order_by(QuizAttempt.created_at.desc()).limit(10).all()
    return render_template("assessments/mock_landing.html", attempts=attempts,
                           available=len(QUESTIONS))


@assessments_bp.post("/mock/start")
@login_required
def mock_start():
    unit = request.form.get("unit", "all")
    duration = request.form.get("duration", type=int) or 20
    count = request.form.get("count", type=int) or 10
    if duration not in {10, 20, 30, 45, 60} or count not in {5, 10, 15, 20}:
        abort(400)
    pool = [q for q in QUESTIONS if unit == "all" or str(q["unit"]) == unit]
    if not pool:
        flash("No questions are available for that selection yet.", "warning")
        return redirect(url_for("assessments.mock_landing"))
    rng = random.SystemRandom()
    chosen = rng.sample(pool, min(count, len(pool)))
    session["mock_exam"] = {"keys": [q["key"] for q in chosen],
                            "started_at": datetime.now(timezone.utc).timestamp(),
                            "duration_seconds": duration * 60, "unit": int(unit) if unit != "all" else 0}
    return redirect(url_for("assessments.mock_exam"))


@assessments_bp.get("/mock/take")
@login_required
def mock_exam():
    exam = session.get("mock_exam")
    if not exam:
        return redirect(url_for("assessments.mock_landing"))
    elapsed = max(0, datetime.now(timezone.utc).timestamp() - exam["started_at"])
    remaining = max(0, int(exam["duration_seconds"] - elapsed))
    if remaining <= 0:
        flash("The exam timer has expired. Submit to record the attempt.", "warning")
    questions = [_question_view(BY_KEY[key]) for key in exam["keys"] if key in BY_KEY]
    return render_template("assessments/mock_exam.html", questions=questions, remaining=remaining)


@assessments_bp.post("/mock/submit")
@login_required
def mock_submit():
    exam = session.get("mock_exam")
    if not exam:
        abort(400)
    elapsed = max(0, datetime.now(timezone.utc).timestamp() - exam["started_at"])
    answers = request.form
    questions = [BY_KEY[key] for key in exam["keys"] if key in BY_KEY]
    correct = sum(1 for q in questions if answers.get(q["key"], "") == str(q["answer"]))
    timed_out = elapsed > exam["duration_seconds"]
    # A late submission is scored but explicitly marked as over time in the result.
    attempt = QuizAttempt(user_id=current_user.id, unit_number=exam["unit"], score=correct, total=len(questions))
    db.session.add(attempt)
    db.session.commit()
    result = {"score": correct, "total": len(questions), "timed_out": timed_out,
              "elapsed_seconds": int(elapsed),
              "answers": [{"question": q["q"], "choices": q["choices"], "selected": answers.get(q["key"], ""),
                           "correct": q["answer"], "is_correct": answers.get(q["key"], "") == str(q["answer"]),
                           "explanation": q["explanation"]} for q in questions]}
    session.pop("mock_exam", None)
    session["last_mock_result"] = result
    return redirect(url_for("assessments.mock_result"))


@assessments_bp.get("/mock/result")
@login_required
def mock_result():
    result = session.get("last_mock_result")
    if not result:
        return redirect(url_for("assessments.mock_landing"))
    return render_template("assessments/mock_result.html", result=result)
