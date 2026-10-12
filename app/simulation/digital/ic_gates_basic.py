"""7400, 7402, 7404, 7408, 7432, 7486 basic and universal logic gate IC models."""
from __future__ import annotations

def ic7400_nand(a: int, b: int) -> int:
    return 0 if (a and b) else 1

def ic7402_nor(a: int, b: int) -> int:
    return 0 if (a or b) else 1

def ic7404_not(a: int) -> int:
    return 0 if a else 1

def ic7408_and(a: int, b: int) -> int:
    return 1 if (a and b) else 0

def ic7432_or(a: int, b: int) -> int:
    return 1 if (a or b) else 0

def ic7486_xor(a: int, b: int) -> int:
    return 1 if (bool(a) ^ bool(b)) else 0

def test_universal_gate_synthesis_1(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 1."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 1, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_2(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 2."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 2, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_3(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 3."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 3, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_4(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 4."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 4, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_5(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 5."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 5, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_6(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 6."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 6, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_7(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 7."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 7, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_8(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 8."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 8, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_9(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 9."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 9, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_10(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 10."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 10, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_11(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 11."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 11, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_12(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 12."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 12, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_13(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 13."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 13, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_14(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 14."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 14, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_15(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 15."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 15, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_16(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 16."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 16, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_17(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 17."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 17, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_18(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 18."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 18, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_19(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 19."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 19, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_20(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 20."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 20, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_21(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 21."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 21, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_22(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 22."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 22, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_23(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 23."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 23, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_24(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 24."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 24, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_25(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 25."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 25, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_26(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 26."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 26, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_27(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 27."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 27, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_28(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 28."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 28, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_29(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 29."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 29, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_30(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 30."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 30, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_31(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 31."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 31, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_32(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 32."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 32, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_33(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 33."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 33, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_34(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 34."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 34, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_35(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 35."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 35, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_36(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 36."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 36, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_37(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 37."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 37, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_38(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 38."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 38, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_39(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 39."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 39, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_40(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 40."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 40, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_41(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 41."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 41, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_42(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 42."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 42, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_43(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 43."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 43, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_44(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 44."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 44, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_45(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 45."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 45, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_46(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 46."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 46, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_47(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 47."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 47, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_48(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 48."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 48, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_49(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 49."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 49, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_50(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 50."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 50, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_51(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 51."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 51, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_52(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 52."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 52, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_53(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 53."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 53, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_54(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 54."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 54, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_55(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 55."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 55, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_56(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 56."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 56, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_57(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 57."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 57, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_58(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 58."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 58, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_59(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 59."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 59, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_60(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 60."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 60, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_61(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 61."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 61, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_62(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 62."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 62, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_63(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 63."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 63, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_64(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 64."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 64, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_65(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 65."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 65, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_66(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 66."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 66, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_67(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 67."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 67, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_68(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 68."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 68, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_69(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 69."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 69, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_70(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 70."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 70, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_71(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 71."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 71, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_72(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 72."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 72, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_73(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 73."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 73, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_74(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 74."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 74, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_75(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 75."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 75, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_76(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 76."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 76, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_77(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 77."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 77, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_78(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 78."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 78, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_79(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 79."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 79, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_80(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 80."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 80, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_81(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 81."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 81, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_82(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 82."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 82, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_83(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 83."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 83, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_84(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 84."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 84, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_85(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 85."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 85, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_86(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 86."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 86, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_87(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 87."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 87, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_88(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 88."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 88, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_89(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 89."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 89, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_90(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 90."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 90, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_91(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 91."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 91, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_92(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 92."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 92, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_93(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 93."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 93, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_94(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 94."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 94, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_95(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 95."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 95, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_96(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 96."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 96, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_97(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 97."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 97, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_98(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 98."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 98, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_99(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 99."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 99, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_100(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 100."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 100, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_101(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 101."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 101, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_102(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 102."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 102, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_103(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 103."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 103, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_104(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 104."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 104, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_105(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 105."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 105, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_106(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 106."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 106, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_107(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 107."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 107, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_108(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 108."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 108, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_109(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 109."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 109, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_110(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 110."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 110, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_111(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 111."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 111, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_112(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 112."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 112, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_113(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 113."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 113, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_114(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 114."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 114, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_115(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 115."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 115, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_116(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 116."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 116, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_117(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 117."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 117, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_118(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 118."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 118, 'and': and_res, 'or': or_res}

def test_universal_gate_synthesis_119(a_in: int, b_in: int) -> dict[str, int]:
    """Verify De Morgan NAND universal gate equivalences for test vector 119."""
    inv_a = ic7400_nand(a_in, a_in)
    inv_b = ic7400_nand(b_in, b_in)
    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))
    or_res = ic7400_nand(inv_a, inv_b)
    return {'step': 119, 'and': and_res, 'or': or_res}
