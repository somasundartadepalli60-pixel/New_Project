from flask import Blueprint, render_template, request
from ..services.calculators import (
    CalculatorInputError, inverting_gain, non_inverting_gain, rc_cutoff,
    timer555_monostable, timer555_astable, converter_resolution,
    memory_capacity, flash_adc_comparators, full_adder,
)

tools_bp = Blueprint("tools", __name__)

CALCULATORS = {
    "inverting": {"title": "Inverting amplifier", "description": "Calculate closed-loop gain and output voltage.", "fields": [("rf", "Feedback resistance Rf (Ω)", "47000"), ("rin", "Input resistance Rin (Ω)", "10000"), ("vin", "Input voltage (V)", "0.2")]},
    "non_inverting": {"title": "Non-inverting amplifier", "description": "Calculate non-inverting gain and output voltage.", "fields": [("rf", "Feedback resistance Rf (Ω)", "30000"), ("rg", "Resistance to ground Rg (Ω)", "10000"), ("vin", "Input voltage (V)", "0.5")]},
    "cutoff": {"title": "First-order RC cutoff", "description": "Estimate the cutoff of a simple first-order RC pole.", "fields": [("r", "Resistance (Ω)", "10000"), ("c", "Capacitance (F)", "0.00000001")]},
    "monostable": {"title": "555 monostable timer", "description": "Estimate pulse width using the classic T ≈ 1.1RC relationship.", "fields": [("r", "Timing resistance (Ω)", "100000"), ("c", "Timing capacitance (F)", "0.00001")]},
    "astable": {"title": "555 astable timer", "description": "Estimate high time, low time, period, frequency and duty cycle.", "fields": [("ra", "RA (Ω)", "10000"), ("rb", "RB (Ω)", "10000"), ("c", "Timing capacitance (F)", "0.00001")]},
    "resolution": {"title": "ADC/DAC resolution", "description": "Estimate ideal code count and step size from bit resolution and range.", "fields": [("bits", "Resolution (bits)", "8"), ("range", "Full-scale range (V)", "5.0")]},
    "memory": {"title": "Memory capacity", "description": "Calculate memory words and capacity from address and word width.", "fields": [("address_bits", "Address lines (bits)", "10"), ("word_bits", "Data width (bits)", "8")]},
    "flash": {"title": "Flash ADC comparator count", "description": "Calculate the conventional 2^N − 1 comparator count.", "fields": [("bits", "Resolution (bits)", "3")]},
    "adder": {"title": "One-bit full adder", "description": "Calculate sum and carry for binary inputs.", "fields": [("a", "Input A (0 or 1)", "1"), ("b", "Input B (0 or 1)", "1"), ("cin", "Carry-in (0 or 1)", "0")]},
}


def _format_result(result):
    formatted = []
    for key, value in result.items():
        if key == "equation":
            formatted.append(("Relationship", value))
        elif key.endswith("_voltage") or key.endswith("_volts"):
            formatted.append((key.replace("_", " ").title(), f"{value:.6g} V"))
        elif key.endswith("_seconds") or key == "time_seconds":
            formatted.append((key.replace("_seconds", "").replace("_", " ").title(), f"{value:.6g} s"))
        elif key.endswith("_hz") or key == "frequency_hz":
            formatted.append((key.replace("_hz", "").replace("_", " ").title(), f"{value:.6g} Hz"))
        elif key.endswith("_percent"):
            formatted.append((key.replace("_percent", "").replace("_", " ").title(), f"{value:.4g}%"))
        elif isinstance(value, float):
            formatted.append((key.replace("_", " ").title(), f"{value:.7g}"))
        else:
            formatted.append((key.replace("_", " ").title(), str(value)))
    return formatted


@tools_bp.route("/", methods=["GET", "POST"])
def index():
    selected = request.values.get("calculator", "inverting")
    if selected not in CALCULATORS:
        selected = "inverting"
    result = None
    error = None
    if request.method == "POST":
        try:
            form = request.form
            if selected == "inverting":
                raw = inverting_gain(form.get("rf"), form.get("rin"), form.get("vin"))
            elif selected == "non_inverting":
                raw = non_inverting_gain(form.get("rf"), form.get("rg"), form.get("vin"))
            elif selected == "cutoff":
                raw = rc_cutoff(form.get("r"), form.get("c"))
            elif selected == "monostable":
                raw = timer555_monostable(form.get("r"), form.get("c"))
            elif selected == "astable":
                raw = timer555_astable(form.get("ra"), form.get("rb"), form.get("c"))
            elif selected == "resolution":
                raw = converter_resolution(form.get("bits"), form.get("range"))
            elif selected == "memory":
                raw = memory_capacity(form.get("address_bits"), form.get("word_bits"))
            elif selected == "flash":
                raw = flash_adc_comparators(form.get("bits"))
            else:
                raw = full_adder(form.get("a"), form.get("b"), form.get("cin"))
            result = _format_result(raw)
        except CalculatorInputError as exc:
            error = str(exc)
    return render_template("tools/index.html", calculators=CALCULATORS,
                           selected=selected, calculator=CALCULATORS[selected],
                           result=result, error=error, values=request.values)
