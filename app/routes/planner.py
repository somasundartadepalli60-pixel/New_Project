from datetime import date, datetime, timedelta
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..extensions import db
from ..models import Topic, TopicProgress, StudyPlan, StudyTask
from ..content.lesson_bank import lesson_detail

planner_bp = Blueprint("planner", __name__)
DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def estimate_minutes(topic, pace):
    """Estimate time from topic complexity and title cues; estimates are editable planning aids."""
    base = 35
    title = topic.title.lower()
    if any(word in title for word in ("introduction", "applications", "features", "characteristics", "types")):
        base = 25
    if any(word in title for word in ("analysis", "architecture", "instrumentation", "successive", "differential", "butterworth")):
        base = 45
    if any(word in title for word in ("dac", "adc", "amplifier", "counter", "flip-flop", "filter", "integrator", "differentiator")):
        base = max(base, 40)
    return {"quick": max(15, round(base * .65)), "balanced": base, "deep": round(base * 1.65)}.get(pace, base)

def build_schedule(topics, start, deadline, daily_minutes, days, pace, completed_ids):
    eligible_days = []
    cursor = start
    while cursor <= deadline:
        if cursor.weekday() in days:
            eligible_days.append(cursor)
        cursor += timedelta(days=1)
    slots = []
    for day in eligible_days:
        remaining = daily_minutes
        while remaining >= 15:
            slots.append((day, remaining))
            break
    ordered = [t for t in topics if t.id not in completed_ids]
    tasks = []
    day_remaining = {day: daily_minutes for day in eligible_days}
    for topic in ordered:
        duration = estimate_minutes(topic, pace)
        # Split long lessons into manageable sessions when necessary.
        parts = []
        while duration > 0:
            part = min(duration, daily_minutes)
            if part < 15 and parts:
                parts[-1] += part
                break
            parts.append(part)
            duration -= part
        for part in parts:
            selected_day = next((d for d in eligible_days if day_remaining[d] >= part), None)
            if selected_day is None:
                selected_day = min(eligible_days, key=lambda d: day_remaining[d], default=None)
                if selected_day is None:
                    return tasks, eligible_days, len(ordered)
                # Over-capacity is shown clearly instead of silently promising impossible hours.
                day_remaining[selected_day] -= part
            else:
                day_remaining[selected_day] -= part
            tasks.append({"topic": topic, "date": selected_day, "minutes": part, "sequence": len(tasks)+1})
    over_capacity = sum(max(0, -minutes) for minutes in day_remaining.values())
    return tasks, eligible_days, over_capacity

@planner_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    today = date.today()
    active = StudyPlan.query.filter_by(user_id=current_user.id, active=True).order_by(StudyPlan.created_at.desc()).first()
    topics = Topic.query.order_by(Topic.unit_number, Topic.id).all()
    progress = TopicProgress.query.filter_by(user_id=current_user.id, status="completed").all()
    completed_ids = {p.topic_id for p in progress}
    errors = []
    if request.method == "POST":
        try:
            start = date.fromisoformat(request.form.get("start_date", ""))
            deadline = date.fromisoformat(request.form.get("deadline", ""))
            daily_minutes = int(request.form.get("daily_minutes", "120"))
            pace = request.form.get("pace", "balanced")
            days = sorted({int(x) for x in request.form.getlist("days") if x.isdigit() and 0 <= int(x) <= 6})
            if start < today:
                errors.append("The start date cannot be in the past.")
            if deadline < start:
                errors.append("The deadline must be on or after the start date.")
            if not 15 <= daily_minutes <= 720:
                errors.append("Daily study time must be between 15 minutes and 12 hours.")
            if not days:
                errors.append("Choose at least one available day.")
            if pace not in {"quick", "balanced", "deep"}:
                errors.append("Choose a valid learning pace.")
            if (deadline - start).days > 366:
                errors.append("Choose a deadline within the next year.")
        except (ValueError, TypeError):
            errors.append("Enter valid start and deadline dates and a valid daily study time.")
        if not errors:
            tasks, study_days, over_capacity = build_schedule(topics, start, deadline, daily_minutes, days, pace, completed_ids)
            StudyPlan.query.filter_by(user_id=current_user.id, active=True).update({"active": False})
            plan = StudyPlan(user_id=current_user.id, title="My LDICA study plan", start_date=start,
                             deadline=deadline, daily_minutes=daily_minutes, available_days=days, pace=pace, active=True)
            db.session.add(plan)
            db.session.flush()
            for item in tasks:
                db.session.add(StudyTask(plan_id=plan.id, topic_id=item["topic"].id, scheduled_date=item["date"],
                                         estimated_minutes=item["minutes"], sequence_number=item["sequence"]))
            db.session.commit()
            flash(f"Study plan created with {len(tasks)} learning sessions.", "success")
            if over_capacity:
                flash("Your deadline is tighter than the available study time. The plan flags an overloaded schedule; consider adding hours or extending the deadline.", "info")
            return redirect(url_for("planner.index"))
    tasks_by_date = {}
    if active:
        for task in active.tasks:
            tasks_by_date.setdefault(task.scheduled_date, []).append(task)
    planned_total = sum(t.estimated_minutes for t in active.tasks) if active else 0
    available_total = 0
    if active:
        cursor = active.start_date
        while cursor <= active.deadline:
            if cursor.weekday() in (active.available_days or []):
                available_total += active.daily_minutes
            cursor += timedelta(days=1)
    return render_template("planner/index.html", active=active, tasks_by_date=tasks_by_date,
                           days=DAY_NAMES, today=today, errors=errors, topic_count=len(topics),
                           completed_count=len(completed_ids), planned_total=planned_total,
                           available_total=available_total, pace_names={"quick":"Quick review","balanced":"Balanced","deep":"Deep learning"})

