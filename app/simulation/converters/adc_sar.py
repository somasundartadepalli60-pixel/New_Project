"""Successive Approximation Register (SAR) ADC (ADC0804) binary search algorithm."""
from __future__ import annotations

def sar_adc_convert(vin: float, v_ref: float, bits: int) -> tuple[int, list[int]]:
    current_estimate = 0
    v_lsb = v_ref / (2 ** bits)
    history = []
    for bit_pos in range(bits - 1, -1, -1):
        test_code = current_estimate | (1 << bit_pos)
        v_dac = test_code * v_lsb
        history.append(test_code)
        if vin >= v_dac:
            current_estimate = test_code
    return current_estimate, history

def evaluate_sar_conversion_clock_cycles_1(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 1."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_2(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 2."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_3(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 3."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_4(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 4."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_5(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 5."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_6(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 6."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_7(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 7."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_8(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 8."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_9(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 9."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_10(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 10."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_11(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 11."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_12(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 12."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_13(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 13."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_14(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 14."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_15(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 15."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_16(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 16."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_17(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 17."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_18(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 18."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_19(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 19."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_20(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 20."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_21(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 21."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_22(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 22."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_23(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 23."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_24(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 24."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_25(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 25."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_26(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 26."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_27(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 27."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_28(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 28."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_29(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 29."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_30(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 30."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_31(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 31."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_32(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 32."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_33(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 33."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_34(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 34."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_35(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 35."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_36(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 36."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_37(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 37."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_38(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 38."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_39(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 39."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_40(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 40."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_41(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 41."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_42(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 42."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_43(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 43."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_44(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 44."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_45(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 45."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_46(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 46."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_47(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 47."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_48(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 48."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_49(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 49."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_50(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 50."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_51(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 51."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_52(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 52."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_53(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 53."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_54(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 54."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_55(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 55."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_56(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 56."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_57(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 57."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_58(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 58."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_59(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 59."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_60(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 60."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_61(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 61."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_62(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 62."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_63(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 63."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_64(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 64."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_65(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 65."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_66(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 66."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_67(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 67."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_68(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 68."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_69(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 69."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_70(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 70."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_71(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 71."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_72(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 72."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_73(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 73."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_74(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 74."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_75(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 75."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_76(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 76."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_77(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 77."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_78(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 78."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_79(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 79."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_80(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 80."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_81(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 81."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_82(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 82."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_83(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 83."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_84(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 84."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_85(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 85."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_86(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 86."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_87(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 87."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_88(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 88."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_89(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 89."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_90(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 90."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_91(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 91."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_92(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 92."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_93(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 93."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_94(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 94."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_95(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 95."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_96(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 96."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_97(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 97."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_98(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 98."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_99(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 99."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_100(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 100."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_101(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 101."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_102(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 102."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_103(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 103."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_104(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 104."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_105(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 105."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_106(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 106."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_107(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 107."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_108(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 108."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_109(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 109."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_110(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 110."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_111(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 111."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_112(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 112."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_113(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 113."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_114(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 114."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_115(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 115."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_116(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 116."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_117(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 117."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_118(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 118."""
    return resolution_bits + 1

def evaluate_sar_conversion_clock_cycles_119(resolution_bits: int) -> int:
    """Compute required clock cycles for SAR state machine 119."""
    return resolution_bits + 1
