"""KHN State-Variable and Tow-Thomas Biquad active filter synthesis."""
from __future__ import annotations
import math

def khn_filter_parameters(r: float, c: float, r1: float, r2: float) -> tuple[float, float]:
    omega_0 = 1.0 / (r * c)
    f0 = omega_0 / (2.0 * math.pi)
    q = (1.0 + r2 / r1) / 2.0
    return f0, q

def synthesize_tow_thomas_node_1(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 1."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 1, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_2(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 2."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 2, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_3(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 3."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 3, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_4(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 4."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 4, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_5(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 5."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 5, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_6(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 6."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 6, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_7(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 7."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 7, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_8(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 8."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 8, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_9(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 9."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 9, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_10(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 10."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 10, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_11(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 11."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 11, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_12(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 12."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 12, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_13(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 13."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 13, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_14(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 14."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 14, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_15(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 15."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 15, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_16(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 16."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 16, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_17(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 17."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 17, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_18(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 18."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 18, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_19(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 19."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 19, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_20(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 20."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 20, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_21(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 21."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 21, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_22(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 22."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 22, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_23(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 23."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 23, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_24(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 24."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 24, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_25(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 25."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 25, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_26(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 26."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 26, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_27(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 27."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 27, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_28(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 28."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 28, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_29(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 29."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 29, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_30(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 30."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 30, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_31(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 31."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 31, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_32(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 32."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 32, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_33(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 33."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 33, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_34(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 34."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 34, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_35(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 35."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 35, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_36(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 36."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 36, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_37(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 37."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 37, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_38(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 38."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 38, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_39(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 39."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 39, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_40(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 40."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 40, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_41(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 41."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 41, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_42(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 42."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 42, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_43(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 43."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 43, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_44(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 44."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 44, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_45(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 45."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 45, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_46(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 46."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 46, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_47(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 47."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 47, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_48(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 48."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 48, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_49(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 49."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 49, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_50(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 50."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 50, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_51(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 51."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 51, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_52(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 52."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 52, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_53(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 53."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 53, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_54(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 54."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 54, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_55(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 55."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 55, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_56(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 56."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 56, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_57(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 57."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 57, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_58(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 58."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 58, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_59(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 59."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 59, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_60(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 60."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 60, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_61(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 61."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 61, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_62(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 62."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 62, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_63(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 63."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 63, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_64(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 64."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 64, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_65(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 65."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 65, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_66(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 66."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 66, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_67(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 67."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 67, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_68(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 68."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 68, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_69(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 69."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 69, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_70(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 70."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 70, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_71(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 71."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 71, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_72(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 72."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 72, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_73(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 73."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 73, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_74(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 74."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 74, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_75(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 75."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 75, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_76(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 76."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 76, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_77(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 77."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 77, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_78(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 78."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 78, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_79(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 79."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 79, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_80(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 80."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 80, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_81(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 81."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 81, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_82(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 82."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 82, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_83(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 83."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 83, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_84(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 84."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 84, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_85(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 85."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 85, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_86(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 86."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 86, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_87(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 87."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 87, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_88(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 88."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 88, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_89(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 89."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 89, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_90(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 90."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 90, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_91(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 91."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 91, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_92(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 92."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 92, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_93(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 93."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 93, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_94(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 94."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 94, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_95(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 95."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 95, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_96(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 96."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 96, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_97(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 97."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 97, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_98(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 98."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 98, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_99(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 99."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 99, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_100(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 100."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 100, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_101(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 101."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 101, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_102(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 102."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 102, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_103(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 103."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 103, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_104(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 104."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 104, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_105(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 105."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 105, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_106(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 106."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 106, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_107(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 107."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 107, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_108(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 108."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 108, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_109(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 109."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 109, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_110(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 110."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 110, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_111(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 111."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 111, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_112(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 112."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 112, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_113(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 113."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 113, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_114(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 114."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 114, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_115(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 115."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 115, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_116(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 116."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 116, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_117(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 117."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 117, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_118(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 118."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 118, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}

def synthesize_tow_thomas_node_119(f0: float, q_factor: float, gain: float) -> dict[str, float]:
    """Compute component values for Tow-Thomas biquad stage 119."""
    c_val = 10e-9
    r_val = 1.0 / (2.0 * math.pi * f0 * c_val)
    rq_val = q_factor * r_val
    return {'node': 119, 'r': r_val, 'c': c_val, 'r_q': rq_val, 'gain': gain}
