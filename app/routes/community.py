"""Phase 18: small-group collaboration, announcements, shared revision and peer challenges."""
import json
import secrets
import string
from datetime import datetime, timezone

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy import desc

from ..extensions import db
from ..models import (GroupAnnouncement, GroupDiscussionPost, PeerQuizChallenge,
                      SharedRevisionList, StudyGroup, StudyGroupMember, Topic)

community_bp = Blueprint("community", __name__)


def _member(group_id):
    group = db.session.get(StudyGroup, group_id) or abort(404)
    membership = StudyGroupMember.query.filter_by(group_id=group.id, user_id=current_user.id).first()
    if not membership:
        abort(403)
    return group, membership


def _new_join_code():
    alphabet = string.ascii_uppercase + string.digits
    for _ in range(8):
        code = "".join(secrets.choice(alphabet) for _ in range(8))
        if not StudyGroup.query.filter_by(join_code=code).first():
            return code
    raise RuntimeError("Could not allocate a unique group code")


@community_bp.get("/")
@login_required
def index():
    memberships = StudyGroupMember.query.filter_by(user_id=current_user.id).all()
    group_ids = [row.group_id for row in memberships]
    groups = StudyGroup.query.filter(StudyGroup.id.in_(group_ids)).order_by(StudyGroup.name).all() if group_ids else []
    return render_template("community/index.html", groups=groups)


@community_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_group():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        if not 3 <= len(name) <= 100 or len(description) > 1000:
            flash("Enter a group name (3–100 characters) and a description under 1,000 characters.", "warning")
            return render_template("community/create.html"), 400
        group = StudyGroup(name=name, description=description, join_code=_new_join_code(), owner_id=current_user.id)
        db.session.add(group)
        db.session.flush()
        db.session.add(StudyGroupMember(group_id=group.id, user_id=current_user.id, role="owner"))
        db.session.commit()
        flash("Study group created. Share its join code only with people you want to invite.", "success")
        return redirect(url_for("community.detail", group_id=group.id))
    return render_template("community/create.html")


@community_bp.route("/join", methods=["POST"])
@login_required
def join_group():
    code = request.form.get("join_code", "").strip().upper()
    group = StudyGroup.query.filter_by(join_code=code).first() if code else None
    if not group:
        flash("That join code was not found.", "warning")
        return redirect(url_for("community.index"))
    existing = StudyGroupMember.query.filter_by(group_id=group.id, user_id=current_user.id).first()
    if not existing:
        db.session.add(StudyGroupMember(group_id=group.id, user_id=current_user.id, role="member"))
        db.session.commit()
    flash("You are now a member of the study group.", "success")
    return redirect(url_for("community.detail", group_id=group.id))


@community_bp.get("/<int:group_id>")
@login_required
def detail(group_id):
    group, membership = _member(group_id)
    posts = GroupDiscussionPost.query.filter_by(group_id=group.id, status="visible").order_by(desc(GroupDiscussionPost.created_at)).limit(100).all()
    announcements = GroupAnnouncement.query.filter_by(group_id=group.id).order_by(desc(GroupAnnouncement.created_at)).limit(30).all()
    shared_lists = SharedRevisionList.query.filter_by(group_id=group.id).order_by(desc(SharedRevisionList.created_at)).all()
    challenges = PeerQuizChallenge.query.filter_by(group_id=group.id).order_by(desc(PeerQuizChallenge.created_at)).all()
    member_count = StudyGroupMember.query.filter_by(group_id=group.id).count()
    return render_template("community/detail.html", group=group, membership=membership, posts=posts,
                           announcements=announcements, shared_lists=shared_lists, challenges=challenges,
                           member_count=member_count, topics=Topic.query.order_by(Topic.unit_number, Topic.title).all(),
                           now=datetime.now(timezone.utc))


@community_bp.post("/<int:group_id>/leave")
@login_required
def leave_group(group_id):
    group, membership = _member(group_id)
    if membership.role == "owner":
        flash("The group owner cannot leave before transferring ownership. You can keep managing the group here.", "warning")
    else:
        db.session.delete(membership)
        db.session.commit()
        flash("You have left the study group.", "info")
        return redirect(url_for("community.index"))
    return redirect(url_for("community.detail", group_id=group.id))


