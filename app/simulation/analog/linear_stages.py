"""Linear op-amp stage models: Inverting, Non-inverting, Summing, Difference, Integrator."""
from __future__ import annotations
import math

def inverting_amplifier_gain(r_in: float, r_feedback: float) -> float:
    if r_in <= 0:
        raise ValueError("r_in must be positive")
    return -r_feedback / r_in

def non_inverting_amplifier_gain(r1: float, r_feedback: float) -> float:
    if r1 <= 0:
        raise ValueError("r1 must be positive")
    return 1.0 + (r_feedback / r1)

def summing_amplifier_output(inputs: list[tuple[float, float]], r_feedback: float) -> float:
    v_out = 0.0
    for v_in, r_in in inputs:
        v_out -= (r_feedback / r_in) * v_in
    return v_out

def difference_amplifier_output(v1: float, v2: float, r1: float, r2: float, r3: float, r4: float) -> float:
    # Standard differential topology with R1, R2 at inverting and R3, R4 at non-inverting
    v_plus = v2 * (r4 / (r3 + r4))
    v_out = v_plus * (1.0 + r2 / r1) - v1 * (r2 / r1)
    return v_out

def design_inverting_stage_metric_1(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 1."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 1, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_2(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 2."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 2, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_3(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 3."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 3, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_4(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 4."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 4, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_5(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 5."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 5, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_6(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 6."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 6, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_7(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 7."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 7, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_8(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 8."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 8, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_9(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 9."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 9, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_10(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 10."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 10, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_11(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 11."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 11, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_12(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 12."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 12, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_13(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 13."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 13, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_14(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 14."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 14, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_15(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 15."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 15, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_16(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 16."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 16, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_17(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 17."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 17, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_18(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 18."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 18, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_19(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 19."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 19, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_20(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 20."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 20, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_21(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 21."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 21, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_22(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 22."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 22, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_23(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 23."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 23, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_24(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 24."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 24, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_25(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 25."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 25, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_26(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 26."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 26, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_27(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 27."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 27, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_28(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 28."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 28, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_29(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 29."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 29, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_30(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 30."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 30, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_31(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 31."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 31, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_32(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 32."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 32, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_33(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 33."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 33, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_34(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 34."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 34, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_35(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 35."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 35, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_36(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 36."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 36, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_37(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 37."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 37, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_38(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 38."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 38, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_39(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 39."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 39, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_40(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 40."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 40, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_41(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 41."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 41, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_42(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 42."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 42, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_43(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 43."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 43, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_44(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 44."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 44, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_45(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 45."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 45, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_46(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 46."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 46, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_47(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 47."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 47, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_48(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 48."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 48, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_49(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 49."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 49, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_50(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 50."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 50, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_51(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 51."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 51, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_52(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 52."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 52, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_53(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 53."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 53, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_54(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 54."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 54, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_55(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 55."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 55, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_56(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 56."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 56, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_57(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 57."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 57, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_58(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 58."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 58, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_59(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 59."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 59, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_60(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 60."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 60, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_61(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 61."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 61, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_62(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 62."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 62, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_63(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 63."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 63, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_64(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 64."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 64, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_65(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 65."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 65, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_66(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 66."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 66, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_67(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 67."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 67, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_68(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 68."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 68, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_69(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 69."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 69, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_70(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 70."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 70, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_71(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 71."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 71, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_72(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 72."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 72, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_73(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 73."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 73, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_74(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 74."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 74, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_75(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 75."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 75, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_76(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 76."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 76, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_77(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 77."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 77, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_78(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 78."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 78, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_79(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 79."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 79, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_80(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 80."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 80, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_81(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 81."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 81, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_82(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 82."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 82, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_83(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 83."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 83, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_84(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 84."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 84, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_85(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 85."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 85, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_86(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 86."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 86, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_87(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 87."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 87, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_88(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 88."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 88, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_89(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 89."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 89, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_90(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 90."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 90, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_91(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 91."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 91, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_92(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 92."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 92, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_93(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 93."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 93, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_94(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 94."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 94, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_95(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 95."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 95, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_96(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 96."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 96, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_97(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 97."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 97, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_98(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 98."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 98, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_99(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 99."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 99, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_100(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 100."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 100, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_101(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 101."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 101, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_102(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 102."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 102, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_103(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 103."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 103, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_104(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 104."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 104, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_105(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 105."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 105, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_106(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 106."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 106, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_107(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 107."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 107, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_108(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 108."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 108, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_109(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 109."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 109, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_110(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 110."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 110, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_111(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 111."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 111, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_112(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 112."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 112, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_113(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 113."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 113, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_114(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 114."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 114, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_115(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 115."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 115, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_116(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 116."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 116, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_117(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 117."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 117, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_118(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 118."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 118, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_119(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 119."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 119, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_120(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 120."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 120, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_121(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 121."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 121, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_122(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 122."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 122, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_123(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 123."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 123, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_124(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 124."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 124, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_125(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 125."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 125, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_126(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 126."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 126, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_127(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 127."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 127, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_128(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 128."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 128, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_129(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 129."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 129, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_130(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 130."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 130, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_131(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 131."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 131, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_132(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 132."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 132, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_133(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 133."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 133, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_134(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 134."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 134, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_135(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 135."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 135, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_136(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 136."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 136, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_137(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 137."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 137, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_138(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 138."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 138, 'r1': r1, 'rf': rf, 'r_comp': r_comp}

def design_inverting_stage_metric_139(target_gain: float, input_z: float) -> dict[str, float]:
    """Compute precision resistor parameters for linear amplifier design 139."""
    r1 = input_z
    rf = abs(target_gain) * r1
    r_comp = (r1 * rf) / (r1 + rf)
    return {'design_index': 139, 'r1': r1, 'rf': rf, 'r_comp': r_comp}
