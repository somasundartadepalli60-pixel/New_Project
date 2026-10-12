"""Phase 17: course, syllabus, outcomes, terms and content approval workflow."""
import os
from datetime import date, datetime, timezone

from flask import Blueprint, abort, current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy import func

from ..extensions import db
from ..models import AcademicCourse, AcademicTerm, ContentReview, LearningOutcome, OutcomeTopicMap, Topic

academic_bp = Blueprint("academic", __name__)
BLOOM_LEVELS = ("Remember", "Understand", "Apply", "Analyse", "Evaluate", "Create")
COURSE_STATUSES = ("draft", "published", "archived")
COVERAGE_LEVELS = ("introduced", "practised", "assessed", "mastered")
REVIEW_STATUSES = ("approved", "changes_requested", "rejected")


def is_academic_admin():
    """Use an explicitly configured admin email; registration never grants admin access."""
    configured = (current_app.config.get("LDICA_ADMIN_EMAIL") or os.environ.get("LDICA_ADMIN_EMAIL") or "").strip().lower()
    return bool(configured and current_user.is_authenticated and current_user.email.lower() == configured)


def require_admin():
    if not is_academic_admin():
        abort(403)


@academic_bp.get("/")
@login_required
def index():
    course_query = AcademicCourse.query
    if not is_academic_admin():
        course_query = course_query.filter_by(status="published")
    courses = course_query.order_by(AcademicCourse.title).all()
    pending_count = ContentReview.query.filter_by(status="pending").count()
    outcome_count = LearningOutcome.query.count()
    mapped_count = OutcomeTopicMap.query.count()
    return render_template("academic/index.html", courses=courses, is_admin=is_academic_admin(),
                           pending_count=pending_count, outcome_count=outcome_count, mapped_count=mapped_count,
                           statuses=COURSE_STATUSES)


@academic_bp.route("/courses/create", methods=["GET", "POST"])
@login_required
def create_course():
    require_admin()
    if request.method == "POST":
        code = request.form.get("code", "").strip().upper()
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        syllabus_version = request.form.get("syllabus_version", "R23").strip()[:40]
        academic_year = request.form.get("academic_year", "").strip()[:20]
        if not (2 <= len(code) <= 30 and 4 <= len(title) <= 180):
            flash("Enter a course code (2–30 characters) and title (4–180 characters).", "warning")
            return render_template("academic/course_form.html"), 400
        if AcademicCourse.query.filter(func.lower(AcademicCourse.code) == code.lower()).first():
            flash("That course code already exists.", "warning")
            return render_template("academic/course_form.html"), 409
        if len(description) > 5000:
            abort(400)
        course = AcademicCourse(code=code, title=title, description=description,
                                syllabus_version=syllabus_version or "Unspecified", academic_year=academic_year,
                                created_by=current_user.id)
        db.session.add(course)
        db.session.commit()
        flash("Course created as a draft. Add outcomes and topic mappings before publishing.", "success")
        return redirect(url_for("academic.course_detail", course_id=course.id))
    return render_template("academic/course_form.html")


@academic_bp.get("/courses/<int:course_id>")
@login_required
def course_detail(course_id):
    course = db.session.get(AcademicCourse, course_id) or abort(404)
    if course.status != "published" and not is_academic_admin():
        abort(404)
    topics = Topic.query.order_by(Topic.unit_number, Topic.title).all()
    terms = list(course.terms)
    outcomes = list(course.outcomes)
    mapping_count = sum(len(outcome.topic_links) for outcome in outcomes)
    return render_template("academic/course_detail.html", course=course, topics=topics, terms=terms,
                           outcomes=outcomes, mapping_count=mapping_count, is_admin=is_academic_admin(),
                           bloom_levels=BLOOM_LEVELS, coverage_levels=COVERAGE_LEVELS)


@academic_bp.post("/courses/<int:course_id>/status")
@login_required
def update_course_status(course_id):
    require_admin()
    course = db.session.get(AcademicCourse, course_id) or abort(404)
    status = request.form.get("status", "")
    if status not in COURSE_STATUSES:
        abort(400)
    if status == "published" and not course.outcomes:
        flash("Add at least one learning outcome before publishing this course.", "warning")
        return redirect(url_for("academic.course_detail", course_id=course.id))
    course.status = status
    course.updated_at = datetime.now(timezone.utc)
    db.session.commit()
    flash(f"Course status updated to {status}.", "success")
    return redirect(url_for("academic.course_detail", course_id=course.id))


