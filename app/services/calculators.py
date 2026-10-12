"""Small, testable calculators for common LDICA study relationships.

These helpers implement standard idealised relationships. Always check the
actual circuit topology, device limits, and convention stated in the lesson.
"""
from math import log2, pi


class CalculatorInputError(ValueError):
    """Raised when a calculation input is outside the supported domain."""


def _positive(name, value):
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise CalculatorInputError(f"{name} must be a number.") from exc
    if number <= 0:
        raise CalculatorInputError(f"{name} must be greater than zero.")
    return number


def inverting_gain(rf_ohms, rin_ohms, vin_volts=None):
    rf = _positive("Feedback resistance", rf_ohms)
    rin = _positive("Input resistance", rin_ohms)
    gain = -rf / rin
    result = {"gain": gain, "equation": "Av = -Rf / Rin"}
    if vin_volts is not None:
        try:
            vin = float(vin_volts)
        except (TypeError, ValueError) as exc:
            raise CalculatorInputError("Input voltage must be a number.") from exc
        result["output_voltage"] = gain * vin
    return result


def non_inverting_gain(rf_ohms, rg_ohms, vin_volts=None):
    rf = _positive("Feedback resistance", rf_ohms)
    rg = _positive("Resistance to ground", rg_ohms)
    gain = 1 + rf / rg
    result = {"gain": gain, "equation": "Av = 1 + Rf / Rg"}
    if vin_volts is not None:
        try:
            vin = float(vin_volts)
        except (TypeError, ValueError) as exc:
            raise CalculatorInputError("Input voltage must be a number.") from exc
        result["output_voltage"] = gain * vin
    return result


def rc_cutoff(resistance_ohms, capacitance_farads):
    resistance = _positive("Resistance", resistance_ohms)
    capacitance = _positive("Capacitance", capacitance_farads)
    return {"frequency_hz": 1 / (2 * pi * resistance * capacitance),
            "equation": "fc = 1 / (2πRC)"}


def timer555_monostable(resistance_ohms, capacitance_farads):
    resistance = _positive("Timing resistance", resistance_ohms)
    capacitance = _positive("Timing capacitance", capacitance_farads)
    return {"time_seconds": 1.1 * resistance * capacitance,
            "equation": "T ≈ 1.1RC"}


def timer555_astable(ra_ohms, rb_ohms, capacitance_farads):
    ra = _positive("RA", ra_ohms)
    rb = _positive("RB", rb_ohms)
    capacitance = _positive("Timing capacitance", capacitance_farads)
    high = 0.693 * (ra + rb) * capacitance
    low = 0.693 * rb * capacitance
    period = high + low
    return {"high_seconds": high, "low_seconds": low,
            "period_seconds": period, "frequency_hz": 1 / period,
            "duty_percent": high / period * 100,
            "equation": "TH ≈ 0.693(RA + RB)C; TL ≈ 0.693RBC"}


def converter_resolution(bits, full_scale_volts):
    try:
        n = int(bits)
    except (TypeError, ValueError) as exc:
        raise CalculatorInputError("Bit resolution must be a whole number.") from exc
    if n < 1 or n > 32:
        raise CalculatorInputError("Bit resolution must be between 1 and 32.")
    full_scale = _positive("Full-scale range", full_scale_volts)
    levels = 2 ** n
    return {"levels": levels, "lsb_volts": full_scale / levels,
            "quantisation_bound_volts": full_scale / levels / 2,
            "equation": "levels = 2^N; ideal step = full-scale range / 2^N"}


def memory_capacity(address_bits, word_bits):
    try:
        addresses = int(address_bits)
        width = int(word_bits)
    except (TypeError, ValueError) as exc:
        raise CalculatorInputError("Address bits and word width must be whole numbers.") from exc
    if not 1 <= addresses <= 32:
        raise CalculatorInputError("Address bits must be between 1 and 32.")
    if not 1 <= width <= 1024:
        raise CalculatorInputError("Word width must be between 1 and 1024 bits.")
    words = 2 ** addresses
    total_bits = words * width
    return {"words": words, "total_bits": total_bits,
            "total_bytes": total_bits / 8,
            "equation": "capacity = 2^(address bits) × bits per word"}


def flash_adc_comparators(bits):
    try:
        n = int(bits)
    except (TypeError, ValueError) as exc:
        raise CalculatorInputError("Bit resolution must be a whole number.") from exc
    if not 1 <= n <= 16:
        raise CalculatorInputError("Flash ADC resolution must be between 1 and 16 bits for this tool.")
    return {"levels": 2 ** n, "comparators": 2 ** n - 1,
            "equation": "Comparator count = 2^N − 1 for a conventional flash ADC"}


def full_adder(a, b, carry_in):
    values = (a, b, carry_in)
    if any(value not in (0, 1, "0", "1") for value in values):
        raise CalculatorInputError("A, B, and carry-in must each be 0 or 1.")
    a, b, carry_in = (int(value) for value in values)
    total = a + b + carry_in
    return {"sum": total % 2, "carry_out": total // 2,
            "equation": "S = A XOR B XOR Cin; Cout = AB + ACin + BCin"}
