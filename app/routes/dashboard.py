from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models import Topic, TopicProgress, Bookmark, PersonalNote, QuizAttempt, StudyPlan

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.get("/")
@login_required
def index():
    topics = Topic.query.order_by(Topic.unit_number, Topic.id).all()
    progress = TopicProgress.query.filter_by(user_id=current_user.id).all()
    status_map = {p.topic_id: p.status for p in progress}
    total = len(topics)
    completed = sum(1 for t in topics if status_map.get(t.id) == "completed")
    in_progress = sum(1 for t in topics if status_map.get(t.id) == "in_progress")
    unit_stats = []
    for unit_number in range(1, 6):
        unit_topics = [t for t in topics if t.unit_number == unit_number]
        unit_done = sum(1 for t in unit_topics if status_map.get(t.id) == "completed")
        unit_stats.append({
            "number": unit_number,
            "title": unit_topics[0].unit_title if unit_topics else f"Unit {unit_number}",
            "total": len(unit_topics), "completed": unit_done,
            "percent": round(unit_done / len(unit_topics) * 100) if unit_topics else 0
        })
    bookmarked = Bookmark.query.filter_by(user_id=current_user.id).all()
    bookmark_topics = [b.topic for b in bookmarked]
    recent = sorted(progress, key=lambda p: p.updated_at or p.id, reverse=True)[:6]
    attempts = QuizAttempt.query.filter_by(user_id=current_user.id).order_by(QuizAttempt.created_at.desc()).limit(5).all()
    active_plan = StudyPlan.query.filter_by(user_id=current_user.id, active=True).order_by(StudyPlan.created_at.desc()).first()
    today_tasks = [task for task in active_plan.tasks if task.scheduled_date.isoformat() == __import__("datetime").date.today().isoformat()] if active_plan else []
    return render_template("dashboard/index.html", active_plan=active_plan, today_tasks=today_tasks, total=total, completed=completed,
        in_progress=in_progress, remaining=total-completed, percent=round(completed/total*100) if total else 0,
        unit_stats=unit_stats, bookmark_topics=bookmark_topics, recent=recent, attempts=attempts)
