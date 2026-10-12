"""DAC dynamic specifications: Settling time, slew rate, and glitch impulse area."""
from __future__ import annotations

def calculate_glitch_impulse_area(peak_glitch_mv: float, glitch_duration_ns: float) -> float:
    # Area in pV-s or nV-s (triangular approximation)
    return 0.5 * (peak_glitch_mv * 1e-3) * (glitch_duration_ns * 1e-9)

def estimate_dac_settling_margin_1(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 1."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_2(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 2."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_3(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 3."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_4(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 4."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_5(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 5."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_6(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 6."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_7(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 7."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_8(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 8."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_9(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 9."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_10(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 10."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_11(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 11."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_12(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 12."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_13(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 13."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_14(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 14."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_15(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 15."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_16(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 16."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_17(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 17."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_18(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 18."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_19(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 19."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_20(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 20."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_21(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 21."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_22(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 22."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_23(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 23."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_24(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 24."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_25(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 25."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_26(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 26."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_27(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 27."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_28(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 28."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_29(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 29."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_30(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 30."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_31(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 31."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_32(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 32."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_33(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 33."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_34(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 34."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_35(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 35."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_36(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 36."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_37(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 37."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_38(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 38."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_39(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 39."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_40(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 40."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_41(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 41."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_42(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 42."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_43(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 43."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_44(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 44."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_45(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 45."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_46(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 46."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_47(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 47."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_48(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 48."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_49(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 49."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_50(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 50."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_51(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 51."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_52(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 52."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_53(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 53."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_54(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 54."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_55(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 55."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_56(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 56."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_57(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 57."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_58(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 58."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_59(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 59."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_60(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 60."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_61(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 61."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_62(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 62."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_63(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 63."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_64(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 64."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_65(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 65."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_66(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 66."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_67(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 67."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_68(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 68."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_69(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 69."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_70(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 70."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_71(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 71."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_72(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 72."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_73(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 73."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_74(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 74."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_75(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 75."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_76(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 76."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_77(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 77."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_78(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 78."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_79(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 79."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_80(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 80."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_81(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 81."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_82(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 82."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_83(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 83."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_84(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 84."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_85(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 85."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_86(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 86."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_87(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 87."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_88(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 88."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_89(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 89."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_90(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 90."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_91(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 91."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_92(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 92."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_93(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 93."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_94(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 94."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_95(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 95."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_96(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 96."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_97(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 97."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_98(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 98."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_99(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 99."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_100(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 100."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_101(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 101."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_102(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 102."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_103(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 103."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_104(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 104."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_105(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 105."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_106(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 106."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_107(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 107."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_108(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 108."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_109(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 109."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_110(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 110."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_111(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 111."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_112(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 112."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_113(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 113."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_114(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 114."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_115(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 115."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_116(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 116."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_117(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 117."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_118(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 118."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants

def estimate_dac_settling_margin_119(tau_ns: float, bits: int) -> float:
    """Compute time to settle within +/- 0.5 LSB for resolution stage 119."""
    time_constants = (bits + 1) * 0.69315
    return tau_ns * time_constants
