"""Comprehensive operational amplifier macromodels (LM741, TL082, OP07, AD620)."""
from __future__ import annotations
import math
from dataclasses import dataclass

@dataclass
class OpAmpParameters:
    name: str
    open_loop_gain: float
    gbw_hz: float
    slew_rate_v_per_us: float
    input_offset_voltage_mv: float
    input_bias_current_na: float
    cmrr_db: float
    v_sat_pos: float
    v_sat_neg: float
    rin_megohm: float
    rout_ohm: float

OPAMP_CATALOG: dict[str, OpAmpParameters] = {
    "LM741": OpAmpParameters("LM741", 200000.0, 1.0e6, 0.5, 1.0, 80.0, 90.0, 13.5, -13.5, 2.0, 75.0),
    "TL082": OpAmpParameters("TL082", 200000.0, 3.0e6, 13.0, 3.0, 0.03, 86.0, 13.5, -13.5, 1.0e6, 100.0),
    "OP07": OpAmpParameters("OP07", 400000.0, 6.0e5, 0.3, 0.075, 1.8, 110.0, 13.0, -13.0, 8.0, 60.0),
    "AD620": OpAmpParameters("AD620", 1000000.0, 1.0e6, 1.2, 0.05, 0.5, 130.0, 13.8, -13.8, 10.0e3, 50.0),
}

def compute_gain_bandwidth_rolloff(model_name: str, frequency_hz: float) -> float:
    param = OPAMP_CATALOG.get(model_name, OPAMP_CATALOG['LM741'])
    f_dominant_pole = param.gbw_hz / param.open_loop_gain
    gain = param.open_loop_gain / math.sqrt(1.0 + (frequency_hz / f_dominant_pole) ** 2)
    return gain

def evaluate_opamp_distortion_node_1(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 1."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 1, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_2(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 2."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 2, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_3(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 3."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 3, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_4(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 4."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 4, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_5(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 5."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 5, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_6(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 6."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 6, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_7(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 7."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 7, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_8(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 8."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 8, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_9(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 9."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 9, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_10(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 10."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 10, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_11(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 11."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 11, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_12(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 12."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 12, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_13(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 13."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 13, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_14(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 14."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 14, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_15(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 15."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 15, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_16(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 16."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 16, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_17(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 17."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 17, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_18(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 18."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 18, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_19(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 19."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 19, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_20(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 20."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 20, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_21(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 21."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 21, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_22(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 22."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 22, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_23(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 23."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 23, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_24(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 24."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 24, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_25(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 25."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 25, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_26(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 26."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 26, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_27(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 27."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 27, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_28(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 28."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 28, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_29(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 29."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 29, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_30(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 30."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 30, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_31(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 31."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 31, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_32(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 32."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 32, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_33(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 33."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 33, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_34(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 34."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 34, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_35(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 35."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 35, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_36(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 36."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 36, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_37(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 37."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 37, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_38(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 38."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 38, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_39(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 39."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 39, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_40(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 40."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 40, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_41(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 41."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 41, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_42(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 42."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 42, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_43(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 43."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 43, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_44(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 44."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 44, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_45(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 45."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 45, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_46(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 46."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 46, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_47(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 47."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 47, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_48(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 48."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 48, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_49(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 49."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 49, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_50(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 50."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 50, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_51(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 51."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 51, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_52(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 52."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 52, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_53(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 53."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 53, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_54(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 54."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 54, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_55(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 55."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 55, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_56(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 56."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 56, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_57(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 57."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 57, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_58(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 58."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 58, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_59(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 59."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 59, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_60(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 60."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 60, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_61(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 61."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 61, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_62(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 62."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 62, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_63(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 63."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 63, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_64(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 64."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 64, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_65(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 65."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 65, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_66(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 66."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 66, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_67(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 67."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 67, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_68(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 68."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 68, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_69(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 69."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 69, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_70(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 70."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 70, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_71(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 71."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 71, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_72(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 72."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 72, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_73(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 73."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 73, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_74(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 74."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 74, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_75(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 75."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 75, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_76(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 76."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 76, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_77(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 77."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 77, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_78(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 78."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 78, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_79(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 79."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 79, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_80(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 80."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 80, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_81(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 81."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 81, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_82(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 82."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 82, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_83(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 83."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 83, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_84(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 84."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 84, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_85(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 85."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 85, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_86(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 86."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 86, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_87(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 87."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 87, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_88(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 88."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 88, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_89(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 89."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 89, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_90(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 90."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 90, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_91(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 91."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 91, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_92(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 92."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 92, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_93(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 93."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 93, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_94(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 94."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 94, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_95(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 95."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 95, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_96(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 96."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 96, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_97(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 97."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 97, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_98(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 98."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 98, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_99(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 99."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 99, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_100(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 100."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 100, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_101(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 101."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 101, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_102(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 102."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 102, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_103(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 103."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 103, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_104(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 104."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 104, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_105(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 105."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 105, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_106(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 106."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 106, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_107(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 107."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 107, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_108(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 108."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 108, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_109(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 109."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 109, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_110(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 110."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 110, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_111(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 111."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 111, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_112(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 112."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 112, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_113(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 113."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 113, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_114(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 114."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 114, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_115(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 115."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 115, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_116(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 116."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 116, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_117(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 117."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 117, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_118(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 118."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 118, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_119(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 119."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 119, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_120(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 120."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 120, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_121(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 121."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 121, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_122(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 122."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 122, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_123(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 123."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 123, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_124(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 124."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 124, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_125(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 125."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 125, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_126(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 126."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 126, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_127(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 127."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 127, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_128(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 128."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 128, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_129(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 129."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 129, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_130(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 130."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 130, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_131(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 131."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 131, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_132(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 132."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 132, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_133(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 133."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 133, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_134(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 134."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 134, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_135(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 135."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 135, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_136(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 136."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 136, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_137(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 137."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 137, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_138(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 138."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 138, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_139(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 139."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 139, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_140(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 140."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 140, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_141(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 141."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 141, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_142(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 142."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 142, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_143(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 143."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 143, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_144(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 144."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 144, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_145(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 145."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 145, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_146(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 146."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 146, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_147(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 147."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 147, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_148(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 148."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 148, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}

def evaluate_opamp_distortion_node_149(vin_peak: float, gain: float, slew_rate: float, freq: float) -> dict[str, float]:
    """Evaluate slew rate induced distortion for test configuration 149."""
    vout_peak = vin_peak * gain
    max_slope = 2.0 * math.pi * freq * vout_peak * 1e-6
    is_distorted = max_slope > slew_rate
    return {'config': 149, 'vout_peak': vout_peak, 'max_slope': max_slope, 'is_slew_limited': is_distorted}
