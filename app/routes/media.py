from flask import Blueprint, render_template, abort, request
from ..models import Topic
import os
import re
from pathlib import Path

media_bp = Blueprint("media", __name__)
BASE_DIR = Path(__file__).resolve().parents[1]
SOURCE_FILES = [
    {"name": "Unit 1 — Operational Amplifiers", "file": "unit-1-operational-amplifiers.pdf", "text": "unit-1-operational-amplifiers.txt", "unit": 1, "description": "Uploaded notes for op-amp models, characteristics, amplifier circuits and voltage regulators."},
    {"name": "Unit 2 — Op-Amp, Timer and PLL Applications", "file": "unit-2-opamp-timer-pll.pdf", "text": "unit-2-opamp-timer-pll.txt", "unit": 2, "description": "Uploaded notes for active filters, waveform generators, 555 timer and PLL."},
    {"name": "Unit 3 — Data Converters", "file": "unit-3-data-converters.pdf", "text": "unit-3-data-converters.txt", "unit": 3, "description": "Uploaded notes for DAC and ADC architectures and specifications."},
    {"name": "Unit 4 — Digital Logic", "file": "unit-4-digital-logic.pdf", "text": "unit-4-digital-logic.txt", "unit": 4, "description": "Uploaded notes for TTL/CMOS, code converters, decoders, encoders, multiplexers and arithmetic logic."},
    {"name": "Supplement — Sequential Circuits", "file": "supplement-sequential-circuits.pdf", "text": "supplement-sequential-circuits.txt", "unit": 5, "description": "Supplementary notes on flip-flops, counters, shift registers and memories."},
    {"name": "Combined LDICA Notes", "file": "combined-ldica-notes.pdf", "text": "combined-ldica-notes.txt", "unit": 0, "description": "Additional notes covering op-amp applications, filters, timer circuits and other LDICA concepts."},
    {"name": "Data Converter Notes Supplement", "file": "unit-3-converter-notes-supplement.pdf", "text": "unit-3-converter-notes-supplement.txt", "unit": 3, "description": "Supplementary text-based notes for weighted-resistor and R-2R DACs and ADC architectures."},
    {"name": "Digital IC Applications Notes", "file": "digital-ic-applications-notes.pdf", "text": "digital-ic-applications-notes.txt", "unit": 0, "description": "Additional notes covering TTL/CMOS logic families, combinational circuits and sequential logic."},
]

@media_bp.get("/")
def index():
    sources = []
    for item in SOURCE_FILES:
        pdf_path = BASE_DIR / "static" / "source-pdfs" / item["file"]
        text_path = BASE_DIR / "content" / "source_text" / item["text"]
        if pdf_path.exists():
            sources.append({**item, "has_text": text_path.exists()})
    query = request.args.get("q", "").strip()[:120]
    matches = []
    if query:
        terms = [part.casefold() for part in query.split() if part.strip()]
        for item in sources:
            text_path = BASE_DIR / "content" / "source_text" / item["text"]
            if not text_path.exists():
                continue
            with open(text_path, "r", encoding="utf-8", errors="replace") as source:
                pages = source.read().split("===== PAGE ")
            for page in pages:
                if not page.strip():
                    continue
                page_no = page.split(" =====", 1)[0].strip()
                body = page.split("=====", 1)[-1].strip()
                folded = body.casefold()
                if all(term in folded for term in terms):
                    excerpt = re.sub(r"\s+", " ", body)
                    position = min((folded.find(term) for term in terms if term in folded), default=0)
                    start = max(0, position - 100)
                    end = min(len(excerpt), position + 260)
                    matches.append({"name": item["name"], "file": item["file"], "page": page_no,
                                    "excerpt": excerpt[start:end]})
                    if len(matches) >= 30:
                        break
            if len(matches) >= 30:
                break
    demos = [
        {"slug":"opamp","title":"Op-amp feedback explorer","description":"Compare inverting and non-inverting closed-loop gain with live parameter changes.","kind":"calculator"},
        {"slug":"timer555","title":"555 timer timing demo","description":"Watch a conceptual capacitor charge/discharge cycle and compare timing estimates.","kind":"animation"},
        {"slug":"adc","title":"ADC quantisation demo","description":"Move an analogue input through discrete quantisation levels and inspect the output code.","kind":"simulation"},
        {"slug":"counter","title":"Binary counter visualiser","description":"Step through binary states and see how the state changes on each clock event.","kind":"simulation"},
    ]
    return render_template("media/index.html", sources=sources, demos=demos, query=query, matches=matches)

@media_bp.get("/demo/<slug>")
def demo(slug):
    definitions = {
        "opamp": {"title":"Op-amp feedback explorer","kind":"gain"},
        "timer555": {"title":"555 timer timing demo","kind":"timer"},
        "adc": {"title":"ADC quantisation demo","kind":"adc"},
        "counter": {"title":"Binary counter visualiser","kind":"counter"},
    }
    if slug not in definitions:
        abort(404)
    return render_template("media/demo.html", demo=definitions[slug])
