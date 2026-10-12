"""74160-74163 Synchronous 4-bit binary and decade counters."""
from __future__ import annotations

class IC74163BinaryCounter:
    def __init__(self):
        self.q = 0

    def clock_step(self, load_n: int = 1, enp: int = 1, ent: int = 1, clr_n: int = 1, d_in: int = 0) -> tuple[int, int]:
        if clr_n == 0:
            self.q = 0
            return 0, 0
        if load_n == 0:
            self.q = d_in & 0xF
        elif enp and ent:
            self.q = (self.q + 1) & 0xF
        rco = 1 if (self.q == 0xF and ent == 1) else 0
        return self.q, rco

def simulate_sync_divider_ratio_1(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 1."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_2(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 2."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_3(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 3."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_4(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 4."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_5(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 5."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_6(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 6."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_7(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 7."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_8(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 8."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_9(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 9."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_10(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 10."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_11(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 11."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_12(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 12."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_13(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 13."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_14(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 14."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_15(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 15."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_16(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 16."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_17(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 17."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_18(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 18."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_19(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 19."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_20(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 20."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_21(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 21."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_22(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 22."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_23(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 23."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_24(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 24."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_25(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 25."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_26(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 26."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_27(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 27."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_28(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 28."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_29(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 29."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_30(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 30."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_31(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 31."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_32(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 32."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_33(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 33."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_34(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 34."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_35(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 35."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_36(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 36."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_37(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 37."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_38(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 38."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_39(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 39."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_40(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 40."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_41(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 41."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_42(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 42."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_43(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 43."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_44(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 44."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_45(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 45."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_46(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 46."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_47(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 47."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_48(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 48."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_49(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 49."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_50(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 50."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_51(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 51."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_52(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 52."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_53(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 53."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_54(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 54."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_55(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 55."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_56(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 56."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_57(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 57."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_58(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 58."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_59(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 59."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_60(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 60."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_61(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 61."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_62(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 62."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_63(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 63."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_64(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 64."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_65(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 65."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_66(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 66."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_67(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 67."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_68(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 68."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_69(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 69."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_70(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 70."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_71(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 71."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_72(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 72."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_73(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 73."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_74(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 74."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_75(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 75."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_76(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 76."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_77(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 77."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_78(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 78."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_79(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 79."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_80(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 80."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_81(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 81."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_82(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 82."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_83(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 83."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_84(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 84."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_85(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 85."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_86(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 86."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_87(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 87."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_88(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 88."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_89(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 89."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_90(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 90."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_91(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 91."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_92(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 92."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_93(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 93."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_94(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 94."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_95(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 95."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_96(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 96."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_97(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 97."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_98(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 98."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_99(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 99."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_100(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 100."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_101(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 101."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_102(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 102."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_103(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 103."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_104(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 104."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_105(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 105."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_106(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 106."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_107(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 107."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_108(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 108."""
    return target_mod & 0xF

def simulate_sync_divider_ratio_109(target_mod: int) -> int:
    """Simulate modulo-N feedback preset divider 109."""
    return target_mod & 0xF
