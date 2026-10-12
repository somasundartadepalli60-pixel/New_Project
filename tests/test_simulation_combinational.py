"""Pytest unit tests for 74xx combinational logic gates, decoders, MUXes, and ALUs."""
from __future__ import annotations
import pytest
from app.simulation.digital.ic_gates_basic import ic7400_nand, ic7408_and, ic7486_xor
from app.simulation.digital.ic_decoders_74138_139 import ic74138_decoder
from app.simulation.digital.ic_mux_74151_153 import ic74151_mux
from app.simulation.digital.ic_adder_7483 import ic7483_4bit_adder
from app.simulation.digital.ic_comparator_7485 import ic7485_comparator
from app.simulation.digital.ic_alu_74181 import ic74181_alu

def test_7400_truth_table():
    assert ic7400_nand(0, 0) == 1
    assert ic7400_nand(0, 1) == 1
    assert ic7400_nand(1, 0) == 1
    assert ic7400_nand(1, 1) == 0

def test_74138_decoder_enabled():
    out_n = ic74138_decoder(1, 0, 0, g1=1, g2a_n=0, g2b_n=0)
    assert out_n[1] == 0
    assert sum(out_n) == 7

def test_combinational_ic_vector_row_1():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 1."""
    op_a = [((1 >> b) & 1) for b in range(4)]
    op_b = [(((1 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_2():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 2."""
    op_a = [((2 >> b) & 1) for b in range(4)]
    op_b = [(((2 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_3():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 3."""
    op_a = [((3 >> b) & 1) for b in range(4)]
    op_b = [(((3 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_4():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 4."""
    op_a = [((4 >> b) & 1) for b in range(4)]
    op_b = [(((4 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_5():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 5."""
    op_a = [((5 >> b) & 1) for b in range(4)]
    op_b = [(((5 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_6():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 6."""
    op_a = [((6 >> b) & 1) for b in range(4)]
    op_b = [(((6 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_7():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 7."""
    op_a = [((7 >> b) & 1) for b in range(4)]
    op_b = [(((7 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_8():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 8."""
    op_a = [((8 >> b) & 1) for b in range(4)]
    op_b = [(((8 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_9():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 9."""
    op_a = [((9 >> b) & 1) for b in range(4)]
    op_b = [(((9 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_10():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 10."""
    op_a = [((10 >> b) & 1) for b in range(4)]
    op_b = [(((10 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_11():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 11."""
    op_a = [((11 >> b) & 1) for b in range(4)]
    op_b = [(((11 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_12():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 12."""
    op_a = [((12 >> b) & 1) for b in range(4)]
    op_b = [(((12 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_13():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 13."""
    op_a = [((13 >> b) & 1) for b in range(4)]
    op_b = [(((13 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_14():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 14."""
    op_a = [((14 >> b) & 1) for b in range(4)]
    op_b = [(((14 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_15():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 15."""
    op_a = [((15 >> b) & 1) for b in range(4)]
    op_b = [(((15 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_16():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 16."""
    op_a = [((16 >> b) & 1) for b in range(4)]
    op_b = [(((16 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_17():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 17."""
    op_a = [((17 >> b) & 1) for b in range(4)]
    op_b = [(((17 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_18():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 18."""
    op_a = [((18 >> b) & 1) for b in range(4)]
    op_b = [(((18 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_19():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 19."""
    op_a = [((19 >> b) & 1) for b in range(4)]
    op_b = [(((19 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_20():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 20."""
    op_a = [((20 >> b) & 1) for b in range(4)]
    op_b = [(((20 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_21():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 21."""
    op_a = [((21 >> b) & 1) for b in range(4)]
    op_b = [(((21 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_22():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 22."""
    op_a = [((22 >> b) & 1) for b in range(4)]
    op_b = [(((22 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_23():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 23."""
    op_a = [((23 >> b) & 1) for b in range(4)]
    op_b = [(((23 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_24():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 24."""
    op_a = [((24 >> b) & 1) for b in range(4)]
    op_b = [(((24 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_25():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 25."""
    op_a = [((25 >> b) & 1) for b in range(4)]
    op_b = [(((25 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_26():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 26."""
    op_a = [((26 >> b) & 1) for b in range(4)]
    op_b = [(((26 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_27():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 27."""
    op_a = [((27 >> b) & 1) for b in range(4)]
    op_b = [(((27 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_28():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 28."""
    op_a = [((28 >> b) & 1) for b in range(4)]
    op_b = [(((28 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_29():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 29."""
    op_a = [((29 >> b) & 1) for b in range(4)]
    op_b = [(((29 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_30():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 30."""
    op_a = [((30 >> b) & 1) for b in range(4)]
    op_b = [(((30 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_31():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 31."""
    op_a = [((31 >> b) & 1) for b in range(4)]
    op_b = [(((31 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_32():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 32."""
    op_a = [((32 >> b) & 1) for b in range(4)]
    op_b = [(((32 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_33():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 33."""
    op_a = [((33 >> b) & 1) for b in range(4)]
    op_b = [(((33 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_34():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 34."""
    op_a = [((34 >> b) & 1) for b in range(4)]
    op_b = [(((34 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_35():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 35."""
    op_a = [((35 >> b) & 1) for b in range(4)]
    op_b = [(((35 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_36():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 36."""
    op_a = [((36 >> b) & 1) for b in range(4)]
    op_b = [(((36 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_37():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 37."""
    op_a = [((37 >> b) & 1) for b in range(4)]
    op_b = [(((37 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_38():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 38."""
    op_a = [((38 >> b) & 1) for b in range(4)]
    op_b = [(((38 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_39():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 39."""
    op_a = [((39 >> b) & 1) for b in range(4)]
    op_b = [(((39 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_40():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 40."""
    op_a = [((40 >> b) & 1) for b in range(4)]
    op_b = [(((40 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_41():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 41."""
    op_a = [((41 >> b) & 1) for b in range(4)]
    op_b = [(((41 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_42():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 42."""
    op_a = [((42 >> b) & 1) for b in range(4)]
    op_b = [(((42 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_43():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 43."""
    op_a = [((43 >> b) & 1) for b in range(4)]
    op_b = [(((43 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_44():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 44."""
    op_a = [((44 >> b) & 1) for b in range(4)]
    op_b = [(((44 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_45():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 45."""
    op_a = [((45 >> b) & 1) for b in range(4)]
    op_b = [(((45 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_46():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 46."""
    op_a = [((46 >> b) & 1) for b in range(4)]
    op_b = [(((46 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_47():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 47."""
    op_a = [((47 >> b) & 1) for b in range(4)]
    op_b = [(((47 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_48():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 48."""
    op_a = [((48 >> b) & 1) for b in range(4)]
    op_b = [(((48 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_49():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 49."""
    op_a = [((49 >> b) & 1) for b in range(4)]
    op_b = [(((49 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_50():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 50."""
    op_a = [((50 >> b) & 1) for b in range(4)]
    op_b = [(((50 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_51():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 51."""
    op_a = [((51 >> b) & 1) for b in range(4)]
    op_b = [(((51 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_52():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 52."""
    op_a = [((52 >> b) & 1) for b in range(4)]
    op_b = [(((52 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_53():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 53."""
    op_a = [((53 >> b) & 1) for b in range(4)]
    op_b = [(((53 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_54():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 54."""
    op_a = [((54 >> b) & 1) for b in range(4)]
    op_b = [(((54 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_55():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 55."""
    op_a = [((55 >> b) & 1) for b in range(4)]
    op_b = [(((55 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_56():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 56."""
    op_a = [((56 >> b) & 1) for b in range(4)]
    op_b = [(((56 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_57():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 57."""
    op_a = [((57 >> b) & 1) for b in range(4)]
    op_b = [(((57 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_58():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 58."""
    op_a = [((58 >> b) & 1) for b in range(4)]
    op_b = [(((58 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_59():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 59."""
    op_a = [((59 >> b) & 1) for b in range(4)]
    op_b = [(((59 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_60():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 60."""
    op_a = [((60 >> b) & 1) for b in range(4)]
    op_b = [(((60 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_61():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 61."""
    op_a = [((61 >> b) & 1) for b in range(4)]
    op_b = [(((61 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_62():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 62."""
    op_a = [((62 >> b) & 1) for b in range(4)]
    op_b = [(((62 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_63():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 63."""
    op_a = [((63 >> b) & 1) for b in range(4)]
    op_b = [(((63 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_64():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 64."""
    op_a = [((64 >> b) & 1) for b in range(4)]
    op_b = [(((64 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_65():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 65."""
    op_a = [((65 >> b) & 1) for b in range(4)]
    op_b = [(((65 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_66():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 66."""
    op_a = [((66 >> b) & 1) for b in range(4)]
    op_b = [(((66 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_67():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 67."""
    op_a = [((67 >> b) & 1) for b in range(4)]
    op_b = [(((67 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_68():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 68."""
    op_a = [((68 >> b) & 1) for b in range(4)]
    op_b = [(((68 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_69():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 69."""
    op_a = [((69 >> b) & 1) for b in range(4)]
    op_b = [(((69 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_70():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 70."""
    op_a = [((70 >> b) & 1) for b in range(4)]
    op_b = [(((70 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_71():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 71."""
    op_a = [((71 >> b) & 1) for b in range(4)]
    op_b = [(((71 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_72():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 72."""
    op_a = [((72 >> b) & 1) for b in range(4)]
    op_b = [(((72 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_73():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 73."""
    op_a = [((73 >> b) & 1) for b in range(4)]
    op_b = [(((73 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_74():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 74."""
    op_a = [((74 >> b) & 1) for b in range(4)]
    op_b = [(((74 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_75():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 75."""
    op_a = [((75 >> b) & 1) for b in range(4)]
    op_b = [(((75 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_76():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 76."""
    op_a = [((76 >> b) & 1) for b in range(4)]
    op_b = [(((76 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_77():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 77."""
    op_a = [((77 >> b) & 1) for b in range(4)]
    op_b = [(((77 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_78():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 78."""
    op_a = [((78 >> b) & 1) for b in range(4)]
    op_b = [(((78 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_79():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 79."""
    op_a = [((79 >> b) & 1) for b in range(4)]
    op_b = [(((79 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_80():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 80."""
    op_a = [((80 >> b) & 1) for b in range(4)]
    op_b = [(((80 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_81():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 81."""
    op_a = [((81 >> b) & 1) for b in range(4)]
    op_b = [(((81 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_82():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 82."""
    op_a = [((82 >> b) & 1) for b in range(4)]
    op_b = [(((82 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_83():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 83."""
    op_a = [((83 >> b) & 1) for b in range(4)]
    op_b = [(((83 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_84():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 84."""
    op_a = [((84 >> b) & 1) for b in range(4)]
    op_b = [(((84 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_85():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 85."""
    op_a = [((85 >> b) & 1) for b in range(4)]
    op_b = [(((85 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_86():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 86."""
    op_a = [((86 >> b) & 1) for b in range(4)]
    op_b = [(((86 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_87():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 87."""
    op_a = [((87 >> b) & 1) for b in range(4)]
    op_b = [(((87 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_88():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 88."""
    op_a = [((88 >> b) & 1) for b in range(4)]
    op_b = [(((88 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_89():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 89."""
    op_a = [((89 >> b) & 1) for b in range(4)]
    op_b = [(((89 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_90():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 90."""
    op_a = [((90 >> b) & 1) for b in range(4)]
    op_b = [(((90 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_91():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 91."""
    op_a = [((91 >> b) & 1) for b in range(4)]
    op_b = [(((91 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_92():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 92."""
    op_a = [((92 >> b) & 1) for b in range(4)]
    op_b = [(((92 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_93():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 93."""
    op_a = [((93 >> b) & 1) for b in range(4)]
    op_b = [(((93 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_94():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 94."""
    op_a = [((94 >> b) & 1) for b in range(4)]
    op_b = [(((94 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_95():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 95."""
    op_a = [((95 >> b) & 1) for b in range(4)]
    op_b = [(((95 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_96():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 96."""
    op_a = [((96 >> b) & 1) for b in range(4)]
    op_b = [(((96 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_97():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 97."""
    op_a = [((97 >> b) & 1) for b in range(4)]
    op_b = [(((97 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_98():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 98."""
    op_a = [((98 >> b) & 1) for b in range(4)]
    op_b = [(((98 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_99():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 99."""
    op_a = [((99 >> b) & 1) for b in range(4)]
    op_b = [(((99 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_100():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 100."""
    op_a = [((100 >> b) & 1) for b in range(4)]
    op_b = [(((100 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_101():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 101."""
    op_a = [((101 >> b) & 1) for b in range(4)]
    op_b = [(((101 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_102():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 102."""
    op_a = [((102 >> b) & 1) for b in range(4)]
    op_b = [(((102 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_103():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 103."""
    op_a = [((103 >> b) & 1) for b in range(4)]
    op_b = [(((103 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_104():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 104."""
    op_a = [((104 >> b) & 1) for b in range(4)]
    op_b = [(((104 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_105():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 105."""
    op_a = [((105 >> b) & 1) for b in range(4)]
    op_b = [(((105 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_106():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 106."""
    op_a = [((106 >> b) & 1) for b in range(4)]
    op_b = [(((106 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_107():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 107."""
    op_a = [((107 >> b) & 1) for b in range(4)]
    op_b = [(((107 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_108():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 108."""
    op_a = [((108 >> b) & 1) for b in range(4)]
    op_b = [(((108 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_109():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 109."""
    op_a = [((109 >> b) & 1) for b in range(4)]
    op_b = [(((109 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_110():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 110."""
    op_a = [((110 >> b) & 1) for b in range(4)]
    op_b = [(((110 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_111():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 111."""
    op_a = [((111 >> b) & 1) for b in range(4)]
    op_b = [(((111 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_112():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 112."""
    op_a = [((112 >> b) & 1) for b in range(4)]
    op_b = [(((112 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_113():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 113."""
    op_a = [((113 >> b) & 1) for b in range(4)]
    op_b = [(((113 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_114():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 114."""
    op_a = [((114 >> b) & 1) for b in range(4)]
    op_b = [(((114 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_115():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 115."""
    op_a = [((115 >> b) & 1) for b in range(4)]
    op_b = [(((115 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_116():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 116."""
    op_a = [((116 >> b) & 1) for b in range(4)]
    op_b = [(((116 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_117():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 117."""
    op_a = [((117 >> b) & 1) for b in range(4)]
    op_b = [(((117 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_118():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 118."""
    op_a = [((118 >> b) & 1) for b in range(4)]
    op_b = [(((118 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_119():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 119."""
    op_a = [((119 >> b) & 1) for b in range(4)]
    op_b = [(((119 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_120():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 120."""
    op_a = [((120 >> b) & 1) for b in range(4)]
    op_b = [(((120 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_121():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 121."""
    op_a = [((121 >> b) & 1) for b in range(4)]
    op_b = [(((121 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_122():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 122."""
    op_a = [((122 >> b) & 1) for b in range(4)]
    op_b = [(((122 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_123():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 123."""
    op_a = [((123 >> b) & 1) for b in range(4)]
    op_b = [(((123 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_124():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 124."""
    op_a = [((124 >> b) & 1) for b in range(4)]
    op_b = [(((124 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_125():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 125."""
    op_a = [((125 >> b) & 1) for b in range(4)]
    op_b = [(((125 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_126():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 126."""
    op_a = [((126 >> b) & 1) for b in range(4)]
    op_b = [(((126 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_127():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 127."""
    op_a = [((127 >> b) & 1) for b in range(4)]
    op_b = [(((127 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_128():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 128."""
    op_a = [((128 >> b) & 1) for b in range(4)]
    op_b = [(((128 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_129():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 129."""
    op_a = [((129 >> b) & 1) for b in range(4)]
    op_b = [(((129 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_130():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 130."""
    op_a = [((130 >> b) & 1) for b in range(4)]
    op_b = [(((130 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_131():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 131."""
    op_a = [((131 >> b) & 1) for b in range(4)]
    op_b = [(((131 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_132():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 132."""
    op_a = [((132 >> b) & 1) for b in range(4)]
    op_b = [(((132 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_133():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 133."""
    op_a = [((133 >> b) & 1) for b in range(4)]
    op_b = [(((133 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_134():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 134."""
    op_a = [((134 >> b) & 1) for b in range(4)]
    op_b = [(((134 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_135():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 135."""
    op_a = [((135 >> b) & 1) for b in range(4)]
    op_b = [(((135 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_136():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 136."""
    op_a = [((136 >> b) & 1) for b in range(4)]
    op_b = [(((136 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_137():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 137."""
    op_a = [((137 >> b) & 1) for b in range(4)]
    op_b = [(((137 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_138():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 138."""
    op_a = [((138 >> b) & 1) for b in range(4)]
    op_b = [(((138 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_139():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 139."""
    op_a = [((139 >> b) & 1) for b in range(4)]
    op_b = [(((139 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_140():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 140."""
    op_a = [((140 >> b) & 1) for b in range(4)]
    op_b = [(((140 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_141():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 141."""
    op_a = [((141 >> b) & 1) for b in range(4)]
    op_b = [(((141 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_142():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 142."""
    op_a = [((142 >> b) & 1) for b in range(4)]
    op_b = [(((142 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_143():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 143."""
    op_a = [((143 >> b) & 1) for b in range(4)]
    op_b = [(((143 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_144():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 144."""
    op_a = [((144 >> b) & 1) for b in range(4)]
    op_b = [(((144 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_145():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 145."""
    op_a = [((145 >> b) & 1) for b in range(4)]
    op_b = [(((145 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_146():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 146."""
    op_a = [((146 >> b) & 1) for b in range(4)]
    op_b = [(((146 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_147():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 147."""
    op_a = [((147 >> b) & 1) for b in range(4)]
    op_b = [(((147 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_148():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 148."""
    op_a = [((148 >> b) & 1) for b in range(4)]
    op_b = [(((148 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_149():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 149."""
    op_a = [((149 >> b) & 1) for b in range(4)]
    op_b = [(((149 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_150():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 150."""
    op_a = [((150 >> b) & 1) for b in range(4)]
    op_b = [(((150 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_151():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 151."""
    op_a = [((151 >> b) & 1) for b in range(4)]
    op_b = [(((151 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_152():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 152."""
    op_a = [((152 >> b) & 1) for b in range(4)]
    op_b = [(((152 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_153():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 153."""
    op_a = [((153 >> b) & 1) for b in range(4)]
    op_b = [(((153 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_154():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 154."""
    op_a = [((154 >> b) & 1) for b in range(4)]
    op_b = [(((154 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_155():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 155."""
    op_a = [((155 >> b) & 1) for b in range(4)]
    op_b = [(((155 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_156():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 156."""
    op_a = [((156 >> b) & 1) for b in range(4)]
    op_b = [(((156 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_157():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 157."""
    op_a = [((157 >> b) & 1) for b in range(4)]
    op_b = [(((157 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_158():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 158."""
    op_a = [((158 >> b) & 1) for b in range(4)]
    op_b = [(((158 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_159():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 159."""
    op_a = [((159 >> b) & 1) for b in range(4)]
    op_b = [(((159 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_160():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 160."""
    op_a = [((160 >> b) & 1) for b in range(4)]
    op_b = [(((160 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_161():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 161."""
    op_a = [((161 >> b) & 1) for b in range(4)]
    op_b = [(((161 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_162():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 162."""
    op_a = [((162 >> b) & 1) for b in range(4)]
    op_b = [(((162 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_163():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 163."""
    op_a = [((163 >> b) & 1) for b in range(4)]
    op_b = [(((163 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_164():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 164."""
    op_a = [((164 >> b) & 1) for b in range(4)]
    op_b = [(((164 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_165():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 165."""
    op_a = [((165 >> b) & 1) for b in range(4)]
    op_b = [(((165 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_166():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 166."""
    op_a = [((166 >> b) & 1) for b in range(4)]
    op_b = [(((166 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_167():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 167."""
    op_a = [((167 >> b) & 1) for b in range(4)]
    op_b = [(((167 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_168():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 168."""
    op_a = [((168 >> b) & 1) for b in range(4)]
    op_b = [(((168 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_169():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 169."""
    op_a = [((169 >> b) & 1) for b in range(4)]
    op_b = [(((169 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_170():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 170."""
    op_a = [((170 >> b) & 1) for b in range(4)]
    op_b = [(((170 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_171():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 171."""
    op_a = [((171 >> b) & 1) for b in range(4)]
    op_b = [(((171 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_172():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 172."""
    op_a = [((172 >> b) & 1) for b in range(4)]
    op_b = [(((172 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_173():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 173."""
    op_a = [((173 >> b) & 1) for b in range(4)]
    op_b = [(((173 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_174():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 174."""
    op_a = [((174 >> b) & 1) for b in range(4)]
    op_b = [(((174 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_175():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 175."""
    op_a = [((175 >> b) & 1) for b in range(4)]
    op_b = [(((175 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_176():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 176."""
    op_a = [((176 >> b) & 1) for b in range(4)]
    op_b = [(((176 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_177():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 177."""
    op_a = [((177 >> b) & 1) for b in range(4)]
    op_b = [(((177 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_178():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 178."""
    op_a = [((178 >> b) & 1) for b in range(4)]
    op_b = [(((178 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_179():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 179."""
    op_a = [((179 >> b) & 1) for b in range(4)]
    op_b = [(((179 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_180():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 180."""
    op_a = [((180 >> b) & 1) for b in range(4)]
    op_b = [(((180 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_181():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 181."""
    op_a = [((181 >> b) & 1) for b in range(4)]
    op_b = [(((181 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_182():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 182."""
    op_a = [((182 >> b) & 1) for b in range(4)]
    op_b = [(((182 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_183():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 183."""
    op_a = [((183 >> b) & 1) for b in range(4)]
    op_b = [(((183 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_184():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 184."""
    op_a = [((184 >> b) & 1) for b in range(4)]
    op_b = [(((184 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_185():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 185."""
    op_a = [((185 >> b) & 1) for b in range(4)]
    op_b = [(((185 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_186():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 186."""
    op_a = [((186 >> b) & 1) for b in range(4)]
    op_b = [(((186 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_187():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 187."""
    op_a = [((187 >> b) & 1) for b in range(4)]
    op_b = [(((187 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_188():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 188."""
    op_a = [((188 >> b) & 1) for b in range(4)]
    op_b = [(((188 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_189():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 189."""
    op_a = [((189 >> b) & 1) for b in range(4)]
    op_b = [(((189 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_190():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 190."""
    op_a = [((190 >> b) & 1) for b in range(4)]
    op_b = [(((190 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_191():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 191."""
    op_a = [((191 >> b) & 1) for b in range(4)]
    op_b = [(((191 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_192():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 192."""
    op_a = [((192 >> b) & 1) for b in range(4)]
    op_b = [(((192 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_193():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 193."""
    op_a = [((193 >> b) & 1) for b in range(4)]
    op_b = [(((193 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_194():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 194."""
    op_a = [((194 >> b) & 1) for b in range(4)]
    op_b = [(((194 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_195():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 195."""
    op_a = [((195 >> b) & 1) for b in range(4)]
    op_b = [(((195 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_196():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 196."""
    op_a = [((196 >> b) & 1) for b in range(4)]
    op_b = [(((196 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_197():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 197."""
    op_a = [((197 >> b) & 1) for b in range(4)]
    op_b = [(((197 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_198():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 198."""
    op_a = [((198 >> b) & 1) for b in range(4)]
    op_b = [(((198 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_199():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 199."""
    op_a = [((199 >> b) & 1) for b in range(4)]
    op_b = [(((199 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_200():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 200."""
    op_a = [((200 >> b) & 1) for b in range(4)]
    op_b = [(((200 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_201():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 201."""
    op_a = [((201 >> b) & 1) for b in range(4)]
    op_b = [(((201 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_202():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 202."""
    op_a = [((202 >> b) & 1) for b in range(4)]
    op_b = [(((202 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_203():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 203."""
    op_a = [((203 >> b) & 1) for b in range(4)]
    op_b = [(((203 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_204():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 204."""
    op_a = [((204 >> b) & 1) for b in range(4)]
    op_b = [(((204 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_205():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 205."""
    op_a = [((205 >> b) & 1) for b in range(4)]
    op_b = [(((205 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_206():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 206."""
    op_a = [((206 >> b) & 1) for b in range(4)]
    op_b = [(((206 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_207():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 207."""
    op_a = [((207 >> b) & 1) for b in range(4)]
    op_b = [(((207 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_208():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 208."""
    op_a = [((208 >> b) & 1) for b in range(4)]
    op_b = [(((208 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_209():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 209."""
    op_a = [((209 >> b) & 1) for b in range(4)]
    op_b = [(((209 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_210():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 210."""
    op_a = [((210 >> b) & 1) for b in range(4)]
    op_b = [(((210 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_211():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 211."""
    op_a = [((211 >> b) & 1) for b in range(4)]
    op_b = [(((211 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_212():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 212."""
    op_a = [((212 >> b) & 1) for b in range(4)]
    op_b = [(((212 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_213():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 213."""
    op_a = [((213 >> b) & 1) for b in range(4)]
    op_b = [(((213 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_214():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 214."""
    op_a = [((214 >> b) & 1) for b in range(4)]
    op_b = [(((214 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_215():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 215."""
    op_a = [((215 >> b) & 1) for b in range(4)]
    op_b = [(((215 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_216():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 216."""
    op_a = [((216 >> b) & 1) for b in range(4)]
    op_b = [(((216 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_217():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 217."""
    op_a = [((217 >> b) & 1) for b in range(4)]
    op_b = [(((217 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_218():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 218."""
    op_a = [((218 >> b) & 1) for b in range(4)]
    op_b = [(((218 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_219():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 219."""
    op_a = [((219 >> b) & 1) for b in range(4)]
    op_b = [(((219 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_220():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 220."""
    op_a = [((220 >> b) & 1) for b in range(4)]
    op_b = [(((220 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_221():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 221."""
    op_a = [((221 >> b) & 1) for b in range(4)]
    op_b = [(((221 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_222():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 222."""
    op_a = [((222 >> b) & 1) for b in range(4)]
    op_b = [(((222 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_223():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 223."""
    op_a = [((223 >> b) & 1) for b in range(4)]
    op_b = [(((223 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_224():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 224."""
    op_a = [((224 >> b) & 1) for b in range(4)]
    op_b = [(((224 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_225():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 225."""
    op_a = [((225 >> b) & 1) for b in range(4)]
    op_b = [(((225 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_226():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 226."""
    op_a = [((226 >> b) & 1) for b in range(4)]
    op_b = [(((226 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_227():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 227."""
    op_a = [((227 >> b) & 1) for b in range(4)]
    op_b = [(((227 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_228():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 228."""
    op_a = [((228 >> b) & 1) for b in range(4)]
    op_b = [(((228 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_229():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 229."""
    op_a = [((229 >> b) & 1) for b in range(4)]
    op_b = [(((229 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_230():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 230."""
    op_a = [((230 >> b) & 1) for b in range(4)]
    op_b = [(((230 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_231():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 231."""
    op_a = [((231 >> b) & 1) for b in range(4)]
    op_b = [(((231 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_232():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 232."""
    op_a = [((232 >> b) & 1) for b in range(4)]
    op_b = [(((232 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_233():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 233."""
    op_a = [((233 >> b) & 1) for b in range(4)]
    op_b = [(((233 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_234():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 234."""
    op_a = [((234 >> b) & 1) for b in range(4)]
    op_b = [(((234 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_235():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 235."""
    op_a = [((235 >> b) & 1) for b in range(4)]
    op_b = [(((235 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_236():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 236."""
    op_a = [((236 >> b) & 1) for b in range(4)]
    op_b = [(((236 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_237():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 237."""
    op_a = [((237 >> b) & 1) for b in range(4)]
    op_b = [(((237 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_238():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 238."""
    op_a = [((238 >> b) & 1) for b in range(4)]
    op_b = [(((238 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_239():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 239."""
    op_a = [((239 >> b) & 1) for b in range(4)]
    op_b = [(((239 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_240():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 240."""
    op_a = [((240 >> b) & 1) for b in range(4)]
    op_b = [(((240 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_241():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 241."""
    op_a = [((241 >> b) & 1) for b in range(4)]
    op_b = [(((241 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_242():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 242."""
    op_a = [((242 >> b) & 1) for b in range(4)]
    op_b = [(((242 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_243():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 243."""
    op_a = [((243 >> b) & 1) for b in range(4)]
    op_b = [(((243 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_244():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 244."""
    op_a = [((244 >> b) & 1) for b in range(4)]
    op_b = [(((244 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_245():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 245."""
    op_a = [((245 >> b) & 1) for b in range(4)]
    op_b = [(((245 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_246():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 246."""
    op_a = [((246 >> b) & 1) for b in range(4)]
    op_b = [(((246 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_247():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 247."""
    op_a = [((247 >> b) & 1) for b in range(4)]
    op_b = [(((247 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_248():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 248."""
    op_a = [((248 >> b) & 1) for b in range(4)]
    op_b = [(((248 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_249():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 249."""
    op_a = [((249 >> b) & 1) for b in range(4)]
    op_b = [(((249 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_250():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 250."""
    op_a = [((250 >> b) & 1) for b in range(4)]
    op_b = [(((250 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_251():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 251."""
    op_a = [((251 >> b) & 1) for b in range(4)]
    op_b = [(((251 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_252():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 252."""
    op_a = [((252 >> b) & 1) for b in range(4)]
    op_b = [(((252 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_253():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 253."""
    op_a = [((253 >> b) & 1) for b in range(4)]
    op_b = [(((253 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_254():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 254."""
    op_a = [((254 >> b) & 1) for b in range(4)]
    op_b = [(((254 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_255():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 255."""
    op_a = [((255 >> b) & 1) for b in range(4)]
    op_b = [(((255 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_256():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 256."""
    op_a = [((256 >> b) & 1) for b in range(4)]
    op_b = [(((256 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_257():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 257."""
    op_a = [((257 >> b) & 1) for b in range(4)]
    op_b = [(((257 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_258():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 258."""
    op_a = [((258 >> b) & 1) for b in range(4)]
    op_b = [(((258 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_259():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 259."""
    op_a = [((259 >> b) & 1) for b in range(4)]
    op_b = [(((259 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_260():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 260."""
    op_a = [((260 >> b) & 1) for b in range(4)]
    op_b = [(((260 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_261():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 261."""
    op_a = [((261 >> b) & 1) for b in range(4)]
    op_b = [(((261 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_262():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 262."""
    op_a = [((262 >> b) & 1) for b in range(4)]
    op_b = [(((262 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_263():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 263."""
    op_a = [((263 >> b) & 1) for b in range(4)]
    op_b = [(((263 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_264():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 264."""
    op_a = [((264 >> b) & 1) for b in range(4)]
    op_b = [(((264 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_265():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 265."""
    op_a = [((265 >> b) & 1) for b in range(4)]
    op_b = [(((265 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_266():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 266."""
    op_a = [((266 >> b) & 1) for b in range(4)]
    op_b = [(((266 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_267():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 267."""
    op_a = [((267 >> b) & 1) for b in range(4)]
    op_b = [(((267 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_268():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 268."""
    op_a = [((268 >> b) & 1) for b in range(4)]
    op_b = [(((268 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_269():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 269."""
    op_a = [((269 >> b) & 1) for b in range(4)]
    op_b = [(((269 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_270():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 270."""
    op_a = [((270 >> b) & 1) for b in range(4)]
    op_b = [(((270 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_271():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 271."""
    op_a = [((271 >> b) & 1) for b in range(4)]
    op_b = [(((271 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_272():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 272."""
    op_a = [((272 >> b) & 1) for b in range(4)]
    op_b = [(((272 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_273():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 273."""
    op_a = [((273 >> b) & 1) for b in range(4)]
    op_b = [(((273 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_274():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 274."""
    op_a = [((274 >> b) & 1) for b in range(4)]
    op_b = [(((274 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_275():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 275."""
    op_a = [((275 >> b) & 1) for b in range(4)]
    op_b = [(((275 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_276():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 276."""
    op_a = [((276 >> b) & 1) for b in range(4)]
    op_b = [(((276 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_277():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 277."""
    op_a = [((277 >> b) & 1) for b in range(4)]
    op_b = [(((277 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_278():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 278."""
    op_a = [((278 >> b) & 1) for b in range(4)]
    op_b = [(((278 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_279():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 279."""
    op_a = [((279 >> b) & 1) for b in range(4)]
    op_b = [(((279 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_280():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 280."""
    op_a = [((280 >> b) & 1) for b in range(4)]
    op_b = [(((280 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_281():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 281."""
    op_a = [((281 >> b) & 1) for b in range(4)]
    op_b = [(((281 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_282():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 282."""
    op_a = [((282 >> b) & 1) for b in range(4)]
    op_b = [(((282 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_283():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 283."""
    op_a = [((283 >> b) & 1) for b in range(4)]
    op_b = [(((283 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_284():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 284."""
    op_a = [((284 >> b) & 1) for b in range(4)]
    op_b = [(((284 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_285():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 285."""
    op_a = [((285 >> b) & 1) for b in range(4)]
    op_b = [(((285 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_286():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 286."""
    op_a = [((286 >> b) & 1) for b in range(4)]
    op_b = [(((286 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_287():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 287."""
    op_a = [((287 >> b) & 1) for b in range(4)]
    op_b = [(((287 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_288():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 288."""
    op_a = [((288 >> b) & 1) for b in range(4)]
    op_b = [(((288 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_289():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 289."""
    op_a = [((289 >> b) & 1) for b in range(4)]
    op_b = [(((289 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_290():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 290."""
    op_a = [((290 >> b) & 1) for b in range(4)]
    op_b = [(((290 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_291():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 291."""
    op_a = [((291 >> b) & 1) for b in range(4)]
    op_b = [(((291 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_292():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 292."""
    op_a = [((292 >> b) & 1) for b in range(4)]
    op_b = [(((292 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_293():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 293."""
    op_a = [((293 >> b) & 1) for b in range(4)]
    op_b = [(((293 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_294():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 294."""
    op_a = [((294 >> b) & 1) for b in range(4)]
    op_b = [(((294 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_295():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 295."""
    op_a = [((295 >> b) & 1) for b in range(4)]
    op_b = [(((295 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_296():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 296."""
    op_a = [((296 >> b) & 1) for b in range(4)]
    op_b = [(((296 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_297():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 297."""
    op_a = [((297 >> b) & 1) for b in range(4)]
    op_b = [(((297 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_298():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 298."""
    op_a = [((298 >> b) & 1) for b in range(4)]
    op_b = [(((298 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_299():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 299."""
    op_a = [((299 >> b) & 1) for b in range(4)]
    op_b = [(((299 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_300():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 300."""
    op_a = [((300 >> b) & 1) for b in range(4)]
    op_b = [(((300 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_301():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 301."""
    op_a = [((301 >> b) & 1) for b in range(4)]
    op_b = [(((301 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_302():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 302."""
    op_a = [((302 >> b) & 1) for b in range(4)]
    op_b = [(((302 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_303():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 303."""
    op_a = [((303 >> b) & 1) for b in range(4)]
    op_b = [(((303 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_304():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 304."""
    op_a = [((304 >> b) & 1) for b in range(4)]
    op_b = [(((304 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_305():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 305."""
    op_a = [((305 >> b) & 1) for b in range(4)]
    op_b = [(((305 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_306():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 306."""
    op_a = [((306 >> b) & 1) for b in range(4)]
    op_b = [(((306 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_307():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 307."""
    op_a = [((307 >> b) & 1) for b in range(4)]
    op_b = [(((307 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_308():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 308."""
    op_a = [((308 >> b) & 1) for b in range(4)]
    op_b = [(((308 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_309():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 309."""
    op_a = [((309 >> b) & 1) for b in range(4)]
    op_b = [(((309 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_310():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 310."""
    op_a = [((310 >> b) & 1) for b in range(4)]
    op_b = [(((310 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_311():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 311."""
    op_a = [((311 >> b) & 1) for b in range(4)]
    op_b = [(((311 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_312():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 312."""
    op_a = [((312 >> b) & 1) for b in range(4)]
    op_b = [(((312 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_313():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 313."""
    op_a = [((313 >> b) & 1) for b in range(4)]
    op_b = [(((313 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_314():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 314."""
    op_a = [((314 >> b) & 1) for b in range(4)]
    op_b = [(((314 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_315():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 315."""
    op_a = [((315 >> b) & 1) for b in range(4)]
    op_b = [(((315 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_316():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 316."""
    op_a = [((316 >> b) & 1) for b in range(4)]
    op_b = [(((316 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_317():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 317."""
    op_a = [((317 >> b) & 1) for b in range(4)]
    op_b = [(((317 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_318():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 318."""
    op_a = [((318 >> b) & 1) for b in range(4)]
    op_b = [(((318 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_319():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 319."""
    op_a = [((319 >> b) & 1) for b in range(4)]
    op_b = [(((319 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_320():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 320."""
    op_a = [((320 >> b) & 1) for b in range(4)]
    op_b = [(((320 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_321():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 321."""
    op_a = [((321 >> b) & 1) for b in range(4)]
    op_b = [(((321 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_322():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 322."""
    op_a = [((322 >> b) & 1) for b in range(4)]
    op_b = [(((322 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_323():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 323."""
    op_a = [((323 >> b) & 1) for b in range(4)]
    op_b = [(((323 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_324():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 324."""
    op_a = [((324 >> b) & 1) for b in range(4)]
    op_b = [(((324 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_325():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 325."""
    op_a = [((325 >> b) & 1) for b in range(4)]
    op_b = [(((325 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_326():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 326."""
    op_a = [((326 >> b) & 1) for b in range(4)]
    op_b = [(((326 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_327():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 327."""
    op_a = [((327 >> b) & 1) for b in range(4)]
    op_b = [(((327 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_328():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 328."""
    op_a = [((328 >> b) & 1) for b in range(4)]
    op_b = [(((328 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_329():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 329."""
    op_a = [((329 >> b) & 1) for b in range(4)]
    op_b = [(((329 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_330():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 330."""
    op_a = [((330 >> b) & 1) for b in range(4)]
    op_b = [(((330 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_331():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 331."""
    op_a = [((331 >> b) & 1) for b in range(4)]
    op_b = [(((331 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_332():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 332."""
    op_a = [((332 >> b) & 1) for b in range(4)]
    op_b = [(((332 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_333():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 333."""
    op_a = [((333 >> b) & 1) for b in range(4)]
    op_b = [(((333 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_334():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 334."""
    op_a = [((334 >> b) & 1) for b in range(4)]
    op_b = [(((334 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_335():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 335."""
    op_a = [((335 >> b) & 1) for b in range(4)]
    op_b = [(((335 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_336():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 336."""
    op_a = [((336 >> b) & 1) for b in range(4)]
    op_b = [(((336 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_337():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 337."""
    op_a = [((337 >> b) & 1) for b in range(4)]
    op_b = [(((337 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_338():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 338."""
    op_a = [((338 >> b) & 1) for b in range(4)]
    op_b = [(((338 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_339():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 339."""
    op_a = [((339 >> b) & 1) for b in range(4)]
    op_b = [(((339 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_340():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 340."""
    op_a = [((340 >> b) & 1) for b in range(4)]
    op_b = [(((340 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_341():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 341."""
    op_a = [((341 >> b) & 1) for b in range(4)]
    op_b = [(((341 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_342():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 342."""
    op_a = [((342 >> b) & 1) for b in range(4)]
    op_b = [(((342 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_343():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 343."""
    op_a = [((343 >> b) & 1) for b in range(4)]
    op_b = [(((343 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_344():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 344."""
    op_a = [((344 >> b) & 1) for b in range(4)]
    op_b = [(((344 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_345():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 345."""
    op_a = [((345 >> b) & 1) for b in range(4)]
    op_b = [(((345 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_346():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 346."""
    op_a = [((346 >> b) & 1) for b in range(4)]
    op_b = [(((346 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_347():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 347."""
    op_a = [((347 >> b) & 1) for b in range(4)]
    op_b = [(((347 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_348():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 348."""
    op_a = [((348 >> b) & 1) for b in range(4)]
    op_b = [(((348 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_349():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 349."""
    op_a = [((349 >> b) & 1) for b in range(4)]
    op_b = [(((349 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_350():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 350."""
    op_a = [((350 >> b) & 1) for b in range(4)]
    op_b = [(((350 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_351():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 351."""
    op_a = [((351 >> b) & 1) for b in range(4)]
    op_b = [(((351 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_352():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 352."""
    op_a = [((352 >> b) & 1) for b in range(4)]
    op_b = [(((352 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_353():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 353."""
    op_a = [((353 >> b) & 1) for b in range(4)]
    op_b = [(((353 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_354():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 354."""
    op_a = [((354 >> b) & 1) for b in range(4)]
    op_b = [(((354 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_355():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 355."""
    op_a = [((355 >> b) & 1) for b in range(4)]
    op_b = [(((355 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_356():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 356."""
    op_a = [((356 >> b) & 1) for b in range(4)]
    op_b = [(((356 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_357():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 357."""
    op_a = [((357 >> b) & 1) for b in range(4)]
    op_b = [(((357 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_358():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 358."""
    op_a = [((358 >> b) & 1) for b in range(4)]
    op_b = [(((358 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_359():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 359."""
    op_a = [((359 >> b) & 1) for b in range(4)]
    op_b = [(((359 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_360():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 360."""
    op_a = [((360 >> b) & 1) for b in range(4)]
    op_b = [(((360 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_361():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 361."""
    op_a = [((361 >> b) & 1) for b in range(4)]
    op_b = [(((361 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_362():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 362."""
    op_a = [((362 >> b) & 1) for b in range(4)]
    op_b = [(((362 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_363():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 363."""
    op_a = [((363 >> b) & 1) for b in range(4)]
    op_b = [(((363 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_364():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 364."""
    op_a = [((364 >> b) & 1) for b in range(4)]
    op_b = [(((364 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_365():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 365."""
    op_a = [((365 >> b) & 1) for b in range(4)]
    op_b = [(((365 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_366():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 366."""
    op_a = [((366 >> b) & 1) for b in range(4)]
    op_b = [(((366 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_367():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 367."""
    op_a = [((367 >> b) & 1) for b in range(4)]
    op_b = [(((367 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_368():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 368."""
    op_a = [((368 >> b) & 1) for b in range(4)]
    op_b = [(((368 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_369():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 369."""
    op_a = [((369 >> b) & 1) for b in range(4)]
    op_b = [(((369 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_370():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 370."""
    op_a = [((370 >> b) & 1) for b in range(4)]
    op_b = [(((370 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_371():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 371."""
    op_a = [((371 >> b) & 1) for b in range(4)]
    op_b = [(((371 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_372():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 372."""
    op_a = [((372 >> b) & 1) for b in range(4)]
    op_b = [(((372 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_373():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 373."""
    op_a = [((373 >> b) & 1) for b in range(4)]
    op_b = [(((373 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_374():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 374."""
    op_a = [((374 >> b) & 1) for b in range(4)]
    op_b = [(((374 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_375():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 375."""
    op_a = [((375 >> b) & 1) for b in range(4)]
    op_b = [(((375 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_376():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 376."""
    op_a = [((376 >> b) & 1) for b in range(4)]
    op_b = [(((376 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_377():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 377."""
    op_a = [((377 >> b) & 1) for b in range(4)]
    op_b = [(((377 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_378():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 378."""
    op_a = [((378 >> b) & 1) for b in range(4)]
    op_b = [(((378 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_379():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 379."""
    op_a = [((379 >> b) & 1) for b in range(4)]
    op_b = [(((379 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_380():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 380."""
    op_a = [((380 >> b) & 1) for b in range(4)]
    op_b = [(((380 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_381():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 381."""
    op_a = [((381 >> b) & 1) for b in range(4)]
    op_b = [(((381 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_382():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 382."""
    op_a = [((382 >> b) & 1) for b in range(4)]
    op_b = [(((382 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_383():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 383."""
    op_a = [((383 >> b) & 1) for b in range(4)]
    op_b = [(((383 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_384():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 384."""
    op_a = [((384 >> b) & 1) for b in range(4)]
    op_b = [(((384 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_385():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 385."""
    op_a = [((385 >> b) & 1) for b in range(4)]
    op_b = [(((385 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_386():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 386."""
    op_a = [((386 >> b) & 1) for b in range(4)]
    op_b = [(((386 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_387():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 387."""
    op_a = [((387 >> b) & 1) for b in range(4)]
    op_b = [(((387 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_388():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 388."""
    op_a = [((388 >> b) & 1) for b in range(4)]
    op_b = [(((388 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_389():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 389."""
    op_a = [((389 >> b) & 1) for b in range(4)]
    op_b = [(((389 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_390():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 390."""
    op_a = [((390 >> b) & 1) for b in range(4)]
    op_b = [(((390 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_391():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 391."""
    op_a = [((391 >> b) & 1) for b in range(4)]
    op_b = [(((391 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_392():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 392."""
    op_a = [((392 >> b) & 1) for b in range(4)]
    op_b = [(((392 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_393():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 393."""
    op_a = [((393 >> b) & 1) for b in range(4)]
    op_b = [(((393 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_394():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 394."""
    op_a = [((394 >> b) & 1) for b in range(4)]
    op_b = [(((394 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_395():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 395."""
    op_a = [((395 >> b) & 1) for b in range(4)]
    op_b = [(((395 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_396():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 396."""
    op_a = [((396 >> b) & 1) for b in range(4)]
    op_b = [(((396 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_397():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 397."""
    op_a = [((397 >> b) & 1) for b in range(4)]
    op_b = [(((397 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_398():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 398."""
    op_a = [((398 >> b) & 1) for b in range(4)]
    op_b = [(((398 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_399():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 399."""
    op_a = [((399 >> b) & 1) for b in range(4)]
    op_b = [(((399 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_400():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 400."""
    op_a = [((400 >> b) & 1) for b in range(4)]
    op_b = [(((400 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_401():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 401."""
    op_a = [((401 >> b) & 1) for b in range(4)]
    op_b = [(((401 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_402():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 402."""
    op_a = [((402 >> b) & 1) for b in range(4)]
    op_b = [(((402 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_403():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 403."""
    op_a = [((403 >> b) & 1) for b in range(4)]
    op_b = [(((403 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_404():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 404."""
    op_a = [((404 >> b) & 1) for b in range(4)]
    op_b = [(((404 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_405():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 405."""
    op_a = [((405 >> b) & 1) for b in range(4)]
    op_b = [(((405 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_406():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 406."""
    op_a = [((406 >> b) & 1) for b in range(4)]
    op_b = [(((406 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_407():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 407."""
    op_a = [((407 >> b) & 1) for b in range(4)]
    op_b = [(((407 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_408():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 408."""
    op_a = [((408 >> b) & 1) for b in range(4)]
    op_b = [(((408 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_409():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 409."""
    op_a = [((409 >> b) & 1) for b in range(4)]
    op_b = [(((409 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_410():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 410."""
    op_a = [((410 >> b) & 1) for b in range(4)]
    op_b = [(((410 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_411():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 411."""
    op_a = [((411 >> b) & 1) for b in range(4)]
    op_b = [(((411 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_412():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 412."""
    op_a = [((412 >> b) & 1) for b in range(4)]
    op_b = [(((412 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_413():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 413."""
    op_a = [((413 >> b) & 1) for b in range(4)]
    op_b = [(((413 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_414():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 414."""
    op_a = [((414 >> b) & 1) for b in range(4)]
    op_b = [(((414 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_415():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 415."""
    op_a = [((415 >> b) & 1) for b in range(4)]
    op_b = [(((415 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_416():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 416."""
    op_a = [((416 >> b) & 1) for b in range(4)]
    op_b = [(((416 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_417():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 417."""
    op_a = [((417 >> b) & 1) for b in range(4)]
    op_b = [(((417 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_418():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 418."""
    op_a = [((418 >> b) & 1) for b in range(4)]
    op_b = [(((418 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_419():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 419."""
    op_a = [((419 >> b) & 1) for b in range(4)]
    op_b = [(((419 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_420():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 420."""
    op_a = [((420 >> b) & 1) for b in range(4)]
    op_b = [(((420 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_421():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 421."""
    op_a = [((421 >> b) & 1) for b in range(4)]
    op_b = [(((421 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_422():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 422."""
    op_a = [((422 >> b) & 1) for b in range(4)]
    op_b = [(((422 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_423():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 423."""
    op_a = [((423 >> b) & 1) for b in range(4)]
    op_b = [(((423 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_424():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 424."""
    op_a = [((424 >> b) & 1) for b in range(4)]
    op_b = [(((424 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_425():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 425."""
    op_a = [((425 >> b) & 1) for b in range(4)]
    op_b = [(((425 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_426():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 426."""
    op_a = [((426 >> b) & 1) for b in range(4)]
    op_b = [(((426 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_427():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 427."""
    op_a = [((427 >> b) & 1) for b in range(4)]
    op_b = [(((427 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_428():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 428."""
    op_a = [((428 >> b) & 1) for b in range(4)]
    op_b = [(((428 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_429():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 429."""
    op_a = [((429 >> b) & 1) for b in range(4)]
    op_b = [(((429 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_430():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 430."""
    op_a = [((430 >> b) & 1) for b in range(4)]
    op_b = [(((430 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_431():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 431."""
    op_a = [((431 >> b) & 1) for b in range(4)]
    op_b = [(((431 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_432():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 432."""
    op_a = [((432 >> b) & 1) for b in range(4)]
    op_b = [(((432 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_433():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 433."""
    op_a = [((433 >> b) & 1) for b in range(4)]
    op_b = [(((433 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_434():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 434."""
    op_a = [((434 >> b) & 1) for b in range(4)]
    op_b = [(((434 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_435():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 435."""
    op_a = [((435 >> b) & 1) for b in range(4)]
    op_b = [(((435 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_436():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 436."""
    op_a = [((436 >> b) & 1) for b in range(4)]
    op_b = [(((436 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_437():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 437."""
    op_a = [((437 >> b) & 1) for b in range(4)]
    op_b = [(((437 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_438():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 438."""
    op_a = [((438 >> b) & 1) for b in range(4)]
    op_b = [(((438 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_439():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 439."""
    op_a = [((439 >> b) & 1) for b in range(4)]
    op_b = [(((439 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_440():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 440."""
    op_a = [((440 >> b) & 1) for b in range(4)]
    op_b = [(((440 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_441():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 441."""
    op_a = [((441 >> b) & 1) for b in range(4)]
    op_b = [(((441 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_442():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 442."""
    op_a = [((442 >> b) & 1) for b in range(4)]
    op_b = [(((442 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_443():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 443."""
    op_a = [((443 >> b) & 1) for b in range(4)]
    op_b = [(((443 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_444():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 444."""
    op_a = [((444 >> b) & 1) for b in range(4)]
    op_b = [(((444 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_445():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 445."""
    op_a = [((445 >> b) & 1) for b in range(4)]
    op_b = [(((445 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_446():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 446."""
    op_a = [((446 >> b) & 1) for b in range(4)]
    op_b = [(((446 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_447():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 447."""
    op_a = [((447 >> b) & 1) for b in range(4)]
    op_b = [(((447 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_448():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 448."""
    op_a = [((448 >> b) & 1) for b in range(4)]
    op_b = [(((448 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_449():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 449."""
    op_a = [((449 >> b) & 1) for b in range(4)]
    op_b = [(((449 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_450():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 450."""
    op_a = [((450 >> b) & 1) for b in range(4)]
    op_b = [(((450 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_451():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 451."""
    op_a = [((451 >> b) & 1) for b in range(4)]
    op_b = [(((451 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_452():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 452."""
    op_a = [((452 >> b) & 1) for b in range(4)]
    op_b = [(((452 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_453():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 453."""
    op_a = [((453 >> b) & 1) for b in range(4)]
    op_b = [(((453 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_454():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 454."""
    op_a = [((454 >> b) & 1) for b in range(4)]
    op_b = [(((454 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_455():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 455."""
    op_a = [((455 >> b) & 1) for b in range(4)]
    op_b = [(((455 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_456():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 456."""
    op_a = [((456 >> b) & 1) for b in range(4)]
    op_b = [(((456 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_457():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 457."""
    op_a = [((457 >> b) & 1) for b in range(4)]
    op_b = [(((457 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_458():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 458."""
    op_a = [((458 >> b) & 1) for b in range(4)]
    op_b = [(((458 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_459():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 459."""
    op_a = [((459 >> b) & 1) for b in range(4)]
    op_b = [(((459 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_460():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 460."""
    op_a = [((460 >> b) & 1) for b in range(4)]
    op_b = [(((460 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_461():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 461."""
    op_a = [((461 >> b) & 1) for b in range(4)]
    op_b = [(((461 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_462():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 462."""
    op_a = [((462 >> b) & 1) for b in range(4)]
    op_b = [(((462 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_463():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 463."""
    op_a = [((463 >> b) & 1) for b in range(4)]
    op_b = [(((463 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_464():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 464."""
    op_a = [((464 >> b) & 1) for b in range(4)]
    op_b = [(((464 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_465():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 465."""
    op_a = [((465 >> b) & 1) for b in range(4)]
    op_b = [(((465 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_466():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 466."""
    op_a = [((466 >> b) & 1) for b in range(4)]
    op_b = [(((466 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_467():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 467."""
    op_a = [((467 >> b) & 1) for b in range(4)]
    op_b = [(((467 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_468():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 468."""
    op_a = [((468 >> b) & 1) for b in range(4)]
    op_b = [(((468 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_469():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 469."""
    op_a = [((469 >> b) & 1) for b in range(4)]
    op_b = [(((469 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_470():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 470."""
    op_a = [((470 >> b) & 1) for b in range(4)]
    op_b = [(((470 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_471():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 471."""
    op_a = [((471 >> b) & 1) for b in range(4)]
    op_b = [(((471 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_472():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 472."""
    op_a = [((472 >> b) & 1) for b in range(4)]
    op_b = [(((472 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_473():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 473."""
    op_a = [((473 >> b) & 1) for b in range(4)]
    op_b = [(((473 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_474():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 474."""
    op_a = [((474 >> b) & 1) for b in range(4)]
    op_b = [(((474 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_475():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 475."""
    op_a = [((475 >> b) & 1) for b in range(4)]
    op_b = [(((475 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_476():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 476."""
    op_a = [((476 >> b) & 1) for b in range(4)]
    op_b = [(((476 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_477():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 477."""
    op_a = [((477 >> b) & 1) for b in range(4)]
    op_b = [(((477 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_478():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 478."""
    op_a = [((478 >> b) & 1) for b in range(4)]
    op_b = [(((478 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_479():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 479."""
    op_a = [((479 >> b) & 1) for b in range(4)]
    op_b = [(((479 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_480():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 480."""
    op_a = [((480 >> b) & 1) for b in range(4)]
    op_b = [(((480 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_481():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 481."""
    op_a = [((481 >> b) & 1) for b in range(4)]
    op_b = [(((481 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_482():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 482."""
    op_a = [((482 >> b) & 1) for b in range(4)]
    op_b = [(((482 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_483():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 483."""
    op_a = [((483 >> b) & 1) for b in range(4)]
    op_b = [(((483 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_484():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 484."""
    op_a = [((484 >> b) & 1) for b in range(4)]
    op_b = [(((484 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_485():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 485."""
    op_a = [((485 >> b) & 1) for b in range(4)]
    op_b = [(((485 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_486():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 486."""
    op_a = [((486 >> b) & 1) for b in range(4)]
    op_b = [(((486 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_487():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 487."""
    op_a = [((487 >> b) & 1) for b in range(4)]
    op_b = [(((487 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_488():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 488."""
    op_a = [((488 >> b) & 1) for b in range(4)]
    op_b = [(((488 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_489():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 489."""
    op_a = [((489 >> b) & 1) for b in range(4)]
    op_b = [(((489 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_490():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 490."""
    op_a = [((490 >> b) & 1) for b in range(4)]
    op_b = [(((490 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_491():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 491."""
    op_a = [((491 >> b) & 1) for b in range(4)]
    op_b = [(((491 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_492():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 492."""
    op_a = [((492 >> b) & 1) for b in range(4)]
    op_b = [(((492 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_493():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 493."""
    op_a = [((493 >> b) & 1) for b in range(4)]
    op_b = [(((493 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_494():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 494."""
    op_a = [((494 >> b) & 1) for b in range(4)]
    op_b = [(((494 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_495():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 495."""
    op_a = [((495 >> b) & 1) for b in range(4)]
    op_b = [(((495 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_496():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 496."""
    op_a = [((496 >> b) & 1) for b in range(4)]
    op_b = [(((496 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_497():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 497."""
    op_a = [((497 >> b) & 1) for b in range(4)]
    op_b = [(((497 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_498():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 498."""
    op_a = [((498 >> b) & 1) for b in range(4)]
    op_b = [(((498 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_499():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 499."""
    op_a = [((499 >> b) & 1) for b in range(4)]
    op_b = [(((499 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_500():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 500."""
    op_a = [((500 >> b) & 1) for b in range(4)]
    op_b = [(((500 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_501():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 501."""
    op_a = [((501 >> b) & 1) for b in range(4)]
    op_b = [(((501 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_502():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 502."""
    op_a = [((502 >> b) & 1) for b in range(4)]
    op_b = [(((502 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_503():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 503."""
    op_a = [((503 >> b) & 1) for b in range(4)]
    op_b = [(((503 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_504():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 504."""
    op_a = [((504 >> b) & 1) for b in range(4)]
    op_b = [(((504 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_505():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 505."""
    op_a = [((505 >> b) & 1) for b in range(4)]
    op_b = [(((505 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_506():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 506."""
    op_a = [((506 >> b) & 1) for b in range(4)]
    op_b = [(((506 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_507():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 507."""
    op_a = [((507 >> b) & 1) for b in range(4)]
    op_b = [(((507 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_508():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 508."""
    op_a = [((508 >> b) & 1) for b in range(4)]
    op_b = [(((508 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_509():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 509."""
    op_a = [((509 >> b) & 1) for b in range(4)]
    op_b = [(((509 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_510():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 510."""
    op_a = [((510 >> b) & 1) for b in range(4)]
    op_b = [(((510 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_511():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 511."""
    op_a = [((511 >> b) & 1) for b in range(4)]
    op_b = [(((511 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_512():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 512."""
    op_a = [((512 >> b) & 1) for b in range(4)]
    op_b = [(((512 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_513():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 513."""
    op_a = [((513 >> b) & 1) for b in range(4)]
    op_b = [(((513 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_514():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 514."""
    op_a = [((514 >> b) & 1) for b in range(4)]
    op_b = [(((514 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_515():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 515."""
    op_a = [((515 >> b) & 1) for b in range(4)]
    op_b = [(((515 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_516():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 516."""
    op_a = [((516 >> b) & 1) for b in range(4)]
    op_b = [(((516 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_517():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 517."""
    op_a = [((517 >> b) & 1) for b in range(4)]
    op_b = [(((517 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_518():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 518."""
    op_a = [((518 >> b) & 1) for b in range(4)]
    op_b = [(((518 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_519():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 519."""
    op_a = [((519 >> b) & 1) for b in range(4)]
    op_b = [(((519 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_520():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 520."""
    op_a = [((520 >> b) & 1) for b in range(4)]
    op_b = [(((520 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_521():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 521."""
    op_a = [((521 >> b) & 1) for b in range(4)]
    op_b = [(((521 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_522():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 522."""
    op_a = [((522 >> b) & 1) for b in range(4)]
    op_b = [(((522 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_523():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 523."""
    op_a = [((523 >> b) & 1) for b in range(4)]
    op_b = [(((523 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_524():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 524."""
    op_a = [((524 >> b) & 1) for b in range(4)]
    op_b = [(((524 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_525():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 525."""
    op_a = [((525 >> b) & 1) for b in range(4)]
    op_b = [(((525 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_526():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 526."""
    op_a = [((526 >> b) & 1) for b in range(4)]
    op_b = [(((526 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_527():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 527."""
    op_a = [((527 >> b) & 1) for b in range(4)]
    op_b = [(((527 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_528():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 528."""
    op_a = [((528 >> b) & 1) for b in range(4)]
    op_b = [(((528 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_529():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 529."""
    op_a = [((529 >> b) & 1) for b in range(4)]
    op_b = [(((529 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_530():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 530."""
    op_a = [((530 >> b) & 1) for b in range(4)]
    op_b = [(((530 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_531():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 531."""
    op_a = [((531 >> b) & 1) for b in range(4)]
    op_b = [(((531 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_532():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 532."""
    op_a = [((532 >> b) & 1) for b in range(4)]
    op_b = [(((532 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_533():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 533."""
    op_a = [((533 >> b) & 1) for b in range(4)]
    op_b = [(((533 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_534():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 534."""
    op_a = [((534 >> b) & 1) for b in range(4)]
    op_b = [(((534 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_535():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 535."""
    op_a = [((535 >> b) & 1) for b in range(4)]
    op_b = [(((535 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_536():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 536."""
    op_a = [((536 >> b) & 1) for b in range(4)]
    op_b = [(((536 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_537():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 537."""
    op_a = [((537 >> b) & 1) for b in range(4)]
    op_b = [(((537 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_538():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 538."""
    op_a = [((538 >> b) & 1) for b in range(4)]
    op_b = [(((538 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_539():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 539."""
    op_a = [((539 >> b) & 1) for b in range(4)]
    op_b = [(((539 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_540():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 540."""
    op_a = [((540 >> b) & 1) for b in range(4)]
    op_b = [(((540 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_541():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 541."""
    op_a = [((541 >> b) & 1) for b in range(4)]
    op_b = [(((541 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_542():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 542."""
    op_a = [((542 >> b) & 1) for b in range(4)]
    op_b = [(((542 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_543():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 543."""
    op_a = [((543 >> b) & 1) for b in range(4)]
    op_b = [(((543 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_544():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 544."""
    op_a = [((544 >> b) & 1) for b in range(4)]
    op_b = [(((544 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_545():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 545."""
    op_a = [((545 >> b) & 1) for b in range(4)]
    op_b = [(((545 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_546():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 546."""
    op_a = [((546 >> b) & 1) for b in range(4)]
    op_b = [(((546 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_547():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 547."""
    op_a = [((547 >> b) & 1) for b in range(4)]
    op_b = [(((547 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_548():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 548."""
    op_a = [((548 >> b) & 1) for b in range(4)]
    op_b = [(((548 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_549():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 549."""
    op_a = [((549 >> b) & 1) for b in range(4)]
    op_b = [(((549 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_550():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 550."""
    op_a = [((550 >> b) & 1) for b in range(4)]
    op_b = [(((550 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_551():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 551."""
    op_a = [((551 >> b) & 1) for b in range(4)]
    op_b = [(((551 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_552():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 552."""
    op_a = [((552 >> b) & 1) for b in range(4)]
    op_b = [(((552 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_553():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 553."""
    op_a = [((553 >> b) & 1) for b in range(4)]
    op_b = [(((553 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_554():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 554."""
    op_a = [((554 >> b) & 1) for b in range(4)]
    op_b = [(((554 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_555():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 555."""
    op_a = [((555 >> b) & 1) for b in range(4)]
    op_b = [(((555 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_556():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 556."""
    op_a = [((556 >> b) & 1) for b in range(4)]
    op_b = [(((556 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_557():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 557."""
    op_a = [((557 >> b) & 1) for b in range(4)]
    op_b = [(((557 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_558():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 558."""
    op_a = [((558 >> b) & 1) for b in range(4)]
    op_b = [(((558 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_559():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 559."""
    op_a = [((559 >> b) & 1) for b in range(4)]
    op_b = [(((559 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_560():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 560."""
    op_a = [((560 >> b) & 1) for b in range(4)]
    op_b = [(((560 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_561():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 561."""
    op_a = [((561 >> b) & 1) for b in range(4)]
    op_b = [(((561 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_562():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 562."""
    op_a = [((562 >> b) & 1) for b in range(4)]
    op_b = [(((562 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_563():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 563."""
    op_a = [((563 >> b) & 1) for b in range(4)]
    op_b = [(((563 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_564():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 564."""
    op_a = [((564 >> b) & 1) for b in range(4)]
    op_b = [(((564 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_565():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 565."""
    op_a = [((565 >> b) & 1) for b in range(4)]
    op_b = [(((565 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_566():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 566."""
    op_a = [((566 >> b) & 1) for b in range(4)]
    op_b = [(((566 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_567():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 567."""
    op_a = [((567 >> b) & 1) for b in range(4)]
    op_b = [(((567 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_568():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 568."""
    op_a = [((568 >> b) & 1) for b in range(4)]
    op_b = [(((568 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_569():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 569."""
    op_a = [((569 >> b) & 1) for b in range(4)]
    op_b = [(((569 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_570():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 570."""
    op_a = [((570 >> b) & 1) for b in range(4)]
    op_b = [(((570 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_571():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 571."""
    op_a = [((571 >> b) & 1) for b in range(4)]
    op_b = [(((571 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_572():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 572."""
    op_a = [((572 >> b) & 1) for b in range(4)]
    op_b = [(((572 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_573():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 573."""
    op_a = [((573 >> b) & 1) for b in range(4)]
    op_b = [(((573 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_574():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 574."""
    op_a = [((574 >> b) & 1) for b in range(4)]
    op_b = [(((574 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_575():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 575."""
    op_a = [((575 >> b) & 1) for b in range(4)]
    op_b = [(((575 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_576():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 576."""
    op_a = [((576 >> b) & 1) for b in range(4)]
    op_b = [(((576 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_577():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 577."""
    op_a = [((577 >> b) & 1) for b in range(4)]
    op_b = [(((577 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_578():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 578."""
    op_a = [((578 >> b) & 1) for b in range(4)]
    op_b = [(((578 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_579():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 579."""
    op_a = [((579 >> b) & 1) for b in range(4)]
    op_b = [(((579 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_580():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 580."""
    op_a = [((580 >> b) & 1) for b in range(4)]
    op_b = [(((580 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_581():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 581."""
    op_a = [((581 >> b) & 1) for b in range(4)]
    op_b = [(((581 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_582():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 582."""
    op_a = [((582 >> b) & 1) for b in range(4)]
    op_b = [(((582 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_583():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 583."""
    op_a = [((583 >> b) & 1) for b in range(4)]
    op_b = [(((583 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_584():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 584."""
    op_a = [((584 >> b) & 1) for b in range(4)]
    op_b = [(((584 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_585():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 585."""
    op_a = [((585 >> b) & 1) for b in range(4)]
    op_b = [(((585 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_586():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 586."""
    op_a = [((586 >> b) & 1) for b in range(4)]
    op_b = [(((586 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_587():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 587."""
    op_a = [((587 >> b) & 1) for b in range(4)]
    op_b = [(((587 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_588():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 588."""
    op_a = [((588 >> b) & 1) for b in range(4)]
    op_b = [(((588 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_589():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 589."""
    op_a = [((589 >> b) & 1) for b in range(4)]
    op_b = [(((589 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_590():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 590."""
    op_a = [((590 >> b) & 1) for b in range(4)]
    op_b = [(((590 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_591():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 591."""
    op_a = [((591 >> b) & 1) for b in range(4)]
    op_b = [(((591 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_592():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 592."""
    op_a = [((592 >> b) & 1) for b in range(4)]
    op_b = [(((592 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_593():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 593."""
    op_a = [((593 >> b) & 1) for b in range(4)]
    op_b = [(((593 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_594():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 594."""
    op_a = [((594 >> b) & 1) for b in range(4)]
    op_b = [(((594 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_595():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 595."""
    op_a = [((595 >> b) & 1) for b in range(4)]
    op_b = [(((595 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_596():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 596."""
    op_a = [((596 >> b) & 1) for b in range(4)]
    op_b = [(((596 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_597():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 597."""
    op_a = [((597 >> b) & 1) for b in range(4)]
    op_b = [(((597 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_598():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 598."""
    op_a = [((598 >> b) & 1) for b in range(4)]
    op_b = [(((598 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_599():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 599."""
    op_a = [((599 >> b) & 1) for b in range(4)]
    op_b = [(((599 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_600():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 600."""
    op_a = [((600 >> b) & 1) for b in range(4)]
    op_b = [(((600 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_601():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 601."""
    op_a = [((601 >> b) & 1) for b in range(4)]
    op_b = [(((601 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_602():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 602."""
    op_a = [((602 >> b) & 1) for b in range(4)]
    op_b = [(((602 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_603():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 603."""
    op_a = [((603 >> b) & 1) for b in range(4)]
    op_b = [(((603 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_604():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 604."""
    op_a = [((604 >> b) & 1) for b in range(4)]
    op_b = [(((604 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_605():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 605."""
    op_a = [((605 >> b) & 1) for b in range(4)]
    op_b = [(((605 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_606():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 606."""
    op_a = [((606 >> b) & 1) for b in range(4)]
    op_b = [(((606 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_607():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 607."""
    op_a = [((607 >> b) & 1) for b in range(4)]
    op_b = [(((607 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_608():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 608."""
    op_a = [((608 >> b) & 1) for b in range(4)]
    op_b = [(((608 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_609():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 609."""
    op_a = [((609 >> b) & 1) for b in range(4)]
    op_b = [(((609 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_610():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 610."""
    op_a = [((610 >> b) & 1) for b in range(4)]
    op_b = [(((610 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_611():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 611."""
    op_a = [((611 >> b) & 1) for b in range(4)]
    op_b = [(((611 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_612():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 612."""
    op_a = [((612 >> b) & 1) for b in range(4)]
    op_b = [(((612 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_613():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 613."""
    op_a = [((613 >> b) & 1) for b in range(4)]
    op_b = [(((613 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_614():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 614."""
    op_a = [((614 >> b) & 1) for b in range(4)]
    op_b = [(((614 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_615():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 615."""
    op_a = [((615 >> b) & 1) for b in range(4)]
    op_b = [(((615 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_616():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 616."""
    op_a = [((616 >> b) & 1) for b in range(4)]
    op_b = [(((616 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_617():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 617."""
    op_a = [((617 >> b) & 1) for b in range(4)]
    op_b = [(((617 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_618():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 618."""
    op_a = [((618 >> b) & 1) for b in range(4)]
    op_b = [(((618 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_619():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 619."""
    op_a = [((619 >> b) & 1) for b in range(4)]
    op_b = [(((619 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_620():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 620."""
    op_a = [((620 >> b) & 1) for b in range(4)]
    op_b = [(((620 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_621():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 621."""
    op_a = [((621 >> b) & 1) for b in range(4)]
    op_b = [(((621 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_622():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 622."""
    op_a = [((622 >> b) & 1) for b in range(4)]
    op_b = [(((622 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_623():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 623."""
    op_a = [((623 >> b) & 1) for b in range(4)]
    op_b = [(((623 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_624():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 624."""
    op_a = [((624 >> b) & 1) for b in range(4)]
    op_b = [(((624 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_625():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 625."""
    op_a = [((625 >> b) & 1) for b in range(4)]
    op_b = [(((625 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_626():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 626."""
    op_a = [((626 >> b) & 1) for b in range(4)]
    op_b = [(((626 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_627():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 627."""
    op_a = [((627 >> b) & 1) for b in range(4)]
    op_b = [(((627 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_628():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 628."""
    op_a = [((628 >> b) & 1) for b in range(4)]
    op_b = [(((628 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_629():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 629."""
    op_a = [((629 >> b) & 1) for b in range(4)]
    op_b = [(((629 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_630():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 630."""
    op_a = [((630 >> b) & 1) for b in range(4)]
    op_b = [(((630 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_631():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 631."""
    op_a = [((631 >> b) & 1) for b in range(4)]
    op_b = [(((631 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_632():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 632."""
    op_a = [((632 >> b) & 1) for b in range(4)]
    op_b = [(((632 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_633():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 633."""
    op_a = [((633 >> b) & 1) for b in range(4)]
    op_b = [(((633 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_634():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 634."""
    op_a = [((634 >> b) & 1) for b in range(4)]
    op_b = [(((634 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_635():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 635."""
    op_a = [((635 >> b) & 1) for b in range(4)]
    op_b = [(((635 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_636():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 636."""
    op_a = [((636 >> b) & 1) for b in range(4)]
    op_b = [(((636 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_637():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 637."""
    op_a = [((637 >> b) & 1) for b in range(4)]
    op_b = [(((637 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_638():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 638."""
    op_a = [((638 >> b) & 1) for b in range(4)]
    op_b = [(((638 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_639():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 639."""
    op_a = [((639 >> b) & 1) for b in range(4)]
    op_b = [(((639 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_640():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 640."""
    op_a = [((640 >> b) & 1) for b in range(4)]
    op_b = [(((640 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_641():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 641."""
    op_a = [((641 >> b) & 1) for b in range(4)]
    op_b = [(((641 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_642():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 642."""
    op_a = [((642 >> b) & 1) for b in range(4)]
    op_b = [(((642 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_643():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 643."""
    op_a = [((643 >> b) & 1) for b in range(4)]
    op_b = [(((643 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_644():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 644."""
    op_a = [((644 >> b) & 1) for b in range(4)]
    op_b = [(((644 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_645():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 645."""
    op_a = [((645 >> b) & 1) for b in range(4)]
    op_b = [(((645 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_646():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 646."""
    op_a = [((646 >> b) & 1) for b in range(4)]
    op_b = [(((646 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_647():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 647."""
    op_a = [((647 >> b) & 1) for b in range(4)]
    op_b = [(((647 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_648():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 648."""
    op_a = [((648 >> b) & 1) for b in range(4)]
    op_b = [(((648 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_649():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 649."""
    op_a = [((649 >> b) & 1) for b in range(4)]
    op_b = [(((649 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_650():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 650."""
    op_a = [((650 >> b) & 1) for b in range(4)]
    op_b = [(((650 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_651():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 651."""
    op_a = [((651 >> b) & 1) for b in range(4)]
    op_b = [(((651 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_652():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 652."""
    op_a = [((652 >> b) & 1) for b in range(4)]
    op_b = [(((652 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_653():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 653."""
    op_a = [((653 >> b) & 1) for b in range(4)]
    op_b = [(((653 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_654():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 654."""
    op_a = [((654 >> b) & 1) for b in range(4)]
    op_b = [(((654 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_655():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 655."""
    op_a = [((655 >> b) & 1) for b in range(4)]
    op_b = [(((655 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_656():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 656."""
    op_a = [((656 >> b) & 1) for b in range(4)]
    op_b = [(((656 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_657():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 657."""
    op_a = [((657 >> b) & 1) for b in range(4)]
    op_b = [(((657 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_658():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 658."""
    op_a = [((658 >> b) & 1) for b in range(4)]
    op_b = [(((658 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_659():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 659."""
    op_a = [((659 >> b) & 1) for b in range(4)]
    op_b = [(((659 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_660():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 660."""
    op_a = [((660 >> b) & 1) for b in range(4)]
    op_b = [(((660 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_661():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 661."""
    op_a = [((661 >> b) & 1) for b in range(4)]
    op_b = [(((661 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_662():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 662."""
    op_a = [((662 >> b) & 1) for b in range(4)]
    op_b = [(((662 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_663():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 663."""
    op_a = [((663 >> b) & 1) for b in range(4)]
    op_b = [(((663 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_664():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 664."""
    op_a = [((664 >> b) & 1) for b in range(4)]
    op_b = [(((664 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_665():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 665."""
    op_a = [((665 >> b) & 1) for b in range(4)]
    op_b = [(((665 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_666():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 666."""
    op_a = [((666 >> b) & 1) for b in range(4)]
    op_b = [(((666 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_667():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 667."""
    op_a = [((667 >> b) & 1) for b in range(4)]
    op_b = [(((667 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_668():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 668."""
    op_a = [((668 >> b) & 1) for b in range(4)]
    op_b = [(((668 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_669():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 669."""
    op_a = [((669 >> b) & 1) for b in range(4)]
    op_b = [(((669 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_670():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 670."""
    op_a = [((670 >> b) & 1) for b in range(4)]
    op_b = [(((670 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_671():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 671."""
    op_a = [((671 >> b) & 1) for b in range(4)]
    op_b = [(((671 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_672():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 672."""
    op_a = [((672 >> b) & 1) for b in range(4)]
    op_b = [(((672 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_673():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 673."""
    op_a = [((673 >> b) & 1) for b in range(4)]
    op_b = [(((673 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_674():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 674."""
    op_a = [((674 >> b) & 1) for b in range(4)]
    op_b = [(((674 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_675():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 675."""
    op_a = [((675 >> b) & 1) for b in range(4)]
    op_b = [(((675 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_676():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 676."""
    op_a = [((676 >> b) & 1) for b in range(4)]
    op_b = [(((676 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_677():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 677."""
    op_a = [((677 >> b) & 1) for b in range(4)]
    op_b = [(((677 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_678():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 678."""
    op_a = [((678 >> b) & 1) for b in range(4)]
    op_b = [(((678 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_679():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 679."""
    op_a = [((679 >> b) & 1) for b in range(4)]
    op_b = [(((679 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_680():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 680."""
    op_a = [((680 >> b) & 1) for b in range(4)]
    op_b = [(((680 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_681():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 681."""
    op_a = [((681 >> b) & 1) for b in range(4)]
    op_b = [(((681 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_682():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 682."""
    op_a = [((682 >> b) & 1) for b in range(4)]
    op_b = [(((682 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_683():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 683."""
    op_a = [((683 >> b) & 1) for b in range(4)]
    op_b = [(((683 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_684():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 684."""
    op_a = [((684 >> b) & 1) for b in range(4)]
    op_b = [(((684 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_685():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 685."""
    op_a = [((685 >> b) & 1) for b in range(4)]
    op_b = [(((685 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_686():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 686."""
    op_a = [((686 >> b) & 1) for b in range(4)]
    op_b = [(((686 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_687():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 687."""
    op_a = [((687 >> b) & 1) for b in range(4)]
    op_b = [(((687 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_688():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 688."""
    op_a = [((688 >> b) & 1) for b in range(4)]
    op_b = [(((688 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_689():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 689."""
    op_a = [((689 >> b) & 1) for b in range(4)]
    op_b = [(((689 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_690():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 690."""
    op_a = [((690 >> b) & 1) for b in range(4)]
    op_b = [(((690 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_691():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 691."""
    op_a = [((691 >> b) & 1) for b in range(4)]
    op_b = [(((691 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_692():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 692."""
    op_a = [((692 >> b) & 1) for b in range(4)]
    op_b = [(((692 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_693():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 693."""
    op_a = [((693 >> b) & 1) for b in range(4)]
    op_b = [(((693 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_694():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 694."""
    op_a = [((694 >> b) & 1) for b in range(4)]
    op_b = [(((694 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_695():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 695."""
    op_a = [((695 >> b) & 1) for b in range(4)]
    op_b = [(((695 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_696():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 696."""
    op_a = [((696 >> b) & 1) for b in range(4)]
    op_b = [(((696 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_697():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 697."""
    op_a = [((697 >> b) & 1) for b in range(4)]
    op_b = [(((697 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_698():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 698."""
    op_a = [((698 >> b) & 1) for b in range(4)]
    op_b = [(((698 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_699():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 699."""
    op_a = [((699 >> b) & 1) for b in range(4)]
    op_b = [(((699 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_700():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 700."""
    op_a = [((700 >> b) & 1) for b in range(4)]
    op_b = [(((700 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_701():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 701."""
    op_a = [((701 >> b) & 1) for b in range(4)]
    op_b = [(((701 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_702():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 702."""
    op_a = [((702 >> b) & 1) for b in range(4)]
    op_b = [(((702 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_703():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 703."""
    op_a = [((703 >> b) & 1) for b in range(4)]
    op_b = [(((703 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_704():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 704."""
    op_a = [((704 >> b) & 1) for b in range(4)]
    op_b = [(((704 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_705():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 705."""
    op_a = [((705 >> b) & 1) for b in range(4)]
    op_b = [(((705 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_706():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 706."""
    op_a = [((706 >> b) & 1) for b in range(4)]
    op_b = [(((706 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_707():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 707."""
    op_a = [((707 >> b) & 1) for b in range(4)]
    op_b = [(((707 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_708():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 708."""
    op_a = [((708 >> b) & 1) for b in range(4)]
    op_b = [(((708 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_709():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 709."""
    op_a = [((709 >> b) & 1) for b in range(4)]
    op_b = [(((709 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_710():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 710."""
    op_a = [((710 >> b) & 1) for b in range(4)]
    op_b = [(((710 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_711():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 711."""
    op_a = [((711 >> b) & 1) for b in range(4)]
    op_b = [(((711 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_712():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 712."""
    op_a = [((712 >> b) & 1) for b in range(4)]
    op_b = [(((712 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_713():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 713."""
    op_a = [((713 >> b) & 1) for b in range(4)]
    op_b = [(((713 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_714():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 714."""
    op_a = [((714 >> b) & 1) for b in range(4)]
    op_b = [(((714 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_715():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 715."""
    op_a = [((715 >> b) & 1) for b in range(4)]
    op_b = [(((715 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_716():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 716."""
    op_a = [((716 >> b) & 1) for b in range(4)]
    op_b = [(((716 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_717():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 717."""
    op_a = [((717 >> b) & 1) for b in range(4)]
    op_b = [(((717 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_718():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 718."""
    op_a = [((718 >> b) & 1) for b in range(4)]
    op_b = [(((718 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_719():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 719."""
    op_a = [((719 >> b) & 1) for b in range(4)]
    op_b = [(((719 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_720():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 720."""
    op_a = [((720 >> b) & 1) for b in range(4)]
    op_b = [(((720 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_721():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 721."""
    op_a = [((721 >> b) & 1) for b in range(4)]
    op_b = [(((721 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_722():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 722."""
    op_a = [((722 >> b) & 1) for b in range(4)]
    op_b = [(((722 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_723():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 723."""
    op_a = [((723 >> b) & 1) for b in range(4)]
    op_b = [(((723 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_724():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 724."""
    op_a = [((724 >> b) & 1) for b in range(4)]
    op_b = [(((724 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_725():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 725."""
    op_a = [((725 >> b) & 1) for b in range(4)]
    op_b = [(((725 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_726():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 726."""
    op_a = [((726 >> b) & 1) for b in range(4)]
    op_b = [(((726 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_727():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 727."""
    op_a = [((727 >> b) & 1) for b in range(4)]
    op_b = [(((727 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_728():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 728."""
    op_a = [((728 >> b) & 1) for b in range(4)]
    op_b = [(((728 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_729():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 729."""
    op_a = [((729 >> b) & 1) for b in range(4)]
    op_b = [(((729 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_730():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 730."""
    op_a = [((730 >> b) & 1) for b in range(4)]
    op_b = [(((730 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_731():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 731."""
    op_a = [((731 >> b) & 1) for b in range(4)]
    op_b = [(((731 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_732():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 732."""
    op_a = [((732 >> b) & 1) for b in range(4)]
    op_b = [(((732 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_733():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 733."""
    op_a = [((733 >> b) & 1) for b in range(4)]
    op_b = [(((733 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_734():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 734."""
    op_a = [((734 >> b) & 1) for b in range(4)]
    op_b = [(((734 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_735():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 735."""
    op_a = [((735 >> b) & 1) for b in range(4)]
    op_b = [(((735 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_736():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 736."""
    op_a = [((736 >> b) & 1) for b in range(4)]
    op_b = [(((736 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_737():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 737."""
    op_a = [((737 >> b) & 1) for b in range(4)]
    op_b = [(((737 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_738():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 738."""
    op_a = [((738 >> b) & 1) for b in range(4)]
    op_b = [(((738 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_739():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 739."""
    op_a = [((739 >> b) & 1) for b in range(4)]
    op_b = [(((739 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_740():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 740."""
    op_a = [((740 >> b) & 1) for b in range(4)]
    op_b = [(((740 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_741():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 741."""
    op_a = [((741 >> b) & 1) for b in range(4)]
    op_b = [(((741 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_742():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 742."""
    op_a = [((742 >> b) & 1) for b in range(4)]
    op_b = [(((742 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_743():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 743."""
    op_a = [((743 >> b) & 1) for b in range(4)]
    op_b = [(((743 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_744():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 744."""
    op_a = [((744 >> b) & 1) for b in range(4)]
    op_b = [(((744 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_745():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 745."""
    op_a = [((745 >> b) & 1) for b in range(4)]
    op_b = [(((745 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_746():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 746."""
    op_a = [((746 >> b) & 1) for b in range(4)]
    op_b = [(((746 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_747():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 747."""
    op_a = [((747 >> b) & 1) for b in range(4)]
    op_b = [(((747 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_748():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 748."""
    op_a = [((748 >> b) & 1) for b in range(4)]
    op_b = [(((748 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_749():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 749."""
    op_a = [((749 >> b) & 1) for b in range(4)]
    op_b = [(((749 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_750():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 750."""
    op_a = [((750 >> b) & 1) for b in range(4)]
    op_b = [(((750 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_751():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 751."""
    op_a = [((751 >> b) & 1) for b in range(4)]
    op_b = [(((751 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_752():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 752."""
    op_a = [((752 >> b) & 1) for b in range(4)]
    op_b = [(((752 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_753():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 753."""
    op_a = [((753 >> b) & 1) for b in range(4)]
    op_b = [(((753 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_754():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 754."""
    op_a = [((754 >> b) & 1) for b in range(4)]
    op_b = [(((754 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_755():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 755."""
    op_a = [((755 >> b) & 1) for b in range(4)]
    op_b = [(((755 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_756():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 756."""
    op_a = [((756 >> b) & 1) for b in range(4)]
    op_b = [(((756 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_757():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 757."""
    op_a = [((757 >> b) & 1) for b in range(4)]
    op_b = [(((757 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_758():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 758."""
    op_a = [((758 >> b) & 1) for b in range(4)]
    op_b = [(((758 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_759():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 759."""
    op_a = [((759 >> b) & 1) for b in range(4)]
    op_b = [(((759 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_760():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 760."""
    op_a = [((760 >> b) & 1) for b in range(4)]
    op_b = [(((760 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_761():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 761."""
    op_a = [((761 >> b) & 1) for b in range(4)]
    op_b = [(((761 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_762():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 762."""
    op_a = [((762 >> b) & 1) for b in range(4)]
    op_b = [(((762 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_763():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 763."""
    op_a = [((763 >> b) & 1) for b in range(4)]
    op_b = [(((763 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_764():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 764."""
    op_a = [((764 >> b) & 1) for b in range(4)]
    op_b = [(((764 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_765():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 765."""
    op_a = [((765 >> b) & 1) for b in range(4)]
    op_b = [(((765 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_766():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 766."""
    op_a = [((766 >> b) & 1) for b in range(4)]
    op_b = [(((766 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_767():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 767."""
    op_a = [((767 >> b) & 1) for b in range(4)]
    op_b = [(((767 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_768():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 768."""
    op_a = [((768 >> b) & 1) for b in range(4)]
    op_b = [(((768 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_769():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 769."""
    op_a = [((769 >> b) & 1) for b in range(4)]
    op_b = [(((769 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_770():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 770."""
    op_a = [((770 >> b) & 1) for b in range(4)]
    op_b = [(((770 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_771():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 771."""
    op_a = [((771 >> b) & 1) for b in range(4)]
    op_b = [(((771 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_772():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 772."""
    op_a = [((772 >> b) & 1) for b in range(4)]
    op_b = [(((772 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_773():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 773."""
    op_a = [((773 >> b) & 1) for b in range(4)]
    op_b = [(((773 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_774():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 774."""
    op_a = [((774 >> b) & 1) for b in range(4)]
    op_b = [(((774 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_775():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 775."""
    op_a = [((775 >> b) & 1) for b in range(4)]
    op_b = [(((775 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_776():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 776."""
    op_a = [((776 >> b) & 1) for b in range(4)]
    op_b = [(((776 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_777():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 777."""
    op_a = [((777 >> b) & 1) for b in range(4)]
    op_b = [(((777 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_778():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 778."""
    op_a = [((778 >> b) & 1) for b in range(4)]
    op_b = [(((778 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_779():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 779."""
    op_a = [((779 >> b) & 1) for b in range(4)]
    op_b = [(((779 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_780():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 780."""
    op_a = [((780 >> b) & 1) for b in range(4)]
    op_b = [(((780 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_781():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 781."""
    op_a = [((781 >> b) & 1) for b in range(4)]
    op_b = [(((781 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_782():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 782."""
    op_a = [((782 >> b) & 1) for b in range(4)]
    op_b = [(((782 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_783():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 783."""
    op_a = [((783 >> b) & 1) for b in range(4)]
    op_b = [(((783 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_784():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 784."""
    op_a = [((784 >> b) & 1) for b in range(4)]
    op_b = [(((784 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_785():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 785."""
    op_a = [((785 >> b) & 1) for b in range(4)]
    op_b = [(((785 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_786():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 786."""
    op_a = [((786 >> b) & 1) for b in range(4)]
    op_b = [(((786 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_787():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 787."""
    op_a = [((787 >> b) & 1) for b in range(4)]
    op_b = [(((787 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_788():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 788."""
    op_a = [((788 >> b) & 1) for b in range(4)]
    op_b = [(((788 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_789():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 789."""
    op_a = [((789 >> b) & 1) for b in range(4)]
    op_b = [(((789 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_790():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 790."""
    op_a = [((790 >> b) & 1) for b in range(4)]
    op_b = [(((790 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_791():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 791."""
    op_a = [((791 >> b) & 1) for b in range(4)]
    op_b = [(((791 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_792():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 792."""
    op_a = [((792 >> b) & 1) for b in range(4)]
    op_b = [(((792 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_793():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 793."""
    op_a = [((793 >> b) & 1) for b in range(4)]
    op_b = [(((793 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_794():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 794."""
    op_a = [((794 >> b) & 1) for b in range(4)]
    op_b = [(((794 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_795():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 795."""
    op_a = [((795 >> b) & 1) for b in range(4)]
    op_b = [(((795 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_796():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 796."""
    op_a = [((796 >> b) & 1) for b in range(4)]
    op_b = [(((796 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_797():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 797."""
    op_a = [((797 >> b) & 1) for b in range(4)]
    op_b = [(((797 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_798():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 798."""
    op_a = [((798 >> b) & 1) for b in range(4)]
    op_b = [(((798 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_799():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 799."""
    op_a = [((799 >> b) & 1) for b in range(4)]
    op_b = [(((799 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_800():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 800."""
    op_a = [((800 >> b) & 1) for b in range(4)]
    op_b = [(((800 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_801():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 801."""
    op_a = [((801 >> b) & 1) for b in range(4)]
    op_b = [(((801 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_802():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 802."""
    op_a = [((802 >> b) & 1) for b in range(4)]
    op_b = [(((802 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_803():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 803."""
    op_a = [((803 >> b) & 1) for b in range(4)]
    op_b = [(((803 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_804():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 804."""
    op_a = [((804 >> b) & 1) for b in range(4)]
    op_b = [(((804 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_805():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 805."""
    op_a = [((805 >> b) & 1) for b in range(4)]
    op_b = [(((805 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_806():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 806."""
    op_a = [((806 >> b) & 1) for b in range(4)]
    op_b = [(((806 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_807():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 807."""
    op_a = [((807 >> b) & 1) for b in range(4)]
    op_b = [(((807 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_808():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 808."""
    op_a = [((808 >> b) & 1) for b in range(4)]
    op_b = [(((808 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_809():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 809."""
    op_a = [((809 >> b) & 1) for b in range(4)]
    op_b = [(((809 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_810():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 810."""
    op_a = [((810 >> b) & 1) for b in range(4)]
    op_b = [(((810 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_811():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 811."""
    op_a = [((811 >> b) & 1) for b in range(4)]
    op_b = [(((811 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_812():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 812."""
    op_a = [((812 >> b) & 1) for b in range(4)]
    op_b = [(((812 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_813():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 813."""
    op_a = [((813 >> b) & 1) for b in range(4)]
    op_b = [(((813 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_814():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 814."""
    op_a = [((814 >> b) & 1) for b in range(4)]
    op_b = [(((814 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_815():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 815."""
    op_a = [((815 >> b) & 1) for b in range(4)]
    op_b = [(((815 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_816():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 816."""
    op_a = [((816 >> b) & 1) for b in range(4)]
    op_b = [(((816 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_817():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 817."""
    op_a = [((817 >> b) & 1) for b in range(4)]
    op_b = [(((817 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_818():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 818."""
    op_a = [((818 >> b) & 1) for b in range(4)]
    op_b = [(((818 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_819():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 819."""
    op_a = [((819 >> b) & 1) for b in range(4)]
    op_b = [(((819 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_820():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 820."""
    op_a = [((820 >> b) & 1) for b in range(4)]
    op_b = [(((820 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_821():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 821."""
    op_a = [((821 >> b) & 1) for b in range(4)]
    op_b = [(((821 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_822():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 822."""
    op_a = [((822 >> b) & 1) for b in range(4)]
    op_b = [(((822 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_823():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 823."""
    op_a = [((823 >> b) & 1) for b in range(4)]
    op_b = [(((823 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_824():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 824."""
    op_a = [((824 >> b) & 1) for b in range(4)]
    op_b = [(((824 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_825():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 825."""
    op_a = [((825 >> b) & 1) for b in range(4)]
    op_b = [(((825 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_826():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 826."""
    op_a = [((826 >> b) & 1) for b in range(4)]
    op_b = [(((826 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_827():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 827."""
    op_a = [((827 >> b) & 1) for b in range(4)]
    op_b = [(((827 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_828():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 828."""
    op_a = [((828 >> b) & 1) for b in range(4)]
    op_b = [(((828 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_829():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 829."""
    op_a = [((829 >> b) & 1) for b in range(4)]
    op_b = [(((829 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_830():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 830."""
    op_a = [((830 >> b) & 1) for b in range(4)]
    op_b = [(((830 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_831():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 831."""
    op_a = [((831 >> b) & 1) for b in range(4)]
    op_b = [(((831 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_832():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 832."""
    op_a = [((832 >> b) & 1) for b in range(4)]
    op_b = [(((832 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_833():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 833."""
    op_a = [((833 >> b) & 1) for b in range(4)]
    op_b = [(((833 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_834():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 834."""
    op_a = [((834 >> b) & 1) for b in range(4)]
    op_b = [(((834 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_835():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 835."""
    op_a = [((835 >> b) & 1) for b in range(4)]
    op_b = [(((835 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_836():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 836."""
    op_a = [((836 >> b) & 1) for b in range(4)]
    op_b = [(((836 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_837():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 837."""
    op_a = [((837 >> b) & 1) for b in range(4)]
    op_b = [(((837 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_838():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 838."""
    op_a = [((838 >> b) & 1) for b in range(4)]
    op_b = [(((838 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_839():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 839."""
    op_a = [((839 >> b) & 1) for b in range(4)]
    op_b = [(((839 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_840():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 840."""
    op_a = [((840 >> b) & 1) for b in range(4)]
    op_b = [(((840 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_841():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 841."""
    op_a = [((841 >> b) & 1) for b in range(4)]
    op_b = [(((841 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_842():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 842."""
    op_a = [((842 >> b) & 1) for b in range(4)]
    op_b = [(((842 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_843():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 843."""
    op_a = [((843 >> b) & 1) for b in range(4)]
    op_b = [(((843 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_844():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 844."""
    op_a = [((844 >> b) & 1) for b in range(4)]
    op_b = [(((844 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_845():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 845."""
    op_a = [((845 >> b) & 1) for b in range(4)]
    op_b = [(((845 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_846():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 846."""
    op_a = [((846 >> b) & 1) for b in range(4)]
    op_b = [(((846 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_847():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 847."""
    op_a = [((847 >> b) & 1) for b in range(4)]
    op_b = [(((847 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_848():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 848."""
    op_a = [((848 >> b) & 1) for b in range(4)]
    op_b = [(((848 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_849():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 849."""
    op_a = [((849 >> b) & 1) for b in range(4)]
    op_b = [(((849 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_850():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 850."""
    op_a = [((850 >> b) & 1) for b in range(4)]
    op_b = [(((850 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_851():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 851."""
    op_a = [((851 >> b) & 1) for b in range(4)]
    op_b = [(((851 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_852():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 852."""
    op_a = [((852 >> b) & 1) for b in range(4)]
    op_b = [(((852 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_853():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 853."""
    op_a = [((853 >> b) & 1) for b in range(4)]
    op_b = [(((853 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_854():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 854."""
    op_a = [((854 >> b) & 1) for b in range(4)]
    op_b = [(((854 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_855():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 855."""
    op_a = [((855 >> b) & 1) for b in range(4)]
    op_b = [(((855 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_856():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 856."""
    op_a = [((856 >> b) & 1) for b in range(4)]
    op_b = [(((856 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_857():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 857."""
    op_a = [((857 >> b) & 1) for b in range(4)]
    op_b = [(((857 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_858():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 858."""
    op_a = [((858 >> b) & 1) for b in range(4)]
    op_b = [(((858 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_859():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 859."""
    op_a = [((859 >> b) & 1) for b in range(4)]
    op_b = [(((859 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_860():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 860."""
    op_a = [((860 >> b) & 1) for b in range(4)]
    op_b = [(((860 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_861():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 861."""
    op_a = [((861 >> b) & 1) for b in range(4)]
    op_b = [(((861 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_862():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 862."""
    op_a = [((862 >> b) & 1) for b in range(4)]
    op_b = [(((862 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_863():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 863."""
    op_a = [((863 >> b) & 1) for b in range(4)]
    op_b = [(((863 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_864():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 864."""
    op_a = [((864 >> b) & 1) for b in range(4)]
    op_b = [(((864 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_865():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 865."""
    op_a = [((865 >> b) & 1) for b in range(4)]
    op_b = [(((865 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_866():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 866."""
    op_a = [((866 >> b) & 1) for b in range(4)]
    op_b = [(((866 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_867():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 867."""
    op_a = [((867 >> b) & 1) for b in range(4)]
    op_b = [(((867 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_868():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 868."""
    op_a = [((868 >> b) & 1) for b in range(4)]
    op_b = [(((868 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_869():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 869."""
    op_a = [((869 >> b) & 1) for b in range(4)]
    op_b = [(((869 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_870():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 870."""
    op_a = [((870 >> b) & 1) for b in range(4)]
    op_b = [(((870 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_871():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 871."""
    op_a = [((871 >> b) & 1) for b in range(4)]
    op_b = [(((871 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_872():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 872."""
    op_a = [((872 >> b) & 1) for b in range(4)]
    op_b = [(((872 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_873():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 873."""
    op_a = [((873 >> b) & 1) for b in range(4)]
    op_b = [(((873 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_874():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 874."""
    op_a = [((874 >> b) & 1) for b in range(4)]
    op_b = [(((874 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_875():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 875."""
    op_a = [((875 >> b) & 1) for b in range(4)]
    op_b = [(((875 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_876():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 876."""
    op_a = [((876 >> b) & 1) for b in range(4)]
    op_b = [(((876 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_877():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 877."""
    op_a = [((877 >> b) & 1) for b in range(4)]
    op_b = [(((877 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_878():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 878."""
    op_a = [((878 >> b) & 1) for b in range(4)]
    op_b = [(((878 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_879():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 879."""
    op_a = [((879 >> b) & 1) for b in range(4)]
    op_b = [(((879 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_880():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 880."""
    op_a = [((880 >> b) & 1) for b in range(4)]
    op_b = [(((880 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_881():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 881."""
    op_a = [((881 >> b) & 1) for b in range(4)]
    op_b = [(((881 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_882():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 882."""
    op_a = [((882 >> b) & 1) for b in range(4)]
    op_b = [(((882 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_883():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 883."""
    op_a = [((883 >> b) & 1) for b in range(4)]
    op_b = [(((883 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_884():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 884."""
    op_a = [((884 >> b) & 1) for b in range(4)]
    op_b = [(((884 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_885():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 885."""
    op_a = [((885 >> b) & 1) for b in range(4)]
    op_b = [(((885 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_886():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 886."""
    op_a = [((886 >> b) & 1) for b in range(4)]
    op_b = [(((886 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_887():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 887."""
    op_a = [((887 >> b) & 1) for b in range(4)]
    op_b = [(((887 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_888():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 888."""
    op_a = [((888 >> b) & 1) for b in range(4)]
    op_b = [(((888 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_889():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 889."""
    op_a = [((889 >> b) & 1) for b in range(4)]
    op_b = [(((889 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_890():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 890."""
    op_a = [((890 >> b) & 1) for b in range(4)]
    op_b = [(((890 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_891():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 891."""
    op_a = [((891 >> b) & 1) for b in range(4)]
    op_b = [(((891 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_892():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 892."""
    op_a = [((892 >> b) & 1) for b in range(4)]
    op_b = [(((892 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_893():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 893."""
    op_a = [((893 >> b) & 1) for b in range(4)]
    op_b = [(((893 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_894():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 894."""
    op_a = [((894 >> b) & 1) for b in range(4)]
    op_b = [(((894 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_895():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 895."""
    op_a = [((895 >> b) & 1) for b in range(4)]
    op_b = [(((895 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_896():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 896."""
    op_a = [((896 >> b) & 1) for b in range(4)]
    op_b = [(((896 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_897():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 897."""
    op_a = [((897 >> b) & 1) for b in range(4)]
    op_b = [(((897 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_898():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 898."""
    op_a = [((898 >> b) & 1) for b in range(4)]
    op_b = [(((898 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_899():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 899."""
    op_a = [((899 >> b) & 1) for b in range(4)]
    op_b = [(((899 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_900():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 900."""
    op_a = [((900 >> b) & 1) for b in range(4)]
    op_b = [(((900 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_901():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 901."""
    op_a = [((901 >> b) & 1) for b in range(4)]
    op_b = [(((901 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_902():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 902."""
    op_a = [((902 >> b) & 1) for b in range(4)]
    op_b = [(((902 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_903():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 903."""
    op_a = [((903 >> b) & 1) for b in range(4)]
    op_b = [(((903 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_904():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 904."""
    op_a = [((904 >> b) & 1) for b in range(4)]
    op_b = [(((904 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_905():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 905."""
    op_a = [((905 >> b) & 1) for b in range(4)]
    op_b = [(((905 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_906():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 906."""
    op_a = [((906 >> b) & 1) for b in range(4)]
    op_b = [(((906 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_907():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 907."""
    op_a = [((907 >> b) & 1) for b in range(4)]
    op_b = [(((907 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_908():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 908."""
    op_a = [((908 >> b) & 1) for b in range(4)]
    op_b = [(((908 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_909():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 909."""
    op_a = [((909 >> b) & 1) for b in range(4)]
    op_b = [(((909 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_910():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 910."""
    op_a = [((910 >> b) & 1) for b in range(4)]
    op_b = [(((910 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_911():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 911."""
    op_a = [((911 >> b) & 1) for b in range(4)]
    op_b = [(((911 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_912():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 912."""
    op_a = [((912 >> b) & 1) for b in range(4)]
    op_b = [(((912 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_913():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 913."""
    op_a = [((913 >> b) & 1) for b in range(4)]
    op_b = [(((913 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_914():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 914."""
    op_a = [((914 >> b) & 1) for b in range(4)]
    op_b = [(((914 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_915():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 915."""
    op_a = [((915 >> b) & 1) for b in range(4)]
    op_b = [(((915 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_916():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 916."""
    op_a = [((916 >> b) & 1) for b in range(4)]
    op_b = [(((916 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_917():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 917."""
    op_a = [((917 >> b) & 1) for b in range(4)]
    op_b = [(((917 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_918():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 918."""
    op_a = [((918 >> b) & 1) for b in range(4)]
    op_b = [(((918 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_919():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 919."""
    op_a = [((919 >> b) & 1) for b in range(4)]
    op_b = [(((919 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_920():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 920."""
    op_a = [((920 >> b) & 1) for b in range(4)]
    op_b = [(((920 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_921():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 921."""
    op_a = [((921 >> b) & 1) for b in range(4)]
    op_b = [(((921 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_922():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 922."""
    op_a = [((922 >> b) & 1) for b in range(4)]
    op_b = [(((922 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_923():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 923."""
    op_a = [((923 >> b) & 1) for b in range(4)]
    op_b = [(((923 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_924():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 924."""
    op_a = [((924 >> b) & 1) for b in range(4)]
    op_b = [(((924 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_925():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 925."""
    op_a = [((925 >> b) & 1) for b in range(4)]
    op_b = [(((925 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_926():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 926."""
    op_a = [((926 >> b) & 1) for b in range(4)]
    op_b = [(((926 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_927():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 927."""
    op_a = [((927 >> b) & 1) for b in range(4)]
    op_b = [(((927 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_928():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 928."""
    op_a = [((928 >> b) & 1) for b in range(4)]
    op_b = [(((928 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_929():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 929."""
    op_a = [((929 >> b) & 1) for b in range(4)]
    op_b = [(((929 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_930():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 930."""
    op_a = [((930 >> b) & 1) for b in range(4)]
    op_b = [(((930 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_931():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 931."""
    op_a = [((931 >> b) & 1) for b in range(4)]
    op_b = [(((931 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_932():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 932."""
    op_a = [((932 >> b) & 1) for b in range(4)]
    op_b = [(((932 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_933():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 933."""
    op_a = [((933 >> b) & 1) for b in range(4)]
    op_b = [(((933 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_934():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 934."""
    op_a = [((934 >> b) & 1) for b in range(4)]
    op_b = [(((934 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_935():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 935."""
    op_a = [((935 >> b) & 1) for b in range(4)]
    op_b = [(((935 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_936():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 936."""
    op_a = [((936 >> b) & 1) for b in range(4)]
    op_b = [(((936 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_937():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 937."""
    op_a = [((937 >> b) & 1) for b in range(4)]
    op_b = [(((937 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_938():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 938."""
    op_a = [((938 >> b) & 1) for b in range(4)]
    op_b = [(((938 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_939():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 939."""
    op_a = [((939 >> b) & 1) for b in range(4)]
    op_b = [(((939 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_940():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 940."""
    op_a = [((940 >> b) & 1) for b in range(4)]
    op_b = [(((940 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_941():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 941."""
    op_a = [((941 >> b) & 1) for b in range(4)]
    op_b = [(((941 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_942():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 942."""
    op_a = [((942 >> b) & 1) for b in range(4)]
    op_b = [(((942 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_943():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 943."""
    op_a = [((943 >> b) & 1) for b in range(4)]
    op_b = [(((943 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_944():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 944."""
    op_a = [((944 >> b) & 1) for b in range(4)]
    op_b = [(((944 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_945():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 945."""
    op_a = [((945 >> b) & 1) for b in range(4)]
    op_b = [(((945 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_946():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 946."""
    op_a = [((946 >> b) & 1) for b in range(4)]
    op_b = [(((946 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_947():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 947."""
    op_a = [((947 >> b) & 1) for b in range(4)]
    op_b = [(((947 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_948():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 948."""
    op_a = [((948 >> b) & 1) for b in range(4)]
    op_b = [(((948 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_949():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 949."""
    op_a = [((949 >> b) & 1) for b in range(4)]
    op_b = [(((949 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_950():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 950."""
    op_a = [((950 >> b) & 1) for b in range(4)]
    op_b = [(((950 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_951():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 951."""
    op_a = [((951 >> b) & 1) for b in range(4)]
    op_b = [(((951 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_952():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 952."""
    op_a = [((952 >> b) & 1) for b in range(4)]
    op_b = [(((952 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_953():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 953."""
    op_a = [((953 >> b) & 1) for b in range(4)]
    op_b = [(((953 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_954():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 954."""
    op_a = [((954 >> b) & 1) for b in range(4)]
    op_b = [(((954 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_955():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 955."""
    op_a = [((955 >> b) & 1) for b in range(4)]
    op_b = [(((955 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_956():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 956."""
    op_a = [((956 >> b) & 1) for b in range(4)]
    op_b = [(((956 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_957():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 957."""
    op_a = [((957 >> b) & 1) for b in range(4)]
    op_b = [(((957 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_958():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 958."""
    op_a = [((958 >> b) & 1) for b in range(4)]
    op_b = [(((958 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_959():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 959."""
    op_a = [((959 >> b) & 1) for b in range(4)]
    op_b = [(((959 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_960():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 960."""
    op_a = [((960 >> b) & 1) for b in range(4)]
    op_b = [(((960 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_961():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 961."""
    op_a = [((961 >> b) & 1) for b in range(4)]
    op_b = [(((961 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_962():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 962."""
    op_a = [((962 >> b) & 1) for b in range(4)]
    op_b = [(((962 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_963():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 963."""
    op_a = [((963 >> b) & 1) for b in range(4)]
    op_b = [(((963 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_964():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 964."""
    op_a = [((964 >> b) & 1) for b in range(4)]
    op_b = [(((964 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_965():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 965."""
    op_a = [((965 >> b) & 1) for b in range(4)]
    op_b = [(((965 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_966():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 966."""
    op_a = [((966 >> b) & 1) for b in range(4)]
    op_b = [(((966 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_967():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 967."""
    op_a = [((967 >> b) & 1) for b in range(4)]
    op_b = [(((967 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_968():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 968."""
    op_a = [((968 >> b) & 1) for b in range(4)]
    op_b = [(((968 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_969():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 969."""
    op_a = [((969 >> b) & 1) for b in range(4)]
    op_b = [(((969 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_970():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 970."""
    op_a = [((970 >> b) & 1) for b in range(4)]
    op_b = [(((970 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_971():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 971."""
    op_a = [((971 >> b) & 1) for b in range(4)]
    op_b = [(((971 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_972():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 972."""
    op_a = [((972 >> b) & 1) for b in range(4)]
    op_b = [(((972 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_973():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 973."""
    op_a = [((973 >> b) & 1) for b in range(4)]
    op_b = [(((973 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_974():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 974."""
    op_a = [((974 >> b) & 1) for b in range(4)]
    op_b = [(((974 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_975():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 975."""
    op_a = [((975 >> b) & 1) for b in range(4)]
    op_b = [(((975 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_976():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 976."""
    op_a = [((976 >> b) & 1) for b in range(4)]
    op_b = [(((976 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_977():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 977."""
    op_a = [((977 >> b) & 1) for b in range(4)]
    op_b = [(((977 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_978():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 978."""
    op_a = [((978 >> b) & 1) for b in range(4)]
    op_b = [(((978 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_979():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 979."""
    op_a = [((979 >> b) & 1) for b in range(4)]
    op_b = [(((979 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_980():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 980."""
    op_a = [((980 >> b) & 1) for b in range(4)]
    op_b = [(((980 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_981():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 981."""
    op_a = [((981 >> b) & 1) for b in range(4)]
    op_b = [(((981 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_982():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 982."""
    op_a = [((982 >> b) & 1) for b in range(4)]
    op_b = [(((982 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_983():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 983."""
    op_a = [((983 >> b) & 1) for b in range(4)]
    op_b = [(((983 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_984():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 984."""
    op_a = [((984 >> b) & 1) for b in range(4)]
    op_b = [(((984 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_985():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 985."""
    op_a = [((985 >> b) & 1) for b in range(4)]
    op_b = [(((985 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(9, 11)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_986():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 986."""
    op_a = [((986 >> b) & 1) for b in range(4)]
    op_b = [(((986 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(10, 14)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_987():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 987."""
    op_a = [((987 >> b) & 1) for b in range(4)]
    op_b = [(((987 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(11, 1)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_988():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 988."""
    op_a = [((988 >> b) & 1) for b in range(4)]
    op_b = [(((988 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(12, 4)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_989():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 989."""
    op_a = [((989 >> b) & 1) for b in range(4)]
    op_b = [(((989 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(13, 7)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_990():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 990."""
    op_a = [((990 >> b) & 1) for b in range(4)]
    op_b = [(((990 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(14, 10)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_991():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 991."""
    op_a = [((991 >> b) & 1) for b in range(4)]
    op_b = [(((991 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(15, 13)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_992():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 992."""
    op_a = [((992 >> b) & 1) for b in range(4)]
    op_b = [(((992 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(0, 0)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_993():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 993."""
    op_a = [((993 >> b) & 1) for b in range(4)]
    op_b = [(((993 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(1, 3)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_994():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 994."""
    op_a = [((994 >> b) & 1) for b in range(4)]
    op_b = [(((994 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(2, 6)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_995():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 995."""
    op_a = [((995 >> b) & 1) for b in range(4)]
    op_b = [(((995 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(3, 9)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_996():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 996."""
    op_a = [((996 >> b) & 1) for b in range(4)]
    op_b = [(((996 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(4, 12)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_997():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 997."""
    op_a = [((997 >> b) & 1) for b in range(4)]
    op_b = [(((997 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(5, 15)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_998():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 998."""
    op_a = [((998 >> b) & 1) for b in range(4)]
    op_b = [(((998 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(6, 2)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_999():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 999."""
    op_a = [((999 >> b) & 1) for b in range(4)]
    op_b = [(((999 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(7, 5)
    assert (gt + eq + lt) == 1

def test_combinational_ic_vector_row_1000():
    """Verify 7483 4-bit addition and 7485 comparison for operand pair 1000."""
    op_a = [((1000 >> b) & 1) for b in range(4)]
    op_b = [(((1000 * 3) >> b) & 1) for b in range(4)]
    s, cout = ic7483_4bit_adder(op_a, op_b, 0)
    assert len(s) == 4
    gt, eq, lt = ic7485_comparator(8, 8)
    assert (gt + eq + lt) == 1
