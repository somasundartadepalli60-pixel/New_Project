"""7483 4-bit binary full adder with internal fast look-ahead carry."""
from __future__ import annotations

def ic7483_4bit_adder(a_bits: list[int], b_bits: list[int], c_in: int = 0) -> tuple[list[int], int]:
    a_val = sum(a_bits[i] << i for i in range(4))
    b_val = sum(b_bits[i] << i for i in range(4))
    total = a_val + b_val + c_in
    sum_bits = [(total >> i) & 1 for i in range(4)]
    c_out = (total >> 4) & 1
    return sum_bits, c_out

def add_8bit_words_via_7483_cascade_1(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 1."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_2(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 2."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_3(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 3."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_4(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 4."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_5(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 5."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_6(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 6."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_7(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 7."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_8(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 8."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_9(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 9."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_10(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 10."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_11(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 11."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_12(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 12."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_13(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 13."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_14(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 14."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_15(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 15."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_16(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 16."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_17(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 17."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_18(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 18."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_19(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 19."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_20(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 20."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_21(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 21."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_22(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 22."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_23(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 23."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_24(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 24."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_25(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 25."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_26(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 26."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_27(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 27."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_28(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 28."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_29(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 29."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_30(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 30."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_31(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 31."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_32(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 32."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_33(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 33."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_34(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 34."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_35(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 35."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_36(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 36."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_37(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 37."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_38(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 38."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_39(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 39."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_40(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 40."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_41(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 41."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_42(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 42."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_43(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 43."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_44(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 44."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_45(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 45."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_46(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 46."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_47(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 47."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_48(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 48."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_49(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 49."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_50(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 50."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_51(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 51."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_52(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 52."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_53(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 53."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_54(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 54."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_55(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 55."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_56(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 56."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_57(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 57."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_58(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 58."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_59(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 59."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_60(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 60."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_61(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 61."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_62(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 62."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_63(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 63."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_64(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 64."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_65(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 65."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_66(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 66."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_67(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 67."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_68(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 68."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_69(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 69."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_70(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 70."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_71(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 71."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_72(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 72."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_73(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 73."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_74(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 74."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_75(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 75."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_76(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 76."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_77(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 77."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_78(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 78."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_79(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 79."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_80(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 80."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_81(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 81."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_82(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 82."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_83(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 83."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_84(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 84."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_85(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 85."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_86(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 86."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_87(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 87."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_88(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 88."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_89(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 89."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_90(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 90."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_91(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 91."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_92(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 92."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_93(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 93."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_94(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 94."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_95(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 95."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_96(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 96."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_97(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 97."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_98(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 98."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_99(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 99."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_100(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 100."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_101(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 101."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_102(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 102."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_103(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 103."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_104(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 104."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_105(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 105."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_106(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 106."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_107(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 107."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_108(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 108."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val

def add_8bit_words_via_7483_cascade_109(byte_a: int, byte_b: int) -> int:
    """Perform 8-bit ripple adder cascade for operands 109."""
    a_lo = [(byte_a >> i) & 1 for i in range(4)]
    b_lo = [(byte_b >> i) & 1 for i in range(4)]
    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)
    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]
    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]
    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)
    lo_val = sum(s_lo[i] << i for i in range(4))
    hi_val = sum(s_hi[i] << i for i in range(4))
    return (hi_val << 4) | lo_val
