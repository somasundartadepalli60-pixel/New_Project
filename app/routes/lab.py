"""Local, deterministic LDICA virtual lab endpoints and workspace."""
from flask import Blueprint, jsonify, render_template, request
import math

lab_bp = Blueprint("lab", __name__)


def _number(payload, name, default, minimum, maximum):
    try:
        value = float(payload.get(name, default))
    except (TypeError, ValueError):
        raise ValueError(f"{name.replace('_', ' ').title()} must be a number.")
    if not math.isfinite(value) or value < minimum or value > maximum:
        raise ValueError(f"{name.replace('_', ' ').title()} must be between {minimum:g} and {maximum:g}.")
    return value


def simulate(payload):
    """Return transparent teaching-model results; this is not SPICE simulation."""
    mode = str(payload.get("mode", "opamp"))
    if mode == "opamp":
        rf = _number(payload, "rf", 47000, 1, 1e9)
        rin = _number(payload, "rin", 10000, 1, 1e9)
        vin = _number(payload, "vin", 0.2, -1000, 1000)
        supply = _number(payload, "supply", 5, 1, 100)
        gain = -rf / rin
        ideal = gain * vin
        output = max(-supply, min(supply, ideal))
        return {"mode": mode, "gain": gain, "ideal_output_v": ideal, "output_v": output,
                "saturated": not math.isclose(ideal, output, rel_tol=1e-9, abs_tol=1e-9),
                "equation": "Av = -Rf / Rin; Vout = Av × Vin (limited here by the selected ideal supply rails)",
                "interpretation": "The output is within the selected ideal rails." if math.isclose(ideal, output, abs_tol=1e-9) else "The ideal output exceeds the selected rails, so the teaching model clips it."}
    if mode == "timer555":
        ra = _number(payload, "ra", 10000, 1, 1e9)
        rb = _number(payload, "rb", 10000, 1, 1e9)
        cap = _number(payload, "capacitance_uf", 10, 0.001, 1e6) * 1e-6
        high = 0.693 * (ra + rb) * cap
        low = 0.693 * rb * cap
        period = high + low
        return {"mode": mode, "high_s": high, "low_s": low, "period_s": period,
                "frequency_hz": 1 / period, "duty_percent": high / period * 100,
                "equation": "TH ≈ 0.693(RA + RB)C; TL ≈ 0.693 RB C",
                "interpretation": "Classic 555 astable approximation; real IC thresholds and component tolerances affect measured values."}
    if mode == "adc":
        bits = int(_number(payload, "bits", 8, 1, 16))
        reference = _number(payload, "reference_v", 5, 0.001, 1000)
        vin = _number(payload, "vin", 2.4, 0, reference)
        levels = 2 ** bits
        lsb = reference / levels
        code = min(levels - 1, int(vin / lsb))
        reconstructed = code * lsb
        return {"mode": mode, "levels": levels, "lsb_v": lsb, "code_decimal": code,
                "code_binary": format(code, f"0{bits}b"), "reconstructed_v": reconstructed,
                "quantization_error_v": vin - reconstructed,
                "equation": "Ideal unipolar step = Vref / 2^N; code = floor(Vin / step), bounded to 0…2^N−1",
                "interpretation": "This uses a floor-code teaching convention; practical ADC transfer functions vary by architecture."}
    if mode == "logic":
        gate = str(payload.get("gate", "AND")).upper()
        a = int(_number(payload, "a", 1, 0, 1))
        b = int(_number(payload, "b", 0, 0, 1))
        operations = {"AND": a & b, "OR": a | b, "XOR": a ^ b, "NAND": 1 - (a & b), "NOR": 1 - (a | b), "XNOR": 1 - (a ^ b)}
        if gate not in operations:
            raise ValueError("Choose AND, OR, XOR, NAND, NOR, or XNOR.")
        return {"mode": mode, "gate": gate, "a": a, "b": b, "output": operations[gate],
                "equation": f"Y = {gate}(A, B)", "interpretation": f"For A={a} and B={b}, the {gate} output is {operations[gate]}."}
    raise ValueError("Choose a supported lab mode.")


@lab_bp.get("/")
def index():
    return render_template("lab/index.html")


@lab_bp.post("/simulate")
def simulate_api():
    payload = request.get_json(silent=True) or request.form.to_dict()
    try:
        return jsonify({"ok": True, "result": simulate(payload)})
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400


@lab_bp.get("/workbench")
def signal_workbench():
    """Render the local waveform, timing and parameter-comparison workbench."""
    return render_template("lab/workbench.html")
