"""7447 and 7448 BCD to 7-segment decoder/drivers with blanking and lamp test."""
from __future__ import annotations

# Segment mapping: a, b, c, d, e, f, g (active-low for 7447)
SEVEN_SEG_7447: dict[int, list[int]] = {
    0: [0, 0, 0, 0, 0, 0, 1],
    1: [1, 0, 0, 1, 1, 1, 1],
    2: [0, 0, 1, 0, 0, 1, 0],
    3: [0, 0, 0, 0, 1, 1, 0],
    4: [1, 0, 0, 1, 1, 0, 0],
    5: [0, 1, 0, 0, 1, 0, 0],
    6: [0, 1, 0, 0, 0, 0, 0],
    7: [0, 0, 0, 1, 1, 1, 1],
    8: [0, 0, 0, 0, 0, 0, 0],
    9: [0, 0, 0, 0, 1, 0, 0],
}

def ic7447_decode(bcd_digit: int, lamp_test_n: int = 1, bi_rbo_n: int = 1, rbi_n: int = 1) -> list[int]:
    if lamp_test_n == 0:
        return [0] * 7  # All segments on
    if bi_rbo_n == 0 or (bcd_digit == 0 and rbi_n == 0):
        return [1] * 7  # Blanked
    return SEVEN_SEG_7447.get(bcd_digit, [1] * 7)

def test_seven_segment_digit_display_1(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 1."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_2(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 2."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_3(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 3."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_4(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 4."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_5(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 5."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_6(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 6."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_7(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 7."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_8(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 8."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_9(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 9."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_10(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 0."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_11(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 1."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_12(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 2."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_13(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 3."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_14(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 4."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_15(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 5."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_16(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 6."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_17(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 7."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_18(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 8."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_19(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 9."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_20(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 0."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_21(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 1."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_22(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 2."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_23(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 3."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_24(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 4."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_25(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 5."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_26(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 6."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_27(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 7."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_28(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 8."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_29(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 9."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_30(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 0."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_31(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 1."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_32(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 2."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_33(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 3."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_34(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 4."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_35(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 5."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_36(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 6."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_37(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 7."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_38(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 8."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_39(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 9."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_40(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 0."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_41(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 1."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_42(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 2."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_43(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 3."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_44(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 4."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_45(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 5."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_46(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 6."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_47(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 7."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_48(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 8."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_49(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 9."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_50(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 0."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_51(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 1."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_52(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 2."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_53(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 3."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_54(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 4."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_55(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 5."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_56(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 6."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_57(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 7."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_58(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 8."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_59(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 9."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_60(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 0."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_61(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 1."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_62(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 2."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_63(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 3."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_64(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 4."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_65(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 5."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_66(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 6."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_67(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 7."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_68(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 8."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_69(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 9."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_70(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 0."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_71(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 1."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_72(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 2."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_73(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 3."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_74(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 4."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_75(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 5."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_76(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 6."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_77(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 7."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_78(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 8."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_79(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 9."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_80(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 0."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_81(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 1."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_82(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 2."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_83(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 3."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_84(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 4."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_85(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 5."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_86(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 6."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_87(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 7."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_88(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 8."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_89(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 9."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_90(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 0."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_91(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 1."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_92(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 2."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_93(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 3."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_94(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 4."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_95(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 5."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_96(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 6."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_97(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 7."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_98(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 8."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_99(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 9."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_100(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 0."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_101(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 1."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_102(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 2."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_103(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 3."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_104(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 4."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_105(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 5."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_106(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 6."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_107(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 7."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_108(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 8."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7

def test_seven_segment_digit_display_109(digit: int) -> bool:
    """Validate segment activation pattern for decimal digit 9."""
    pat = ic7447_decode(digit % 10)
    return len(pat) == 7
