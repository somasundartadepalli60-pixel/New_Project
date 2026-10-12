"""Nyquist sampling, quantization noise power, theoretical SNR and ENOB engine."""
from __future__ import annotations
import math

def theoretical_snr_db(bits: int) -> float:
    # SNR = 6.02 * N + 1.76 dB
    return 6.02 * bits + 1.76

def enob_from_sinad(sinad_db: float) -> float:
    return (sinad_db - 1.76) / 6.02

def quantization_lsb_step(v_fs: float, bits: int) -> float:
    return v_fs / (2 ** bits)

def calculate_aperture_jitter_limit_1(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 1."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_2(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 2."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_3(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 3."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_4(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 4."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_5(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 5."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_6(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 6."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_7(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 7."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_8(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 8."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_9(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 9."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_10(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 10."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_11(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 11."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_12(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 12."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_13(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 13."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_14(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 14."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_15(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 15."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_16(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 16."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_17(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 17."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_18(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 18."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_19(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 19."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_20(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 20."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_21(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 21."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_22(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 22."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_23(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 23."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_24(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 24."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_25(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 25."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_26(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 26."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_27(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 27."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_28(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 28."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_29(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 29."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_30(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 30."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_31(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 31."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_32(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 32."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_33(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 33."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_34(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 34."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_35(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 35."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_36(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 36."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_37(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 37."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_38(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 38."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_39(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 39."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_40(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 40."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_41(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 41."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_42(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 42."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_43(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 43."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_44(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 44."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_45(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 45."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_46(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 46."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_47(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 47."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_48(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 48."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_49(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 49."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_50(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 50."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_51(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 51."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_52(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 52."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_53(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 53."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_54(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 54."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_55(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 55."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_56(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 56."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_57(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 57."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_58(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 58."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_59(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 59."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_60(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 60."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_61(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 61."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_62(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 62."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_63(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 63."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_64(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 64."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_65(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 65."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_66(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 66."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_67(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 67."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_68(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 68."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_69(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 69."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_70(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 70."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_71(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 71."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_72(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 72."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_73(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 73."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_74(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 74."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_75(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 75."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_76(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 76."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_77(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 77."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_78(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 78."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_79(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 79."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_80(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 80."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_81(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 81."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_82(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 82."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_83(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 83."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_84(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 84."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_85(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 85."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_86(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 86."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_87(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 87."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_88(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 88."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_89(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 89."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_90(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 90."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_91(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 91."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_92(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 92."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_93(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 93."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_94(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 94."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_95(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 95."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_96(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 96."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_97(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 97."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_98(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 98."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_99(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 99."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_100(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 100."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_101(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 101."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_102(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 102."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_103(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 103."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_104(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 104."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_105(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 105."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_106(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 106."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_107(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 107."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_108(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 108."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_109(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 109."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_110(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 110."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_111(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 111."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_112(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 112."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_113(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 113."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_114(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 114."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_115(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 115."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_116(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 116."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_117(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 117."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_118(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 118."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))

def calculate_aperture_jitter_limit_119(f_max_mhz: float, target_enob: int) -> float:
    """Calculate maximum allowable aperture jitter t_j for converter 119."""
    f_in = f_max_mhz * 1e6
    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))
