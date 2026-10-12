"""Local-first search across the seeded syllabus and bundled source PDFs."""
from functools import lru_cache
from pathlib import Path
import re

from flask import Blueprint, current_app, render_template, request, jsonify
from ..models import Topic
from ..content.lesson_bank import lesson_detail

search_bp = Blueprint("search", __name__)
STOP_WORDS = {"about", "after", "again", "also", "among", "and", "are", "can", "could", "does", "explain", "find", "from", "have", "into", "is", "its", "that", "the", "their", "then", "this", "what", "when", "where", "which", "with", "would", "your"}


def _terms(query):
    return [word.lower() for word in re.findall(r"[A-Za-z0-9][A-Za-z0-9+./-]*", query) if len(word) > 1 and word.lower() not in STOP_WORDS]


def _snippet(text, terms, radius=190):
    clean = re.sub(r"\s+", " ", text or "").strip()
    lower = clean.lower()
    positions = [lower.find(term.lower()) for term in terms if lower.find(term.lower()) >= 0]
    start = max(0, min(positions) - radius // 3) if positions else 0
    end = min(len(clean), start + radius)
    return ("…" if start else "") + clean[start:end] + ("…" if end < len(clean) else "")


@lru_cache(maxsize=3)
def _pdf_page_index(pdf_directory):
    """Extract text once per process; scanned/image-only pages are skipped honestly."""
    try:
        from pypdf import PdfReader
    except ImportError:
        return []
    pages = []
    directory = Path(pdf_directory)
    if not directory.is_dir():
        return pages
    for path in sorted(directory.glob("*.pdf")):
        try:
            reader = PdfReader(str(path))
            for number, page in enumerate(reader.pages, start=1):
                text = (page.extract_text() or "").strip()
                pages.append({"title": path.stem.replace("-", " ").replace("_", " ").title(),
                              "filename": path.name, "page": number, "text": text,
                              "has_text": bool(text)})
        except Exception:
            # A damaged or unsupported PDF should not make lesson search unavailable.
            continue
    return pages


def search_content(query, unit=None, limit=30):
    """Rank lesson and source-page matches with a transparent local term scorer."""
    terms = _terms(query)
    if not terms:
        return {"results": [], "terms": [], "indexed_pdf_pages": 0, "pdf_search_available": False}
    results = []
    topics_query = Topic.query
    if unit in {1, 2, 3, 4, 5}:
        topics_query = topics_query.filter_by(unit_number=unit)
    for topic in topics_query.order_by(Topic.unit_number, Topic.title).all():
        detail = lesson_detail(topic)
        body = " ".join([topic.title, topic.summary, topic.explanation, topic.formula or "",
                          topic.source_note or "", str(topic.applications or []), str(detail)])
        lower = body.lower()
        score = sum(lower.count(term) * (4 if term in topic.title.lower() else 1) for term in terms)
        if score:
            results.append({"kind": "lesson", "title": topic.title, "unit": topic.unit_number,
                            "summary": topic.summary, "snippet": _snippet(body, terms),
                            "url": f"/learn/{topic.slug}", "score": score})
    pdf_directory = str(Path(current_app.static_folder) / "source-pdfs")
    pdf_pages = _pdf_page_index(pdf_directory)
    for page in pdf_pages:
        # Preserve page-level index status so the UI can identify image-only
        # documents instead of implying that every PDF is fully searchable.
        if not page.get("has_text", bool(page["text"])):
            continue
        lower = page["text"].lower()
        score = sum(lower.count(term) for term in terms)
        if score:
            results.append({"kind": "source PDF", "title": page["title"], "unit": None,
                            "summary": f"Source document · page {page['page']}",
                            "snippet": _snippet(page["text"], terms),
                            "url": f"/static/source-pdfs/{page['filename']}#page={page['page']}",
                            "page": page["page"], "score": score})
    results.sort(key=lambda item: (item["score"], item["kind"] == "lesson"), reverse=True)
    text_pages = [page for page in pdf_pages if page.get("has_text", bool(page["text"]))]
    no_text_by_document = {}
    for page in pdf_pages:
        if not page.get("has_text", bool(page["text"])):
            no_text_by_document.setdefault(page["filename"], 0)
            no_text_by_document[page["filename"]] += 1
    return {"results": results[:max(1, min(limit, 60))], "terms": terms,
            "indexed_pdf_pages": len(text_pages), "pdf_page_count": len(pdf_pages),
            "unindexed_pdf_pages": sum(no_text_by_document.values()),
            "pdfs_requiring_ocr": sorted(no_text_by_document),
            "pdf_search_available": bool(text_pages)}


@search_bp.get("/")
def index():
    query = request.args.get("q", "")[:120].strip()
    unit_value = request.args.get("unit", "").strip()
    unit = int(unit_value) if unit_value.isdigit() and int(unit_value) in {1, 2, 3, 4, 5} else None
    payload = search_content(query, unit) if query else {"results": [], "terms": [], "indexed_pdf_pages": 0, "pdf_page_count": 0, "unindexed_pdf_pages": 0, "pdfs_requiring_ocr": [], "pdf_search_available": False}
    return render_template("search/index.html", query=query, unit=unit, **payload)


@search_bp.get("/api")
def api():
    query = request.args.get("q", "")[:120].strip()
    unit_value = request.args.get("unit", "").strip()
    unit = int(unit_value) if unit_value.isdigit() and int(unit_value) in {1, 2, 3, 4, 5} else None
    payload = search_content(query, unit) if query else {"results": [], "terms": [], "indexed_pdf_pages": 0, "pdf_page_count": 0, "unindexed_pdf_pages": 0, "pdfs_requiring_ocr": [], "pdf_search_available": False}
    return jsonify(payload)
