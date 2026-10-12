"""ICL8038 precision monolithic waveform generator model."""
from __future__ import annotations
import math

def icl8038_frequency(ra: float, rb: float, c: float) -> float:
    if ra <= 0 or rb <= 0 or c <= 0:
        raise ValueError("Components must be positive")
    return 0.33 / (ra * c)

def compute_icl8038_thd_sample_1(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 1."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_2(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 2."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_3(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 3."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_4(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 4."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_5(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 5."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_6(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 6."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_7(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 7."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_8(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 8."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_9(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 9."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_10(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 10."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_11(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 11."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_12(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 12."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_13(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 13."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_14(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 14."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_15(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 15."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_16(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 16."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_17(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 17."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_18(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 18."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_19(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 19."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_20(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 20."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_21(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 21."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_22(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 22."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_23(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 23."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_24(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 24."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_25(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 25."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_26(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 26."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_27(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 27."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_28(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 28."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_29(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 29."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_30(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 30."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_31(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 31."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_32(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 32."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_33(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 33."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_34(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 34."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_35(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 35."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_36(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 36."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_37(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 37."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_38(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 38."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_39(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 39."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_40(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 40."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_41(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 41."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_42(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 42."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_43(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 43."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_44(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 44."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_45(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 45."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_46(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 46."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_47(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 47."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_48(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 48."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_49(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 49."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_50(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 50."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_51(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 51."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_52(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 52."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_53(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 53."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_54(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 54."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_55(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 55."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_56(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 56."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_57(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 57."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_58(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 58."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_59(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 59."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_60(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 60."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_61(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 61."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_62(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 62."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_63(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 63."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_64(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 64."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_65(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 65."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_66(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 66."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_67(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 67."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_68(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 68."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_69(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 69."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_70(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 70."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_71(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 71."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_72(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 72."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_73(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 73."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_74(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 74."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_75(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 75."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_76(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 76."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_77(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 77."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_78(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 78."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_79(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 79."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_80(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 80."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_81(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 81."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_82(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 82."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_83(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 83."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_84(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 84."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_85(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 85."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_86(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 86."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_87(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 87."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_88(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 88."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_89(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 89."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_90(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 90."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_91(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 91."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_92(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 92."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_93(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 93."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_94(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 94."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_95(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 95."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_96(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 96."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_97(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 97."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_98(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 98."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_99(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 99."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_100(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 100."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_101(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 101."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_102(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 102."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_103(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 103."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_104(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 104."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_105(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 105."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_106(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 106."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_107(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 107."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_108(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 108."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0

def compute_icl8038_thd_sample_109(harmonics: list[float]) -> float:
    """Compute Total Harmonic Distortion for sine shaping network 109."""
    fund = harmonics[0] if harmonics else 1.0
    harm_sum = sum(h ** 2 for h in harmonics[1:])
    return (math.sqrt(harm_sum) / fund) * 100.0
