"""Three Op-Amp Instrumentation Amplifier architecture and CMRR sensitivity model."""
from __future__ import annotations
import math

def instrumentation_amplifier_gain(r1: float, rg: float, r2: float, r3: float) -> float:
    if rg <= 0 or r2 <= 0:
        raise ValueError("Resistances must be positive")
    preamp_gain = 1.0 + (2.0 * r1) / rg
    diff_gain = r3 / r2
    return preamp_gain * diff_gain

def calculate_cmrr_degradation(resistor_tolerance_percent: float, diff_gain: float) -> float:
    delta = resistor_tolerance_percent / 100.0
    worst_case_cmrr = diff_gain / (4.0 * delta) if delta > 0 else 1e9
    cmrr_db = 20.0 * math.log10(max(worst_case_cmrr, 1.0))
    return cmrr_db

def evaluate_ina_channel_spec_1(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 1."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 1, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_2(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 2."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 2, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_3(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 3."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 3, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_4(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 4."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 4, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_5(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 5."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 5, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_6(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 6."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 6, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_7(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 7."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 7, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_8(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 8."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 8, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_9(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 9."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 9, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_10(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 10."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 10, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_11(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 11."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 11, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_12(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 12."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 12, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_13(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 13."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 13, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_14(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 14."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 14, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_15(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 15."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 15, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_16(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 16."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 16, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_17(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 17."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 17, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_18(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 18."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 18, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_19(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 19."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 19, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_20(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 20."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 20, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_21(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 21."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 21, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_22(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 22."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 22, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_23(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 23."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 23, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_24(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 24."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 24, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_25(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 25."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 25, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_26(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 26."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 26, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_27(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 27."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 27, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_28(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 28."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 28, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_29(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 29."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 29, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_30(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 30."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 30, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_31(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 31."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 31, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_32(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 32."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 32, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_33(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 33."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 33, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_34(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 34."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 34, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_35(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 35."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 35, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_36(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 36."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 36, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_37(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 37."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 37, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_38(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 38."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 38, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_39(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 39."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 39, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_40(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 40."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 40, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_41(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 41."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 41, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_42(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 42."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 42, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_43(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 43."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 43, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_44(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 44."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 44, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_45(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 45."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 45, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_46(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 46."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 46, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_47(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 47."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 47, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_48(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 48."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 48, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_49(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 49."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 49, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_50(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 50."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 50, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_51(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 51."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 51, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_52(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 52."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 52, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_53(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 53."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 53, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_54(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 54."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 54, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_55(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 55."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 55, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_56(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 56."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 56, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_57(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 57."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 57, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_58(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 58."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 58, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_59(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 59."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 59, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_60(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 60."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 60, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_61(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 61."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 61, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_62(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 62."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 62, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_63(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 63."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 63, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_64(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 64."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 64, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_65(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 65."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 65, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_66(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 66."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 66, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_67(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 67."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 67, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_68(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 68."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 68, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_69(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 69."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 69, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_70(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 70."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 70, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_71(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 71."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 71, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_72(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 72."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 72, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_73(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 73."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 73, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_74(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 74."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 74, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_75(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 75."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 75, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_76(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 76."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 76, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_77(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 77."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 77, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_78(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 78."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 78, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_79(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 79."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 79, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_80(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 80."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 80, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_81(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 81."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 81, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_82(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 82."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 82, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_83(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 83."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 83, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_84(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 84."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 84, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_85(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 85."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 85, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_86(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 86."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 86, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_87(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 87."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 87, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_88(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 88."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 88, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_89(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 89."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 89, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_90(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 90."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 90, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_91(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 91."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 91, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_92(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 92."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 92, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_93(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 93."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 93, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_94(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 94."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 94, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_95(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 95."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 95, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_96(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 96."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 96, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_97(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 97."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 97, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_98(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 98."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 98, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_99(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 99."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 99, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_100(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 100."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 100, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_101(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 101."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 101, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_102(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 102."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 102, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_103(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 103."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 103, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_104(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 104."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 104, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_105(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 105."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 105, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_106(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 106."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 106, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_107(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 107."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 107, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_108(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 108."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 108, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_109(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 109."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 109, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_110(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 110."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 110, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_111(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 111."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 111, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_112(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 112."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 112, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_113(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 113."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 113, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_114(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 114."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 114, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_115(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 115."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 115, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_116(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 116."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 116, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_117(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 117."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 117, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_118(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 118."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 118, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_119(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 119."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 119, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_120(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 120."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 120, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_121(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 121."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 121, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_122(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 122."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 122, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_123(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 123."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 123, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_124(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 124."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 124, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_125(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 125."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 125, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_126(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 126."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 126, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_127(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 127."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 127, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_128(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 128."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 128, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}

def evaluate_ina_channel_spec_129(v_diff_mv: float, v_cm_v: float, rg_ohm: float) -> dict[str, float]:
    """Simulate biomedical/industrial instrumentation transducer channel 129."""
    gain = 1.0 + (100000.0 / rg_ohm)
    v_out_signal = (v_diff_mv * 1e-3) * gain
    v_out_error = v_cm_v * (gain / 10000.0)
    snr = 20.0 * math.log10(abs(v_out_signal / (v_out_error + 1e-12)))
    return {'channel': 129, 'gain': gain, 'v_out': v_out_signal, 'error': v_out_error, 'snr': snr}
