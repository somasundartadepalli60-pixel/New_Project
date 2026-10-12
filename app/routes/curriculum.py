"""Curriculum coverage and content-quality tools for the LDICA catalogue."""
from collections import Counter
from flask import Blueprint, render_template, request
from ..models import Topic

curriculum_bp = Blueprint("curriculum", __name__)


def audit_topic(topic):
    """Return transparent, rule-based quality signals; never imply source verification."""
    checks = {
        "summary": bool((topic.summary or "").strip()),
        "explanation": len((topic.explanation or "").strip()) >= 100,
        "formula_or_note": bool((topic.formula or "").strip()),
        "applications": bool(topic.applications),
        "source_note": bool((topic.source_note or "").strip()),
    }
    warnings = []
    if not checks["summary"]:
        warnings.append("Missing topic summary")
    if not checks["explanation"]:
        warnings.append("Explanation is missing or very short")
    if not checks["formula_or_note"]:
        warnings.append("No formula or explicit formula note")
    if not checks["applications"]:
        warnings.append("No application examples listed")
    source = (topic.source_note or "").lower()
    if not source or "consult" in source or "verify" in source or "refer" in source:
        warnings.append("Source-page verification may still be required")
    return {"topic": topic, "checks": checks, "score": round(sum(checks.values()) / len(checks) * 100), "warnings": warnings}


@curriculum_bp.get("/")
def index():
    unit_filter = request.args.get("unit", type=int)
    status_filter = request.args.get("status", "all")
    query = request.args.get("q", "").strip()[:100]
    topics_query = Topic.query
    if unit_filter:
        topics_query = topics_query.filter_by(unit_number=unit_filter)
    if query:
        pattern = f"%{query}%"
        from ..extensions import db
        topics_query = topics_query.filter(db.or_(Topic.title.ilike(pattern), Topic.summary.ilike(pattern), Topic.explanation.ilike(pattern)))
    topics = topics_query.order_by(Topic.unit_number, Topic.title).all()
    audits = [audit_topic(topic) for topic in topics]
    if status_filter == "needs-review":
        audits = [item for item in audits if item["warnings"]]
    elif status_filter == "ready-check":
        audits = [item for item in audits if not item["warnings"]]
    all_topics = Topic.query.all()
    all_audits = [audit_topic(topic) for topic in all_topics]
    by_unit = Counter(item["topic"].unit_number for item in all_audits)
    average_score = round(sum(item["score"] for item in all_audits) / len(all_audits)) if all_audits else 0
    needs_review = sum(bool(item["warnings"]) for item in all_audits)
    return render_template("curriculum/index.html", audits=audits, unit_filter=unit_filter,
                           status_filter=status_filter, query=query, total=len(all_topics),
                           average_score=average_score, needs_review=needs_review,
                           by_unit=sorted(by_unit.items()))
