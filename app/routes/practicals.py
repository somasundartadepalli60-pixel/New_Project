"""Phase 16: assignment, practical-log, submission and rubric workflow."""
from datetime import date, datetime, timezone
import json

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy import desc

from ..extensions import db
from ..models import PracticalAssignment, PracticalSubmission

practicals_bp = Blueprint("practicals", __name__)

DEFAULT_RUBRIC = [
    {"key": "principle", "label": "Principle and theory", "max": 4},
    {"key": "method", "label": "Method and procedure", "max": 4},
    {"key": "observations", "label": "Observations and results", "max": 4},
    {"key": "analysis", "label": "Analysis and conclusion", "max": 4},
    {"key": "presentation", "label": "Clarity and report quality", "max": 4},
]


def _rubric_for(assignment):
    try:
        rubric = json.loads(assignment.rubric_json or "[]")
        if isinstance(rubric, list) and rubric and all(
            isinstance(row, dict) and row.get("key") and isinstance(row.get("max"), int)
            and 1 <= row["max"] <= 20 for row in rubric
        ):
            return rubric
    except (ValueError, TypeError):
        pass
    return DEFAULT_RUBRIC


@practicals_bp.get("/")
@login_required
def index():
    assignments = PracticalAssignment.query.order_by(desc(PracticalAssignment.created_at)).all()
    submissions = {row.assignment_id: row for row in PracticalSubmission.query.filter_by(user_id=current_user.id).all()}
    return render_template("practicals/index.html", assignments=assignments, submissions=submissions, today=date.today())


@practicals_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        instructions = request.form.get("instructions", "").strip()
        unit_number = request.form.get("unit_number", type=int) or 0
        due_raw = request.form.get("due_date", "").strip()
        if len(title) < 4 or len(title) > 160 or len(instructions) < 20 or len(instructions) > 12000:
            flash("Provide a title (4–160 characters) and instructions (20–12,000 characters).", "warning")
            return render_template("practicals/create.html", today=date.today().isoformat()), 400
        if unit_number not in range(0, 6):
            abort(400)
        due_date = None
        if due_raw:
            try:
                due_date = date.fromisoformat(due_raw)
            except ValueError:
                abort(400)
        assignment = PracticalAssignment(
            creator_id=current_user.id, title=title, instructions=instructions,
            unit_number=unit_number, due_date=due_date,
            rubric_json=json.dumps(DEFAULT_RUBRIC),
        )
        db.session.add(assignment)
        db.session.commit()
        flash("Assignment created. You can now record your practical work and report.", "success")
        return redirect(url_for("practicals.detail", assignment_id=assignment.id))
    return render_template("practicals/create.html", today=date.today().isoformat())


@practicals_bp.get("/<int:assignment_id>")
@login_required
def detail(assignment_id):
    assignment = db.session.get(PracticalAssignment, assignment_id) or abort(404)
    submission = PracticalSubmission.query.filter_by(assignment_id=assignment.id, user_id=current_user.id).first()
    rubric = _rubric_for(assignment)
    scores = {}
    if submission:
        try:
            scores = json.loads(submission.rubric_scores_json or "{}")
        except ValueError:
            scores = {}
    return render_template("practicals/detail.html", assignment=assignment, submission=submission,
                           rubric=rubric, scores=scores, today=date.today().isoformat())


@practicals_bp.post("/<int:assignment_id>/save")
@login_required
def save_report(assignment_id):
    assignment = db.session.get(PracticalAssignment, assignment_id) or abort(404)
    existing = PracticalSubmission.query.filter_by(assignment_id=assignment.id, user_id=current_user.id).first()
    if existing and existing.status == "submitted":
        flash("This report has been submitted. Create a new revision by reopening it first.", "warning")
        return redirect(url_for("practicals.detail", assignment_id=assignment.id))
    fields = {key: request.form.get(key, "").strip() for key in ("aim", "theory", "procedure", "observations", "analysis", "conclusion", "viva_answers")}
    if any(len(value) > 20000 for value in fields.values()):
        abort(400)
    if not fields["aim"] or not fields["procedure"]:
        flash("Add at least the experiment aim and procedure before saving.", "warning")
        return redirect(url_for("practicals.detail", assignment_id=assignment.id))
    if existing is None:
        existing = PracticalSubmission(assignment_id=assignment.id, user_id=current_user.id)
        db.session.add(existing)
    existing.aim = fields["aim"]
    existing.theory = fields["theory"]
    existing.procedure = fields["procedure"]
    existing.observations = fields["observations"]
    existing.analysis = fields["analysis"]
    existing.conclusion = fields["conclusion"]
    existing.viva_answers = fields["viva_answers"]
    existing.status = "draft"
    existing.updated_at = datetime.now(timezone.utc)
    db.session.commit()
    flash("Practical report saved as a draft.", "success")
    return redirect(url_for("practicals.detail", assignment_id=assignment.id))


@practicals_bp.post("/<int:assignment_id>/submit")
@login_required
def submit_report(assignment_id):
    assignment = db.session.get(PracticalAssignment, assignment_id) or abort(404)
    submission = PracticalSubmission.query.filter_by(assignment_id=assignment.id, user_id=current_user.id).first()
    if not submission:
        flash("Save your practical report before submitting it.", "warning")
        return redirect(url_for("practicals.detail", assignment_id=assignment.id))
    if not submission.aim.strip() or not submission.procedure.strip() or not submission.conclusion.strip():
        flash("Complete the aim, procedure and conclusion before submission.", "warning")
        return redirect(url_for("practicals.detail", assignment_id=assignment.id))
    rubric = _rubric_for(assignment)
    scores = {}
    for item in rubric:
        raw = request.form.get("rubric_" + item["key"], "0")
        try:
            score = int(raw)
        except ValueError:
            abort(400)
        if score < 0 or score > item["max"]:
            abort(400)
        scores[item["key"]] = score
    submission.rubric_scores_json = json.dumps(scores)
    submission.rubric_total = sum(scores.values())
    submission.rubric_max = sum(item["max"] for item in rubric)
    submission.status = "submitted"
    submission.submitted_at = datetime.now(timezone.utc)
    submission.updated_at = datetime.now(timezone.utc)
    db.session.commit()
    flash("Report submitted and self-assessment rubric recorded.", "success")
    return redirect(url_for("practicals.detail", assignment_id=assignment.id))


@practicals_bp.post("/<int:assignment_id>/reopen")
@login_required
def reopen_report(assignment_id):
    assignment = db.session.get(PracticalAssignment, assignment_id) or abort(404)
    submission = PracticalSubmission.query.filter_by(assignment_id=assignment.id, user_id=current_user.id).first()
    if not submission or submission.status != "submitted":
        abort(400)
    submission.status = "draft"
    submission.updated_at = datetime.now(timezone.utc)
    db.session.commit()
    flash("Report reopened for revision. Submit it again when ready.", "info")
    return redirect(url_for("practicals.detail", assignment_id=assignment.id))
