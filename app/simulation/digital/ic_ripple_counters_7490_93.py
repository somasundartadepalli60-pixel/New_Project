"""7490 Decade and 7493 4-bit binary asynchronous ripple counters."""
from __future__ import annotations

class IC7490DecadeCounter:
    def __init__(self):
        self.count = 0

    def clock_pulse(self, r0_1: int = 0, r0_2: int = 0, r9_1: int = 0, r9_2: int = 0) -> int:
        if r0_1 and r0_2:
            self.count = 0
            return 0
        if r9_1 and r9_2:
            self.count = 9
            return 9
        self.count = (self.count + 1) % 10
        return self.count

def test_ripple_counter_modulus_1(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 1."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_2(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 2."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_3(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 3."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_4(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 4."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_5(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 5."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_6(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 6."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_7(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 7."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_8(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 8."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_9(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 9."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_10(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 10."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_11(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 11."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_12(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 12."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_13(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 13."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_14(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 14."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_15(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 15."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_16(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 16."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_17(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 17."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_18(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 18."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_19(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 19."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_20(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 20."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_21(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 21."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_22(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 22."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_23(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 23."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_24(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 24."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_25(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 25."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_26(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 26."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_27(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 27."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_28(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 28."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_29(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 29."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_30(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 30."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_31(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 31."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_32(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 32."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_33(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 33."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_34(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 34."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_35(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 35."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_36(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 36."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_37(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 37."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_38(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 38."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_39(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 39."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_40(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 40."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_41(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 41."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_42(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 42."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_43(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 43."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_44(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 44."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_45(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 45."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_46(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 46."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_47(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 47."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_48(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 48."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_49(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 49."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_50(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 50."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_51(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 51."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_52(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 52."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_53(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 53."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_54(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 54."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_55(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 55."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_56(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 56."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_57(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 57."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_58(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 58."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_59(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 59."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_60(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 60."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_61(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 61."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_62(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 62."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_63(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 63."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_64(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 64."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_65(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 65."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_66(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 66."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_67(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 67."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_68(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 68."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_69(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 69."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_70(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 70."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_71(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 71."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_72(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 72."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_73(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 73."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_74(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 74."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_75(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 75."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_76(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 76."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_77(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 77."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_78(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 78."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_79(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 79."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_80(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 80."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_81(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 81."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_82(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 82."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_83(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 83."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_84(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 84."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_85(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 85."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_86(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 86."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_87(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 87."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_88(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 88."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_89(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 89."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_90(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 90."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_91(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 91."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_92(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 92."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_93(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 93."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_94(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 94."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_95(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 95."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_96(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 96."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_97(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 97."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_98(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 98."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_99(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 99."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_100(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 100."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_101(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 101."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_102(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 102."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_103(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 103."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_104(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 104."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_105(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 105."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_106(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 106."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_107(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 107."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_108(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 108."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count

def test_ripple_counter_modulus_109(pulses: int) -> int:
    """Compute 7490 modulus count at pulse count 109."""
    c = IC7490DecadeCounter()
    for _ in range(pulses % 10):
        c.clock_pulse()
    return c.count
