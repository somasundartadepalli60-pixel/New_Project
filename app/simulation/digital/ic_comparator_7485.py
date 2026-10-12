"""7485 4-bit magnitude comparator with cascading expansion inputs."""
from __future__ import annotations

def ic7485_comparator(a_val: int, b_val: int, cascade_gt: int = 0, cascade_eq: int = 1, cascade_lt: int = 0) -> tuple[int, int, int]:
    if a_val > b_val:
        return 1, 0, 0
    elif a_val < b_val:
        return 0, 0, 1
    else:
        return cascade_gt, cascade_eq, cascade_lt

def test_comparator_pair_comparison_1(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 1."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_2(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 2."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_3(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 3."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_4(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 4."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_5(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 5."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_6(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 6."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_7(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 7."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_8(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 8."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_9(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 9."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_10(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 10."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_11(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 11."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_12(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 12."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_13(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 13."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_14(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 14."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_15(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 15."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_16(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 16."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_17(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 17."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_18(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 18."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_19(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 19."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_20(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 20."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_21(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 21."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_22(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 22."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_23(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 23."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_24(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 24."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_25(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 25."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_26(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 26."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_27(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 27."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_28(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 28."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_29(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 29."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_30(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 30."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_31(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 31."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_32(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 32."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_33(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 33."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_34(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 34."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_35(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 35."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_36(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 36."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_37(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 37."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_38(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 38."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_39(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 39."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_40(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 40."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_41(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 41."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_42(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 42."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_43(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 43."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_44(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 44."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_45(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 45."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_46(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 46."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_47(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 47."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_48(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 48."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_49(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 49."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_50(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 50."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_51(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 51."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_52(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 52."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_53(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 53."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_54(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 54."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_55(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 55."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_56(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 56."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_57(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 57."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_58(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 58."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_59(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 59."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_60(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 60."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_61(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 61."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_62(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 62."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_63(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 63."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_64(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 64."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_65(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 65."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_66(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 66."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_67(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 67."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_68(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 68."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_69(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 69."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_70(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 70."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_71(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 71."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_72(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 72."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_73(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 73."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_74(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 74."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_75(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 75."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_76(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 76."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_77(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 77."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_78(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 78."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_79(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 79."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_80(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 80."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_81(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 81."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_82(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 82."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_83(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 83."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_84(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 84."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_85(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 85."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_86(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 86."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_87(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 87."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_88(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 88."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_89(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 89."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_90(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 90."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_91(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 91."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_92(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 92."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_93(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 93."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_94(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 94."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_95(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 95."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_96(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 96."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_97(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 97."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_98(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 98."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_99(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 99."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_100(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 100."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_101(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 101."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_102(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 102."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_103(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 103."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_104(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 104."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_105(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 105."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_106(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 106."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_107(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 107."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_108(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 108."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')

def test_comparator_pair_comparison_109(op_a: int, op_b: int) -> str:
    """Compute relational result for 4-bit operands 109."""
    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)
    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')
