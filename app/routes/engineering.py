"""Local interactive digital/analog engineering workbenches (teaching models)."""
from flask import Blueprint, render_template

engineering_bp = Blueprint("engineering", __name__)


@engineering_bp.get("/")
def index():
    return render_template("engineering/index.html")
