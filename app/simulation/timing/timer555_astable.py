"""555 Astable Multivibrator oscillation parameters and duty cycle control."""
from __future__ import annotations

def astable_timing_parameters(ra_ohm: float, rb_ohm: float, c_farad: float) -> dict[str, float]:
    if ra_ohm <= 0 or rb_ohm <= 0 or c_farad <= 0:
        raise ValueError("Components must be positive")
    t_high = 0.693 * (ra_ohm + rb_ohm) * c_farad
    t_low = 0.693 * rb_ohm * c_farad
    period = t_high + t_low
    freq = 1.44 / ((ra_ohm + 2.0 * rb_ohm) * c_farad)
    duty_cycle = (ra_ohm + rb_ohm) / (ra_ohm + 2.0 * rb_ohm)
    return {
        "t_high": t_high,
        "t_low": t_low,
        "period": period,
        "frequency_hz": freq,
        "duty_cycle": duty_cycle,
    }

def design_astable_oscillator_stage_1(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 1."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 1, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_2(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 2."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 2, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_3(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 3."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 3, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_4(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 4."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 4, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_5(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 5."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 5, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_6(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 6."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 6, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_7(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 7."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 7, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_8(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 8."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 8, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_9(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 9."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 9, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_10(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 10."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 10, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_11(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 11."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 11, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_12(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 12."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 12, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_13(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 13."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 13, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_14(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 14."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 14, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_15(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 15."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 15, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_16(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 16."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 16, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_17(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 17."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 17, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_18(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 18."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 18, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_19(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 19."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 19, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_20(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 20."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 20, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_21(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 21."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 21, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_22(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 22."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 22, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_23(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 23."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 23, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_24(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 24."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 24, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_25(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 25."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 25, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_26(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 26."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 26, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_27(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 27."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 27, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_28(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 28."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 28, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_29(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 29."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 29, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_30(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 30."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 30, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_31(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 31."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 31, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_32(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 32."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 32, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_33(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 33."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 33, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_34(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 34."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 34, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_35(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 35."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 35, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_36(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 36."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 36, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_37(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 37."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 37, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_38(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 38."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 38, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_39(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 39."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 39, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_40(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 40."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 40, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_41(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 41."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 41, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_42(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 42."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 42, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_43(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 43."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 43, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_44(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 44."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 44, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_45(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 45."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 45, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_46(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 46."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 46, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_47(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 47."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 47, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_48(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 48."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 48, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_49(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 49."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 49, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_50(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 50."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 50, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_51(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 51."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 51, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_52(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 52."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 52, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_53(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 53."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 53, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_54(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 54."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 54, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_55(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 55."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 55, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_56(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 56."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 56, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_57(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 57."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 57, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_58(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 58."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 58, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_59(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 59."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 59, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_60(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 60."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 60, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_61(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 61."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 61, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_62(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 62."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 62, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_63(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 63."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 63, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_64(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 64."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 64, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_65(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 65."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 65, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_66(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 66."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 66, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_67(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 67."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 67, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_68(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 68."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 68, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_69(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 69."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 69, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_70(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 70."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 70, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_71(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 71."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 71, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_72(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 72."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 72, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_73(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 73."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 73, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_74(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 74."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 74, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_75(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 75."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 75, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_76(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 76."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 76, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_77(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 77."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 77, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_78(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 78."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 78, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_79(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 79."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 79, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_80(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 80."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 80, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_81(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 81."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 81, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_82(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 82."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 82, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_83(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 83."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 83, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_84(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 84."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 84, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_85(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 85."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 85, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_86(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 86."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 86, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_87(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 87."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 87, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_88(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 88."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 88, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_89(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 89."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 89, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_90(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 90."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 90, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_91(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 91."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 91, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_92(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 92."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 92, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_93(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 93."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 93, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_94(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 94."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 94, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_95(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 95."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 95, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_96(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 96."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 96, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_97(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 97."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 97, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_98(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 98."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 98, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_99(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 99."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 99, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_100(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 100."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 100, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_101(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 101."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 101, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_102(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 102."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 102, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_103(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 103."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 103, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_104(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 104."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 104, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_105(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 105."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 105, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_106(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 106."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 106, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_107(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 107."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 107, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_108(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 108."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 108, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_109(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 109."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 109, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_110(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 110."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 110, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_111(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 111."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 111, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_112(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 112."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 112, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_113(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 113."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 113, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_114(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 114."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 114, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_115(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 115."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 115, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_116(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 116."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 116, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_117(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 117."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 117, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_118(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 118."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 118, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_119(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 119."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 119, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_120(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 120."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 120, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_121(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 121."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 121, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_122(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 122."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 122, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_123(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 123."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 123, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_124(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 124."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 124, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_125(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 125."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 125, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_126(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 126."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 126, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_127(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 127."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 127, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_128(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 128."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 128, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}

def design_astable_oscillator_stage_129(target_freq_khz: float, duty_target: float) -> dict[str, float]:
    """Synthesize Ra and Rb values for astable frequency specification 129."""
    c_val = 10e-9
    f_hz = target_freq_khz * 1e3
    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)
    r_total = 1.44 / (f_hz * c_val)
    rb = r_total * (1.0 - duty_target)
    ra = r_total - 2.0 * rb
    return {'stage_id': 129, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}
