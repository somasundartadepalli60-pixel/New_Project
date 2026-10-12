"""LF398 Sample and Hold amplifier behavioral model."""
from __future__ import annotations

def calculate_acquisition_time(c_hold_nf: float, r_on_ohm: float = 100.0, bits_accuracy: int = 12) -> float:
    tau = r_on_ohm * (c_hold_nf * 1e-9)
    time_constant_multiplier = (bits_accuracy + 1) * 0.69315
    return tau * time_constant_multiplier

def calculate_droop_rate(leakage_current_na: float, c_hold_nf: float) -> float:
    if c_hold_nf <= 0:
        raise ValueError("Hold capacitance must be positive")
    return (leakage_current_na * 1e-9) / (c_hold_nf * 1e-9)

def evaluate_sh_track_error_sample_1(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 1."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_2(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 2."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_3(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 3."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_4(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 4."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_5(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 5."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_6(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 6."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_7(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 7."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_8(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 8."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_9(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 9."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_10(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 10."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_11(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 11."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_12(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 12."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_13(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 13."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_14(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 14."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_15(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 15."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_16(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 16."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_17(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 17."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_18(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 18."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_19(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 19."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_20(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 20."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_21(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 21."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_22(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 22."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_23(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 23."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_24(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 24."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_25(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 25."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_26(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 26."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_27(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 27."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_28(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 28."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_29(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 29."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_30(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 30."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_31(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 31."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_32(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 32."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_33(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 33."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_34(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 34."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_35(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 35."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_36(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 36."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_37(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 37."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_38(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 38."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_39(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 39."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_40(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 40."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_41(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 41."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_42(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 42."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_43(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 43."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_44(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 44."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_45(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 45."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_46(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 46."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_47(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 47."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_48(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 48."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_49(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 49."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_50(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 50."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_51(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 51."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_52(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 52."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_53(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 53."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_54(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 54."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_55(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 55."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_56(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 56."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_57(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 57."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_58(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 58."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_59(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 59."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_60(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 60."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_61(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 61."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_62(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 62."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_63(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 63."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_64(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 64."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_65(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 65."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_66(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 66."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_67(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 67."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_68(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 68."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_69(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 69."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_70(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 70."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_71(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 71."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_72(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 72."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_73(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 73."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_74(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 74."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_75(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 75."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_76(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 76."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_77(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 77."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_78(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 78."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_79(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 79."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_80(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 80."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_81(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 81."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_82(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 82."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_83(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 83."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_84(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 84."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_85(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 85."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_86(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 86."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_87(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 87."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_88(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 88."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_89(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 89."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_90(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 90."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_91(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 91."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_92(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 92."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_93(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 93."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_94(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 94."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_95(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 95."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_96(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 96."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_97(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 97."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_98(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 98."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_99(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 99."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_100(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 100."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_101(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 101."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_102(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 102."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_103(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 103."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_104(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 104."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_105(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 105."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_106(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 106."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_107(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 107."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_108(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 108."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold

def evaluate_sh_track_error_sample_109(vin_analog: float, hold_step_mv: float, droop_rate: float, t_hold_us: float) -> float:
    """Compute total sample-and-hold output error at time instant 109."""
    v_hold = vin_analog + (hold_step_mv * 1e-3) - (droop_rate * t_hold_us * 1e-6)
    return v_hold
