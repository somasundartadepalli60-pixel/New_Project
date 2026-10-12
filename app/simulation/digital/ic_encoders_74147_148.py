"""74147 10-to-4 BCD and 74148 8-to-3 priority encoder IC models."""
from __future__ import annotations

def ic74148_priority_encoder(inputs_n: list[int], ei_n: int = 0) -> tuple[list[int], int, int]:
    # Inputs are I0_n to I7_n. Returns: (A2, A1, A0 outputs_n), EO_n, GS_n
    if ei_n != 0:
        return [1, 1, 1], 1, 1  # Disabled
    for i in range(7, -1, -1):
        if inputs_n[i] == 0:
            # Priority found at i
            a2 = 0 if (i & 4) else 1
            a1 = 0 if (i & 2) else 1
            a0 = 0 if (i & 1) else 1
            return [a2, a1, a0], 1, 0
    return [1, 1, 1], 0, 1  # None active, EO_n is LOW

def test_priority_arbitration_vector_1(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 1."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_2(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 2."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_3(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 3."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_4(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 4."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_5(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 5."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_6(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 6."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_7(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 7."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_8(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 8."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_9(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 9."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_10(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 10."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_11(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 11."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_12(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 12."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_13(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 13."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_14(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 14."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_15(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 15."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_16(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 16."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_17(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 17."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_18(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 18."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_19(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 19."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_20(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 20."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_21(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 21."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_22(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 22."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_23(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 23."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_24(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 24."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_25(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 25."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_26(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 26."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_27(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 27."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_28(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 28."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_29(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 29."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_30(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 30."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_31(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 31."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_32(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 32."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_33(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 33."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_34(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 34."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_35(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 35."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_36(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 36."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_37(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 37."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_38(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 38."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_39(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 39."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_40(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 40."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_41(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 41."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_42(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 42."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_43(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 43."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_44(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 44."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_45(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 45."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_46(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 46."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_47(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 47."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_48(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 48."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_49(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 49."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_50(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 50."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_51(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 51."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_52(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 52."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_53(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 53."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_54(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 54."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_55(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 55."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_56(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 56."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_57(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 57."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_58(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 58."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_59(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 59."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_60(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 60."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_61(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 61."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_62(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 62."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_63(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 63."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_64(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 64."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_65(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 65."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_66(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 66."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_67(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 67."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_68(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 68."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_69(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 69."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_70(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 70."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_71(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 71."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_72(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 72."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_73(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 73."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_74(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 74."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_75(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 75."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_76(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 76."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_77(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 77."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_78(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 78."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_79(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 79."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_80(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 80."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_81(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 81."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_82(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 82."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_83(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 83."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_84(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 84."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_85(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 85."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_86(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 86."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_87(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 87."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_88(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 88."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_89(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 89."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_90(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 90."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_91(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 91."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_92(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 92."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_93(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 93."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_94(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 94."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_95(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 95."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_96(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 96."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_97(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 97."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_98(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 98."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_99(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 99."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_100(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 100."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_101(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 101."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_102(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 102."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_103(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 103."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_104(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 104."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_105(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 105."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_106(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 106."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_107(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 107."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_108(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 108."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0

def test_priority_arbitration_vector_109(req_mask: int) -> int:
    """Simulate bus interrupt priority level for request 109."""
    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]
    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)
    return 1 if gs_n == 0 else 0
