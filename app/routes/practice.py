from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..extensions import db
from ..models import Topic, QuizAttempt

practice_bp = Blueprint("practice", __name__)

QUESTIONS = [
    {"unit": 1, "q": "For an ideal inverting amplifier with Rin = 10 kΩ and Rf = 100 kΩ, the voltage gain is:", "choices": ["+10", "−10", "+11", "−0.1"], "answer": 1, "explanation": "For the inverting configuration, Av = −Rf/Rin = −100/10 = −10."},
    {"unit": 2, "q": "The nominal trigger level of a classic 555 timer is approximately:", "choices": ["VCC/4", "VCC/3", "VCC/2", "2VCC/3"], "answer": 1, "explanation": "The internal three-resistor divider establishes a trigger reference near VCC/3."},
    {"unit": 3, "q": "An ideal N-bit converter has how many possible output codes?", "choices": ["N", "2N", "N²", "2^N"], "answer": 3, "explanation": "N bits represent 2^N distinct binary codes."},
    {"unit": 4, "q": "A multiplexer is primarily used to:", "choices": ["Store a bit", "Select one of several inputs", "Convert analogue to digital", "Generate a clock only"], "answer": 1, "explanation": "A multiplexer routes a selected data input to its output."},
    {"unit": 5, "q": "Which memory normally requires periodic refresh?", "choices": ["SRAM", "DRAM", "Mask ROM", "PROM"], "answer": 1, "explanation": "DRAM stores charge that leaks over time, so refresh is required."},
]

@practice_bp.get("/")
@login_required
def index():
    return render_template("quizzes/index.html", questions=QUESTIONS)

@practice_bp.post("/submit")
@login_required
def submit():
    answers = {}
    score = 0
    for i, question in enumerate(QUESTIONS):
        raw = request.form.get(f"q{i}")
        try:
            selected = int(raw) if raw is not None else -1
        except ValueError:
            selected = -1
        answers[i] = selected
        if selected == question["answer"]:
            score += 1
    attempt = QuizAttempt(user_id=current_user.id, unit_number=0, score=score, total=len(QUESTIONS))
    db.session.add(attempt)
    db.session.commit()
    return render_template("quizzes/results.html", questions=QUESTIONS, answers=answers, score=score)
