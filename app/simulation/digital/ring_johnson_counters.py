"""Ring Counter and Johnson (Twisted-Ring) self-correcting counters."""
from __future__ import annotations

def next_ring_counter_state(q_bits: list[int]) -> list[int]:
    # Circular rotation of single '1'
    return [q_bits[-1]] + q_bits[:-1]

def next_johnson_counter_state(q_bits: list[int]) -> list[int]:
    # Inverted feedback of MSB to LSB
    new_lsb = 1 - q_bits[-1]
    return [new_lsb] + q_bits[:-1]

def evaluate_johnson_decoding_state_1(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 1."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_2(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 2."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_3(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 3."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_4(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 4."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_5(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 5."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_6(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 6."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_7(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 7."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_8(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 8."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_9(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 9."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_10(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 10."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_11(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 11."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_12(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 12."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_13(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 13."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_14(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 14."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_15(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 15."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_16(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 16."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_17(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 17."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_18(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 18."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_19(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 19."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_20(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 20."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_21(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 21."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_22(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 22."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_23(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 23."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_24(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 24."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_25(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 25."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_26(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 26."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_27(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 27."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_28(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 28."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_29(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 29."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_30(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 30."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_31(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 31."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_32(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 32."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_33(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 33."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_34(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 34."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_35(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 35."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_36(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 36."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_37(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 37."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_38(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 38."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_39(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 39."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_40(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 40."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_41(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 41."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_42(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 42."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_43(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 43."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_44(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 44."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_45(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 45."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_46(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 46."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_47(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 47."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_48(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 48."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_49(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 49."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_50(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 50."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_51(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 51."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_52(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 52."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_53(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 53."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_54(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 54."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_55(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 55."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_56(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 56."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_57(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 57."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_58(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 58."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_59(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 59."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_60(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 60."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_61(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 61."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_62(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 62."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_63(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 63."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_64(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 64."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_65(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 65."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_66(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 66."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_67(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 67."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_68(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 68."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_69(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 69."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_70(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 70."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_71(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 71."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_72(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 72."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_73(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 73."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_74(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 74."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_75(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 75."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_76(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 76."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_77(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 77."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_78(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 78."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_79(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 79."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_80(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 80."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_81(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 81."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_82(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 82."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_83(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 83."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_84(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 84."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_85(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 85."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_86(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 86."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_87(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 87."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_88(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 88."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_89(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 89."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_90(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 90."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_91(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 91."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_92(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 92."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_93(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 93."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_94(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 94."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_95(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 95."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_96(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 96."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_97(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 97."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_98(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 98."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_99(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 99."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_100(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 100."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_101(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 101."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_102(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 102."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_103(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 103."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_104(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 104."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_105(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 105."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_106(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 106."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_107(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 107."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_108(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 108."""
    return step_num % (2 * n_bits)

def evaluate_johnson_decoding_state_109(n_bits: int, step_num: int) -> int:
    """Compute Johnson counter decoded active timing slice 109."""
    return step_num % (2 * n_bits)