@community_bp.post("/<int:group_id>/posts")
@login_required
def create_post(group_id):
    group, _ = _member(group_id)
    body = request.form.get("body", "").strip()
    if not 2 <= len(body) <= 3000:
        flash("Discussion posts must be between 2 and 3,000 characters.", "warning")
    else:
        db.session.add(GroupDiscussionPost(group_id=group.id, author_id=current_user.id, body=body))
        db.session.commit()
        flash("Discussion post added.", "success")
    return redirect(url_for("community.detail", group_id=group.id) + "#discussion")


@community_bp.post("/<int:group_id>/posts/<int:post_id>/moderate")
@login_required
def moderate_post(group_id, post_id):
    group, membership = _member(group_id)
    post = db.session.get(GroupDiscussionPost, post_id) or abort(404)
    if post.group_id != group.id:
        abort(404)
    if membership.role != "owner" and post.author_id != current_user.id:
        abort(403)
    action = request.form.get("action", "")
    if action not in {"hide", "restore", "delete"}:
        abort(400)
    if action == "delete":
        db.session.delete(post)
    else:
        post.status = "hidden" if action == "hide" else "visible"
    db.session.commit()
    flash("Discussion post updated.", "success")
    return redirect(url_for("community.detail", group_id=group.id) + "#discussion")


@community_bp.post("/<int:group_id>/announcements")
@login_required
def create_announcement(group_id):
    group, membership = _member(group_id)
    if membership.role != "owner":
        abort(403)
    title = request.form.get("title", "").strip()
    body = request.form.get("body", "").strip()
    if not 3 <= len(title) <= 140 or not 2 <= len(body) <= 3000:
        flash("Provide a title (3–140 characters) and announcement text (2–3,000 characters).", "warning")
    else:
        db.session.add(GroupAnnouncement(group_id=group.id, author_id=current_user.id, title=title, body=body))
        db.session.commit()
        flash("Announcement published to group members.", "success")
    return redirect(url_for("community.detail", group_id=group.id) + "#announcements")


@community_bp.post("/<int:group_id>/revision-lists")
@login_required
def create_revision_list(group_id):
    group, _ = _member(group_id)
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    raw_ids = request.form.getlist("topic_ids")
    if not 3 <= len(title) <= 120 or len(description) > 500 or len(raw_ids) > 69:
        flash("Check the revision-list title, description and topic selection.", "warning")
        return redirect(url_for("community.detail", group_id=group.id) + "#revision-lists")
    try:
        topic_ids = sorted({int(value) for value in raw_ids})
    except ValueError:
        abort(400)
    valid_ids = {row[0] for row in db.session.query(Topic.id).filter(Topic.id.in_(topic_ids)).all()} if topic_ids else set()
    if valid_ids != set(topic_ids):
        abort(400)
    db.session.add(SharedRevisionList(group_id=group.id, creator_id=current_user.id, title=title,
                                      description=description, topic_ids_json=json.dumps(topic_ids)))
    db.session.commit()
    flash("Shared revision list created.", "success")
    return redirect(url_for("community.detail", group_id=group.id) + "#revision-lists")


@community_bp.post("/<int:group_id>/challenges")
@login_required
def create_challenge(group_id):
    group, _ = _member(group_id)
    title = request.form.get("title", "").strip()
    unit_number = request.form.get("unit_number", type=int) or 0
    question_count = request.form.get("question_count", type=int) or 5
    if not 3 <= len(title) <= 120 or unit_number not in range(0, 6) or question_count not in {5, 10, 15, 20}:
        flash("Choose a title, valid unit and a challenge length of 5, 10, 15 or 20 questions.", "warning")
    else:
        db.session.add(PeerQuizChallenge(group_id=group.id, creator_id=current_user.id, title=title,
                                         unit_number=unit_number, question_count=question_count))
        db.session.commit()
        flash("Peer challenge created. Members can use it as a shared practice target.", "success")
    return redirect(url_for("community.detail", group_id=group.id) + "#challenges")
