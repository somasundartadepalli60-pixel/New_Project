from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from flask_login import current_user, login_required
from ..extensions import db
from ..models import Topic, TopicProgress, Bookmark, PersonalNote
from ..content.lesson_bank import lesson_detail

learning_bp = Blueprint("learning", __name__)

@learning_bp.get("/")
def list_topics():
    query = request.args.get("q", "").strip()
    unit = request.args.get("unit", type=int)
    topics_query = Topic.query
    if query:
        like = f"%{query}%"
        topics_query = topics_query.filter(db.or_(Topic.title.ilike(like), Topic.summary.ilike(like), Topic.explanation.ilike(like)))
    if unit:
        topics_query = topics_query.filter_by(unit_number=unit)
    topics = topics_query.order_by(Topic.unit_number, Topic.id).all()
    statuses = {}
    if current_user.is_authenticated:
        statuses = {p.topic_id: p.status for p in TopicProgress.query.filter_by(user_id=current_user.id).all()}
    return render_template("lessons/list.html", topics=topics, statuses=statuses, query=query, unit=unit)

@learning_bp.get("/<slug>")
def lesson(slug):
    topic = Topic.query.filter_by(slug=slug).first_or_404()
    status = "not_started"
    bookmarked = False
    note = ""
    if current_user.is_authenticated:
        p = TopicProgress.query.filter_by(user_id=current_user.id, topic_id=topic.id).first()
        status = p.status if p else "not_started"
        bookmarked = Bookmark.query.filter_by(user_id=current_user.id, topic_id=topic.id).first() is not None
        n = PersonalNote.query.filter_by(user_id=current_user.id, topic_id=topic.id).first()
        note = n.body if n else ""
    related = Topic.query.filter_by(unit_number=topic.unit_number).order_by(Topic.id).all()
    idx = next((i for i, item in enumerate(related) if item.id == topic.id), 0)
    previous_topic = related[idx-1] if idx > 0 else None
    next_topic = related[idx+1] if idx+1 < len(related) else None
    detail = lesson_detail(topic)
    return render_template("lessons/detail.html", topic=topic, detail=detail, status=status, bookmarked=bookmarked,
                           note=note, previous_topic=previous_topic, next_topic=next_topic)

@learning_bp.post("/<slug>/progress")
@login_required
def update_progress(slug):
    topic = Topic.query.filter_by(slug=slug).first_or_404()
    status = request.form.get("status")
    if status not in {"not_started", "in_progress", "completed"}:
        abort(400)
    progress = TopicProgress.query.filter_by(user_id=current_user.id, topic_id=topic.id).first()
    if not progress:
        progress = TopicProgress(user_id=current_user.id, topic_id=topic.id)
        db.session.add(progress)
    progress.status = status
    db.session.commit()
    flash("Topic progress updated.", "success")
    return redirect(url_for("learning.lesson", slug=slug))

@learning_bp.post("/<slug>/bookmark")
@login_required
def toggle_bookmark(slug):
    topic = Topic.query.filter_by(slug=slug).first_or_404()
    bookmark = Bookmark.query.filter_by(user_id=current_user.id, topic_id=topic.id).first()
    if bookmark:
        db.session.delete(bookmark)
        flash("Bookmark removed.", "info")
    else:
        db.session.add(Bookmark(user_id=current_user.id, topic_id=topic.id))
        flash("Topic bookmarked.", "success")
    db.session.commit()
    return redirect(url_for("learning.lesson", slug=slug))

@learning_bp.post("/<slug>/note")
@login_required
def save_note(slug):
    topic = Topic.query.filter_by(slug=slug).first_or_404()
    body = request.form.get("body", "").strip()
    if len(body) > 10000:
        flash("Notes must be 10,000 characters or fewer.", "error")
        return redirect(url_for("learning.lesson", slug=slug))
    note = PersonalNote.query.filter_by(user_id=current_user.id, topic_id=topic.id).first()
    if note is None:
        note = PersonalNote(user_id=current_user.id, topic_id=topic.id)
        db.session.add(note)
    note.body = body
    db.session.commit()
    flash("Your note was saved.", "success")
    return redirect(url_for("learning.lesson", slug=slug))
