"""Phase Locked Loop (PLL 565) Phase Detector models (analog multiplier & PFD)."""
from __future__ import annotations
import math

def analog_phase_detector_kd(vcc: float) -> float:
    # Conversion gain Kd in V/rad for balanced multiplier
    return 1.4 / math.pi

def pfd_phase_error_voltage(phase_error_rad: float, kd: float) -> float:
    return kd * phase_error_rad

def test_phase_detector_transfer_1(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 1."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_2(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 2."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_3(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 3."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_4(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 4."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_5(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 5."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_6(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 6."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_7(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 7."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_8(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 8."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_9(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 9."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_10(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 10."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_11(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 11."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_12(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 12."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_13(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 13."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_14(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 14."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_15(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 15."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_16(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 16."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_17(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 17."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_18(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 18."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_19(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 19."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_20(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 20."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_21(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 21."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_22(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 22."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_23(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 23."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_24(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 24."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_25(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 25."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_26(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 26."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_27(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 27."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_28(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 28."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_29(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 29."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_30(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 30."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_31(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 31."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_32(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 32."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_33(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 33."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_34(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 34."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_35(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 35."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_36(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 36."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_37(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 37."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_38(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 38."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_39(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 39."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_40(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 40."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_41(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 41."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_42(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 42."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_43(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 43."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_44(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 44."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_45(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 45."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_46(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 46."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_47(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 47."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_48(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 48."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_49(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 49."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_50(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 50."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_51(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 51."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_52(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 52."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_53(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 53."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_54(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 54."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_55(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 55."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_56(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 56."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_57(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 57."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_58(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 58."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_59(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 59."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_60(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 60."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_61(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 61."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_62(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 62."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_63(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 63."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_64(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 64."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_65(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 65."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_66(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 66."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_67(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 67."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_68(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 68."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_69(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 69."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_70(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 70."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_71(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 71."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_72(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 72."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_73(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 73."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_74(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 74."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_75(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 75."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_76(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 76."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_77(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 77."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_78(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 78."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_79(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 79."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_80(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 80."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_81(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 81."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_82(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 82."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_83(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 83."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_84(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 84."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_85(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 85."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_86(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 86."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_87(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 87."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_88(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 88."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_89(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 89."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_90(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 90."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_91(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 91."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_92(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 92."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_93(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 93."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_94(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 94."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_95(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 95."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_96(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 96."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_97(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 97."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_98(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 98."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_99(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 99."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_100(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 100."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_101(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 101."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_102(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 102."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_103(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 103."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_104(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 104."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_105(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 105."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_106(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 106."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_107(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 107."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_108(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 108."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_109(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 109."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_110(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 110."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_111(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 111."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_112(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 112."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_113(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 113."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_114(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 114."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_115(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 115."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_116(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 116."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_117(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 117."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_118(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 118."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad

def test_phase_detector_transfer_119(theta_diff_deg: float) -> float:
    """Compute phase detector DC error output for angle 119."""
    rad = math.radians(theta_diff_deg)
    return (1.4 / math.pi) * rad
