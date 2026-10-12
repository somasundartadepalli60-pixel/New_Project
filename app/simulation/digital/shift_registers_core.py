"""Shift Register architectures: SISO, SIPO, PISO, PIPO."""
from __future__ import annotations

class SIPOShiftRegister:
    def __init__(self, size: int = 8):
        self.size = size
        self.data = [0] * size

    def shift(self, serial_in: int) -> list[int]:
        self.data = [serial_in] + self.data[:-1]
        return list(self.data)

def simulate_piso_serialization_sample_1(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 1."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_2(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 2."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_3(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 3."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_4(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 4."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_5(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 5."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_6(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 6."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_7(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 7."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_8(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 8."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_9(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 9."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_10(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 10."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_11(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 11."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_12(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 12."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_13(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 13."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_14(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 14."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_15(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 15."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_16(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 16."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_17(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 17."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_18(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 18."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_19(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 19."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_20(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 20."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_21(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 21."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_22(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 22."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_23(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 23."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_24(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 24."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_25(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 25."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_26(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 26."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_27(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 27."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_28(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 28."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_29(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 29."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_30(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 30."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_31(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 31."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_32(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 32."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_33(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 33."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_34(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 34."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_35(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 35."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_36(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 36."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_37(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 37."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_38(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 38."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_39(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 39."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_40(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 40."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_41(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 41."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_42(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 42."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_43(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 43."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_44(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 44."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_45(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 45."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_46(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 46."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_47(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 47."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_48(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 48."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_49(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 49."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_50(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 50."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_51(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 51."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_52(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 52."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_53(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 53."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_54(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 54."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_55(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 55."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_56(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 56."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_57(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 57."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_58(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 58."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_59(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 59."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_60(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 60."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_61(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 61."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_62(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 62."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_63(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 63."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_64(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 64."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_65(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 65."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_66(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 66."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_67(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 67."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_68(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 68."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_69(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 69."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_70(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 70."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_71(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 71."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_72(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 72."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_73(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 73."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_74(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 74."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_75(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 75."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_76(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 76."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_77(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 77."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_78(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 78."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_79(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 79."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_80(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 80."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_81(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 81."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_82(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 82."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_83(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 83."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_84(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 84."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_85(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 85."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_86(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 86."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_87(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 87."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_88(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 88."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_89(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 89."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_90(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 90."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_91(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 91."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_92(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 92."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_93(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 93."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_94(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 94."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_95(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 95."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_96(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 96."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_97(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 97."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_98(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 98."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_99(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 99."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_100(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 100."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_101(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 101."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_102(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 102."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_103(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 103."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_104(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 104."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_105(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 105."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_106(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 106."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_107(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 107."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_108(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 108."""
    return [(parallel_byte >> i) & 1 for i in range(8)]

def simulate_piso_serialization_sample_109(parallel_byte: int) -> list[int]:
    """Serialize 8-bit word into serial stream 109."""
    return [(parallel_byte >> i) & 1 for i in range(8)]