@academic_bp.post("/courses/<int:course_id>/terms")
@login_required
def create_term(course_id):
    require_admin()
    course = db.session.get(AcademicCourse, course_id) or abort(404)
    name = request.form.get("name", "").strip()
    try:
        start_date = date.fromisoformat(request.form.get("start_date", ""))
        end_date = date.fromisoformat(request.form.get("end_date", ""))
    except ValueError:
        abort(400)
    if not 2 <= len(name) <= 80 or end_date < start_date:
        flash("Provide a term name and an end date on or after the start date.", "warning")
        return redirect(url_for("academic.course_detail", course_id=course.id))
    db.session.add(AcademicTerm(course_id=course.id, name=name, start_date=start_date, end_date=end_date))
    db.session.commit()
    flash("Academic term added.", "success")
    return redirect(url_for("academic.course_detail", course_id=course.id))


@academic_bp.post("/courses/<int:course_id>/outcomes")
@login_required
def create_outcome(course_id):
    require_admin()
    course = db.session.get(AcademicCourse, course_id) or abort(404)
    code = request.form.get("code", "").strip().upper()
    statement = request.form.get("statement", "").strip()
    bloom_level = request.form.get("bloom_level", "Understand")
    method = request.form.get("assessment_method", "Quiz / examination").strip()[:100]
    if not 1 <= len(code) <= 30 or not 10 <= len(statement) <= 500 or bloom_level not in BLOOM_LEVELS:
        flash("Check the outcome code, statement and Bloom level.", "warning")
        return redirect(url_for("academic.course_detail", course_id=course.id))
    if LearningOutcome.query.filter_by(course_id=course.id, code=code).first():
        flash("That outcome code already exists in this course.", "warning")
        return redirect(url_for("academic.course_detail", course_id=course.id))
    db.session.add(LearningOutcome(course_id=course.id, code=code, statement=statement,
                                   bloom_level=bloom_level, assessment_method=method))
    db.session.commit()
    flash("Learning outcome added.", "success")
    return redirect(url_for("academic.course_detail", course_id=course.id))


@academic_bp.post("/outcomes/<int:outcome_id>/map")
@login_required
def map_outcome(outcome_id):
    require_admin()
    outcome = db.session.get(LearningOutcome, outcome_id) or abort(404)
    topic_id = request.form.get("topic_id", type=int)
    coverage = request.form.get("coverage_level", "introduced")
    notes = request.form.get("notes", "").strip()
    topic = db.session.get(Topic, topic_id) if topic_id else None
    if not topic or coverage not in COVERAGE_LEVELS or len(notes) > 500:
        abort(400)
    if OutcomeTopicMap.query.filter_by(outcome_id=outcome.id, topic_id=topic.id).first():
        flash("This topic is already mapped to that outcome.", "info")
    else:
        db.session.add(OutcomeTopicMap(outcome_id=outcome.id, topic_id=topic.id,
                                       coverage_level=coverage, notes=notes))
        db.session.commit()
        flash("Topic mapped to learning outcome.", "success")
    return redirect(url_for("academic.course_detail", course_id=outcome.course_id))


@academic_bp.route("/content-review", methods=["GET", "POST"])
@login_required
def content_review():
    if request.method == "POST":
        topic_id = request.form.get("topic_id", type=int)
        topic = db.session.get(Topic, topic_id) if topic_id else None
        summary = request.form.get("change_summary", "").strip()
        proposed = request.form.get("proposed_content", "").strip()
        if not topic or not 8 <= len(summary) <= 240 or not 20 <= len(proposed) <= 12000:
            flash("Choose a topic and provide a change summary and proposed content.", "warning")
            return redirect(url_for("academic.content_review"))
        review = ContentReview(topic_id=topic.id, submitted_by=current_user.id,
                               change_summary=summary, proposed_content=proposed)
        db.session.add(review)
        db.session.commit()
        flash("Content proposal submitted for review. The published lesson has not been changed.", "success")
        return redirect(url_for("academic.content_review"))
    query = ContentReview.query
    if not is_academic_admin():
        query = query.filter_by(submitted_by=current_user.id)
    reviews = query.order_by(ContentReview.created_at.desc()).limit(100).all()
    topics = Topic.query.order_by(Topic.unit_number, Topic.title).all()
    return render_template("academic/reviews.html", reviews=reviews, topics=topics, is_admin=is_academic_admin(),
                           review_statuses=REVIEW_STATUSES)


@academic_bp.post("/content-review/<int:review_id>/decision")
@login_required
def decide_review(review_id):
    require_admin()
    review = db.session.get(ContentReview, review_id) or abort(404)
    if review.status != "pending":
        flash("This proposal has already been reviewed.", "info")
        return redirect(url_for("academic.content_review"))
    decision = request.form.get("status", "")
    notes = request.form.get("reviewer_notes", "").strip()
    if decision not in REVIEW_STATUSES or len(notes) > 4000:
        abort(400)
    review.status = decision
    review.reviewer_id = current_user.id
    review.reviewer_notes = notes
    review.reviewed_at = datetime.now(timezone.utc)
    db.session.commit()
    flash("Review decision saved. Proposed content remains separate from the published lesson.", "success")
    return redirect(url_for("academic.content_review"))
