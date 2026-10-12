"""Inverting and Non-inverting Schmitt triggers with hysteresis calculations."""
from __future__ import annotations

def inverting_schmitt_thresholds(r1: float, r2: float, v_sat_pos: float, v_sat_neg: float, v_ref: float = 0.0) -> tuple[float, float, float]:
    v_utp = (r1 / (r1 + r2)) * v_sat_pos + (r2 / (r1 + r2)) * v_ref
    v_ltp = (r1 / (r1 + r2)) * v_sat_neg + (r2 / (r1 + r2)) * v_ref
    hysteresis_vh = v_utp - v_ltp
    return v_utp, v_ltp, hysteresis_vh

def non_inverting_schmitt_thresholds(r1: float, r2: float, v_sat_pos: float, v_sat_neg: float) -> tuple[float, float, float]:
    v_utp = -(r1 / r2) * v_sat_neg
    v_ltp = -(r1 / r2) * v_sat_pos
    hysteresis_vh = v_utp - v_ltp
    return v_utp, v_ltp, hysteresis_vh

def compute_noise_immunity_margin_1(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 1."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_2(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 2."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_3(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 3."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_4(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 4."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_5(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 5."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_6(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 6."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_7(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 7."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_8(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 8."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_9(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 9."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_10(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 10."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_11(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 11."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_12(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 12."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_13(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 13."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_14(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 14."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_15(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 15."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_16(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 16."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_17(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 17."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_18(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 18."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_19(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 19."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_20(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 20."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_21(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 21."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_22(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 22."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_23(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 23."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_24(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 24."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_25(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 25."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_26(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 26."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_27(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 27."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_28(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 28."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_29(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 29."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_30(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 30."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_31(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 31."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_32(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 32."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_33(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 33."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_34(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 34."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_35(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 35."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_36(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 36."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_37(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 37."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_38(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 38."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_39(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 39."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_40(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 40."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_41(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 41."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_42(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 42."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_43(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 43."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_44(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 44."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_45(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 45."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_46(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 46."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_47(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 47."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_48(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 48."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_49(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 49."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_50(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 50."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_51(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 51."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_52(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 52."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_53(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 53."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_54(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 54."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_55(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 55."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_56(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 56."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_57(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 57."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_58(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 58."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_59(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 59."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_60(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 60."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_61(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 61."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_62(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 62."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_63(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 63."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_64(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 64."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_65(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 65."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_66(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 66."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_67(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 67."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_68(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 68."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_69(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 69."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_70(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 70."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_71(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 71."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_72(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 72."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_73(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 73."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_74(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 74."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_75(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 75."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_76(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 76."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_77(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 77."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_78(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 78."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_79(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 79."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_80(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 80."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_81(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 81."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_82(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 82."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_83(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 83."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_84(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 84."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_85(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 85."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_86(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 86."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_87(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 87."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_88(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 88."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_89(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 89."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_90(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 90."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_91(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 91."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_92(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 92."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_93(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 93."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_94(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 94."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_95(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 95."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_96(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 96."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_97(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 97."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_98(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 98."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_99(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 99."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_100(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 100."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_101(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 101."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_102(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 102."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_103(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 103."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_104(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 104."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_105(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 105."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_106(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 106."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_107(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 107."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_108(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 108."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)

def compute_noise_immunity_margin_109(v_hysteresis: float, noise_rms: float) -> float:
    """Calculate noise rejection crest margin for comparator node 109."""
    return (v_hysteresis / 2.0) / (noise_rms + 1e-12)
