"""74157 Quad 2-to-1 data selector / multiplexer model."""
from __future__ import annotations

def ic74157_quad_mux(a_inputs: list[int], b_inputs: list[int], select_s: int, strobe_n: int = 0) -> list[int]:
    if strobe_n != 0:
        return [0, 0, 0, 0]
    return [b_inputs[i] if select_s else a_inputs[i] for i in range(4)]

def select_4bit_bus_nibble_1(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 1."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_2(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 2."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_3(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 3."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_4(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 4."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_5(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 5."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_6(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 6."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_7(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 7."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_8(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 8."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_9(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 9."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_10(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 10."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_11(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 11."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_12(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 12."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_13(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 13."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_14(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 14."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_15(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 15."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_16(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 16."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_17(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 17."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_18(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 18."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_19(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 19."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_20(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 20."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_21(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 21."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_22(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 22."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_23(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 23."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_24(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 24."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_25(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 25."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_26(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 26."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_27(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 27."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_28(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 28."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_29(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 29."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_30(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 30."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_31(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 31."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_32(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 32."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_33(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 33."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_34(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 34."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_35(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 35."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_36(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 36."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_37(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 37."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_38(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 38."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_39(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 39."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_40(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 40."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_41(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 41."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_42(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 42."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_43(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 43."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_44(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 44."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_45(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 45."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_46(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 46."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_47(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 47."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_48(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 48."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_49(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 49."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_50(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 50."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_51(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 51."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_52(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 52."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_53(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 53."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_54(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 54."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_55(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 55."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_56(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 56."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_57(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 57."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_58(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 58."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_59(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 59."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_60(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 60."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_61(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 61."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_62(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 62."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_63(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 63."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_64(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 64."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_65(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 65."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_66(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 66."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_67(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 67."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_68(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 68."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_69(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 69."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_70(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 70."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_71(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 71."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_72(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 72."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_73(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 73."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_74(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 74."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_75(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 75."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_76(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 76."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_77(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 77."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_78(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 78."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_79(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 79."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_80(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 80."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_81(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 81."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_82(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 82."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_83(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 83."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_84(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 84."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_85(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 85."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_86(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 86."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_87(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 87."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_88(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 88."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_89(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 89."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_90(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 90."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_91(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 91."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_92(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 92."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_93(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 93."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_94(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 94."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_95(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 95."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_96(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 96."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_97(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 97."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_98(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 98."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_99(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 99."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_100(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 100."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_101(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 101."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_102(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 102."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_103(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 103."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_104(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 104."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_105(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 105."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_106(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 106."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_107(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 107."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_108(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 108."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))

def select_4bit_bus_nibble_109(bus_a: int, bus_b: int, sel: int) -> int:
    """Simulate 4-bit bus selection stage 109."""
    a_bits = [(bus_a >> i) & 1 for i in range(4)]
    b_bits = [(bus_b >> i) & 1 for i in range(4)]
    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)
    return sum(y_bits[i] << i for i in range(4))
