"""Local concept knowledge graph for navigating the LDICA syllabus."""
from collections import defaultdict, deque
from flask import Blueprint, jsonify, render_template, request
from ..models import Topic

graph_bp = Blueprint("graph", __name__)

# These links are pedagogical navigation suggestions, not claims that the PDF
# explicitly defines a formal prerequisite graph.
CURATED_LINKS = [
    # Unit 1: op-amp foundations and common applications.
    ("ideal-practical-opamp", "opamp-characteristics", "builds on"),
    ("opamp-characteristics", "opamp-dc-ac", "extends"),
    ("ideal-practical-opamp", "inverting-amplifier", "applies"),
    ("ideal-practical-opamp", "non-inverting-amplifier", "applies"),
    ("inverting-amplifier", "differential-amplifier", "compares"),
    ("differential-amplifier", "instrumentation-amplifier", "extends"),
    ("inverting-amplifier", "differentiator", "adapts"),
    ("inverting-amplifier", "integrator", "adapts"),
    ("comparators", "schmitt-trigger", "adds hysteresis"),
    ("comparators", "voltage-regulators", "contrasts applications"),
    ("ic741", "opamp-characteristics", "device example"),
    # Unit 2: filters, waveform generators, timer and PLL applications.
    ("inverting-amplifier", "active-filters", "active circuit foundation"),
    ("active-filters", "band-pass-filter", "filter class"),
    ("active-filters", "band-reject-filter", "filter class"),
    ("active-filters", "all-pass-filter", "filter class"),
    ("active-filters", "first-order-lpf", "filter example"),
    ("active-filters", "first-order-hpf", "filter example"),
    ("comparators", "square-wave-generator", "switching concept"),
    ("schmitt-trigger", "square-wave-generator", "switching feedback"),
    ("integrator", "triangular-generator", "wave shaping"),
    ("integrator", "sawtooth-generator", "wave shaping"),
    ("ic555-functional", "ic555-monostable", "operating mode"),
    ("ic555-functional", "ic555-astable", "operating mode"),
    ("ic555-astable", "ic555-applications", "application"),
    ("pll-principle", "ic565-pll", "IC implementation"),
    ("ic565-pll", "ic565-applications", "application"),
    ("square-wave-generator", "ic555-astable", "timing comparison"),
    # Unit 3: DAC/ADC fundamentals and architectures.
    ("data-converter-intro", "basic-dac", "conversion family"),
    ("data-converter-intro", "parallel-comparator-adc", "conversion family"),
    ("basic-dac", "weighted-resistor-dac", "architecture"),
    ("basic-dac", "r2r-ladder-dac", "architecture"),
    ("r2r-ladder-dac", "inverted-r2r-dac", "related topology"),
    ("parallel-comparator-adc", "counter-adc", "architecture comparison"),
    ("parallel-comparator-adc", "sar-adc", "architecture comparison"),
    ("sar-adc", "dual-slope-adc", "architecture comparison"),
    ("dac-specifications", "basic-dac", "performance measures"),
    ("adc-specifications", "parallel-comparator-adc", "performance measures"),
    ("ic565-pll", "data-converter-intro", "cross-unit signal systems"),
    # Unit 4: combinational logic and standard logic ICs.
    ("ttl-74xx", "cmos-40xx", "logic-family comparison"),
    ("code-converters", "decoders", "code processing"),
    ("decoders", "led-lcd-decoders", "display application"),
    ("encoders", "priority-encoders", "priority extension"),
    ("multiplexers", "demultiplexers", "data routing comparison"),
    ("priority-generators-checkers", "magnitude-comparators", "combinational comparison"),
    ("parallel-binary-adder", "parallel-binary-subtractor", "arithmetic circuits"),
    ("code-converters", "parallel-binary-adder", "digital representation"),
    # Unit 5: sequential logic and memory.
    ("sequential-ics", "sr-flip-flop", "storage element"),
    ("sr-flip-flop", "jk-flip-flop", "flip-flop comparison"),
    ("jk-flip-flop", "d-flip-flop", "flip-flop comparison"),
    ("jk-flip-flop", "t-flip-flop", "flip-flop comparison"),
    ("d-flip-flop", "shift-registers", "storage application"),
    ("t-flip-flop", "synchronous-counters", "counting application"),
    ("synchronous-counters", "decade-counters", "counter application"),
    ("rom-architecture", "rom-types-applications", "memory classification"),
    ("ram-architecture", "static-ram", "memory type"),
    ("ram-architecture", "dynamic-ram", "memory type"),
    ("multiplexers", "shift-registers", "data movement concepts"),
]

