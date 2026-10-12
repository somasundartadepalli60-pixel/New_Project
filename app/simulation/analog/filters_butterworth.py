"""Butterworth Sallen-Key and Multiple-Feedback active filter synthesis."""
from __future__ import annotations
import math

def butterworth_sallen_key_lowpass(fc_hz: float, r_val: float) -> tuple[float, float]:
    omega_c = 2.0 * math.pi * fc_hz
    c1 = math.sqrt(2.0) / (omega_c * r_val)
    c2 = 1.0 / (math.sqrt(2.0) * omega_c * r_val)
    return c1, c2

def butterworth_transfer_magnitude(order: int, fc_hz: float, freq_hz: float) -> float:
    ratio = freq_hz / fc_hz
    mag = 1.0 / math.sqrt(1.0 + ratio ** (2 * order))
    return mag

def design_butterworth_stage_1(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 1."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 1, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_2(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 2."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 2, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_3(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 3."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 3, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_4(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 4."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 4, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_5(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 5."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 5, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_6(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 6."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 6, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_7(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 7."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 7, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_8(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 8."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 8, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_9(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 9."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 9, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_10(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 10."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 10, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_11(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 11."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 11, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_12(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 12."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 12, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_13(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 13."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 13, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_14(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 14."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 14, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_15(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 15."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 15, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_16(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 16."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 16, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_17(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 17."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 17, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_18(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 18."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 18, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_19(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 19."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 19, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_20(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 20."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 20, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_21(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 21."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 21, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_22(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 22."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 22, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_23(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 23."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 23, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_24(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 24."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 24, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_25(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 25."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 25, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_26(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 26."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 26, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_27(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 27."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 27, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_28(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 28."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 28, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_29(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 29."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 29, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_30(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 30."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 30, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_31(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 31."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 31, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_32(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 32."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 32, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_33(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 33."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 33, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_34(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 34."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 34, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_35(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 35."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 35, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_36(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 36."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 36, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_37(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 37."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 37, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_38(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 38."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 38, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_39(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 39."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 39, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_40(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 40."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 40, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_41(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 41."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 41, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_42(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 42."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 42, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_43(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 43."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 43, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_44(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 44."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 44, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_45(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 45."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 45, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_46(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 46."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 46, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_47(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 47."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 47, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_48(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 48."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 48, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_49(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 49."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 49, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_50(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 50."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 50, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_51(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 51."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 51, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_52(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 52."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 52, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_53(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 53."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 53, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_54(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 54."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 54, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_55(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 55."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 55, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_56(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 56."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 56, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_57(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 57."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 57, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_58(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 58."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 58, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_59(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 59."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 59, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_60(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 60."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 60, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_61(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 61."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 61, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_62(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 62."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 62, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_63(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 63."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 63, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_64(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 64."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 64, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_65(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 65."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 65, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_66(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 66."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 66, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_67(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 67."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 67, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_68(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 68."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 68, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_69(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 69."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 69, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_70(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 70."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 70, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_71(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 71."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 71, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_72(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 72."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 72, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_73(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 73."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 73, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_74(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 74."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 74, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_75(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 75."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 75, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_76(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 76."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 76, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_77(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 77."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 77, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_78(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 78."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 78, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_79(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 79."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 79, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_80(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 80."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 80, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_81(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 81."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 81, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_82(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 82."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 82, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_83(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 83."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 83, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_84(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 84."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 84, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_85(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 85."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 85, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_86(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 86."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 86, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_87(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 87."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 87, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_88(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 88."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 88, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_89(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 89."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 89, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_90(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 90."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 90, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_91(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 91."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 91, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_92(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 92."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 92, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_93(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 93."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 93, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_94(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 94."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 94, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_95(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 95."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 95, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_96(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 96."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 96, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_97(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 97."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 97, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_98(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 98."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 98, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_99(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 99."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 99, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_100(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 100."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 100, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_101(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 101."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 101, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_102(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 102."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 102, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_103(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 103."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 103, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_104(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 104."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 104, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_105(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 105."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 105, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_106(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 106."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 106, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_107(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 107."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 107, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_108(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 108."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 108, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_109(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 109."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 109, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_110(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 110."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 110, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_111(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 111."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 111, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_112(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 112."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 112, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_113(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 113."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 113, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_114(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 114."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 114, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_115(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 115."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 115, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_116(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 116."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 116, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_117(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 117."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 117, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_118(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 118."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 118, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_119(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 119."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 119, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_120(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 120."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 120, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_121(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 121."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 121, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_122(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 122."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 122, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_123(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 123."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 123, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_124(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 124."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 124, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_125(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 125."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 125, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_126(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 126."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 126, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_127(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 127."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 127, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_128(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 128."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 128, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_129(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 129."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 129, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_130(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 130."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 130, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_131(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 131."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 131, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_132(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 132."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 132, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_133(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 133."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 133, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_134(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 134."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 134, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_135(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 135."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 135, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_136(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 136."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 136, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_137(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 137."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 137, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_138(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 138."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 138, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}

def design_butterworth_stage_139(order: int, fc: float, gain: float) -> dict[str, float]:
    """Compute attenuation and phase roll-off for filter specification 139."""
    attenuation_octave = 6.02 * order
    attenuation_decade = 20.0 * order
    f_3db = fc
    return {'spec_id': 139, 'order': order, 'attenuation_octave': attenuation_octave, 'attenuation_decade': attenuation_decade}
