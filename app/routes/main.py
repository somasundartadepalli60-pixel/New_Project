from flask import Blueprint, render_template
from ..models import Topic
from ..content.catalog import UNITS

main_bp = Blueprint("main", __name__)

@main_bp.get("/")
def index():
    counts = {u["number"]: len(u["topics"]) for u in UNITS}
    return render_template("index.html", units=UNITS, counts=counts, total_topics=sum(counts.values()))

@main_bp.get("/syllabus")
def syllabus():
    return render_template("syllabus.html", units=UNITS)

@main_bp.get("/health")
def health():
    return {"status": "ok"}
