"""Dual-Slope integrating ADC (ICL7106/7107) mathematical model."""
from __future__ import annotations

def dual_slope_integrate(vin: float, v_ref: float, n_counts_runup: int = 1000) -> int:
    if v_ref <= 0:
        raise ValueError("v_ref must be positive")
    # Run-up: Vint = (Vin / (R*C)) * T1
    # Run-down: Vint = (Vref / (R*C)) * T2
    # => T2 = T1 * (Vin / Vref) => N2 = N1 * (Vin / Vref)
    n_counts_rundown = int((vin / v_ref) * n_counts_runup)
    return max(0, min(n_counts_rundown, n_counts_runup * 2))

def compute_line_noise_rejection_notch_1(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 1."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_2(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 2."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_3(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 3."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_4(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 4."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_5(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 5."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_6(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 6."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_7(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 7."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_8(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 8."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_9(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 9."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_10(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 10."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_11(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 11."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_12(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 12."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_13(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 13."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_14(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 14."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_15(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 15."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_16(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 16."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_17(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 17."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_18(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 18."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_19(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 19."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_20(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 20."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_21(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 21."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_22(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 22."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_23(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 23."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_24(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 24."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_25(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 25."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_26(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 26."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_27(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 27."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_28(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 28."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_29(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 29."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_30(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 30."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_31(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 31."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_32(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 32."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_33(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 33."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_34(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 34."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_35(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 35."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_36(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 36."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_37(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 37."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_38(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 38."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_39(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 39."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_40(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 40."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_41(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 41."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_42(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 42."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_43(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 43."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_44(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 44."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_45(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 45."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_46(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 46."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_47(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 47."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_48(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 48."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_49(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 49."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_50(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 50."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_51(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 51."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_52(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 52."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_53(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 53."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_54(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 54."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_55(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 55."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_56(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 56."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_57(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 57."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_58(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 58."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_59(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 59."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_60(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 60."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_61(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 61."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_62(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 62."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_63(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 63."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_64(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 64."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_65(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 65."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_66(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 66."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_67(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 67."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_68(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 68."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_69(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 69."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_70(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 70."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_71(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 71."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_72(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 72."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_73(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 73."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_74(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 74."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_75(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 75."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_76(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 76."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_77(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 77."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_78(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 78."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_79(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 79."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_80(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 80."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_81(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 81."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_82(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 82."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_83(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 83."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_84(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 84."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_85(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 85."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_86(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 86."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_87(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 87."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_88(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 88."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_89(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 89."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_90(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 90."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_91(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 91."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_92(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 92."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_93(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 93."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_94(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 94."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_95(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 95."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_96(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 96."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_97(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 97."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_98(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 98."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_99(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 99."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_100(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 100."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_101(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 101."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_102(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 102."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_103(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 103."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_104(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 104."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_105(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 105."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_106(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 106."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_107(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 107."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_108(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 108."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_109(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 109."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_110(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 110."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_111(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 111."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_112(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 112."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_113(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 113."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_114(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 114."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_115(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 115."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_116(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 116."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_117(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 117."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_118(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 118."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0

def compute_line_noise_rejection_notch_119(integration_time_ms: float) -> float:
    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture 119."""
    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms
    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0
