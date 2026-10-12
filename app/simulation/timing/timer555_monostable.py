"""555 Monostable Multivibrator simulation and pulse timing equations."""
from __future__ import annotations
import math

def monostable_pulse_width(ra_ohm: float, c_farad: float) -> float:
    if ra_ohm <= 0 or c_farad <= 0:
        raise ValueError("Resistance and capacitance must be positive")
    return 1.1 * ra_ohm * c_farad

def monostable_charge_curve(ra_ohm: float, c_farad: float, vcc: float, t_sec: float) -> float:
    tau = ra_ohm * c_farad
    return vcc * (1.0 - math.exp(-t_sec / tau)) if tau > 0 else 0.0

def design_monostable_pulse_generator_1(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 1."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 1, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_2(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 2."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 2, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_3(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 3."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 3, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_4(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 4."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 4, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_5(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 5."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 5, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_6(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 6."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 6, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_7(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 7."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 7, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_8(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 8."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 8, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_9(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 9."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 9, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_10(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 10."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 10, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_11(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 11."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 11, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_12(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 12."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 12, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_13(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 13."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 13, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_14(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 14."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 14, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_15(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 15."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 15, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_16(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 16."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 16, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_17(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 17."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 17, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_18(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 18."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 18, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_19(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 19."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 19, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_20(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 20."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 20, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_21(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 21."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 21, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_22(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 22."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 22, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_23(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 23."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 23, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_24(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 24."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 24, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_25(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 25."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 25, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_26(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 26."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 26, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_27(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 27."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 27, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_28(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 28."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 28, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_29(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 29."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 29, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_30(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 30."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 30, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_31(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 31."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 31, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_32(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 32."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 32, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_33(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 33."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 33, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_34(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 34."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 34, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_35(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 35."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 35, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_36(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 36."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 36, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_37(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 37."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 37, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_38(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 38."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 38, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_39(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 39."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 39, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_40(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 40."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 40, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_41(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 41."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 41, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_42(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 42."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 42, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_43(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 43."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 43, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_44(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 44."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 44, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_45(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 45."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 45, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_46(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 46."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 46, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_47(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 47."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 47, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_48(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 48."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 48, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_49(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 49."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 49, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_50(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 50."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 50, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_51(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 51."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 51, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_52(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 52."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 52, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_53(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 53."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 53, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_54(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 54."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 54, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_55(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 55."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 55, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_56(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 56."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 56, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_57(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 57."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 57, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_58(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 58."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 58, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_59(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 59."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 59, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_60(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 60."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 60, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_61(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 61."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 61, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_62(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 62."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 62, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_63(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 63."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 63, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_64(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 64."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 64, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_65(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 65."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 65, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_66(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 66."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 66, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_67(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 67."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 67, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_68(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 68."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 68, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_69(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 69."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 69, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_70(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 70."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 70, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_71(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 71."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 71, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_72(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 72."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 72, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_73(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 73."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 73, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_74(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 74."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 74, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_75(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 75."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 75, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_76(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 76."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 76, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_77(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 77."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 77, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_78(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 78."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 78, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_79(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 79."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 79, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_80(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 80."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 80, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_81(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 81."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 81, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_82(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 82."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 82, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_83(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 83."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 83, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_84(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 84."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 84, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_85(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 85."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 85, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_86(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 86."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 86, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_87(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 87."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 87, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_88(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 88."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 88, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_89(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 89."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 89, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_90(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 90."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 90, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_91(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 91."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 91, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_92(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 92."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 92, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_93(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 93."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 93, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_94(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 94."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 94, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_95(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 95."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 95, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_96(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 96."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 96, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_97(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 97."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 97, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_98(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 98."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 98, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_99(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 99."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 99, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_100(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 100."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 100, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_101(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 101."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 101, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_102(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 102."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 102, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_103(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 103."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 103, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_104(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 104."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 104, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_105(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 105."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 105, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_106(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 106."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 106, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_107(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 107."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 107, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_108(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 108."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 108, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_109(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 109."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 109, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_110(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 110."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 110, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_111(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 111."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 111, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_112(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 112."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 112, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_113(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 113."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 113, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_114(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 114."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 114, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_115(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 115."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 115, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_116(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 116."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 116, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_117(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 117."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 117, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_118(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 118."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 118, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_119(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 119."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 119, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_120(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 120."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 120, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_121(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 121."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 121, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_122(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 122."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 122, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_123(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 123."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 123, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_124(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 124."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 124, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_125(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 125."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 125, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_126(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 126."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 126, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_127(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 127."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 127, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_128(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 128."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 128, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}

def design_monostable_pulse_generator_129(target_width_ms: float, c_target_uf: float) -> dict[str, float]:
    """Calculate timing resistor Ra for target pulse duration 129."""
    t_sec = target_width_ms * 1e-3
    c_f = c_target_uf * 1e-6
    ra = t_sec / (1.1 * c_f)
    return {'design_id': 129, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}
