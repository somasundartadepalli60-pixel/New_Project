"""LM566 Voltage-Controlled Oscillator (VCO) mathematical model."""
from __future__ import annotations

def vco566_output_frequency(vcc: float, vc: float, r1: float, c1: float) -> float:
    if r1 <= 0 or c1 <= 0 or vcc <= 0:
        raise ValueError("Circuit parameters must be positive")
    # Classical NE/SE566 equation: fo = 2*(Vcc - Vc) / (R1 * C1 * Vcc)
    return (2.0 * (vcc - vc)) / (r1 * c1 * vcc)

def vco566_conversion_gain(vcc: float, r1: float, c1: float) -> float:
    # Ko = df_o / dVc in rad/s/V
    df_dvc = -2.0 / (r1 * c1 * vcc)
    return abs(2.0 * 3.14159265 * df_dvc)

def evaluate_vco566_linear_sweep_1(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 1."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 1, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_2(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 2."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 2, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_3(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 3."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 3, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_4(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 4."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 4, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_5(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 5."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 5, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_6(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 6."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 6, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_7(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 7."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 7, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_8(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 8."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 8, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_9(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 9."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 9, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_10(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 10."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 10, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_11(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 11."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 11, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_12(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 12."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 12, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_13(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 13."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 13, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_14(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 14."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 14, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_15(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 15."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 15, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_16(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 16."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 16, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_17(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 17."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 17, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_18(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 18."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 18, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_19(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 19."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 19, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_20(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 20."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 20, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_21(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 21."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 21, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_22(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 22."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 22, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_23(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 23."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 23, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_24(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 24."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 24, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_25(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 25."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 25, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_26(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 26."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 26, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_27(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 27."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 27, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_28(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 28."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 28, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_29(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 29."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 29, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_30(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 30."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 30, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_31(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 31."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 31, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_32(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 32."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 32, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_33(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 33."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 33, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_34(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 34."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 34, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_35(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 35."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 35, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_36(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 36."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 36, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_37(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 37."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 37, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_38(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 38."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 38, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_39(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 39."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 39, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_40(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 40."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 40, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_41(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 41."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 41, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_42(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 42."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 42, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_43(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 43."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 43, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_44(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 44."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 44, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_45(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 45."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 45, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_46(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 46."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 46, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_47(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 47."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 47, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_48(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 48."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 48, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_49(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 49."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 49, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_50(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 50."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 50, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_51(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 51."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 51, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_52(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 52."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 52, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_53(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 53."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 53, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_54(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 54."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 54, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_55(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 55."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 55, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_56(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 56."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 56, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_57(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 57."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 57, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_58(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 58."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 58, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_59(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 59."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 59, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_60(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 60."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 60, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_61(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 61."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 61, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_62(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 62."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 62, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_63(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 63."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 63, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_64(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 64."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 64, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_65(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 65."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 65, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_66(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 66."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 66, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_67(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 67."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 67, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_68(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 68."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 68, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_69(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 69."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 69, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_70(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 70."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 70, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_71(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 71."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 71, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_72(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 72."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 72, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_73(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 73."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 73, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_74(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 74."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 74, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_75(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 75."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 75, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_76(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 76."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 76, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_77(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 77."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 77, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_78(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 78."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 78, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_79(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 79."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 79, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_80(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 80."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 80, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_81(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 81."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 81, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_82(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 82."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 82, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_83(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 83."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 83, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_84(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 84."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 84, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_85(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 85."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 85, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_86(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 86."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 86, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_87(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 87."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 87, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_88(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 88."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 88, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_89(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 89."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 89, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_90(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 90."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 90, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_91(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 91."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 91, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_92(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 92."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 92, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_93(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 93."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 93, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_94(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 94."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 94, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_95(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 95."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 95, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_96(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 96."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 96, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_97(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 97."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 97, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_98(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 98."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 98, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_99(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 99."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 99, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_100(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 100."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 100, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_101(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 101."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 101, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_102(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 102."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 102, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_103(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 103."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 103, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_104(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 104."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 104, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_105(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 105."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 105, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_106(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 106."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 106, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_107(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 107."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 107, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_108(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 108."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 108, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_109(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 109."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 109, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_110(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 110."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 110, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_111(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 111."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 111, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_112(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 112."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 112, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_113(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 113."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 113, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_114(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 114."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 114, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_115(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 115."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 115, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_116(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 116."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 116, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_117(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 117."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 117, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_118(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 118."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 118, 'vc': v_control, 'f_out': f_out}

def evaluate_vco566_linear_sweep_119(v_control: float) -> dict[str, float]:
    """Compute VCO output frequency for voltage tuning point 119."""
    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)
    return {'point': 119, 'vc': v_control, 'f_out': f_out}
