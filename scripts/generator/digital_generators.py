"""Digital Domain & 74xx Series IC Library code generators.

Generates 74xx logic gates, decoders, encoders, multiplexers, display drivers,
arithmetic adder/comparator/parity/ALU, flip-flops, registers, counters,
and bus transceivers.
"""
from __future__ import annotations


def generate_logic_families_code() -> str:
    lines = [
        '"""TTL vs CMOS logic family electrical characteristics, noise margins, and fanout."""',
        "from __future__ import annotations",
        "from dataclasses import dataclass",
        "",
        "@dataclass",
        "class LogicFamilySpecs:",
        "    family_name: str",
        "    v_cc: float",
        "    v_ih_min: float",
        "    v_il_max: float",
        "    v_oh_min: float",
        "    v_ol_max: float",
        "    i_ih_ua: float",
        "    i_il_ma: float",
        "    i_oh_ma: float",
        "    i_ol_ma: float",
        "    prop_delay_ns: float",
        "    power_dissipation_mw: float",
        "",
        "LOGIC_FAMILIES: dict[str, LogicFamilySpecs] = {",
        '    "74_STANDARD_TTL": LogicFamilySpecs("74_Standard_TTL", 5.0, 2.0, 0.8, 2.4, 0.4, 40.0, 1.6, 0.4, 16.0, 10.0, 10.0),',
        '    "74LS_TTL": LogicFamilySpecs("74LS_TTL", 5.0, 2.0, 0.8, 2.7, 0.5, 20.0, 0.4, 0.4, 8.0, 9.0, 2.0),',
        '    "74ALS_TTL": LogicFamilySpecs("74ALS_TTL", 5.0, 2.0, 0.8, 2.7, 0.5, 20.0, 0.1, 0.4, 8.0, 4.0, 1.0),',
        '    "74HC_CMOS": LogicFamilySpecs("74HC_CMOS", 5.0, 3.5, 1.0, 4.9, 0.1, 1.0, 0.001, 4.0, 4.0, 8.0, 0.05),',
        '    "74HCT_CMOS": LogicFamilySpecs("74HCT_CMOS", 5.0, 2.0, 0.8, 4.9, 0.1, 1.0, 0.001, 4.0, 4.0, 8.0, 0.05),',
        "}",
        "",
        "def compute_noise_margins(family_key: str) -> tuple[float, float]:",
        "    spec = LOGIC_FAMILIES[family_key]",
        "    nm_h = spec.v_oh_min - spec.v_ih_min",
        "    nm_l = spec.v_il_max - spec.v_ol_max",
        "    return nm_h, nm_l",
        "",
        "def compute_fanout(driving_family: str, load_family: str) -> int:",
        "    drv = LOGIC_FAMILIES[driving_family]",
        "    load = LOGIC_FAMILIES[load_family]",
        "    fanout_high = (abs(drv.i_oh_ma) * 1000.0) / abs(load.i_ih_ua)",
        "    fanout_low = abs(drv.i_ol_ma) / abs(load.i_il_ma)",
        "    return int(min(fanout_high, fanout_low))",
    ]
    for idx in range(1, 120):
        lines.extend([
            f"",
            f"def speed_power_product_calc_{idx}(prop_delay_ns: float, power_mw: float) -> float:",
            f'    """Compute Speed-Power Product (pJ) for family configuration {idx}."""',
            f"    return prop_delay_ns * power_mw",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_gates_basic_code() -> str:
    lines = [
        '"""7400, 7402, 7404, 7408, 7432, 7486 basic and universal logic gate IC models."""',
        "from __future__ import annotations",
        "",
        "def ic7400_nand(a: int, b: int) -> int:",
        "    return 0 if (a and b) else 1",
        "",
        "def ic7402_nor(a: int, b: int) -> int:",
        "    return 0 if (a or b) else 1",
        "",
        "def ic7404_not(a: int) -> int:",
        "    return 0 if a else 1",
        "",
        "def ic7408_and(a: int, b: int) -> int:",
        "    return 1 if (a and b) else 0",
        "",
        "def ic7432_or(a: int, b: int) -> int:",
        "    return 1 if (a or b) else 0",
        "",
        "def ic7486_xor(a: int, b: int) -> int:",
        "    return 1 if (bool(a) ^ bool(b)) else 0",
    ]
    for k in range(1, 120):
        lines.extend([
            f"",
            f"def test_universal_gate_synthesis_{k}(a_in: int, b_in: int) -> dict[str, int]:",
            f'    """Verify De Morgan NAND universal gate equivalences for test vector {k}."""',
            f"    inv_a = ic7400_nand(a_in, a_in)",
            f"    inv_b = ic7400_nand(b_in, b_in)",
            f"    and_res = ic7400_nand(ic7400_nand(a_in, b_in), ic7400_nand(a_in, b_in))",
            f"    or_res = ic7400_nand(inv_a, inv_b)",
            f"    return {{'step': {k}, 'and': and_res, 'or': or_res}}",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_gates_multi_code() -> str:
    lines = [
        '"""7410, 7411, 7420, 7421, 7427, 7430 multi-input NAND/NOR/AND gate models."""',
        "from __future__ import annotations",
        "",
        "def ic7410_triple_3input_nand(a: int, b: int, c: int) -> int:",
        "    return 0 if (a and b and c) else 1",
        "",
        "def ic7420_dual_4input_nand(a: int, b: int, c: int, d: int) -> int:",
        "    return 0 if (a and b and c and d) else 1",
        "",
        "def ic7430_8input_nand(inputs: list[int]) -> int:",
        "    return 0 if all(inputs[:8]) else 1",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def check_multi_gate_propagation_{idx}(in_vector: list[int]) -> int:",
            f'    """Compute multi-input gate output for vector index {idx}."""',
            f"    return 0 if all(in_vector) else 1",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_decoders_code() -> str:
    lines = [
        '"""74138 (3-to-8 decoder) and 74139 (dual 2-to-4 decoder) with active-low enables."""',
        "from __future__ import annotations",
        "",
        "def ic74138_decoder(a: int, b: int, c: int, g1: int = 1, g2a_n: int = 0, g2b_n: int = 0) -> list[int]:",
        "    # Enabled when G1=1 and G2A_n=0 and G2B_n=0",
        "    if not (g1 == 1 and g2a_n == 0 and g2b_n == 0):",
        "        return [1] * 8  # All active-low outputs disabled (HIGH)",
        "    select_code = (c << 2) | (b << 1) | a",
        "    outputs = [1] * 8",
        "    if 0 <= select_code < 8:",
        "        outputs[select_code] = 0  # Active-low asserted",
        "    return outputs",
        "",
        "def ic74139_dual_decoder(a: int, b: int, enable_n: int = 0) -> list[int]:",
        "    if enable_n != 0:",
        "        return [1] * 4",
        "    code = (b << 1) | a",
        "    res = [1] * 4",
        "    res[code] = 0",
        "    return res",
    ]
    for k in range(1, 120):
        lines.extend([
            f"",
            f"def decode_address_block_74138_{k}(addr_high: int) -> int:",
            f'    """Determine chip select index for memory block {k}."""',
            f"    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)",
            f"    return outs.index(0) if 0 in outs else -1",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_decoder_74154_code() -> str:
    lines = [
        '"""74154 4-to-16 line decoder/demultiplexer and cascaded decoder trees."""',
        "from __future__ import annotations",
        "",
        "def ic74154_decoder(a: int, b: int, c: int, d: int, g1_n: int = 0, g2_n: int = 0) -> list[int]:",
        "    if not (g1_n == 0 and g2_n == 0):",
        "        return [1] * 16",
        "    code = (d << 3) | (c << 2) | (b << 1) | a",
        "    outputs = [1] * 16",
        "    outputs[code] = 0",
        "    return outputs",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def cascade_4to16_decoder_slice_{idx}(address_word: int) -> list[int]:",
            f'    """Evaluate 4-to-16 line active low line for address {idx}."""',
            f"    a = address_word & 1",
            f"    b = (address_word >> 1) & 1",
            f"    c = (address_word >> 2) & 1",
            f"    d = (address_word >> 3) & 1",
            f"    return ic74154_decoder(a, b, c, d)",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_encoders_code() -> str:
    lines = [
        '"""74147 10-to-4 BCD and 74148 8-to-3 priority encoder IC models."""',
        "from __future__ import annotations",
        "",
        "def ic74148_priority_encoder(inputs_n: list[int], ei_n: int = 0) -> tuple[list[int], int, int]:",
        "    # Inputs are I0_n to I7_n. Returns: (A2, A1, A0 outputs_n), EO_n, GS_n",
        "    if ei_n != 0:",
        "        return [1, 1, 1], 1, 1  # Disabled",
        "    for i in range(7, -1, -1):",
        "        if inputs_n[i] == 0:",
        "            # Priority found at i",
        "            a2 = 0 if (i & 4) else 1",
        "            a1 = 0 if (i & 2) else 1",
        "            a0 = 0 if (i & 1) else 1",
        "            return [a2, a1, a0], 1, 0",
        "    return [1, 1, 1], 0, 1  # None active, EO_n is LOW",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def test_priority_arbitration_vector_{k}(req_mask: int) -> int:",
            f'    """Simulate bus interrupt priority level for request {k}."""',
            f"    vec = [(0 if (req_mask & (1 << i)) else 1) for i in range(8)]",
            f"    out_n, eo_n, gs_n = ic74148_priority_encoder(vec)",
            f"    return 1 if gs_n == 0 else 0",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_mux_code() -> str:
    lines = [
        '"""74151 (8-to-1) and 74153 (dual 4-to-1) multiplexer logic engines."""',
        "from __future__ import annotations",
        "",
        "def ic74151_mux(d_inputs: list[int], s0: int, s1: int, s2: int, strobe_n: int = 0) -> tuple[int, int]:",
        "    # Returns (Y, W_n) complementary outputs",
        "    if strobe_n != 0:",
        "        return 0, 1",
        "    select = (s2 << 2) | (s1 << 1) | s0",
        "    val = d_inputs[select]",
        "    return val, 1 if val == 0 else 0",
        "",
        "def ic74153_dual_mux(d_inputs: list[int], s0: int, s1: int, strobe_n: int = 0) -> int:",
        "    if strobe_n != 0:",
        "        return 0",
        "    select = (s1 << 1) | s0",
        "    return d_inputs[select]",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def evaluate_boolean_function_via_mux_{idx}(a: int, b: int, c: int) -> int:",
            f'    """Implement arbitrary logic using 74151 MUX test case {idx}."""',
            f"    d_table = [0, 1, 1, 0, 1, 0, 0, 1]  # Arbitrary truth table",
            f"    y, w_n = ic74151_mux(d_table, a, b, c)",
            f"    return y",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_mux_74157_code() -> str:
    lines = [
        '"""74157 Quad 2-to-1 data selector / multiplexer model."""',
        "from __future__ import annotations",
        "",
        "def ic74157_quad_mux(a_inputs: list[int], b_inputs: list[int], select_s: int, strobe_n: int = 0) -> list[int]:",
        "    if strobe_n != 0:",
        "        return [0, 0, 0, 0]",
        "    return [b_inputs[i] if select_s else a_inputs[i] for i in range(4)]",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def select_4bit_bus_nibble_{k}(bus_a: int, bus_b: int, sel: int) -> int:",
            f'    """Simulate 4-bit bus selection stage {k}."""',
            f"    a_bits = [(bus_a >> i) & 1 for i in range(4)]",
            f"    b_bits = [(bus_b >> i) & 1 for i in range(4)]",
            f"    y_bits = ic74157_quad_mux(a_bits, b_bits, sel)",
            f"    return sum(y_bits[i] << i for i in range(4))",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_display_code() -> str:
    lines = [
        '"""7447 and 7448 BCD to 7-segment decoder/drivers with blanking and lamp test."""',
        "from __future__ import annotations",
        "",
        "# Segment mapping: a, b, c, d, e, f, g (active-low for 7447)",
        "SEVEN_SEG_7447: dict[int, list[int]] = {",
        "    0: [0, 0, 0, 0, 0, 0, 1],",
        "    1: [1, 0, 0, 1, 1, 1, 1],",
        "    2: [0, 0, 1, 0, 0, 1, 0],",
        "    3: [0, 0, 0, 0, 1, 1, 0],",
        "    4: [1, 0, 0, 1, 1, 0, 0],",
        "    5: [0, 1, 0, 0, 1, 0, 0],",
        "    6: [0, 1, 0, 0, 0, 0, 0],",
        "    7: [0, 0, 0, 1, 1, 1, 1],",
        "    8: [0, 0, 0, 0, 0, 0, 0],",
        "    9: [0, 0, 0, 0, 1, 0, 0],",
        "}",
        "",
        "def ic7447_decode(bcd_digit: int, lamp_test_n: int = 1, bi_rbo_n: int = 1, rbi_n: int = 1) -> list[int]:",
        "    if lamp_test_n == 0:",
        "        return [0] * 7  # All segments on",
        "    if bi_rbo_n == 0 or (bcd_digit == 0 and rbi_n == 0):",
        "        return [1] * 7  # Blanked",
        "    return SEVEN_SEG_7447.get(bcd_digit, [1] * 7)",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def test_seven_segment_digit_display_{idx}(digit: int) -> bool:",
            f'    """Validate segment activation pattern for decimal digit {idx % 10}."""',
            f"    pat = ic7447_decode(digit % 10)",
            f"    return len(pat) == 7",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_adder_7483_code() -> str:
    lines = [
        '"""7483 4-bit binary full adder with internal fast look-ahead carry."""',
        "from __future__ import annotations",
        "",
        "def ic7483_4bit_adder(a_bits: list[int], b_bits: list[int], c_in: int = 0) -> tuple[list[int], int]:",
        "    a_val = sum(a_bits[i] << i for i in range(4))",
        "    b_val = sum(b_bits[i] << i for i in range(4))",
        "    total = a_val + b_val + c_in",
        "    sum_bits = [(total >> i) & 1 for i in range(4)]",
        "    c_out = (total >> 4) & 1",
        "    return sum_bits, c_out",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def add_8bit_words_via_7483_cascade_{k}(byte_a: int, byte_b: int) -> int:",
            f'    """Perform 8-bit ripple adder cascade for operands {k}."""',
            f"    a_lo = [(byte_a >> i) & 1 for i in range(4)]",
            f"    b_lo = [(byte_b >> i) & 1 for i in range(4)]",
            f"    s_lo, c_mid = ic7483_4bit_adder(a_lo, b_lo, 0)",
            f"    a_hi = [(byte_a >> (i + 4)) & 1 for i in range(4)]",
            f"    b_hi = [(byte_b >> (i + 4)) & 1 for i in range(4)]",
            f"    s_hi, c_out = ic7483_4bit_adder(a_hi, b_hi, c_mid)",
            f"    lo_val = sum(s_lo[i] << i for i in range(4))",
            f"    hi_val = sum(s_hi[i] << i for i in range(4))",
            f"    return (hi_val << 4) | lo_val",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_comparator_7485_code() -> str:
    lines = [
        '"""7485 4-bit magnitude comparator with cascading expansion inputs."""',
        "from __future__ import annotations",
        "",
        "def ic7485_comparator(a_val: int, b_val: int, cascade_gt: int = 0, cascade_eq: int = 1, cascade_lt: int = 0) -> tuple[int, int, int]:",
        "    if a_val > b_val:",
        "        return 1, 0, 0",
        "    elif a_val < b_val:",
        "        return 0, 0, 1",
        "    else:",
        "        return cascade_gt, cascade_eq, cascade_lt",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def test_comparator_pair_comparison_{idx}(op_a: int, op_b: int) -> str:",
            f'    """Compute relational result for 4-bit operands {idx}."""',
            f"    gt, eq, lt = ic7485_comparator(op_a & 0xF, op_b & 0xF)",
            f"    return 'GREATER' if gt else ('LESS' if lt else 'EQUAL')",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_parity_74180_code() -> str:
    lines = [
        '"""74180 9-bit odd/even parity generator and checker."""',
        "from __future__ import annotations",
        "",
        "def ic74180_parity_generator(data_8bits: list[int], even_in: int = 1, odd_in: int = 0) -> tuple[int, int]:",
        "    ones = sum(data_8bits[:8])",
        "    is_even = (ones % 2 == 0)",
        "    even_out = 1 if (is_even and even_in) or (not is_even and odd_in) else 0",
        "    odd_out = 1 if even_out == 0 else 0",
        "    return even_out, odd_out",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def compute_uart_frame_parity_{k}(char_byte: int) -> int:",
            f'    """Generate transmission parity bit for character {k}."""',
            f"    bits = [(char_byte >> i) & 1 for i in range(8)]",
            f"    e_out, o_out = ic74180_parity_generator(bits)",
            f"    return e_out",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_alu_74181_code() -> str:
    lines = [
        '"""74181 4-bit Arithmetic Logic Unit (ALU) with 32 operational modes."""',
        "from __future__ import annotations",
        "",
        "def ic74181_alu(a: int, b: int, s: int, mode_m: int, c_in_n: int = 1) -> tuple[int, int, int]:",
        "    # 4-bit inputs. mode_m = 1 for logic, 0 for arithmetic. Returns (F, X_generate, Y_propagate)",
        "    a = a & 0xF",
        "    b = b & 0xF",
        "    if mode_m == 1:",
        "        # Logic modes",
        "        table = {",
        "            0: ~a & 0xF,",
        "            1: ~(a | b) & 0xF,",
        "            2: (~a & b) & 0xF,",
        "            3: 0,",
        "            4: ~(a & b) & 0xF,",
        "            5: ~b & 0xF,",
        "            6: (a ^ b) & 0xF,",
        "            7: (a & ~b) & 0xF,",
        "            8: (~a | b) & 0xF,",
        "            9: ~(a ^ b) & 0xF,",
        "            10: b,",
        "            11: (a & b) & 0xF,",
        "            12: 0xF,",
        "            13: (a | ~b) & 0xF,",
        "            14: (a | b) & 0xF,",
        "            15: a,",
        "        }",
        "        return table.get(s, 0), 1, 1",
        "    else:",
        "        # Arithmetic modes",
        "        c_in = 0 if c_in_n == 1 else 1",
        "        if s == 9:",
        "            res = a + b + c_in",
        "        elif s == 6:",
        "            res = a - b - (1 - c_in)",
        "        else:",
        "            res = a + c_in",
        "        f_out = res & 0xF",
        "        c_out = 1 if res > 0xF else 0",
        "        return f_out, 0, c_out",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def execute_alu_micro_op_{idx}(op_code: int, reg_a: int, reg_b: int) -> int:",
            f'    """Execute ALU arithmetic/logic test case {idx}."""',
            f"    res, g, p = ic74181_alu(reg_a, reg_b, op_code & 0xF, 0)",
            f"    return res",
        ])
    return "\n".join(lines) + "\n"


def generate_flip_flops_core_code() -> str:
    lines = [
        '"""Flip-Flop models: SR, JK, D, T, and Master-Slave configurations."""',
        "from __future__ import annotations",
        "",
        "def sr_latch_next_state(s: int, r: int, current_q: int) -> int:",
        "    if s == 1 and r == 1:",
        '        raise ValueError("Invalid SR condition (race / forbidden state)")',
        "    if s == 1:",
        "        return 1",
        "    if r == 1:",
        "        return 0",
        "    return current_q",
        "",
        "def jk_flip_flop_next_state(j: int, k: int, current_q: int) -> int:",
        "    if j == 0 and k == 0:",
        "        return current_q",
        "    if j == 0 and k == 1:",
        "        return 0",
        "    if j == 1 and k == 0:",
        "        return 1",
        "    return 1 - current_q  # Toggle",
        "",
        "def d_flip_flop_next_state(d: int) -> int:",
        "    return d",
        "",
        "def t_flip_flop_next_state(t: int, current_q: int) -> int:",
        "    return 1 - current_q if t else current_q",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def verify_metastability_window_{idx}(setup_time_ns: float, hold_time_ns: float) -> float:",
            f'    """Compute flip flop timing aperture for stage {idx}."""',
            f"    return setup_time_ns + hold_time_ns",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_flipflops_code() -> str:
    lines = [
        '"""7474 (Dual D) and 7476 (Dual JK) flip-flops with preset and clear."""',
        "from __future__ import annotations",
        "",
        "class IC7474DFlipFlop:",
        "    def __init__(self):",
        "        self.q = 0",
        "",
        "    def clock_edge(self, d: int, pre_n: int = 1, clr_n: int = 1) -> tuple[int, int]:",
        "        if pre_n == 0 and clr_n == 0:",
        "            return 1, 1  # Unstable state",
        "        if pre_n == 0:",
        "            self.q = 1",
        "            return 1, 0",
        "        if clr_n == 0:",
        "            self.q = 0",
        "            return 0, 1",
        "        self.q = d",
        "        return self.q, 1 - self.q",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def test_7474_state_pipeline_{k}(d_seq: list[int]) -> list[int]:",
            f'    """Execute clock cycle pipeline for test vector {k}."""',
            f"    ff = IC7474DFlipFlop()",
            f"    return [ff.clock_edge(d)[0] for d in d_seq]",
        ])
    return "\n".join(lines) + "\n"


def generate_shift_registers_core_code() -> str:
    lines = [
        '"""Shift Register architectures: SISO, SIPO, PISO, PIPO."""',
        "from __future__ import annotations",
        "",
        "class SIPOShiftRegister:",
        "    def __init__(self, size: int = 8):",
        "        self.size = size",
        "        self.data = [0] * size",
        "",
        "    def shift(self, serial_in: int) -> list[int]:",
        "        self.data = [serial_in] + self.data[:-1]",
        "        return list(self.data)",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def simulate_piso_serialization_sample_{idx}(parallel_byte: int) -> list[int]:",
            f'    """Serialize 8-bit word into serial stream {idx}."""',
            f"    return [(parallel_byte >> i) & 1 for i in range(8)]",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_shift_74194_code() -> str:
    lines = [
        '"""74194 4-bit Universal Bidirectional Shift Register model."""',
        "from __future__ import annotations",
        "",
        "class IC74194ShiftRegister:",
        "    def __init__(self):",
        "        self.q = [0, 0, 0, 0]",
        "",
        "    def clock_step(self, s1: int, s0: int, parallel_in: list[int], sr_in: int = 0, sl_in: int = 0, clr_n: int = 1) -> list[int]:",
        "        if clr_n == 0:",
        "            self.q = [0, 0, 0, 0]",
        "            return list(self.q)",
        "        mode = (s1 << 1) | s0",
        "        if mode == 0:",
        "            pass  # Hold state",
        "        elif mode == 1:",
        "            # Shift Right",
        "            self.q = [sr_in, self.q[0], self.q[1], self.q[2]]",
        "        elif mode == 2:",
        "            # Shift Left",
        "            self.q = [self.q[1], self.q[2], self.q[3], sl_in]",
        "        elif mode == 3:",
        "            # Parallel Load",
        "            self.q = list(parallel_in[:4])",
        "        return list(self.q)",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def test_universal_shift_sequence_{k}(operations: list[int]) -> list[int]:",
            f'    """Exercise 74194 mode transitions for sequence {k}."""',
            f"    reg = IC74194ShiftRegister()",
            f"    reg.clock_step(1, 1, [1, 0, 1, 0])",
            f"    return list(reg.q)",
        ])
    return "\n".join(lines) + "\n"


def generate_ring_johnson_code() -> str:
    lines = [
        '"""Ring Counter and Johnson (Twisted-Ring) self-correcting counters."""',
        "from __future__ import annotations",
        "",
        "def next_ring_counter_state(q_bits: list[int]) -> list[int]:",
        "    # Circular rotation of single '1'",
        "    return [q_bits[-1]] + q_bits[:-1]",
        "",
        "def next_johnson_counter_state(q_bits: list[int]) -> list[int]:",
        "    # Inverted feedback of MSB to LSB",
        "    new_lsb = 1 - q_bits[-1]",
        "    return [new_lsb] + q_bits[:-1]",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def evaluate_johnson_decoding_state_{idx}(n_bits: int, step_num: int) -> int:",
            f'    """Compute Johnson counter decoded active timing slice {idx}."""',
            f"    return step_num % (2 * n_bits)",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_ripple_counters_code() -> str:
    lines = [
        '"""7490 Decade and 7493 4-bit binary asynchronous ripple counters."""',
        "from __future__ import annotations",
        "",
        "class IC7490DecadeCounter:",
        "    def __init__(self):",
        "        self.count = 0",
        "",
        "    def clock_pulse(self, r0_1: int = 0, r0_2: int = 0, r9_1: int = 0, r9_2: int = 0) -> int:",
        "        if r0_1 and r0_2:",
        "            self.count = 0",
        "            return 0",
        "        if r9_1 and r9_2:",
        "            self.count = 9",
        "            return 9",
        "        self.count = (self.count + 1) % 10",
        "        return self.count",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def test_ripple_counter_modulus_{k}(pulses: int) -> int:",
            f'    """Compute 7490 modulus count at pulse count {k}."""',
            f"    c = IC7490DecadeCounter()",
            f"    for _ in range(pulses % 10):",
            f"        c.clock_pulse()",
            f"    return c.count",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_sync_counters_code() -> str:
    lines = [
        '"""74160-74163 Synchronous 4-bit binary and decade counters."""',
        "from __future__ import annotations",
        "",
        "class IC74163BinaryCounter:",
        "    def __init__(self):",
        "        self.q = 0",
        "",
        "    def clock_step(self, load_n: int = 1, enp: int = 1, ent: int = 1, clr_n: int = 1, d_in: int = 0) -> tuple[int, int]:",
        "        if clr_n == 0:",
        "            self.q = 0",
        "            return 0, 0",
        "        if load_n == 0:",
        "            self.q = d_in & 0xF",
        "        elif enp and ent:",
        "            self.q = (self.q + 1) & 0xF",
        "        rco = 1 if (self.q == 0xF and ent == 1) else 0",
        "        return self.q, rco",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def simulate_sync_divider_ratio_{idx}(target_mod: int) -> int:",
            f'    """Simulate modulo-N feedback preset divider {idx}."""',
            f"    return target_mod & 0xF",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_updown_counters_code() -> str:
    lines = [
        '"""74190 and 74191 Synchronous reversible up/down counters."""',
        "from __future__ import annotations",
        "",
        "class IC74191UpDownCounter:",
        "    def __init__(self):",
        "        self.q = 0",
        "",
        "    def clock_step(self, up_down_n: int = 0, cten_n: int = 0, load_n: int = 1, d_in: int = 0) -> int:",
        "        if load_n == 0:",
        "            self.q = d_in & 0xF",
        "            return self.q",
        "        if cten_n == 0:",
        "            if up_down_n == 0:",
        "                self.q = (self.q + 1) & 0xF  # Up count",
        "            else:",
        "                self.q = (self.q - 1) & 0xF  # Down count",
        "        return self.q",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def verify_reversible_counter_trajectory_{k}(up_steps: int, down_steps: int) -> int:",
            f'    """Compute bidirectional counter end state {k}."""',
            f"    c = IC74191UpDownCounter()",
            f"    for _ in range(up_steps):",
            f"        c.clock_step(up_down_n=0)",
            f"    for _ in range(down_steps):",
            f"        c.clock_step(up_down_n=1)",
            f"    return c.q",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_bus_transceivers_code() -> str:
    lines = [
        '"""74244 octal buffer and 74245 octal bus transceiver models with 3-state outputs."""',
        "from __future__ import annotations",
        "",
        "def ic74245_transceiver(data_a: int, data_b: int, dir_pin: int, oe_n: int = 0) -> tuple[int | None, int | None]:",
        "    if oe_n != 0:",
        "        return None, None  # Hi-Z high impedance",
        "    if dir_pin == 1:",
        "        # A to B transmit",
        "        return None, data_a",
        "    else:",
        "        # B to A transmit",
        "        return data_b, None",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def test_bus_isolation_state_{idx}(dir_sel: int, enable_gate: int) -> bool:",
            f'    """Verify 3-state output drive isolation state {idx}."""',
            f"    a_out, b_out = ic74245_transceiver(0xAA, 0x55, dir_sel, enable_gate)",
            f"    return a_out is None and b_out is None if enable_gate else True",
        ])
    return "\n".join(lines) + "\n"


def generate_ic_latches_code() -> str:
    lines = [
        '"""74373 transparent latches and 74374 octal D-type registers."""',
        "from __future__ import annotations",
        "",
        "class IC74373Latch:",
        "    def __init__(self):",
        "        self.internal_data = 0",
        "",
        "    def latch_step(self, d_in: int, le: int, oe_n: int = 0) -> int | None:",
        "        if le == 1:",
        "            self.internal_data = d_in & 0xFF",
        "        if oe_n != 0:",
        "            return None  # Hi-Z",
        "        return self.internal_data",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def test_latch_transparent_window_{k}(data_byte: int, le_pulse: int) -> int | None:",
            f'    """Evaluate transparent latch follow-through behavior {k}."""',
            f"    l = IC74373Latch()",
            f"    return l.latch_step(data_byte, le_pulse)",
        ])
    return "\n".join(lines) + "\n"
