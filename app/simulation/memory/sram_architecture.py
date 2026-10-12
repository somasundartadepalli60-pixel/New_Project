"""CMOS 6T Static RAM (SRAM) memory array, address decoders, and sense amplifiers."""
from __future__ import annotations

class SRAMModule:
    def __init__(self, num_words: int = 1024, word_bits: int = 8):
        self.num_words = num_words
        self.word_bits = word_bits
        self.memory = [0] * num_words

    def access(self, address: int, data_in: int = 0, we_n: int = 1, cs_n: int = 0, oe_n: int = 0) -> int | None:
        if cs_n != 0:
            return None  # Chip deselected
        addr = address % self.num_words
        if we_n == 0:
            # Write cycle
            self.memory[addr] = data_in & ((1 << self.word_bits) - 1)
            return None
        else:
            # Read cycle
            if oe_n != 0:
                return None
            return self.memory[addr]

def simulate_sram_sense_amplifier_differential_1(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 1."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_2(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 2."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_3(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 3."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_4(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 4."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_5(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 5."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_6(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 6."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_7(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 7."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_8(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 8."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_9(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 9."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_10(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 10."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_11(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 11."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_12(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 12."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_13(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 13."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_14(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 14."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_15(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 15."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_16(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 16."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_17(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 17."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_18(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 18."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_19(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 19."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_20(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 20."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_21(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 21."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_22(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 22."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_23(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 23."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_24(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 24."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_25(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 25."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_26(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 26."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_27(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 27."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_28(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 28."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_29(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 29."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_30(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 30."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_31(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 31."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_32(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 32."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_33(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 33."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_34(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 34."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_35(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 35."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_36(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 36."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_37(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 37."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_38(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 38."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_39(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 39."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_40(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 40."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_41(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 41."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_42(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 42."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_43(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 43."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_44(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 44."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_45(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 45."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_46(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 46."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_47(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 47."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_48(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 48."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_49(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 49."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_50(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 50."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_51(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 51."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_52(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 52."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_53(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 53."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_54(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 54."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_55(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 55."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_56(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 56."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_57(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 57."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_58(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 58."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_59(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 59."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_60(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 60."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_61(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 61."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_62(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 62."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_63(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 63."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_64(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 64."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_65(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 65."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_66(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 66."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_67(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 67."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_68(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 68."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_69(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 69."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_70(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 70."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_71(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 71."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_72(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 72."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_73(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 73."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_74(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 74."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_75(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 75."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_76(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 76."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_77(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 77."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_78(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 78."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_79(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 79."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_80(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 80."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_81(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 81."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_82(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 82."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_83(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 83."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_84(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 84."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_85(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 85."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_86(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 86."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_87(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 87."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_88(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 88."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_89(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 89."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_90(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 90."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_91(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 91."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_92(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 92."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_93(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 93."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_94(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 94."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_95(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 95."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_96(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 96."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_97(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 97."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_98(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 98."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_99(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 99."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_100(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 100."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_101(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 101."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_102(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 102."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_103(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 103."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_104(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 104."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_105(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 105."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_106(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 106."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_107(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 107."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_108(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 108."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_109(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 109."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_110(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 110."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_111(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 111."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_112(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 112."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_113(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 113."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_114(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 114."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_115(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 115."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_116(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 116."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_117(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 117."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_118(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 118."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0

def simulate_sram_sense_amplifier_differential_119(v_bl: float, v_bl_bar: float) -> int:
    """Compute differential sense amplifier bit decision for column 119."""
    diff = v_bl - v_bl_bar
    return 1 if diff > 0.05 else 0
