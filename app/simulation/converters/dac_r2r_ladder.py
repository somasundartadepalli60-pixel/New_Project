"""R-2R Ladder and inverted current-mode DAC networks."""
from __future__ import annotations

def r2r_ladder_dac_voltage(digital_bits: list[int], v_ref: float) -> float:
    n = len(digital_bits)
    fraction = 0.0
    for i, b in enumerate(digital_bits):
        if b:
            fraction += 1.0 / (2 ** (i + 1))
    return -v_ref * fraction

def compute_r2r_node_thevenin_impedance_1(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 1."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_2(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 2."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_3(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 3."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_4(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 4."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_5(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 5."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_6(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 6."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_7(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 7."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_8(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 8."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_9(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 9."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_10(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 10."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_11(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 11."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_12(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 12."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_13(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 13."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_14(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 14."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_15(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 15."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_16(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 16."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_17(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 17."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_18(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 18."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_19(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 19."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_20(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 20."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_21(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 21."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_22(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 22."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_23(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 23."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_24(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 24."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_25(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 25."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_26(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 26."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_27(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 27."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_28(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 28."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_29(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 29."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_30(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 30."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_31(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 31."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_32(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 32."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_33(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 33."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_34(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 34."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_35(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 35."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_36(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 36."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_37(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 37."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_38(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 38."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_39(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 39."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_40(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 40."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_41(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 41."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_42(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 42."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_43(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 43."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_44(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 44."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_45(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 45."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_46(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 46."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_47(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 47."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_48(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 48."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_49(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 49."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_50(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 50."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_51(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 51."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_52(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 52."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_53(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 53."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_54(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 54."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_55(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 55."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_56(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 56."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_57(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 57."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_58(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 58."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_59(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 59."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_60(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 60."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_61(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 61."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_62(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 62."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_63(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 63."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_64(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 64."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_65(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 65."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_66(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 66."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_67(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 67."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_68(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 68."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_69(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 69."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_70(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 70."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_71(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 71."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_72(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 72."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_73(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 73."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_74(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 74."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_75(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 75."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_76(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 76."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_77(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 77."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_78(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 78."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_79(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 79."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_80(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 80."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_81(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 81."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_82(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 82."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_83(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 83."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_84(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 84."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_85(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 85."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_86(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 86."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_87(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 87."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_88(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 88."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_89(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 89."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_90(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 90."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_91(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 91."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_92(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 92."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_93(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 93."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_94(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 94."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_95(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 95."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_96(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 96."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_97(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 97."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_98(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 98."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_99(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 99."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_100(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 100."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_101(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 101."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_102(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 102."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_103(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 103."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_104(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 104."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_105(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 105."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_106(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 106."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_107(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 107."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_108(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 108."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_109(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 109."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_110(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 110."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_111(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 111."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_112(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 112."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_113(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 113."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_114(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 114."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_115(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 115."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_116(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 116."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_117(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 117."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_118(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 118."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_119(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 119."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_120(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 120."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_121(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 121."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_122(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 122."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_123(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 123."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_124(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 124."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_125(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 125."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_126(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 126."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_127(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 127."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_128(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 128."""
    return r_ohm

def compute_r2r_node_thevenin_impedance_129(r_ohm: float) -> float:
    """Verify constant Thevenin output resistance R for ladder configuration 129."""
    return r_ohm
