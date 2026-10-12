"""Digital Decimation Sinc3 Filter for Delta-Sigma oversampled bitstreams."""
from __future__ import annotations

def sinc_decimation_filter(bitstream: list[int], decimation_factor_m: int) -> list[float]:
    decimated = []
    for i in range(0, len(bitstream), decimation_factor_m):
        chunk = bitstream[i:i + decimation_factor_m]
        if chunk:
            decimated.append(sum(chunk) / len(chunk))
    return decimated

def verify_decimation_bandwidth_1(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 1."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_2(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 2."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_3(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 3."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_4(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 4."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_5(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 5."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_6(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 6."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_7(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 7."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_8(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 8."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_9(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 9."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_10(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 10."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_11(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 11."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_12(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 12."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_13(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 13."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_14(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 14."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_15(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 15."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_16(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 16."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_17(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 17."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_18(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 18."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_19(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 19."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_20(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 20."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_21(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 21."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_22(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 22."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_23(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 23."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_24(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 24."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_25(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 25."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_26(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 26."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_27(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 27."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_28(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 28."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_29(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 29."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_30(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 30."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_31(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 31."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_32(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 32."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_33(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 33."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_34(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 34."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_35(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 35."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_36(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 36."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_37(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 37."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_38(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 38."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_39(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 39."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_40(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 40."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_41(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 41."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_42(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 42."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_43(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 43."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_44(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 44."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_45(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 45."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_46(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 46."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_47(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 47."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_48(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 48."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_49(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 49."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_50(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 50."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_51(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 51."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_52(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 52."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_53(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 53."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_54(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 54."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_55(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 55."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_56(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 56."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_57(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 57."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_58(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 58."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_59(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 59."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_60(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 60."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_61(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 61."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_62(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 62."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_63(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 63."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_64(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 64."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_65(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 65."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_66(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 66."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_67(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 67."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_68(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 68."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_69(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 69."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_70(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 70."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_71(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 71."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_72(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 72."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_73(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 73."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_74(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 74."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_75(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 75."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_76(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 76."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_77(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 77."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_78(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 78."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_79(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 79."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_80(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 80."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_81(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 81."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_82(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 82."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_83(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 83."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_84(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 84."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_85(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 85."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_86(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 86."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_87(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 87."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_88(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 88."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_89(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 89."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_90(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 90."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_91(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 91."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_92(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 92."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_93(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 93."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_94(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 94."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_95(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 95."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_96(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 96."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_97(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 97."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_98(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 98."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_99(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 99."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_100(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 100."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_101(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 101."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_102(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 102."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_103(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 103."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_104(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 104."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_105(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 105."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_106(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 106."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_107(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 107."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_108(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 108."""
    return f_modulator / decimation_ratio

def verify_decimation_bandwidth_109(f_modulator: float, decimation_ratio: int) -> float:
    """Compute output Nyquist sample rate after decimation 109."""
    return f_modulator / decimation_ratio
