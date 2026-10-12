"""Learner-facing analytics derived from the user's own recorded activity."""
from collections import defaultdict
from datetime import datetime, timedelta, timezone
import csv
import io

from flask import Blueprint, Response, render_template
from flask_login import current_user, login_required
from sqlalchemy import desc

from ..models import ConceptMastery, MasteryResponse, QuizAttempt, ReviewSchedule, TopicProgress

analytics_bp = Blueprint("analytics", __name__)


def _aware(value):
    if value is not None and value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value


def _snapshot(user_id):
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=27)
    responses = (MasteryResponse.query.filter_by(user_id=user_id)
                 .filter(MasteryResponse.created_at >= start)
                 .order_by(MasteryResponse.created_at.asc()).all())
    mastery = ConceptMastery.query.filter_by(user_id=user_id).all()
    schedules = ReviewSchedule.query.filter_by(user_id=user_id).all()
    progress = TopicProgress.query.filter_by(user_id=user_id).all()
    attempts = QuizAttempt.query.filter_by(user_id=user_id).order_by(desc(QuizAttempt.created_at)).limit(30).all()

    # Fixed 4-week buckets make the trend comparable even on quiet days.
    weeks = []
    for offset in (3, 2, 1, 0):
        begin = (now - timedelta(days=(offset + 1) * 7)).date()
        finish = (now - timedelta(days=offset * 7)).date()
        bucket = [r for r in responses if begin <= _aware(r.created_at).date() < finish]
        weeks.append({"label": begin.strftime("%d %b"), "attempts": len(bucket),
                      "accuracy": round(sum(r.is_correct for r in bucket) / len(bucket) * 100) if bucket else None})

    by_unit = defaultdict(lambda: {"concepts": 0, "attempts": 0, "correct": 0, "mastery_total": 0.0})
    for record in mastery:
        row = by_unit[record.unit_number]
        row["concepts"] += 1
        row["attempts"] += record.attempts
        row["correct"] += record.correct_count
        row["mastery_total"] += record.mastery_score
    units = []
    for unit in sorted(by_unit):
        row = by_unit[unit]
        units.append({"unit": unit, "concepts": row["concepts"], "attempts": row["attempts"],
                      "accuracy": round(row["correct"] / row["attempts"] * 100) if row["attempts"] else 0,
                      "mastery": round(row["mastery_total"] / row["concepts"]) if row["concepts"] else 0})

    due = sum(1 for item in schedules if _aware(item.due_at) <= now)
    recent = responses[-50:]
    total_answers = sum(r.attempts for r in mastery)
    total_correct = sum(r.correct_count for r in mastery)
    topics_started = sum(1 for item in progress if item.status != "not_started")
    avg_mastery = round(sum(item.mastery_score for item in mastery) / len(mastery)) if mastery else 0
    return {
        "weeks": weeks, "units": units, "mastery": sorted(mastery, key=lambda item: (item.mastery_score, item.concept_title)),
        "attempts": total_answers, "accuracy": round(total_correct / total_answers * 100) if total_answers else 0,
        "avg_mastery": avg_mastery, "tracked_concepts": len(mastery), "topics_started": topics_started,
        "due_reviews": due, "recent_count": len(recent),
        "recent_accuracy": round(sum(r.is_correct for r in recent) / len(recent) * 100) if recent else 0,
        "quiz_attempts": attempts,
    }


@analytics_bp.get("/")
@login_required
def index():
    return render_template("analytics/index.html", data=_snapshot(current_user.id))


@analytics_bp.get("/export.csv")
@login_required
def export_csv():
    data = _snapshot(current_user.id)
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow(["LDICA Learning Analytics"])
    writer.writerow(["Metric", "Value"])
    writer.writerow(["Total practice attempts", data["attempts"]])
    writer.writerow(["Overall accuracy percent", data["accuracy"]])
    writer.writerow(["Average recorded mastery percent", data["avg_mastery"]])
    writer.writerow(["Tracked concepts", data["tracked_concepts"]])
    writer.writerow(["Topics started", data["topics_started"]])
    writer.writerow(["Reviews due", data["due_reviews"]])
    writer.writerow([])
    writer.writerow(["Unit", "Tracked concepts", "Attempts", "Accuracy percent", "Average mastery percent"])
    for row in data["units"]:
        writer.writerow([row["unit"], row["concepts"], row["attempts"], row["accuracy"], row["mastery"]])
    writer.writerow([])
    writer.writerow(["Concept", "Unit", "Attempts", "Accuracy percent", "Mastery percent", "Next review UTC"])
    for item in data["mastery"]:
        due = _aware(item.next_review_at).isoformat() if item.next_review_at else ""
        writer.writerow([item.concept_title, item.unit_number, item.attempts, item.accuracy, round(item.mastery_score), due])
    return Response("\ufeff" + output.getvalue(), mimetype="text/csv; charset=utf-8",
                    headers={"Content-Disposition": "attachment; filename=ldica-learning-analytics.csv"})