@planner_bp.post("/task/<int:task_id>/complete")
@login_required
def complete_task(task_id):
    task = StudyTask.query.join(StudyPlan).filter(StudyTask.id == task_id, StudyPlan.user_id == current_user.id).first_or_404()
    task.status = "completed"
    progress = TopicProgress.query.filter_by(user_id=current_user.id, topic_id=task.topic_id).first()
    if not progress:
        progress = TopicProgress(user_id=current_user.id, topic_id=task.topic_id, status="in_progress")
        db.session.add(progress)
    db.session.commit()
    flash("Study session marked complete. Update the lesson status when you have mastered the topic.", "success")
    return redirect(url_for("planner.index"))

@planner_bp.post("/deactivate")
@login_required
def deactivate():
    StudyPlan.query.filter_by(user_id=current_user.id, active=True).update({"active": False})
    db.session.commit()
    flash("Your active study plan has been paused.", "info")
    return redirect(url_for("planner.index"))


@planner_bp.get("/pack/<date_text>")
@login_required
def daily_pack(date_text):
    """Assemble a date-specific lesson bundle from the user's saved schedule."""
    try:
        selected_date = date.fromisoformat(date_text)
    except ValueError:
        return redirect(url_for("planner.index"))
    plan = StudyPlan.query.filter_by(user_id=current_user.id, active=True).order_by(StudyPlan.created_at.desc()).first()
    tasks = [task for task in plan.tasks if task.scheduled_date == selected_date] if plan else []
    lessons = [{"task": task, "detail": lesson_detail(task.topic)} for task in tasks]
    return render_template("planner/pack.html", plan=plan, selected_date=selected_date, lessons=lessons)

@planner_bp.get("/calendar.ics")
@login_required
def calendar_export():
    """Export the active plan as a standard iCalendar file for local calendar apps."""
    from flask import Response
    plan = StudyPlan.query.filter_by(user_id=current_user.id, active=True).order_by(StudyPlan.created_at.desc()).first()
    if not plan:
        flash("Create an active study plan before exporting a calendar.", "info")
        return redirect(url_for("planner.index"))
    def escape(value):
        return str(value).replace("\\\\", "\\\\\\\\").replace(";", "\\\\;").replace(",", "\\\\,").replace("\\n", "\\\\n")
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//LDICA Master Learning Hub//Study Plan//EN", "CALSCALE:GREGORIAN"]
    for task in plan.tasks:
        start = task.scheduled_date.strftime("%Y%m%d")
        end = (task.scheduled_date + timedelta(days=1)).strftime("%Y%m%d")
        lines.extend(["BEGIN:VEVENT", f"UID:ldica-task-{task.id}@local", f"DTSTART;VALUE=DATE:{start}",
                      f"DTEND;VALUE=DATE:{end}", f"SUMMARY:{escape(task.topic.title)}",
                      f"DESCRIPTION:{escape(f'Unit {task.topic.unit_number}; estimated {task.estimated_minutes} minutes. Open the LDICA learning hub to study this topic.')}",
                      "END:VEVENT"])
    lines.append("END:VCALENDAR")
    return Response("\\r\\n".join(lines) + "\\r\\n", mimetype="text/calendar",
                    headers={"Content-Disposition": "attachment; filename=ldica-study-plan.ics"})