def _graph_payload():
    topics = Topic.query.order_by(Topic.unit_number, Topic.title).all()
    nodes = [{
        "id": topic.slug, "slug": topic.slug, "title": topic.title,
        "unit": topic.unit_number, "unit_title": topic.unit_title,
        "summary": topic.summary or "", "explanation": topic.explanation or "",
        "formula": topic.formula or "", "diagram_type": topic.diagram_type or "concept",
        "url": f"/learn/{topic.slug}",
    } for topic in topics]
    by_slug = {node["id"]: node for node in nodes}
    edges, seen = [], set()
    def add_edge(source, target, label, kind="suggested"):
        if source not in by_slug or target not in by_slug or source == target:
            return
        key = (source, target)
        if key in seen:
            return
        seen.add(key)
        edges.append({"source": source, "target": target, "label": label, "kind": kind})
    for source, target, label in CURATED_LINKS:
        add_edge(source, target, label)
    # Keep the graph navigable even where the original topic names differ from
    # a curated relationship: connect each topic to its unit anchor.
    for node in nodes:
        unit_anchor = f"unit-{node['unit']}-anchor"
        if unit_anchor not in by_slug:
            # Unit anchors are virtual graph nodes, not database records.
            by_slug[unit_anchor] = {
                "id": unit_anchor, "slug": unit_anchor,
                "title": f"Unit {node['unit']}: {node['unit_title']}",
                "unit": node["unit"], "unit_title": node["unit_title"],
                "summary": f"Entry point for topics mapped to {node['unit_title']}.",
                "explanation": "This is a navigation anchor generated from the syllabus catalogue. Connections indicate grouping, not a formal prerequisite.",
                "formula": "", "diagram_type": "unit", "url": "/syllabus",
                "is_anchor": True,
            }
            nodes.append(by_slug[unit_anchor])
        add_edge(unit_anchor, node["id"], "unit topic", "unit")
    # Sequential unit anchors make cross-unit routes discoverable without
    # labelling these links as prerequisites.
    for unit_number in range(1, 5):
        add_edge(f"unit-{unit_number}-anchor", f"unit-{unit_number + 1}-anchor", "next syllabus unit", "sequence")
    return nodes, edges

@graph_bp.get("/")
def index():
    return render_template("graph/index.html")

@graph_bp.get("/data")
def data():
    nodes, edges = _graph_payload()
    try:
        unit = int(request.args.get("unit", "0"))
    except ValueError:
        unit = 0
    if unit:
        selected = {node["id"] for node in nodes if node["unit"] == unit}
        # Include edges touching selected nodes and their unit anchor.
        edges = [edge for edge in edges if edge["source"] in selected and edge["target"] in selected]
        visible = {endpoint for edge in edges for endpoint in (edge["source"], edge["target"])}
        nodes = [node for node in nodes if node["id"] in visible or node["unit"] == unit]
    return jsonify({"nodes": nodes, "edges": edges, "units": sorted({node["unit"] for node in nodes})})

@graph_bp.get("/path")
def path():
    source = request.args.get("from", "").strip()
    target = request.args.get("to", "").strip()
    nodes, edges = _graph_payload()
    by_id = {node["id"]: node for node in nodes}
    if source not in by_id or target not in by_id:
        return jsonify({"ok": False, "error": "Choose two concepts from the available graph."}), 400
    adjacency = defaultdict(list)
    for edge in edges:
        # Treat links as navigable in either direction for path discovery.
        adjacency[edge["source"]].append(edge["target"])
        adjacency[edge["target"]].append(edge["source"])
    queue = deque([source])
    previous = {source: None}
    while queue:
        current = queue.popleft()
        if current == target:
            break
        for neighbour in adjacency[current]:
            if neighbour not in previous:
                previous[neighbour] = current
                queue.append(neighbour)
    if target not in previous:
        return jsonify({"ok": False, "error": "No connected path was found between those concepts."}), 404
    path_ids, current = [], target
    while current is not None:
        path_ids.append(current)
        current = previous[current]
    path_ids.reverse()
    return jsonify({"ok": True, "path": [by_id[item] for item in path_ids]})
