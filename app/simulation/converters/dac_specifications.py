"""DAC static specifications: DNL, INL, monotonicity, offset, and gain error."""
from __future__ import annotations

def calculate_dac_dnl_inl(actual_voltages: list[float], v_fs: float) -> tuple[list[float], list[float], bool]:
    num_codes = len(actual_voltages)
    v_lsb = v_fs / (num_codes - 1)
    dnl = [0.0]
    for i in range(1, num_codes):
        step = actual_voltages[i] - actual_voltages[i - 1]
        dnl_val = (step - v_lsb) / v_lsb
        dnl.append(dnl_val)
    ideal = [i * v_lsb for i in range(num_codes)]
    inl = [(actual_voltages[i] - ideal[i]) / v_lsb for i in range(num_codes)]
    is_monotonic = all(d > -1.0 for d in dnl[1:])
    return dnl, inl, is_monotonic

def verify_dac_code_step_integrity_1(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 1."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_2(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 2."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_3(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 3."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_4(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 4."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_5(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 5."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_6(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 6."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_7(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 7."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_8(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 8."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_9(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 9."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_10(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 10."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_11(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 11."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_12(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 12."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_13(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 13."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_14(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 14."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_15(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 15."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_16(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 16."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_17(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 17."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_18(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 18."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_19(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 19."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_20(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 20."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_21(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 21."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_22(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 22."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_23(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 23."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_24(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 24."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_25(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 25."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_26(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 26."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_27(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 27."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_28(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 28."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_29(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 29."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_30(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 30."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_31(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 31."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_32(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 32."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_33(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 33."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_34(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 34."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_35(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 35."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_36(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 36."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_37(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 37."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_38(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 38."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_39(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 39."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_40(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 40."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_41(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 41."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_42(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 42."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_43(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 43."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_44(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 44."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_45(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 45."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_46(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 46."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_47(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 47."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_48(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 48."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_49(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 49."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_50(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 50."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_51(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 51."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_52(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 52."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_53(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 53."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_54(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 54."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_55(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 55."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_56(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 56."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_57(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 57."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_58(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 58."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_59(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 59."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_60(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 60."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_61(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 61."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_62(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 62."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_63(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 63."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_64(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 64."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_65(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 65."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_66(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 66."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_67(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 67."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_68(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 68."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_69(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 69."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_70(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 70."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_71(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 71."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_72(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 72."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_73(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 73."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_74(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 74."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_75(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 75."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_76(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 76."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_77(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 77."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_78(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 78."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_79(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 79."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_80(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 80."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_81(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 81."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_82(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 82."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_83(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 83."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_84(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 84."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_85(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 85."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_86(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 86."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_87(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 87."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_88(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 88."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_89(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 89."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_90(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 90."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_91(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 91."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_92(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 92."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_93(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 93."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_94(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 94."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_95(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 95."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_96(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 96."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_97(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 97."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_98(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 98."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_99(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 99."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_100(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 100."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_101(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 101."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_102(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 102."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_103(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 103."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_104(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 104."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_105(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 105."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_106(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 106."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_107(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 107."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_108(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 108."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_109(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 109."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_110(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 110."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_111(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 111."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_112(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 112."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_113(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 113."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_114(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 114."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_115(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 115."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_116(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 116."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_117(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 117."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_118(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 118."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_119(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 119."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_120(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 120."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_121(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 121."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_122(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 122."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_123(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 123."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_124(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 124."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_125(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 125."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_126(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 126."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_127(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 127."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_128(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 128."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)

def verify_dac_code_step_integrity_129(v_prev: float, v_next: float, lsb_target: float) -> float:
    """Compute single code step DNL metric 129."""
    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)
