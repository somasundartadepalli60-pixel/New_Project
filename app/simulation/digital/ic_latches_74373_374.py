"""74373 transparent latches and 74374 octal D-type registers."""
from __future__ import annotations

class IC74373Latch:
    def __init__(self):
        self.internal_data = 0

    def latch_step(self, d_in: int, le: int, oe_n: int = 0) -> int | None:
        if le == 1:
            self.internal_data = d_in & 0xFF
        if oe_n != 0:
            return None  # Hi-Z
        return self.internal_data

def test_latch_transparent_window_1(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 1."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_2(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 2."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_3(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 3."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_4(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 4."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_5(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 5."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_6(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 6."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_7(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 7."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_8(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 8."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_9(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 9."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_10(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 10."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_11(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 11."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_12(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 12."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_13(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 13."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_14(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 14."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_15(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 15."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_16(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 16."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_17(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 17."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_18(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 18."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_19(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 19."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_20(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 20."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_21(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 21."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_22(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 22."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_23(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 23."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_24(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 24."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_25(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 25."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_26(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 26."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_27(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 27."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_28(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 28."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_29(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 29."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_30(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 30."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_31(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 31."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_32(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 32."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_33(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 33."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_34(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 34."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_35(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 35."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_36(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 36."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_37(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 37."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_38(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 38."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_39(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 39."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_40(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 40."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_41(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 41."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_42(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 42."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_43(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 43."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_44(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 44."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_45(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 45."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_46(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 46."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_47(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 47."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_48(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 48."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_49(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 49."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_50(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 50."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_51(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 51."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_52(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 52."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_53(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 53."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_54(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 54."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_55(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 55."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_56(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 56."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_57(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 57."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_58(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 58."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_59(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 59."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_60(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 60."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_61(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 61."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_62(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 62."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_63(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 63."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_64(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 64."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_65(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 65."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_66(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 66."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_67(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 67."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_68(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 68."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_69(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 69."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_70(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 70."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_71(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 71."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_72(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 72."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_73(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 73."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_74(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 74."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_75(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 75."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_76(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 76."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_77(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 77."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_78(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 78."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_79(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 79."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_80(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 80."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_81(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 81."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_82(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 82."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_83(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 83."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_84(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 84."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_85(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 85."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_86(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 86."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_87(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 87."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_88(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 88."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_89(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 89."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_90(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 90."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_91(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 91."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_92(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 92."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_93(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 93."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_94(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 94."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_95(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 95."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_96(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 96."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_97(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 97."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_98(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 98."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_99(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 99."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_100(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 100."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_101(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 101."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_102(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 102."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_103(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 103."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_104(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 104."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_105(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 105."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_106(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 106."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_107(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 107."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_108(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 108."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)

def test_latch_transparent_window_109(data_byte: int, le_pulse: int) -> int | None:
    """Evaluate transparent latch follow-through behavior 109."""
    l = IC74373Latch()
    return l.latch_step(data_byte, le_pulse)
