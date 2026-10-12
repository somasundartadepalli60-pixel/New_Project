from flask import Blueprint, render_template, request
from ..models import Topic
from ..content.lesson_bank import lesson_detail

tutor_bp = Blueprint("tutor", __name__)

def respond(question, topic=None):
    """Local topic-aware study helper. It uses stored lessons; it does not call a remote LLM."""
    q = (question or "").strip()
    if not q:
        return {"heading": "Ask a question", "answer": "Enter a question or choose a suggested prompt.", "steps": []}
    lower = q.lower()
    if topic is None:
        terms = [word for word in lower.replace("?", " ").replace(",", " ").split() if len(word) > 3]
        candidates = []
        for item in Topic.query.all():
            score = sum(1 for term in terms if term in (item.title + " " + item.summary + " " + item.explanation).lower())
            if score:
                candidates.append((score, item))
        topic = sorted(candidates, key=lambda pair: pair[0], reverse=True)[0][1] if candidates else None
    if topic is None:
        return {"heading": "Let's narrow it down", "answer": "I couldn't match that question confidently to a stored lesson. Try including a topic name such as inverting amplifier, 555 astable timer, R-2R DAC, multiplexer, or JK flip-flop. This offline tutor uses the course content bundled with the site and does not invent an answer from a remote model.", "steps": []}
    detail = lesson_detail(topic)
    if any(k in lower for k in ("formula", "equation", "calculate", "numerical", "solve", "example")):
        answer = f"For **{topic.title}**, start with the relationship: {topic.formula or 'Use the circuit-specific relationship in the lesson.'} Then identify the known values, convert units, substitute carefully, and check whether the result is physically possible."
        steps = detail.get("worked_steps", [])
        if detail.get("example"):
            steps = list(steps) + [f"Worked example: {detail['example']}"]
    elif any(k in lower for k in ("diagram", "draw", "block", "circuit", "flowchart")):
        answer = f"The lesson page for **{topic.title}** contains a conceptual diagram. Use it to trace input → processing/action → output. For a pin-accurate schematic, compare the matching source PDF in the Source Library; the site's conceptual drawings are learning aids, not substitutes for the original circuit."
        steps = ["Open the lesson diagram.", "Identify each input, active block, feedback path, and output.", "Explain what changes when an input or control signal changes."]
    elif any(k in lower for k in ("remember", "memory trick", "easy", "mnemonic")):
        answer = f"Memory cue for **{topic.title}**: remember it as *purpose → structure → operation → equation/truth table → limitations → application*. Recreate the diagram from memory, then explain each signal in one sentence."
        steps = ["Recall the purpose without looking.", "Sketch the main blocks.", "Write the governing equation or truth table.", "Check your explanation against the lesson."]
    else:
        answer = f"**{topic.title}:** {topic.explanation} The key relationship is {topic.formula or 'the circuit-specific operating rule described in the lesson'}. Use the worked example and common-mistake panel to test your understanding."
        steps = detail.get("worked_steps", [])
    return {"heading": topic.title, "answer": answer, "steps": steps, "example": detail.get("example"),
            "check": detail.get("check"), "answer_check": detail.get("answer")}

@tutor_bp.route("/", methods=["GET", "POST"])
def index():
    topics = Topic.query.order_by(Topic.unit_number, Topic.title).all()
    response = None
    question = ""
    selected_slug = request.values.get("topic", request.args.get("topic", ""))
    selected = Topic.query.filter_by(slug=selected_slug).first() if selected_slug else None
    if request.method == "POST":
        question = request.form.get("question", "")
        response = respond(question, selected)
    return render_template("tutor/index.html", topics=topics, response=response, question=question, selected_slug=selected_slug)
