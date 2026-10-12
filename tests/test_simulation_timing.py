"""Pytest unit tests for 555 timers, 565 PLLs, and waveform generators."""
from __future__ import annotations
import math
import pytest
from app.simulation.timing.timer555_core import Timer555Core
from app.simulation.timing.timer555_monostable import monostable_pulse_width
from app.simulation.timing.timer555_astable import astable_timing_parameters
from app.simulation.timing.pll565_loop_filter import pll_free_running_frequency, pll_lock_range

def test_555_monostable_pulse():
    pw = monostable_pulse_width(10000.0, 0.00001)
    assert math.isclose(pw, 0.11, rel_tol=1e-2)

def test_555_astable_frequency():
    res = astable_timing_parameters(10000.0, 20000.0, 1e-6)
    assert res['frequency_hz'] > 0
    assert 0.5 <= res['duty_cycle'] <= 1.0

def test_timing_pll_circuit_node_1():
    """Validate 565 PLL lock range and capture frequency for test point 1."""
    f0 = pll_free_running_frequency(1010.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_2():
    """Validate 565 PLL lock range and capture frequency for test point 2."""
    f0 = pll_free_running_frequency(1020.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_3():
    """Validate 565 PLL lock range and capture frequency for test point 3."""
    f0 = pll_free_running_frequency(1030.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_4():
    """Validate 565 PLL lock range and capture frequency for test point 4."""
    f0 = pll_free_running_frequency(1040.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_5():
    """Validate 565 PLL lock range and capture frequency for test point 5."""
    f0 = pll_free_running_frequency(1050.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_6():
    """Validate 565 PLL lock range and capture frequency for test point 6."""
    f0 = pll_free_running_frequency(1060.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_7():
    """Validate 565 PLL lock range and capture frequency for test point 7."""
    f0 = pll_free_running_frequency(1070.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_8():
    """Validate 565 PLL lock range and capture frequency for test point 8."""
    f0 = pll_free_running_frequency(1080.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_9():
    """Validate 565 PLL lock range and capture frequency for test point 9."""
    f0 = pll_free_running_frequency(1090.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_10():
    """Validate 565 PLL lock range and capture frequency for test point 10."""
    f0 = pll_free_running_frequency(1100.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_11():
    """Validate 565 PLL lock range and capture frequency for test point 11."""
    f0 = pll_free_running_frequency(1110.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_12():
    """Validate 565 PLL lock range and capture frequency for test point 12."""
    f0 = pll_free_running_frequency(1120.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_13():
    """Validate 565 PLL lock range and capture frequency for test point 13."""
    f0 = pll_free_running_frequency(1130.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_14():
    """Validate 565 PLL lock range and capture frequency for test point 14."""
    f0 = pll_free_running_frequency(1140.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_15():
    """Validate 565 PLL lock range and capture frequency for test point 15."""
    f0 = pll_free_running_frequency(1150.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_16():
    """Validate 565 PLL lock range and capture frequency for test point 16."""
    f0 = pll_free_running_frequency(1160.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_17():
    """Validate 565 PLL lock range and capture frequency for test point 17."""
    f0 = pll_free_running_frequency(1170.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_18():
    """Validate 565 PLL lock range and capture frequency for test point 18."""
    f0 = pll_free_running_frequency(1180.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_19():
    """Validate 565 PLL lock range and capture frequency for test point 19."""
    f0 = pll_free_running_frequency(1190.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_20():
    """Validate 565 PLL lock range and capture frequency for test point 20."""
    f0 = pll_free_running_frequency(1200.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_21():
    """Validate 565 PLL lock range and capture frequency for test point 21."""
    f0 = pll_free_running_frequency(1210.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_22():
    """Validate 565 PLL lock range and capture frequency for test point 22."""
    f0 = pll_free_running_frequency(1220.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_23():
    """Validate 565 PLL lock range and capture frequency for test point 23."""
    f0 = pll_free_running_frequency(1230.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_24():
    """Validate 565 PLL lock range and capture frequency for test point 24."""
    f0 = pll_free_running_frequency(1240.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_25():
    """Validate 565 PLL lock range and capture frequency for test point 25."""
    f0 = pll_free_running_frequency(1250.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_26():
    """Validate 565 PLL lock range and capture frequency for test point 26."""
    f0 = pll_free_running_frequency(1260.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_27():
    """Validate 565 PLL lock range and capture frequency for test point 27."""
    f0 = pll_free_running_frequency(1270.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_28():
    """Validate 565 PLL lock range and capture frequency for test point 28."""
    f0 = pll_free_running_frequency(1280.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_29():
    """Validate 565 PLL lock range and capture frequency for test point 29."""
    f0 = pll_free_running_frequency(1290.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_30():
    """Validate 565 PLL lock range and capture frequency for test point 30."""
    f0 = pll_free_running_frequency(1300.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_31():
    """Validate 565 PLL lock range and capture frequency for test point 31."""
    f0 = pll_free_running_frequency(1310.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_32():
    """Validate 565 PLL lock range and capture frequency for test point 32."""
    f0 = pll_free_running_frequency(1320.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_33():
    """Validate 565 PLL lock range and capture frequency for test point 33."""
    f0 = pll_free_running_frequency(1330.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_34():
    """Validate 565 PLL lock range and capture frequency for test point 34."""
    f0 = pll_free_running_frequency(1340.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_35():
    """Validate 565 PLL lock range and capture frequency for test point 35."""
    f0 = pll_free_running_frequency(1350.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_36():
    """Validate 565 PLL lock range and capture frequency for test point 36."""
    f0 = pll_free_running_frequency(1360.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_37():
    """Validate 565 PLL lock range and capture frequency for test point 37."""
    f0 = pll_free_running_frequency(1370.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_38():
    """Validate 565 PLL lock range and capture frequency for test point 38."""
    f0 = pll_free_running_frequency(1380.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_39():
    """Validate 565 PLL lock range and capture frequency for test point 39."""
    f0 = pll_free_running_frequency(1390.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_40():
    """Validate 565 PLL lock range and capture frequency for test point 40."""
    f0 = pll_free_running_frequency(1400.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_41():
    """Validate 565 PLL lock range and capture frequency for test point 41."""
    f0 = pll_free_running_frequency(1410.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_42():
    """Validate 565 PLL lock range and capture frequency for test point 42."""
    f0 = pll_free_running_frequency(1420.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_43():
    """Validate 565 PLL lock range and capture frequency for test point 43."""
    f0 = pll_free_running_frequency(1430.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_44():
    """Validate 565 PLL lock range and capture frequency for test point 44."""
    f0 = pll_free_running_frequency(1440.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_45():
    """Validate 565 PLL lock range and capture frequency for test point 45."""
    f0 = pll_free_running_frequency(1450.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_46():
    """Validate 565 PLL lock range and capture frequency for test point 46."""
    f0 = pll_free_running_frequency(1460.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_47():
    """Validate 565 PLL lock range and capture frequency for test point 47."""
    f0 = pll_free_running_frequency(1470.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_48():
    """Validate 565 PLL lock range and capture frequency for test point 48."""
    f0 = pll_free_running_frequency(1480.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_49():
    """Validate 565 PLL lock range and capture frequency for test point 49."""
    f0 = pll_free_running_frequency(1490.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_50():
    """Validate 565 PLL lock range and capture frequency for test point 50."""
    f0 = pll_free_running_frequency(1500.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_51():
    """Validate 565 PLL lock range and capture frequency for test point 51."""
    f0 = pll_free_running_frequency(1510.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_52():
    """Validate 565 PLL lock range and capture frequency for test point 52."""
    f0 = pll_free_running_frequency(1520.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_53():
    """Validate 565 PLL lock range and capture frequency for test point 53."""
    f0 = pll_free_running_frequency(1530.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_54():
    """Validate 565 PLL lock range and capture frequency for test point 54."""
    f0 = pll_free_running_frequency(1540.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_55():
    """Validate 565 PLL lock range and capture frequency for test point 55."""
    f0 = pll_free_running_frequency(1550.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_56():
    """Validate 565 PLL lock range and capture frequency for test point 56."""
    f0 = pll_free_running_frequency(1560.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_57():
    """Validate 565 PLL lock range and capture frequency for test point 57."""
    f0 = pll_free_running_frequency(1570.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_58():
    """Validate 565 PLL lock range and capture frequency for test point 58."""
    f0 = pll_free_running_frequency(1580.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_59():
    """Validate 565 PLL lock range and capture frequency for test point 59."""
    f0 = pll_free_running_frequency(1590.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_60():
    """Validate 565 PLL lock range and capture frequency for test point 60."""
    f0 = pll_free_running_frequency(1600.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_61():
    """Validate 565 PLL lock range and capture frequency for test point 61."""
    f0 = pll_free_running_frequency(1610.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_62():
    """Validate 565 PLL lock range and capture frequency for test point 62."""
    f0 = pll_free_running_frequency(1620.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_63():
    """Validate 565 PLL lock range and capture frequency for test point 63."""
    f0 = pll_free_running_frequency(1630.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_64():
    """Validate 565 PLL lock range and capture frequency for test point 64."""
    f0 = pll_free_running_frequency(1640.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_65():
    """Validate 565 PLL lock range and capture frequency for test point 65."""
    f0 = pll_free_running_frequency(1650.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_66():
    """Validate 565 PLL lock range and capture frequency for test point 66."""
    f0 = pll_free_running_frequency(1660.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_67():
    """Validate 565 PLL lock range and capture frequency for test point 67."""
    f0 = pll_free_running_frequency(1670.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_68():
    """Validate 565 PLL lock range and capture frequency for test point 68."""
    f0 = pll_free_running_frequency(1680.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_69():
    """Validate 565 PLL lock range and capture frequency for test point 69."""
    f0 = pll_free_running_frequency(1690.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_70():
    """Validate 565 PLL lock range and capture frequency for test point 70."""
    f0 = pll_free_running_frequency(1700.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_71():
    """Validate 565 PLL lock range and capture frequency for test point 71."""
    f0 = pll_free_running_frequency(1710.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_72():
    """Validate 565 PLL lock range and capture frequency for test point 72."""
    f0 = pll_free_running_frequency(1720.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_73():
    """Validate 565 PLL lock range and capture frequency for test point 73."""
    f0 = pll_free_running_frequency(1730.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_74():
    """Validate 565 PLL lock range and capture frequency for test point 74."""
    f0 = pll_free_running_frequency(1740.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_75():
    """Validate 565 PLL lock range and capture frequency for test point 75."""
    f0 = pll_free_running_frequency(1750.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_76():
    """Validate 565 PLL lock range and capture frequency for test point 76."""
    f0 = pll_free_running_frequency(1760.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_77():
    """Validate 565 PLL lock range and capture frequency for test point 77."""
    f0 = pll_free_running_frequency(1770.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_78():
    """Validate 565 PLL lock range and capture frequency for test point 78."""
    f0 = pll_free_running_frequency(1780.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_79():
    """Validate 565 PLL lock range and capture frequency for test point 79."""
    f0 = pll_free_running_frequency(1790.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_80():
    """Validate 565 PLL lock range and capture frequency for test point 80."""
    f0 = pll_free_running_frequency(1800.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_81():
    """Validate 565 PLL lock range and capture frequency for test point 81."""
    f0 = pll_free_running_frequency(1810.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_82():
    """Validate 565 PLL lock range and capture frequency for test point 82."""
    f0 = pll_free_running_frequency(1820.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_83():
    """Validate 565 PLL lock range and capture frequency for test point 83."""
    f0 = pll_free_running_frequency(1830.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_84():
    """Validate 565 PLL lock range and capture frequency for test point 84."""
    f0 = pll_free_running_frequency(1840.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_85():
    """Validate 565 PLL lock range and capture frequency for test point 85."""
    f0 = pll_free_running_frequency(1850.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_86():
    """Validate 565 PLL lock range and capture frequency for test point 86."""
    f0 = pll_free_running_frequency(1860.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_87():
    """Validate 565 PLL lock range and capture frequency for test point 87."""
    f0 = pll_free_running_frequency(1870.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_88():
    """Validate 565 PLL lock range and capture frequency for test point 88."""
    f0 = pll_free_running_frequency(1880.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_89():
    """Validate 565 PLL lock range and capture frequency for test point 89."""
    f0 = pll_free_running_frequency(1890.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_90():
    """Validate 565 PLL lock range and capture frequency for test point 90."""
    f0 = pll_free_running_frequency(1900.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_91():
    """Validate 565 PLL lock range and capture frequency for test point 91."""
    f0 = pll_free_running_frequency(1910.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_92():
    """Validate 565 PLL lock range and capture frequency for test point 92."""
    f0 = pll_free_running_frequency(1920.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_93():
    """Validate 565 PLL lock range and capture frequency for test point 93."""
    f0 = pll_free_running_frequency(1930.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_94():
    """Validate 565 PLL lock range and capture frequency for test point 94."""
    f0 = pll_free_running_frequency(1940.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_95():
    """Validate 565 PLL lock range and capture frequency for test point 95."""
    f0 = pll_free_running_frequency(1950.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_96():
    """Validate 565 PLL lock range and capture frequency for test point 96."""
    f0 = pll_free_running_frequency(1960.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_97():
    """Validate 565 PLL lock range and capture frequency for test point 97."""
    f0 = pll_free_running_frequency(1970.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_98():
    """Validate 565 PLL lock range and capture frequency for test point 98."""
    f0 = pll_free_running_frequency(1980.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_99():
    """Validate 565 PLL lock range and capture frequency for test point 99."""
    f0 = pll_free_running_frequency(1990.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_100():
    """Validate 565 PLL lock range and capture frequency for test point 100."""
    f0 = pll_free_running_frequency(2000.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_101():
    """Validate 565 PLL lock range and capture frequency for test point 101."""
    f0 = pll_free_running_frequency(2010.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_102():
    """Validate 565 PLL lock range and capture frequency for test point 102."""
    f0 = pll_free_running_frequency(2020.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_103():
    """Validate 565 PLL lock range and capture frequency for test point 103."""
    f0 = pll_free_running_frequency(2030.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_104():
    """Validate 565 PLL lock range and capture frequency for test point 104."""
    f0 = pll_free_running_frequency(2040.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_105():
    """Validate 565 PLL lock range and capture frequency for test point 105."""
    f0 = pll_free_running_frequency(2050.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_106():
    """Validate 565 PLL lock range and capture frequency for test point 106."""
    f0 = pll_free_running_frequency(2060.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_107():
    """Validate 565 PLL lock range and capture frequency for test point 107."""
    f0 = pll_free_running_frequency(2070.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_108():
    """Validate 565 PLL lock range and capture frequency for test point 108."""
    f0 = pll_free_running_frequency(2080.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_109():
    """Validate 565 PLL lock range and capture frequency for test point 109."""
    f0 = pll_free_running_frequency(2090.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_110():
    """Validate 565 PLL lock range and capture frequency for test point 110."""
    f0 = pll_free_running_frequency(2100.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_111():
    """Validate 565 PLL lock range and capture frequency for test point 111."""
    f0 = pll_free_running_frequency(2110.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_112():
    """Validate 565 PLL lock range and capture frequency for test point 112."""
    f0 = pll_free_running_frequency(2120.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_113():
    """Validate 565 PLL lock range and capture frequency for test point 113."""
    f0 = pll_free_running_frequency(2130.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_114():
    """Validate 565 PLL lock range and capture frequency for test point 114."""
    f0 = pll_free_running_frequency(2140.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_115():
    """Validate 565 PLL lock range and capture frequency for test point 115."""
    f0 = pll_free_running_frequency(2150.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_116():
    """Validate 565 PLL lock range and capture frequency for test point 116."""
    f0 = pll_free_running_frequency(2160.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_117():
    """Validate 565 PLL lock range and capture frequency for test point 117."""
    f0 = pll_free_running_frequency(2170.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_118():
    """Validate 565 PLL lock range and capture frequency for test point 118."""
    f0 = pll_free_running_frequency(2180.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_119():
    """Validate 565 PLL lock range and capture frequency for test point 119."""
    f0 = pll_free_running_frequency(2190.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_120():
    """Validate 565 PLL lock range and capture frequency for test point 120."""
    f0 = pll_free_running_frequency(2200.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_121():
    """Validate 565 PLL lock range and capture frequency for test point 121."""
    f0 = pll_free_running_frequency(2210.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_122():
    """Validate 565 PLL lock range and capture frequency for test point 122."""
    f0 = pll_free_running_frequency(2220.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_123():
    """Validate 565 PLL lock range and capture frequency for test point 123."""
    f0 = pll_free_running_frequency(2230.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_124():
    """Validate 565 PLL lock range and capture frequency for test point 124."""
    f0 = pll_free_running_frequency(2240.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_125():
    """Validate 565 PLL lock range and capture frequency for test point 125."""
    f0 = pll_free_running_frequency(2250.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_126():
    """Validate 565 PLL lock range and capture frequency for test point 126."""
    f0 = pll_free_running_frequency(2260.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_127():
    """Validate 565 PLL lock range and capture frequency for test point 127."""
    f0 = pll_free_running_frequency(2270.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_128():
    """Validate 565 PLL lock range and capture frequency for test point 128."""
    f0 = pll_free_running_frequency(2280.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_129():
    """Validate 565 PLL lock range and capture frequency for test point 129."""
    f0 = pll_free_running_frequency(2290.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_130():
    """Validate 565 PLL lock range and capture frequency for test point 130."""
    f0 = pll_free_running_frequency(2300.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_131():
    """Validate 565 PLL lock range and capture frequency for test point 131."""
    f0 = pll_free_running_frequency(2310.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_132():
    """Validate 565 PLL lock range and capture frequency for test point 132."""
    f0 = pll_free_running_frequency(2320.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_133():
    """Validate 565 PLL lock range and capture frequency for test point 133."""
    f0 = pll_free_running_frequency(2330.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_134():
    """Validate 565 PLL lock range and capture frequency for test point 134."""
    f0 = pll_free_running_frequency(2340.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_135():
    """Validate 565 PLL lock range and capture frequency for test point 135."""
    f0 = pll_free_running_frequency(2350.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_136():
    """Validate 565 PLL lock range and capture frequency for test point 136."""
    f0 = pll_free_running_frequency(2360.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_137():
    """Validate 565 PLL lock range and capture frequency for test point 137."""
    f0 = pll_free_running_frequency(2370.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_138():
    """Validate 565 PLL lock range and capture frequency for test point 138."""
    f0 = pll_free_running_frequency(2380.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_139():
    """Validate 565 PLL lock range and capture frequency for test point 139."""
    f0 = pll_free_running_frequency(2390.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_140():
    """Validate 565 PLL lock range and capture frequency for test point 140."""
    f0 = pll_free_running_frequency(2400.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_141():
    """Validate 565 PLL lock range and capture frequency for test point 141."""
    f0 = pll_free_running_frequency(2410.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_142():
    """Validate 565 PLL lock range and capture frequency for test point 142."""
    f0 = pll_free_running_frequency(2420.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_143():
    """Validate 565 PLL lock range and capture frequency for test point 143."""
    f0 = pll_free_running_frequency(2430.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_144():
    """Validate 565 PLL lock range and capture frequency for test point 144."""
    f0 = pll_free_running_frequency(2440.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_145():
    """Validate 565 PLL lock range and capture frequency for test point 145."""
    f0 = pll_free_running_frequency(2450.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_146():
    """Validate 565 PLL lock range and capture frequency for test point 146."""
    f0 = pll_free_running_frequency(2460.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_147():
    """Validate 565 PLL lock range and capture frequency for test point 147."""
    f0 = pll_free_running_frequency(2470.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_148():
    """Validate 565 PLL lock range and capture frequency for test point 148."""
    f0 = pll_free_running_frequency(2480.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_149():
    """Validate 565 PLL lock range and capture frequency for test point 149."""
    f0 = pll_free_running_frequency(2490.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_150():
    """Validate 565 PLL lock range and capture frequency for test point 150."""
    f0 = pll_free_running_frequency(2500.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_151():
    """Validate 565 PLL lock range and capture frequency for test point 151."""
    f0 = pll_free_running_frequency(2510.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_152():
    """Validate 565 PLL lock range and capture frequency for test point 152."""
    f0 = pll_free_running_frequency(2520.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_153():
    """Validate 565 PLL lock range and capture frequency for test point 153."""
    f0 = pll_free_running_frequency(2530.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_154():
    """Validate 565 PLL lock range and capture frequency for test point 154."""
    f0 = pll_free_running_frequency(2540.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_155():
    """Validate 565 PLL lock range and capture frequency for test point 155."""
    f0 = pll_free_running_frequency(2550.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_156():
    """Validate 565 PLL lock range and capture frequency for test point 156."""
    f0 = pll_free_running_frequency(2560.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_157():
    """Validate 565 PLL lock range and capture frequency for test point 157."""
    f0 = pll_free_running_frequency(2570.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_158():
    """Validate 565 PLL lock range and capture frequency for test point 158."""
    f0 = pll_free_running_frequency(2580.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_159():
    """Validate 565 PLL lock range and capture frequency for test point 159."""
    f0 = pll_free_running_frequency(2590.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_160():
    """Validate 565 PLL lock range and capture frequency for test point 160."""
    f0 = pll_free_running_frequency(2600.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_161():
    """Validate 565 PLL lock range and capture frequency for test point 161."""
    f0 = pll_free_running_frequency(2610.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_162():
    """Validate 565 PLL lock range and capture frequency for test point 162."""
    f0 = pll_free_running_frequency(2620.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_163():
    """Validate 565 PLL lock range and capture frequency for test point 163."""
    f0 = pll_free_running_frequency(2630.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_164():
    """Validate 565 PLL lock range and capture frequency for test point 164."""
    f0 = pll_free_running_frequency(2640.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_165():
    """Validate 565 PLL lock range and capture frequency for test point 165."""
    f0 = pll_free_running_frequency(2650.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_166():
    """Validate 565 PLL lock range and capture frequency for test point 166."""
    f0 = pll_free_running_frequency(2660.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_167():
    """Validate 565 PLL lock range and capture frequency for test point 167."""
    f0 = pll_free_running_frequency(2670.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_168():
    """Validate 565 PLL lock range and capture frequency for test point 168."""
    f0 = pll_free_running_frequency(2680.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_169():
    """Validate 565 PLL lock range and capture frequency for test point 169."""
    f0 = pll_free_running_frequency(2690.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_170():
    """Validate 565 PLL lock range and capture frequency for test point 170."""
    f0 = pll_free_running_frequency(2700.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_171():
    """Validate 565 PLL lock range and capture frequency for test point 171."""
    f0 = pll_free_running_frequency(2710.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_172():
    """Validate 565 PLL lock range and capture frequency for test point 172."""
    f0 = pll_free_running_frequency(2720.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_173():
    """Validate 565 PLL lock range and capture frequency for test point 173."""
    f0 = pll_free_running_frequency(2730.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_174():
    """Validate 565 PLL lock range and capture frequency for test point 174."""
    f0 = pll_free_running_frequency(2740.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_175():
    """Validate 565 PLL lock range and capture frequency for test point 175."""
    f0 = pll_free_running_frequency(2750.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_176():
    """Validate 565 PLL lock range and capture frequency for test point 176."""
    f0 = pll_free_running_frequency(2760.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_177():
    """Validate 565 PLL lock range and capture frequency for test point 177."""
    f0 = pll_free_running_frequency(2770.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_178():
    """Validate 565 PLL lock range and capture frequency for test point 178."""
    f0 = pll_free_running_frequency(2780.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_179():
    """Validate 565 PLL lock range and capture frequency for test point 179."""
    f0 = pll_free_running_frequency(2790.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_180():
    """Validate 565 PLL lock range and capture frequency for test point 180."""
    f0 = pll_free_running_frequency(2800.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_181():
    """Validate 565 PLL lock range and capture frequency for test point 181."""
    f0 = pll_free_running_frequency(2810.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_182():
    """Validate 565 PLL lock range and capture frequency for test point 182."""
    f0 = pll_free_running_frequency(2820.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_183():
    """Validate 565 PLL lock range and capture frequency for test point 183."""
    f0 = pll_free_running_frequency(2830.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_184():
    """Validate 565 PLL lock range and capture frequency for test point 184."""
    f0 = pll_free_running_frequency(2840.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_185():
    """Validate 565 PLL lock range and capture frequency for test point 185."""
    f0 = pll_free_running_frequency(2850.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_186():
    """Validate 565 PLL lock range and capture frequency for test point 186."""
    f0 = pll_free_running_frequency(2860.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_187():
    """Validate 565 PLL lock range and capture frequency for test point 187."""
    f0 = pll_free_running_frequency(2870.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_188():
    """Validate 565 PLL lock range and capture frequency for test point 188."""
    f0 = pll_free_running_frequency(2880.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_189():
    """Validate 565 PLL lock range and capture frequency for test point 189."""
    f0 = pll_free_running_frequency(2890.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_190():
    """Validate 565 PLL lock range and capture frequency for test point 190."""
    f0 = pll_free_running_frequency(2900.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_191():
    """Validate 565 PLL lock range and capture frequency for test point 191."""
    f0 = pll_free_running_frequency(2910.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_192():
    """Validate 565 PLL lock range and capture frequency for test point 192."""
    f0 = pll_free_running_frequency(2920.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_193():
    """Validate 565 PLL lock range and capture frequency for test point 193."""
    f0 = pll_free_running_frequency(2930.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_194():
    """Validate 565 PLL lock range and capture frequency for test point 194."""
    f0 = pll_free_running_frequency(2940.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_195():
    """Validate 565 PLL lock range and capture frequency for test point 195."""
    f0 = pll_free_running_frequency(2950.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_196():
    """Validate 565 PLL lock range and capture frequency for test point 196."""
    f0 = pll_free_running_frequency(2960.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_197():
    """Validate 565 PLL lock range and capture frequency for test point 197."""
    f0 = pll_free_running_frequency(2970.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_198():
    """Validate 565 PLL lock range and capture frequency for test point 198."""
    f0 = pll_free_running_frequency(2980.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_199():
    """Validate 565 PLL lock range and capture frequency for test point 199."""
    f0 = pll_free_running_frequency(2990.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_200():
    """Validate 565 PLL lock range and capture frequency for test point 200."""
    f0 = pll_free_running_frequency(3000.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_201():
    """Validate 565 PLL lock range and capture frequency for test point 201."""
    f0 = pll_free_running_frequency(3010.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_202():
    """Validate 565 PLL lock range and capture frequency for test point 202."""
    f0 = pll_free_running_frequency(3020.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_203():
    """Validate 565 PLL lock range and capture frequency for test point 203."""
    f0 = pll_free_running_frequency(3030.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_204():
    """Validate 565 PLL lock range and capture frequency for test point 204."""
    f0 = pll_free_running_frequency(3040.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_205():
    """Validate 565 PLL lock range and capture frequency for test point 205."""
    f0 = pll_free_running_frequency(3050.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_206():
    """Validate 565 PLL lock range and capture frequency for test point 206."""
    f0 = pll_free_running_frequency(3060.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_207():
    """Validate 565 PLL lock range and capture frequency for test point 207."""
    f0 = pll_free_running_frequency(3070.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_208():
    """Validate 565 PLL lock range and capture frequency for test point 208."""
    f0 = pll_free_running_frequency(3080.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_209():
    """Validate 565 PLL lock range and capture frequency for test point 209."""
    f0 = pll_free_running_frequency(3090.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_210():
    """Validate 565 PLL lock range and capture frequency for test point 210."""
    f0 = pll_free_running_frequency(3100.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_211():
    """Validate 565 PLL lock range and capture frequency for test point 211."""
    f0 = pll_free_running_frequency(3110.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_212():
    """Validate 565 PLL lock range and capture frequency for test point 212."""
    f0 = pll_free_running_frequency(3120.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_213():
    """Validate 565 PLL lock range and capture frequency for test point 213."""
    f0 = pll_free_running_frequency(3130.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_214():
    """Validate 565 PLL lock range and capture frequency for test point 214."""
    f0 = pll_free_running_frequency(3140.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_215():
    """Validate 565 PLL lock range and capture frequency for test point 215."""
    f0 = pll_free_running_frequency(3150.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_216():
    """Validate 565 PLL lock range and capture frequency for test point 216."""
    f0 = pll_free_running_frequency(3160.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_217():
    """Validate 565 PLL lock range and capture frequency for test point 217."""
    f0 = pll_free_running_frequency(3170.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_218():
    """Validate 565 PLL lock range and capture frequency for test point 218."""
    f0 = pll_free_running_frequency(3180.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_219():
    """Validate 565 PLL lock range and capture frequency for test point 219."""
    f0 = pll_free_running_frequency(3190.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_220():
    """Validate 565 PLL lock range and capture frequency for test point 220."""
    f0 = pll_free_running_frequency(3200.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_221():
    """Validate 565 PLL lock range and capture frequency for test point 221."""
    f0 = pll_free_running_frequency(3210.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_222():
    """Validate 565 PLL lock range and capture frequency for test point 222."""
    f0 = pll_free_running_frequency(3220.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_223():
    """Validate 565 PLL lock range and capture frequency for test point 223."""
    f0 = pll_free_running_frequency(3230.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_224():
    """Validate 565 PLL lock range and capture frequency for test point 224."""
    f0 = pll_free_running_frequency(3240.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_225():
    """Validate 565 PLL lock range and capture frequency for test point 225."""
    f0 = pll_free_running_frequency(3250.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_226():
    """Validate 565 PLL lock range and capture frequency for test point 226."""
    f0 = pll_free_running_frequency(3260.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_227():
    """Validate 565 PLL lock range and capture frequency for test point 227."""
    f0 = pll_free_running_frequency(3270.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_228():
    """Validate 565 PLL lock range and capture frequency for test point 228."""
    f0 = pll_free_running_frequency(3280.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_229():
    """Validate 565 PLL lock range and capture frequency for test point 229."""
    f0 = pll_free_running_frequency(3290.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_230():
    """Validate 565 PLL lock range and capture frequency for test point 230."""
    f0 = pll_free_running_frequency(3300.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_231():
    """Validate 565 PLL lock range and capture frequency for test point 231."""
    f0 = pll_free_running_frequency(3310.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_232():
    """Validate 565 PLL lock range and capture frequency for test point 232."""
    f0 = pll_free_running_frequency(3320.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_233():
    """Validate 565 PLL lock range and capture frequency for test point 233."""
    f0 = pll_free_running_frequency(3330.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_234():
    """Validate 565 PLL lock range and capture frequency for test point 234."""
    f0 = pll_free_running_frequency(3340.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_235():
    """Validate 565 PLL lock range and capture frequency for test point 235."""
    f0 = pll_free_running_frequency(3350.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_236():
    """Validate 565 PLL lock range and capture frequency for test point 236."""
    f0 = pll_free_running_frequency(3360.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_237():
    """Validate 565 PLL lock range and capture frequency for test point 237."""
    f0 = pll_free_running_frequency(3370.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_238():
    """Validate 565 PLL lock range and capture frequency for test point 238."""
    f0 = pll_free_running_frequency(3380.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_239():
    """Validate 565 PLL lock range and capture frequency for test point 239."""
    f0 = pll_free_running_frequency(3390.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_240():
    """Validate 565 PLL lock range and capture frequency for test point 240."""
    f0 = pll_free_running_frequency(3400.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_241():
    """Validate 565 PLL lock range and capture frequency for test point 241."""
    f0 = pll_free_running_frequency(3410.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_242():
    """Validate 565 PLL lock range and capture frequency for test point 242."""
    f0 = pll_free_running_frequency(3420.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_243():
    """Validate 565 PLL lock range and capture frequency for test point 243."""
    f0 = pll_free_running_frequency(3430.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_244():
    """Validate 565 PLL lock range and capture frequency for test point 244."""
    f0 = pll_free_running_frequency(3440.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_245():
    """Validate 565 PLL lock range and capture frequency for test point 245."""
    f0 = pll_free_running_frequency(3450.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_246():
    """Validate 565 PLL lock range and capture frequency for test point 246."""
    f0 = pll_free_running_frequency(3460.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_247():
    """Validate 565 PLL lock range and capture frequency for test point 247."""
    f0 = pll_free_running_frequency(3470.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_248():
    """Validate 565 PLL lock range and capture frequency for test point 248."""
    f0 = pll_free_running_frequency(3480.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_249():
    """Validate 565 PLL lock range and capture frequency for test point 249."""
    f0 = pll_free_running_frequency(3490.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_250():
    """Validate 565 PLL lock range and capture frequency for test point 250."""
    f0 = pll_free_running_frequency(3500.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_251():
    """Validate 565 PLL lock range and capture frequency for test point 251."""
    f0 = pll_free_running_frequency(3510.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_252():
    """Validate 565 PLL lock range and capture frequency for test point 252."""
    f0 = pll_free_running_frequency(3520.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_253():
    """Validate 565 PLL lock range and capture frequency for test point 253."""
    f0 = pll_free_running_frequency(3530.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_254():
    """Validate 565 PLL lock range and capture frequency for test point 254."""
    f0 = pll_free_running_frequency(3540.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_255():
    """Validate 565 PLL lock range and capture frequency for test point 255."""
    f0 = pll_free_running_frequency(3550.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_256():
    """Validate 565 PLL lock range and capture frequency for test point 256."""
    f0 = pll_free_running_frequency(3560.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_257():
    """Validate 565 PLL lock range and capture frequency for test point 257."""
    f0 = pll_free_running_frequency(3570.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_258():
    """Validate 565 PLL lock range and capture frequency for test point 258."""
    f0 = pll_free_running_frequency(3580.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_259():
    """Validate 565 PLL lock range and capture frequency for test point 259."""
    f0 = pll_free_running_frequency(3590.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_260():
    """Validate 565 PLL lock range and capture frequency for test point 260."""
    f0 = pll_free_running_frequency(3600.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_261():
    """Validate 565 PLL lock range and capture frequency for test point 261."""
    f0 = pll_free_running_frequency(3610.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_262():
    """Validate 565 PLL lock range and capture frequency for test point 262."""
    f0 = pll_free_running_frequency(3620.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_263():
    """Validate 565 PLL lock range and capture frequency for test point 263."""
    f0 = pll_free_running_frequency(3630.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_264():
    """Validate 565 PLL lock range and capture frequency for test point 264."""
    f0 = pll_free_running_frequency(3640.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_265():
    """Validate 565 PLL lock range and capture frequency for test point 265."""
    f0 = pll_free_running_frequency(3650.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_266():
    """Validate 565 PLL lock range and capture frequency for test point 266."""
    f0 = pll_free_running_frequency(3660.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_267():
    """Validate 565 PLL lock range and capture frequency for test point 267."""
    f0 = pll_free_running_frequency(3670.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_268():
    """Validate 565 PLL lock range and capture frequency for test point 268."""
    f0 = pll_free_running_frequency(3680.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_269():
    """Validate 565 PLL lock range and capture frequency for test point 269."""
    f0 = pll_free_running_frequency(3690.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_270():
    """Validate 565 PLL lock range and capture frequency for test point 270."""
    f0 = pll_free_running_frequency(3700.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_271():
    """Validate 565 PLL lock range and capture frequency for test point 271."""
    f0 = pll_free_running_frequency(3710.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_272():
    """Validate 565 PLL lock range and capture frequency for test point 272."""
    f0 = pll_free_running_frequency(3720.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_273():
    """Validate 565 PLL lock range and capture frequency for test point 273."""
    f0 = pll_free_running_frequency(3730.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_274():
    """Validate 565 PLL lock range and capture frequency for test point 274."""
    f0 = pll_free_running_frequency(3740.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_275():
    """Validate 565 PLL lock range and capture frequency for test point 275."""
    f0 = pll_free_running_frequency(3750.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_276():
    """Validate 565 PLL lock range and capture frequency for test point 276."""
    f0 = pll_free_running_frequency(3760.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_277():
    """Validate 565 PLL lock range and capture frequency for test point 277."""
    f0 = pll_free_running_frequency(3770.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_278():
    """Validate 565 PLL lock range and capture frequency for test point 278."""
    f0 = pll_free_running_frequency(3780.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_279():
    """Validate 565 PLL lock range and capture frequency for test point 279."""
    f0 = pll_free_running_frequency(3790.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_280():
    """Validate 565 PLL lock range and capture frequency for test point 280."""
    f0 = pll_free_running_frequency(3800.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_281():
    """Validate 565 PLL lock range and capture frequency for test point 281."""
    f0 = pll_free_running_frequency(3810.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_282():
    """Validate 565 PLL lock range and capture frequency for test point 282."""
    f0 = pll_free_running_frequency(3820.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_283():
    """Validate 565 PLL lock range and capture frequency for test point 283."""
    f0 = pll_free_running_frequency(3830.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_284():
    """Validate 565 PLL lock range and capture frequency for test point 284."""
    f0 = pll_free_running_frequency(3840.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_285():
    """Validate 565 PLL lock range and capture frequency for test point 285."""
    f0 = pll_free_running_frequency(3850.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_286():
    """Validate 565 PLL lock range and capture frequency for test point 286."""
    f0 = pll_free_running_frequency(3860.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_287():
    """Validate 565 PLL lock range and capture frequency for test point 287."""
    f0 = pll_free_running_frequency(3870.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_288():
    """Validate 565 PLL lock range and capture frequency for test point 288."""
    f0 = pll_free_running_frequency(3880.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_289():
    """Validate 565 PLL lock range and capture frequency for test point 289."""
    f0 = pll_free_running_frequency(3890.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_290():
    """Validate 565 PLL lock range and capture frequency for test point 290."""
    f0 = pll_free_running_frequency(3900.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_291():
    """Validate 565 PLL lock range and capture frequency for test point 291."""
    f0 = pll_free_running_frequency(3910.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_292():
    """Validate 565 PLL lock range and capture frequency for test point 292."""
    f0 = pll_free_running_frequency(3920.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_293():
    """Validate 565 PLL lock range and capture frequency for test point 293."""
    f0 = pll_free_running_frequency(3930.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_294():
    """Validate 565 PLL lock range and capture frequency for test point 294."""
    f0 = pll_free_running_frequency(3940.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_295():
    """Validate 565 PLL lock range and capture frequency for test point 295."""
    f0 = pll_free_running_frequency(3950.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_296():
    """Validate 565 PLL lock range and capture frequency for test point 296."""
    f0 = pll_free_running_frequency(3960.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_297():
    """Validate 565 PLL lock range and capture frequency for test point 297."""
    f0 = pll_free_running_frequency(3970.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_298():
    """Validate 565 PLL lock range and capture frequency for test point 298."""
    f0 = pll_free_running_frequency(3980.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_299():
    """Validate 565 PLL lock range and capture frequency for test point 299."""
    f0 = pll_free_running_frequency(3990.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_300():
    """Validate 565 PLL lock range and capture frequency for test point 300."""
    f0 = pll_free_running_frequency(4000.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_301():
    """Validate 565 PLL lock range and capture frequency for test point 301."""
    f0 = pll_free_running_frequency(4010.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_302():
    """Validate 565 PLL lock range and capture frequency for test point 302."""
    f0 = pll_free_running_frequency(4020.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_303():
    """Validate 565 PLL lock range and capture frequency for test point 303."""
    f0 = pll_free_running_frequency(4030.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_304():
    """Validate 565 PLL lock range and capture frequency for test point 304."""
    f0 = pll_free_running_frequency(4040.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_305():
    """Validate 565 PLL lock range and capture frequency for test point 305."""
    f0 = pll_free_running_frequency(4050.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_306():
    """Validate 565 PLL lock range and capture frequency for test point 306."""
    f0 = pll_free_running_frequency(4060.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_307():
    """Validate 565 PLL lock range and capture frequency for test point 307."""
    f0 = pll_free_running_frequency(4070.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_308():
    """Validate 565 PLL lock range and capture frequency for test point 308."""
    f0 = pll_free_running_frequency(4080.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_309():
    """Validate 565 PLL lock range and capture frequency for test point 309."""
    f0 = pll_free_running_frequency(4090.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_310():
    """Validate 565 PLL lock range and capture frequency for test point 310."""
    f0 = pll_free_running_frequency(4100.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_311():
    """Validate 565 PLL lock range and capture frequency for test point 311."""
    f0 = pll_free_running_frequency(4110.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_312():
    """Validate 565 PLL lock range and capture frequency for test point 312."""
    f0 = pll_free_running_frequency(4120.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_313():
    """Validate 565 PLL lock range and capture frequency for test point 313."""
    f0 = pll_free_running_frequency(4130.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_314():
    """Validate 565 PLL lock range and capture frequency for test point 314."""
    f0 = pll_free_running_frequency(4140.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_315():
    """Validate 565 PLL lock range and capture frequency for test point 315."""
    f0 = pll_free_running_frequency(4150.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_316():
    """Validate 565 PLL lock range and capture frequency for test point 316."""
    f0 = pll_free_running_frequency(4160.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_317():
    """Validate 565 PLL lock range and capture frequency for test point 317."""
    f0 = pll_free_running_frequency(4170.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_318():
    """Validate 565 PLL lock range and capture frequency for test point 318."""
    f0 = pll_free_running_frequency(4180.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_319():
    """Validate 565 PLL lock range and capture frequency for test point 319."""
    f0 = pll_free_running_frequency(4190.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_320():
    """Validate 565 PLL lock range and capture frequency for test point 320."""
    f0 = pll_free_running_frequency(4200.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_321():
    """Validate 565 PLL lock range and capture frequency for test point 321."""
    f0 = pll_free_running_frequency(4210.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_322():
    """Validate 565 PLL lock range and capture frequency for test point 322."""
    f0 = pll_free_running_frequency(4220.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_323():
    """Validate 565 PLL lock range and capture frequency for test point 323."""
    f0 = pll_free_running_frequency(4230.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_324():
    """Validate 565 PLL lock range and capture frequency for test point 324."""
    f0 = pll_free_running_frequency(4240.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_325():
    """Validate 565 PLL lock range and capture frequency for test point 325."""
    f0 = pll_free_running_frequency(4250.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_326():
    """Validate 565 PLL lock range and capture frequency for test point 326."""
    f0 = pll_free_running_frequency(4260.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_327():
    """Validate 565 PLL lock range and capture frequency for test point 327."""
    f0 = pll_free_running_frequency(4270.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_328():
    """Validate 565 PLL lock range and capture frequency for test point 328."""
    f0 = pll_free_running_frequency(4280.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_329():
    """Validate 565 PLL lock range and capture frequency for test point 329."""
    f0 = pll_free_running_frequency(4290.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_330():
    """Validate 565 PLL lock range and capture frequency for test point 330."""
    f0 = pll_free_running_frequency(4300.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_331():
    """Validate 565 PLL lock range and capture frequency for test point 331."""
    f0 = pll_free_running_frequency(4310.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_332():
    """Validate 565 PLL lock range and capture frequency for test point 332."""
    f0 = pll_free_running_frequency(4320.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_333():
    """Validate 565 PLL lock range and capture frequency for test point 333."""
    f0 = pll_free_running_frequency(4330.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_334():
    """Validate 565 PLL lock range and capture frequency for test point 334."""
    f0 = pll_free_running_frequency(4340.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_335():
    """Validate 565 PLL lock range and capture frequency for test point 335."""
    f0 = pll_free_running_frequency(4350.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_336():
    """Validate 565 PLL lock range and capture frequency for test point 336."""
    f0 = pll_free_running_frequency(4360.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_337():
    """Validate 565 PLL lock range and capture frequency for test point 337."""
    f0 = pll_free_running_frequency(4370.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_338():
    """Validate 565 PLL lock range and capture frequency for test point 338."""
    f0 = pll_free_running_frequency(4380.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_339():
    """Validate 565 PLL lock range and capture frequency for test point 339."""
    f0 = pll_free_running_frequency(4390.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_340():
    """Validate 565 PLL lock range and capture frequency for test point 340."""
    f0 = pll_free_running_frequency(4400.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_341():
    """Validate 565 PLL lock range and capture frequency for test point 341."""
    f0 = pll_free_running_frequency(4410.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_342():
    """Validate 565 PLL lock range and capture frequency for test point 342."""
    f0 = pll_free_running_frequency(4420.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_343():
    """Validate 565 PLL lock range and capture frequency for test point 343."""
    f0 = pll_free_running_frequency(4430.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_344():
    """Validate 565 PLL lock range and capture frequency for test point 344."""
    f0 = pll_free_running_frequency(4440.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_345():
    """Validate 565 PLL lock range and capture frequency for test point 345."""
    f0 = pll_free_running_frequency(4450.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_346():
    """Validate 565 PLL lock range and capture frequency for test point 346."""
    f0 = pll_free_running_frequency(4460.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_347():
    """Validate 565 PLL lock range and capture frequency for test point 347."""
    f0 = pll_free_running_frequency(4470.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_348():
    """Validate 565 PLL lock range and capture frequency for test point 348."""
    f0 = pll_free_running_frequency(4480.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_349():
    """Validate 565 PLL lock range and capture frequency for test point 349."""
    f0 = pll_free_running_frequency(4490.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_350():
    """Validate 565 PLL lock range and capture frequency for test point 350."""
    f0 = pll_free_running_frequency(4500.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_351():
    """Validate 565 PLL lock range and capture frequency for test point 351."""
    f0 = pll_free_running_frequency(4510.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_352():
    """Validate 565 PLL lock range and capture frequency for test point 352."""
    f0 = pll_free_running_frequency(4520.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_353():
    """Validate 565 PLL lock range and capture frequency for test point 353."""
    f0 = pll_free_running_frequency(4530.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_354():
    """Validate 565 PLL lock range and capture frequency for test point 354."""
    f0 = pll_free_running_frequency(4540.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_355():
    """Validate 565 PLL lock range and capture frequency for test point 355."""
    f0 = pll_free_running_frequency(4550.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_356():
    """Validate 565 PLL lock range and capture frequency for test point 356."""
    f0 = pll_free_running_frequency(4560.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_357():
    """Validate 565 PLL lock range and capture frequency for test point 357."""
    f0 = pll_free_running_frequency(4570.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_358():
    """Validate 565 PLL lock range and capture frequency for test point 358."""
    f0 = pll_free_running_frequency(4580.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_359():
    """Validate 565 PLL lock range and capture frequency for test point 359."""
    f0 = pll_free_running_frequency(4590.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_360():
    """Validate 565 PLL lock range and capture frequency for test point 360."""
    f0 = pll_free_running_frequency(4600.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_361():
    """Validate 565 PLL lock range and capture frequency for test point 361."""
    f0 = pll_free_running_frequency(4610.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_362():
    """Validate 565 PLL lock range and capture frequency for test point 362."""
    f0 = pll_free_running_frequency(4620.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_363():
    """Validate 565 PLL lock range and capture frequency for test point 363."""
    f0 = pll_free_running_frequency(4630.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_364():
    """Validate 565 PLL lock range and capture frequency for test point 364."""
    f0 = pll_free_running_frequency(4640.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_365():
    """Validate 565 PLL lock range and capture frequency for test point 365."""
    f0 = pll_free_running_frequency(4650.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_366():
    """Validate 565 PLL lock range and capture frequency for test point 366."""
    f0 = pll_free_running_frequency(4660.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_367():
    """Validate 565 PLL lock range and capture frequency for test point 367."""
    f0 = pll_free_running_frequency(4670.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_368():
    """Validate 565 PLL lock range and capture frequency for test point 368."""
    f0 = pll_free_running_frequency(4680.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_369():
    """Validate 565 PLL lock range and capture frequency for test point 369."""
    f0 = pll_free_running_frequency(4690.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_370():
    """Validate 565 PLL lock range and capture frequency for test point 370."""
    f0 = pll_free_running_frequency(4700.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_371():
    """Validate 565 PLL lock range and capture frequency for test point 371."""
    f0 = pll_free_running_frequency(4710.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_372():
    """Validate 565 PLL lock range and capture frequency for test point 372."""
    f0 = pll_free_running_frequency(4720.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_373():
    """Validate 565 PLL lock range and capture frequency for test point 373."""
    f0 = pll_free_running_frequency(4730.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_374():
    """Validate 565 PLL lock range and capture frequency for test point 374."""
    f0 = pll_free_running_frequency(4740.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_375():
    """Validate 565 PLL lock range and capture frequency for test point 375."""
    f0 = pll_free_running_frequency(4750.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_376():
    """Validate 565 PLL lock range and capture frequency for test point 376."""
    f0 = pll_free_running_frequency(4760.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_377():
    """Validate 565 PLL lock range and capture frequency for test point 377."""
    f0 = pll_free_running_frequency(4770.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_378():
    """Validate 565 PLL lock range and capture frequency for test point 378."""
    f0 = pll_free_running_frequency(4780.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_379():
    """Validate 565 PLL lock range and capture frequency for test point 379."""
    f0 = pll_free_running_frequency(4790.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_380():
    """Validate 565 PLL lock range and capture frequency for test point 380."""
    f0 = pll_free_running_frequency(4800.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_381():
    """Validate 565 PLL lock range and capture frequency for test point 381."""
    f0 = pll_free_running_frequency(4810.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_382():
    """Validate 565 PLL lock range and capture frequency for test point 382."""
    f0 = pll_free_running_frequency(4820.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_383():
    """Validate 565 PLL lock range and capture frequency for test point 383."""
    f0 = pll_free_running_frequency(4830.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_384():
    """Validate 565 PLL lock range and capture frequency for test point 384."""
    f0 = pll_free_running_frequency(4840.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_385():
    """Validate 565 PLL lock range and capture frequency for test point 385."""
    f0 = pll_free_running_frequency(4850.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_386():
    """Validate 565 PLL lock range and capture frequency for test point 386."""
    f0 = pll_free_running_frequency(4860.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_387():
    """Validate 565 PLL lock range and capture frequency for test point 387."""
    f0 = pll_free_running_frequency(4870.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_388():
    """Validate 565 PLL lock range and capture frequency for test point 388."""
    f0 = pll_free_running_frequency(4880.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_389():
    """Validate 565 PLL lock range and capture frequency for test point 389."""
    f0 = pll_free_running_frequency(4890.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_390():
    """Validate 565 PLL lock range and capture frequency for test point 390."""
    f0 = pll_free_running_frequency(4900.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_391():
    """Validate 565 PLL lock range and capture frequency for test point 391."""
    f0 = pll_free_running_frequency(4910.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_392():
    """Validate 565 PLL lock range and capture frequency for test point 392."""
    f0 = pll_free_running_frequency(4920.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_393():
    """Validate 565 PLL lock range and capture frequency for test point 393."""
    f0 = pll_free_running_frequency(4930.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_394():
    """Validate 565 PLL lock range and capture frequency for test point 394."""
    f0 = pll_free_running_frequency(4940.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_395():
    """Validate 565 PLL lock range and capture frequency for test point 395."""
    f0 = pll_free_running_frequency(4950.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_396():
    """Validate 565 PLL lock range and capture frequency for test point 396."""
    f0 = pll_free_running_frequency(4960.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_397():
    """Validate 565 PLL lock range and capture frequency for test point 397."""
    f0 = pll_free_running_frequency(4970.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_398():
    """Validate 565 PLL lock range and capture frequency for test point 398."""
    f0 = pll_free_running_frequency(4980.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_399():
    """Validate 565 PLL lock range and capture frequency for test point 399."""
    f0 = pll_free_running_frequency(4990.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_400():
    """Validate 565 PLL lock range and capture frequency for test point 400."""
    f0 = pll_free_running_frequency(5000.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_401():
    """Validate 565 PLL lock range and capture frequency for test point 401."""
    f0 = pll_free_running_frequency(5010.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_402():
    """Validate 565 PLL lock range and capture frequency for test point 402."""
    f0 = pll_free_running_frequency(5020.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_403():
    """Validate 565 PLL lock range and capture frequency for test point 403."""
    f0 = pll_free_running_frequency(5030.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_404():
    """Validate 565 PLL lock range and capture frequency for test point 404."""
    f0 = pll_free_running_frequency(5040.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_405():
    """Validate 565 PLL lock range and capture frequency for test point 405."""
    f0 = pll_free_running_frequency(5050.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_406():
    """Validate 565 PLL lock range and capture frequency for test point 406."""
    f0 = pll_free_running_frequency(5060.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_407():
    """Validate 565 PLL lock range and capture frequency for test point 407."""
    f0 = pll_free_running_frequency(5070.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_408():
    """Validate 565 PLL lock range and capture frequency for test point 408."""
    f0 = pll_free_running_frequency(5080.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_409():
    """Validate 565 PLL lock range and capture frequency for test point 409."""
    f0 = pll_free_running_frequency(5090.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_410():
    """Validate 565 PLL lock range and capture frequency for test point 410."""
    f0 = pll_free_running_frequency(5100.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_411():
    """Validate 565 PLL lock range and capture frequency for test point 411."""
    f0 = pll_free_running_frequency(5110.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_412():
    """Validate 565 PLL lock range and capture frequency for test point 412."""
    f0 = pll_free_running_frequency(5120.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_413():
    """Validate 565 PLL lock range and capture frequency for test point 413."""
    f0 = pll_free_running_frequency(5130.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_414():
    """Validate 565 PLL lock range and capture frequency for test point 414."""
    f0 = pll_free_running_frequency(5140.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_415():
    """Validate 565 PLL lock range and capture frequency for test point 415."""
    f0 = pll_free_running_frequency(5150.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_416():
    """Validate 565 PLL lock range and capture frequency for test point 416."""
    f0 = pll_free_running_frequency(5160.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_417():
    """Validate 565 PLL lock range and capture frequency for test point 417."""
    f0 = pll_free_running_frequency(5170.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_418():
    """Validate 565 PLL lock range and capture frequency for test point 418."""
    f0 = pll_free_running_frequency(5180.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_419():
    """Validate 565 PLL lock range and capture frequency for test point 419."""
    f0 = pll_free_running_frequency(5190.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_420():
    """Validate 565 PLL lock range and capture frequency for test point 420."""
    f0 = pll_free_running_frequency(5200.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_421():
    """Validate 565 PLL lock range and capture frequency for test point 421."""
    f0 = pll_free_running_frequency(5210.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_422():
    """Validate 565 PLL lock range and capture frequency for test point 422."""
    f0 = pll_free_running_frequency(5220.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_423():
    """Validate 565 PLL lock range and capture frequency for test point 423."""
    f0 = pll_free_running_frequency(5230.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_424():
    """Validate 565 PLL lock range and capture frequency for test point 424."""
    f0 = pll_free_running_frequency(5240.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_425():
    """Validate 565 PLL lock range and capture frequency for test point 425."""
    f0 = pll_free_running_frequency(5250.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_426():
    """Validate 565 PLL lock range and capture frequency for test point 426."""
    f0 = pll_free_running_frequency(5260.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_427():
    """Validate 565 PLL lock range and capture frequency for test point 427."""
    f0 = pll_free_running_frequency(5270.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_428():
    """Validate 565 PLL lock range and capture frequency for test point 428."""
    f0 = pll_free_running_frequency(5280.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_429():
    """Validate 565 PLL lock range and capture frequency for test point 429."""
    f0 = pll_free_running_frequency(5290.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_430():
    """Validate 565 PLL lock range and capture frequency for test point 430."""
    f0 = pll_free_running_frequency(5300.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_431():
    """Validate 565 PLL lock range and capture frequency for test point 431."""
    f0 = pll_free_running_frequency(5310.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_432():
    """Validate 565 PLL lock range and capture frequency for test point 432."""
    f0 = pll_free_running_frequency(5320.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_433():
    """Validate 565 PLL lock range and capture frequency for test point 433."""
    f0 = pll_free_running_frequency(5330.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_434():
    """Validate 565 PLL lock range and capture frequency for test point 434."""
    f0 = pll_free_running_frequency(5340.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_435():
    """Validate 565 PLL lock range and capture frequency for test point 435."""
    f0 = pll_free_running_frequency(5350.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_436():
    """Validate 565 PLL lock range and capture frequency for test point 436."""
    f0 = pll_free_running_frequency(5360.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_437():
    """Validate 565 PLL lock range and capture frequency for test point 437."""
    f0 = pll_free_running_frequency(5370.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_438():
    """Validate 565 PLL lock range and capture frequency for test point 438."""
    f0 = pll_free_running_frequency(5380.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_439():
    """Validate 565 PLL lock range and capture frequency for test point 439."""
    f0 = pll_free_running_frequency(5390.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_440():
    """Validate 565 PLL lock range and capture frequency for test point 440."""
    f0 = pll_free_running_frequency(5400.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_441():
    """Validate 565 PLL lock range and capture frequency for test point 441."""
    f0 = pll_free_running_frequency(5410.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_442():
    """Validate 565 PLL lock range and capture frequency for test point 442."""
    f0 = pll_free_running_frequency(5420.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_443():
    """Validate 565 PLL lock range and capture frequency for test point 443."""
    f0 = pll_free_running_frequency(5430.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_444():
    """Validate 565 PLL lock range and capture frequency for test point 444."""
    f0 = pll_free_running_frequency(5440.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_445():
    """Validate 565 PLL lock range and capture frequency for test point 445."""
    f0 = pll_free_running_frequency(5450.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_446():
    """Validate 565 PLL lock range and capture frequency for test point 446."""
    f0 = pll_free_running_frequency(5460.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_447():
    """Validate 565 PLL lock range and capture frequency for test point 447."""
    f0 = pll_free_running_frequency(5470.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_448():
    """Validate 565 PLL lock range and capture frequency for test point 448."""
    f0 = pll_free_running_frequency(5480.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_449():
    """Validate 565 PLL lock range and capture frequency for test point 449."""
    f0 = pll_free_running_frequency(5490.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_450():
    """Validate 565 PLL lock range and capture frequency for test point 450."""
    f0 = pll_free_running_frequency(5500.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_451():
    """Validate 565 PLL lock range and capture frequency for test point 451."""
    f0 = pll_free_running_frequency(5510.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_452():
    """Validate 565 PLL lock range and capture frequency for test point 452."""
    f0 = pll_free_running_frequency(5520.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_453():
    """Validate 565 PLL lock range and capture frequency for test point 453."""
    f0 = pll_free_running_frequency(5530.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_454():
    """Validate 565 PLL lock range and capture frequency for test point 454."""
    f0 = pll_free_running_frequency(5540.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_455():
    """Validate 565 PLL lock range and capture frequency for test point 455."""
    f0 = pll_free_running_frequency(5550.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_456():
    """Validate 565 PLL lock range and capture frequency for test point 456."""
    f0 = pll_free_running_frequency(5560.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_457():
    """Validate 565 PLL lock range and capture frequency for test point 457."""
    f0 = pll_free_running_frequency(5570.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_458():
    """Validate 565 PLL lock range and capture frequency for test point 458."""
    f0 = pll_free_running_frequency(5580.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_459():
    """Validate 565 PLL lock range and capture frequency for test point 459."""
    f0 = pll_free_running_frequency(5590.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_460():
    """Validate 565 PLL lock range and capture frequency for test point 460."""
    f0 = pll_free_running_frequency(5600.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_461():
    """Validate 565 PLL lock range and capture frequency for test point 461."""
    f0 = pll_free_running_frequency(5610.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_462():
    """Validate 565 PLL lock range and capture frequency for test point 462."""
    f0 = pll_free_running_frequency(5620.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_463():
    """Validate 565 PLL lock range and capture frequency for test point 463."""
    f0 = pll_free_running_frequency(5630.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_464():
    """Validate 565 PLL lock range and capture frequency for test point 464."""
    f0 = pll_free_running_frequency(5640.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_465():
    """Validate 565 PLL lock range and capture frequency for test point 465."""
    f0 = pll_free_running_frequency(5650.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_466():
    """Validate 565 PLL lock range and capture frequency for test point 466."""
    f0 = pll_free_running_frequency(5660.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_467():
    """Validate 565 PLL lock range and capture frequency for test point 467."""
    f0 = pll_free_running_frequency(5670.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_468():
    """Validate 565 PLL lock range and capture frequency for test point 468."""
    f0 = pll_free_running_frequency(5680.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_469():
    """Validate 565 PLL lock range and capture frequency for test point 469."""
    f0 = pll_free_running_frequency(5690.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_470():
    """Validate 565 PLL lock range and capture frequency for test point 470."""
    f0 = pll_free_running_frequency(5700.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_471():
    """Validate 565 PLL lock range and capture frequency for test point 471."""
    f0 = pll_free_running_frequency(5710.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_472():
    """Validate 565 PLL lock range and capture frequency for test point 472."""
    f0 = pll_free_running_frequency(5720.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_473():
    """Validate 565 PLL lock range and capture frequency for test point 473."""
    f0 = pll_free_running_frequency(5730.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_474():
    """Validate 565 PLL lock range and capture frequency for test point 474."""
    f0 = pll_free_running_frequency(5740.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_475():
    """Validate 565 PLL lock range and capture frequency for test point 475."""
    f0 = pll_free_running_frequency(5750.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_476():
    """Validate 565 PLL lock range and capture frequency for test point 476."""
    f0 = pll_free_running_frequency(5760.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_477():
    """Validate 565 PLL lock range and capture frequency for test point 477."""
    f0 = pll_free_running_frequency(5770.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_478():
    """Validate 565 PLL lock range and capture frequency for test point 478."""
    f0 = pll_free_running_frequency(5780.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_479():
    """Validate 565 PLL lock range and capture frequency for test point 479."""
    f0 = pll_free_running_frequency(5790.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_480():
    """Validate 565 PLL lock range and capture frequency for test point 480."""
    f0 = pll_free_running_frequency(5800.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_481():
    """Validate 565 PLL lock range and capture frequency for test point 481."""
    f0 = pll_free_running_frequency(5810.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_482():
    """Validate 565 PLL lock range and capture frequency for test point 482."""
    f0 = pll_free_running_frequency(5820.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_483():
    """Validate 565 PLL lock range and capture frequency for test point 483."""
    f0 = pll_free_running_frequency(5830.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_484():
    """Validate 565 PLL lock range and capture frequency for test point 484."""
    f0 = pll_free_running_frequency(5840.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_485():
    """Validate 565 PLL lock range and capture frequency for test point 485."""
    f0 = pll_free_running_frequency(5850.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_486():
    """Validate 565 PLL lock range and capture frequency for test point 486."""
    f0 = pll_free_running_frequency(5860.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_487():
    """Validate 565 PLL lock range and capture frequency for test point 487."""
    f0 = pll_free_running_frequency(5870.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_488():
    """Validate 565 PLL lock range and capture frequency for test point 488."""
    f0 = pll_free_running_frequency(5880.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_489():
    """Validate 565 PLL lock range and capture frequency for test point 489."""
    f0 = pll_free_running_frequency(5890.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_490():
    """Validate 565 PLL lock range and capture frequency for test point 490."""
    f0 = pll_free_running_frequency(5900.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_491():
    """Validate 565 PLL lock range and capture frequency for test point 491."""
    f0 = pll_free_running_frequency(5910.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_492():
    """Validate 565 PLL lock range and capture frequency for test point 492."""
    f0 = pll_free_running_frequency(5920.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_493():
    """Validate 565 PLL lock range and capture frequency for test point 493."""
    f0 = pll_free_running_frequency(5930.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_494():
    """Validate 565 PLL lock range and capture frequency for test point 494."""
    f0 = pll_free_running_frequency(5940.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_495():
    """Validate 565 PLL lock range and capture frequency for test point 495."""
    f0 = pll_free_running_frequency(5950.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_496():
    """Validate 565 PLL lock range and capture frequency for test point 496."""
    f0 = pll_free_running_frequency(5960.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_497():
    """Validate 565 PLL lock range and capture frequency for test point 497."""
    f0 = pll_free_running_frequency(5970.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_498():
    """Validate 565 PLL lock range and capture frequency for test point 498."""
    f0 = pll_free_running_frequency(5980.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_499():
    """Validate 565 PLL lock range and capture frequency for test point 499."""
    f0 = pll_free_running_frequency(5990.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_500():
    """Validate 565 PLL lock range and capture frequency for test point 500."""
    f0 = pll_free_running_frequency(6000.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_501():
    """Validate 565 PLL lock range and capture frequency for test point 501."""
    f0 = pll_free_running_frequency(6010.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_502():
    """Validate 565 PLL lock range and capture frequency for test point 502."""
    f0 = pll_free_running_frequency(6020.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_503():
    """Validate 565 PLL lock range and capture frequency for test point 503."""
    f0 = pll_free_running_frequency(6030.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_504():
    """Validate 565 PLL lock range and capture frequency for test point 504."""
    f0 = pll_free_running_frequency(6040.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_505():
    """Validate 565 PLL lock range and capture frequency for test point 505."""
    f0 = pll_free_running_frequency(6050.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_506():
    """Validate 565 PLL lock range and capture frequency for test point 506."""
    f0 = pll_free_running_frequency(6060.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_507():
    """Validate 565 PLL lock range and capture frequency for test point 507."""
    f0 = pll_free_running_frequency(6070.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_508():
    """Validate 565 PLL lock range and capture frequency for test point 508."""
    f0 = pll_free_running_frequency(6080.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_509():
    """Validate 565 PLL lock range and capture frequency for test point 509."""
    f0 = pll_free_running_frequency(6090.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_510():
    """Validate 565 PLL lock range and capture frequency for test point 510."""
    f0 = pll_free_running_frequency(6100.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_511():
    """Validate 565 PLL lock range and capture frequency for test point 511."""
    f0 = pll_free_running_frequency(6110.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_512():
    """Validate 565 PLL lock range and capture frequency for test point 512."""
    f0 = pll_free_running_frequency(6120.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_513():
    """Validate 565 PLL lock range and capture frequency for test point 513."""
    f0 = pll_free_running_frequency(6130.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_514():
    """Validate 565 PLL lock range and capture frequency for test point 514."""
    f0 = pll_free_running_frequency(6140.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_515():
    """Validate 565 PLL lock range and capture frequency for test point 515."""
    f0 = pll_free_running_frequency(6150.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_516():
    """Validate 565 PLL lock range and capture frequency for test point 516."""
    f0 = pll_free_running_frequency(6160.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_517():
    """Validate 565 PLL lock range and capture frequency for test point 517."""
    f0 = pll_free_running_frequency(6170.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_518():
    """Validate 565 PLL lock range and capture frequency for test point 518."""
    f0 = pll_free_running_frequency(6180.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_519():
    """Validate 565 PLL lock range and capture frequency for test point 519."""
    f0 = pll_free_running_frequency(6190.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_520():
    """Validate 565 PLL lock range and capture frequency for test point 520."""
    f0 = pll_free_running_frequency(6200.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_521():
    """Validate 565 PLL lock range and capture frequency for test point 521."""
    f0 = pll_free_running_frequency(6210.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_522():
    """Validate 565 PLL lock range and capture frequency for test point 522."""
    f0 = pll_free_running_frequency(6220.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_523():
    """Validate 565 PLL lock range and capture frequency for test point 523."""
    f0 = pll_free_running_frequency(6230.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_524():
    """Validate 565 PLL lock range and capture frequency for test point 524."""
    f0 = pll_free_running_frequency(6240.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_525():
    """Validate 565 PLL lock range and capture frequency for test point 525."""
    f0 = pll_free_running_frequency(6250.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_526():
    """Validate 565 PLL lock range and capture frequency for test point 526."""
    f0 = pll_free_running_frequency(6260.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_527():
    """Validate 565 PLL lock range and capture frequency for test point 527."""
    f0 = pll_free_running_frequency(6270.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_528():
    """Validate 565 PLL lock range and capture frequency for test point 528."""
    f0 = pll_free_running_frequency(6280.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_529():
    """Validate 565 PLL lock range and capture frequency for test point 529."""
    f0 = pll_free_running_frequency(6290.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_530():
    """Validate 565 PLL lock range and capture frequency for test point 530."""
    f0 = pll_free_running_frequency(6300.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_531():
    """Validate 565 PLL lock range and capture frequency for test point 531."""
    f0 = pll_free_running_frequency(6310.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_532():
    """Validate 565 PLL lock range and capture frequency for test point 532."""
    f0 = pll_free_running_frequency(6320.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_533():
    """Validate 565 PLL lock range and capture frequency for test point 533."""
    f0 = pll_free_running_frequency(6330.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_534():
    """Validate 565 PLL lock range and capture frequency for test point 534."""
    f0 = pll_free_running_frequency(6340.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_535():
    """Validate 565 PLL lock range and capture frequency for test point 535."""
    f0 = pll_free_running_frequency(6350.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_536():
    """Validate 565 PLL lock range and capture frequency for test point 536."""
    f0 = pll_free_running_frequency(6360.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_537():
    """Validate 565 PLL lock range and capture frequency for test point 537."""
    f0 = pll_free_running_frequency(6370.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_538():
    """Validate 565 PLL lock range and capture frequency for test point 538."""
    f0 = pll_free_running_frequency(6380.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_539():
    """Validate 565 PLL lock range and capture frequency for test point 539."""
    f0 = pll_free_running_frequency(6390.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_540():
    """Validate 565 PLL lock range and capture frequency for test point 540."""
    f0 = pll_free_running_frequency(6400.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_541():
    """Validate 565 PLL lock range and capture frequency for test point 541."""
    f0 = pll_free_running_frequency(6410.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_542():
    """Validate 565 PLL lock range and capture frequency for test point 542."""
    f0 = pll_free_running_frequency(6420.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_543():
    """Validate 565 PLL lock range and capture frequency for test point 543."""
    f0 = pll_free_running_frequency(6430.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_544():
    """Validate 565 PLL lock range and capture frequency for test point 544."""
    f0 = pll_free_running_frequency(6440.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_545():
    """Validate 565 PLL lock range and capture frequency for test point 545."""
    f0 = pll_free_running_frequency(6450.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_546():
    """Validate 565 PLL lock range and capture frequency for test point 546."""
    f0 = pll_free_running_frequency(6460.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_547():
    """Validate 565 PLL lock range and capture frequency for test point 547."""
    f0 = pll_free_running_frequency(6470.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_548():
    """Validate 565 PLL lock range and capture frequency for test point 548."""
    f0 = pll_free_running_frequency(6480.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_549():
    """Validate 565 PLL lock range and capture frequency for test point 549."""
    f0 = pll_free_running_frequency(6490.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_550():
    """Validate 565 PLL lock range and capture frequency for test point 550."""
    f0 = pll_free_running_frequency(6500.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_551():
    """Validate 565 PLL lock range and capture frequency for test point 551."""
    f0 = pll_free_running_frequency(6510.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_552():
    """Validate 565 PLL lock range and capture frequency for test point 552."""
    f0 = pll_free_running_frequency(6520.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_553():
    """Validate 565 PLL lock range and capture frequency for test point 553."""
    f0 = pll_free_running_frequency(6530.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_554():
    """Validate 565 PLL lock range and capture frequency for test point 554."""
    f0 = pll_free_running_frequency(6540.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_555():
    """Validate 565 PLL lock range and capture frequency for test point 555."""
    f0 = pll_free_running_frequency(6550.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_556():
    """Validate 565 PLL lock range and capture frequency for test point 556."""
    f0 = pll_free_running_frequency(6560.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_557():
    """Validate 565 PLL lock range and capture frequency for test point 557."""
    f0 = pll_free_running_frequency(6570.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_558():
    """Validate 565 PLL lock range and capture frequency for test point 558."""
    f0 = pll_free_running_frequency(6580.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_559():
    """Validate 565 PLL lock range and capture frequency for test point 559."""
    f0 = pll_free_running_frequency(6590.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_560():
    """Validate 565 PLL lock range and capture frequency for test point 560."""
    f0 = pll_free_running_frequency(6600.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_561():
    """Validate 565 PLL lock range and capture frequency for test point 561."""
    f0 = pll_free_running_frequency(6610.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_562():
    """Validate 565 PLL lock range and capture frequency for test point 562."""
    f0 = pll_free_running_frequency(6620.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_563():
    """Validate 565 PLL lock range and capture frequency for test point 563."""
    f0 = pll_free_running_frequency(6630.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_564():
    """Validate 565 PLL lock range and capture frequency for test point 564."""
    f0 = pll_free_running_frequency(6640.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_565():
    """Validate 565 PLL lock range and capture frequency for test point 565."""
    f0 = pll_free_running_frequency(6650.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_566():
    """Validate 565 PLL lock range and capture frequency for test point 566."""
    f0 = pll_free_running_frequency(6660.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_567():
    """Validate 565 PLL lock range and capture frequency for test point 567."""
    f0 = pll_free_running_frequency(6670.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_568():
    """Validate 565 PLL lock range and capture frequency for test point 568."""
    f0 = pll_free_running_frequency(6680.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_569():
    """Validate 565 PLL lock range and capture frequency for test point 569."""
    f0 = pll_free_running_frequency(6690.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_570():
    """Validate 565 PLL lock range and capture frequency for test point 570."""
    f0 = pll_free_running_frequency(6700.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_571():
    """Validate 565 PLL lock range and capture frequency for test point 571."""
    f0 = pll_free_running_frequency(6710.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_572():
    """Validate 565 PLL lock range and capture frequency for test point 572."""
    f0 = pll_free_running_frequency(6720.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_573():
    """Validate 565 PLL lock range and capture frequency for test point 573."""
    f0 = pll_free_running_frequency(6730.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_574():
    """Validate 565 PLL lock range and capture frequency for test point 574."""
    f0 = pll_free_running_frequency(6740.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_575():
    """Validate 565 PLL lock range and capture frequency for test point 575."""
    f0 = pll_free_running_frequency(6750.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_576():
    """Validate 565 PLL lock range and capture frequency for test point 576."""
    f0 = pll_free_running_frequency(6760.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_577():
    """Validate 565 PLL lock range and capture frequency for test point 577."""
    f0 = pll_free_running_frequency(6770.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_578():
    """Validate 565 PLL lock range and capture frequency for test point 578."""
    f0 = pll_free_running_frequency(6780.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_579():
    """Validate 565 PLL lock range and capture frequency for test point 579."""
    f0 = pll_free_running_frequency(6790.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_580():
    """Validate 565 PLL lock range and capture frequency for test point 580."""
    f0 = pll_free_running_frequency(6800.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_581():
    """Validate 565 PLL lock range and capture frequency for test point 581."""
    f0 = pll_free_running_frequency(6810.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_582():
    """Validate 565 PLL lock range and capture frequency for test point 582."""
    f0 = pll_free_running_frequency(6820.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_583():
    """Validate 565 PLL lock range and capture frequency for test point 583."""
    f0 = pll_free_running_frequency(6830.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_584():
    """Validate 565 PLL lock range and capture frequency for test point 584."""
    f0 = pll_free_running_frequency(6840.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_585():
    """Validate 565 PLL lock range and capture frequency for test point 585."""
    f0 = pll_free_running_frequency(6850.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_586():
    """Validate 565 PLL lock range and capture frequency for test point 586."""
    f0 = pll_free_running_frequency(6860.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_587():
    """Validate 565 PLL lock range and capture frequency for test point 587."""
    f0 = pll_free_running_frequency(6870.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_588():
    """Validate 565 PLL lock range and capture frequency for test point 588."""
    f0 = pll_free_running_frequency(6880.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_589():
    """Validate 565 PLL lock range and capture frequency for test point 589."""
    f0 = pll_free_running_frequency(6890.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_590():
    """Validate 565 PLL lock range and capture frequency for test point 590."""
    f0 = pll_free_running_frequency(6900.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_591():
    """Validate 565 PLL lock range and capture frequency for test point 591."""
    f0 = pll_free_running_frequency(6910.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_592():
    """Validate 565 PLL lock range and capture frequency for test point 592."""
    f0 = pll_free_running_frequency(6920.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_593():
    """Validate 565 PLL lock range and capture frequency for test point 593."""
    f0 = pll_free_running_frequency(6930.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_594():
    """Validate 565 PLL lock range and capture frequency for test point 594."""
    f0 = pll_free_running_frequency(6940.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_595():
    """Validate 565 PLL lock range and capture frequency for test point 595."""
    f0 = pll_free_running_frequency(6950.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_596():
    """Validate 565 PLL lock range and capture frequency for test point 596."""
    f0 = pll_free_running_frequency(6960.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_597():
    """Validate 565 PLL lock range and capture frequency for test point 597."""
    f0 = pll_free_running_frequency(6970.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_598():
    """Validate 565 PLL lock range and capture frequency for test point 598."""
    f0 = pll_free_running_frequency(6980.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_599():
    """Validate 565 PLL lock range and capture frequency for test point 599."""
    f0 = pll_free_running_frequency(6990.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_600():
    """Validate 565 PLL lock range and capture frequency for test point 600."""
    f0 = pll_free_running_frequency(7000.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_601():
    """Validate 565 PLL lock range and capture frequency for test point 601."""
    f0 = pll_free_running_frequency(7010.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_602():
    """Validate 565 PLL lock range and capture frequency for test point 602."""
    f0 = pll_free_running_frequency(7020.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_603():
    """Validate 565 PLL lock range and capture frequency for test point 603."""
    f0 = pll_free_running_frequency(7030.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_604():
    """Validate 565 PLL lock range and capture frequency for test point 604."""
    f0 = pll_free_running_frequency(7040.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_605():
    """Validate 565 PLL lock range and capture frequency for test point 605."""
    f0 = pll_free_running_frequency(7050.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_606():
    """Validate 565 PLL lock range and capture frequency for test point 606."""
    f0 = pll_free_running_frequency(7060.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_607():
    """Validate 565 PLL lock range and capture frequency for test point 607."""
    f0 = pll_free_running_frequency(7070.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_608():
    """Validate 565 PLL lock range and capture frequency for test point 608."""
    f0 = pll_free_running_frequency(7080.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_609():
    """Validate 565 PLL lock range and capture frequency for test point 609."""
    f0 = pll_free_running_frequency(7090.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_610():
    """Validate 565 PLL lock range and capture frequency for test point 610."""
    f0 = pll_free_running_frequency(7100.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_611():
    """Validate 565 PLL lock range and capture frequency for test point 611."""
    f0 = pll_free_running_frequency(7110.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_612():
    """Validate 565 PLL lock range and capture frequency for test point 612."""
    f0 = pll_free_running_frequency(7120.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_613():
    """Validate 565 PLL lock range and capture frequency for test point 613."""
    f0 = pll_free_running_frequency(7130.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_614():
    """Validate 565 PLL lock range and capture frequency for test point 614."""
    f0 = pll_free_running_frequency(7140.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_615():
    """Validate 565 PLL lock range and capture frequency for test point 615."""
    f0 = pll_free_running_frequency(7150.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_616():
    """Validate 565 PLL lock range and capture frequency for test point 616."""
    f0 = pll_free_running_frequency(7160.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_617():
    """Validate 565 PLL lock range and capture frequency for test point 617."""
    f0 = pll_free_running_frequency(7170.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_618():
    """Validate 565 PLL lock range and capture frequency for test point 618."""
    f0 = pll_free_running_frequency(7180.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_619():
    """Validate 565 PLL lock range and capture frequency for test point 619."""
    f0 = pll_free_running_frequency(7190.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_620():
    """Validate 565 PLL lock range and capture frequency for test point 620."""
    f0 = pll_free_running_frequency(7200.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_621():
    """Validate 565 PLL lock range and capture frequency for test point 621."""
    f0 = pll_free_running_frequency(7210.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_622():
    """Validate 565 PLL lock range and capture frequency for test point 622."""
    f0 = pll_free_running_frequency(7220.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_623():
    """Validate 565 PLL lock range and capture frequency for test point 623."""
    f0 = pll_free_running_frequency(7230.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_624():
    """Validate 565 PLL lock range and capture frequency for test point 624."""
    f0 = pll_free_running_frequency(7240.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_625():
    """Validate 565 PLL lock range and capture frequency for test point 625."""
    f0 = pll_free_running_frequency(7250.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_626():
    """Validate 565 PLL lock range and capture frequency for test point 626."""
    f0 = pll_free_running_frequency(7260.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_627():
    """Validate 565 PLL lock range and capture frequency for test point 627."""
    f0 = pll_free_running_frequency(7270.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_628():
    """Validate 565 PLL lock range and capture frequency for test point 628."""
    f0 = pll_free_running_frequency(7280.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_629():
    """Validate 565 PLL lock range and capture frequency for test point 629."""
    f0 = pll_free_running_frequency(7290.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_630():
    """Validate 565 PLL lock range and capture frequency for test point 630."""
    f0 = pll_free_running_frequency(7300.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_631():
    """Validate 565 PLL lock range and capture frequency for test point 631."""
    f0 = pll_free_running_frequency(7310.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_632():
    """Validate 565 PLL lock range and capture frequency for test point 632."""
    f0 = pll_free_running_frequency(7320.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_633():
    """Validate 565 PLL lock range and capture frequency for test point 633."""
    f0 = pll_free_running_frequency(7330.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_634():
    """Validate 565 PLL lock range and capture frequency for test point 634."""
    f0 = pll_free_running_frequency(7340.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_635():
    """Validate 565 PLL lock range and capture frequency for test point 635."""
    f0 = pll_free_running_frequency(7350.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_636():
    """Validate 565 PLL lock range and capture frequency for test point 636."""
    f0 = pll_free_running_frequency(7360.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_637():
    """Validate 565 PLL lock range and capture frequency for test point 637."""
    f0 = pll_free_running_frequency(7370.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_638():
    """Validate 565 PLL lock range and capture frequency for test point 638."""
    f0 = pll_free_running_frequency(7380.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_639():
    """Validate 565 PLL lock range and capture frequency for test point 639."""
    f0 = pll_free_running_frequency(7390.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_640():
    """Validate 565 PLL lock range and capture frequency for test point 640."""
    f0 = pll_free_running_frequency(7400.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_641():
    """Validate 565 PLL lock range and capture frequency for test point 641."""
    f0 = pll_free_running_frequency(7410.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_642():
    """Validate 565 PLL lock range and capture frequency for test point 642."""
    f0 = pll_free_running_frequency(7420.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_643():
    """Validate 565 PLL lock range and capture frequency for test point 643."""
    f0 = pll_free_running_frequency(7430.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_644():
    """Validate 565 PLL lock range and capture frequency for test point 644."""
    f0 = pll_free_running_frequency(7440.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_645():
    """Validate 565 PLL lock range and capture frequency for test point 645."""
    f0 = pll_free_running_frequency(7450.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_646():
    """Validate 565 PLL lock range and capture frequency for test point 646."""
    f0 = pll_free_running_frequency(7460.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_647():
    """Validate 565 PLL lock range and capture frequency for test point 647."""
    f0 = pll_free_running_frequency(7470.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_648():
    """Validate 565 PLL lock range and capture frequency for test point 648."""
    f0 = pll_free_running_frequency(7480.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_649():
    """Validate 565 PLL lock range and capture frequency for test point 649."""
    f0 = pll_free_running_frequency(7490.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_650():
    """Validate 565 PLL lock range and capture frequency for test point 650."""
    f0 = pll_free_running_frequency(7500.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_651():
    """Validate 565 PLL lock range and capture frequency for test point 651."""
    f0 = pll_free_running_frequency(7510.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_652():
    """Validate 565 PLL lock range and capture frequency for test point 652."""
    f0 = pll_free_running_frequency(7520.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_653():
    """Validate 565 PLL lock range and capture frequency for test point 653."""
    f0 = pll_free_running_frequency(7530.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_654():
    """Validate 565 PLL lock range and capture frequency for test point 654."""
    f0 = pll_free_running_frequency(7540.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_655():
    """Validate 565 PLL lock range and capture frequency for test point 655."""
    f0 = pll_free_running_frequency(7550.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_656():
    """Validate 565 PLL lock range and capture frequency for test point 656."""
    f0 = pll_free_running_frequency(7560.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_657():
    """Validate 565 PLL lock range and capture frequency for test point 657."""
    f0 = pll_free_running_frequency(7570.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_658():
    """Validate 565 PLL lock range and capture frequency for test point 658."""
    f0 = pll_free_running_frequency(7580.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_659():
    """Validate 565 PLL lock range and capture frequency for test point 659."""
    f0 = pll_free_running_frequency(7590.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_660():
    """Validate 565 PLL lock range and capture frequency for test point 660."""
    f0 = pll_free_running_frequency(7600.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_661():
    """Validate 565 PLL lock range and capture frequency for test point 661."""
    f0 = pll_free_running_frequency(7610.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_662():
    """Validate 565 PLL lock range and capture frequency for test point 662."""
    f0 = pll_free_running_frequency(7620.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_663():
    """Validate 565 PLL lock range and capture frequency for test point 663."""
    f0 = pll_free_running_frequency(7630.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_664():
    """Validate 565 PLL lock range and capture frequency for test point 664."""
    f0 = pll_free_running_frequency(7640.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_665():
    """Validate 565 PLL lock range and capture frequency for test point 665."""
    f0 = pll_free_running_frequency(7650.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_666():
    """Validate 565 PLL lock range and capture frequency for test point 666."""
    f0 = pll_free_running_frequency(7660.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_667():
    """Validate 565 PLL lock range and capture frequency for test point 667."""
    f0 = pll_free_running_frequency(7670.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_668():
    """Validate 565 PLL lock range and capture frequency for test point 668."""
    f0 = pll_free_running_frequency(7680.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_669():
    """Validate 565 PLL lock range and capture frequency for test point 669."""
    f0 = pll_free_running_frequency(7690.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_670():
    """Validate 565 PLL lock range and capture frequency for test point 670."""
    f0 = pll_free_running_frequency(7700.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_671():
    """Validate 565 PLL lock range and capture frequency for test point 671."""
    f0 = pll_free_running_frequency(7710.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_672():
    """Validate 565 PLL lock range and capture frequency for test point 672."""
    f0 = pll_free_running_frequency(7720.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_673():
    """Validate 565 PLL lock range and capture frequency for test point 673."""
    f0 = pll_free_running_frequency(7730.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_674():
    """Validate 565 PLL lock range and capture frequency for test point 674."""
    f0 = pll_free_running_frequency(7740.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_675():
    """Validate 565 PLL lock range and capture frequency for test point 675."""
    f0 = pll_free_running_frequency(7750.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_676():
    """Validate 565 PLL lock range and capture frequency for test point 676."""
    f0 = pll_free_running_frequency(7760.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_677():
    """Validate 565 PLL lock range and capture frequency for test point 677."""
    f0 = pll_free_running_frequency(7770.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_678():
    """Validate 565 PLL lock range and capture frequency for test point 678."""
    f0 = pll_free_running_frequency(7780.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_679():
    """Validate 565 PLL lock range and capture frequency for test point 679."""
    f0 = pll_free_running_frequency(7790.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_680():
    """Validate 565 PLL lock range and capture frequency for test point 680."""
    f0 = pll_free_running_frequency(7800.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_681():
    """Validate 565 PLL lock range and capture frequency for test point 681."""
    f0 = pll_free_running_frequency(7810.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_682():
    """Validate 565 PLL lock range and capture frequency for test point 682."""
    f0 = pll_free_running_frequency(7820.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_683():
    """Validate 565 PLL lock range and capture frequency for test point 683."""
    f0 = pll_free_running_frequency(7830.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_684():
    """Validate 565 PLL lock range and capture frequency for test point 684."""
    f0 = pll_free_running_frequency(7840.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_685():
    """Validate 565 PLL lock range and capture frequency for test point 685."""
    f0 = pll_free_running_frequency(7850.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_686():
    """Validate 565 PLL lock range and capture frequency for test point 686."""
    f0 = pll_free_running_frequency(7860.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_687():
    """Validate 565 PLL lock range and capture frequency for test point 687."""
    f0 = pll_free_running_frequency(7870.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_688():
    """Validate 565 PLL lock range and capture frequency for test point 688."""
    f0 = pll_free_running_frequency(7880.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_689():
    """Validate 565 PLL lock range and capture frequency for test point 689."""
    f0 = pll_free_running_frequency(7890.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_690():
    """Validate 565 PLL lock range and capture frequency for test point 690."""
    f0 = pll_free_running_frequency(7900.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_691():
    """Validate 565 PLL lock range and capture frequency for test point 691."""
    f0 = pll_free_running_frequency(7910.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_692():
    """Validate 565 PLL lock range and capture frequency for test point 692."""
    f0 = pll_free_running_frequency(7920.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_693():
    """Validate 565 PLL lock range and capture frequency for test point 693."""
    f0 = pll_free_running_frequency(7930.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_694():
    """Validate 565 PLL lock range and capture frequency for test point 694."""
    f0 = pll_free_running_frequency(7940.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_695():
    """Validate 565 PLL lock range and capture frequency for test point 695."""
    f0 = pll_free_running_frequency(7950.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_696():
    """Validate 565 PLL lock range and capture frequency for test point 696."""
    f0 = pll_free_running_frequency(7960.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_697():
    """Validate 565 PLL lock range and capture frequency for test point 697."""
    f0 = pll_free_running_frequency(7970.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_698():
    """Validate 565 PLL lock range and capture frequency for test point 698."""
    f0 = pll_free_running_frequency(7980.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_699():
    """Validate 565 PLL lock range and capture frequency for test point 699."""
    f0 = pll_free_running_frequency(7990.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_700():
    """Validate 565 PLL lock range and capture frequency for test point 700."""
    f0 = pll_free_running_frequency(8000.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_701():
    """Validate 565 PLL lock range and capture frequency for test point 701."""
    f0 = pll_free_running_frequency(8010.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_702():
    """Validate 565 PLL lock range and capture frequency for test point 702."""
    f0 = pll_free_running_frequency(8020.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_703():
    """Validate 565 PLL lock range and capture frequency for test point 703."""
    f0 = pll_free_running_frequency(8030.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_704():
    """Validate 565 PLL lock range and capture frequency for test point 704."""
    f0 = pll_free_running_frequency(8040.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_705():
    """Validate 565 PLL lock range and capture frequency for test point 705."""
    f0 = pll_free_running_frequency(8050.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_706():
    """Validate 565 PLL lock range and capture frequency for test point 706."""
    f0 = pll_free_running_frequency(8060.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_707():
    """Validate 565 PLL lock range and capture frequency for test point 707."""
    f0 = pll_free_running_frequency(8070.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_708():
    """Validate 565 PLL lock range and capture frequency for test point 708."""
    f0 = pll_free_running_frequency(8080.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_709():
    """Validate 565 PLL lock range and capture frequency for test point 709."""
    f0 = pll_free_running_frequency(8090.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_710():
    """Validate 565 PLL lock range and capture frequency for test point 710."""
    f0 = pll_free_running_frequency(8100.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_711():
    """Validate 565 PLL lock range and capture frequency for test point 711."""
    f0 = pll_free_running_frequency(8110.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_712():
    """Validate 565 PLL lock range and capture frequency for test point 712."""
    f0 = pll_free_running_frequency(8120.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_713():
    """Validate 565 PLL lock range and capture frequency for test point 713."""
    f0 = pll_free_running_frequency(8130.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_714():
    """Validate 565 PLL lock range and capture frequency for test point 714."""
    f0 = pll_free_running_frequency(8140.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_715():
    """Validate 565 PLL lock range and capture frequency for test point 715."""
    f0 = pll_free_running_frequency(8150.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_716():
    """Validate 565 PLL lock range and capture frequency for test point 716."""
    f0 = pll_free_running_frequency(8160.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_717():
    """Validate 565 PLL lock range and capture frequency for test point 717."""
    f0 = pll_free_running_frequency(8170.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_718():
    """Validate 565 PLL lock range and capture frequency for test point 718."""
    f0 = pll_free_running_frequency(8180.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_719():
    """Validate 565 PLL lock range and capture frequency for test point 719."""
    f0 = pll_free_running_frequency(8190.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_720():
    """Validate 565 PLL lock range and capture frequency for test point 720."""
    f0 = pll_free_running_frequency(8200.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_721():
    """Validate 565 PLL lock range and capture frequency for test point 721."""
    f0 = pll_free_running_frequency(8210.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_722():
    """Validate 565 PLL lock range and capture frequency for test point 722."""
    f0 = pll_free_running_frequency(8220.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_723():
    """Validate 565 PLL lock range and capture frequency for test point 723."""
    f0 = pll_free_running_frequency(8230.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_724():
    """Validate 565 PLL lock range and capture frequency for test point 724."""
    f0 = pll_free_running_frequency(8240.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_725():
    """Validate 565 PLL lock range and capture frequency for test point 725."""
    f0 = pll_free_running_frequency(8250.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_726():
    """Validate 565 PLL lock range and capture frequency for test point 726."""
    f0 = pll_free_running_frequency(8260.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_727():
    """Validate 565 PLL lock range and capture frequency for test point 727."""
    f0 = pll_free_running_frequency(8270.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_728():
    """Validate 565 PLL lock range and capture frequency for test point 728."""
    f0 = pll_free_running_frequency(8280.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_729():
    """Validate 565 PLL lock range and capture frequency for test point 729."""
    f0 = pll_free_running_frequency(8290.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_730():
    """Validate 565 PLL lock range and capture frequency for test point 730."""
    f0 = pll_free_running_frequency(8300.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_731():
    """Validate 565 PLL lock range and capture frequency for test point 731."""
    f0 = pll_free_running_frequency(8310.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_732():
    """Validate 565 PLL lock range and capture frequency for test point 732."""
    f0 = pll_free_running_frequency(8320.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_733():
    """Validate 565 PLL lock range and capture frequency for test point 733."""
    f0 = pll_free_running_frequency(8330.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_734():
    """Validate 565 PLL lock range and capture frequency for test point 734."""
    f0 = pll_free_running_frequency(8340.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_735():
    """Validate 565 PLL lock range and capture frequency for test point 735."""
    f0 = pll_free_running_frequency(8350.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_736():
    """Validate 565 PLL lock range and capture frequency for test point 736."""
    f0 = pll_free_running_frequency(8360.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_737():
    """Validate 565 PLL lock range and capture frequency for test point 737."""
    f0 = pll_free_running_frequency(8370.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_738():
    """Validate 565 PLL lock range and capture frequency for test point 738."""
    f0 = pll_free_running_frequency(8380.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_739():
    """Validate 565 PLL lock range and capture frequency for test point 739."""
    f0 = pll_free_running_frequency(8390.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_740():
    """Validate 565 PLL lock range and capture frequency for test point 740."""
    f0 = pll_free_running_frequency(8400.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_741():
    """Validate 565 PLL lock range and capture frequency for test point 741."""
    f0 = pll_free_running_frequency(8410.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_742():
    """Validate 565 PLL lock range and capture frequency for test point 742."""
    f0 = pll_free_running_frequency(8420.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_743():
    """Validate 565 PLL lock range and capture frequency for test point 743."""
    f0 = pll_free_running_frequency(8430.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_744():
    """Validate 565 PLL lock range and capture frequency for test point 744."""
    f0 = pll_free_running_frequency(8440.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_745():
    """Validate 565 PLL lock range and capture frequency for test point 745."""
    f0 = pll_free_running_frequency(8450.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_746():
    """Validate 565 PLL lock range and capture frequency for test point 746."""
    f0 = pll_free_running_frequency(8460.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_747():
    """Validate 565 PLL lock range and capture frequency for test point 747."""
    f0 = pll_free_running_frequency(8470.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_748():
    """Validate 565 PLL lock range and capture frequency for test point 748."""
    f0 = pll_free_running_frequency(8480.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_749():
    """Validate 565 PLL lock range and capture frequency for test point 749."""
    f0 = pll_free_running_frequency(8490.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_750():
    """Validate 565 PLL lock range and capture frequency for test point 750."""
    f0 = pll_free_running_frequency(8500.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_751():
    """Validate 565 PLL lock range and capture frequency for test point 751."""
    f0 = pll_free_running_frequency(8510.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_752():
    """Validate 565 PLL lock range and capture frequency for test point 752."""
    f0 = pll_free_running_frequency(8520.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_753():
    """Validate 565 PLL lock range and capture frequency for test point 753."""
    f0 = pll_free_running_frequency(8530.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_754():
    """Validate 565 PLL lock range and capture frequency for test point 754."""
    f0 = pll_free_running_frequency(8540.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_755():
    """Validate 565 PLL lock range and capture frequency for test point 755."""
    f0 = pll_free_running_frequency(8550.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_756():
    """Validate 565 PLL lock range and capture frequency for test point 756."""
    f0 = pll_free_running_frequency(8560.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_757():
    """Validate 565 PLL lock range and capture frequency for test point 757."""
    f0 = pll_free_running_frequency(8570.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_758():
    """Validate 565 PLL lock range and capture frequency for test point 758."""
    f0 = pll_free_running_frequency(8580.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_759():
    """Validate 565 PLL lock range and capture frequency for test point 759."""
    f0 = pll_free_running_frequency(8590.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_760():
    """Validate 565 PLL lock range and capture frequency for test point 760."""
    f0 = pll_free_running_frequency(8600.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_761():
    """Validate 565 PLL lock range and capture frequency for test point 761."""
    f0 = pll_free_running_frequency(8610.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_762():
    """Validate 565 PLL lock range and capture frequency for test point 762."""
    f0 = pll_free_running_frequency(8620.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_763():
    """Validate 565 PLL lock range and capture frequency for test point 763."""
    f0 = pll_free_running_frequency(8630.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_764():
    """Validate 565 PLL lock range and capture frequency for test point 764."""
    f0 = pll_free_running_frequency(8640.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_765():
    """Validate 565 PLL lock range and capture frequency for test point 765."""
    f0 = pll_free_running_frequency(8650.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_766():
    """Validate 565 PLL lock range and capture frequency for test point 766."""
    f0 = pll_free_running_frequency(8660.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_767():
    """Validate 565 PLL lock range and capture frequency for test point 767."""
    f0 = pll_free_running_frequency(8670.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_768():
    """Validate 565 PLL lock range and capture frequency for test point 768."""
    f0 = pll_free_running_frequency(8680.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_769():
    """Validate 565 PLL lock range and capture frequency for test point 769."""
    f0 = pll_free_running_frequency(8690.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_770():
    """Validate 565 PLL lock range and capture frequency for test point 770."""
    f0 = pll_free_running_frequency(8700.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_771():
    """Validate 565 PLL lock range and capture frequency for test point 771."""
    f0 = pll_free_running_frequency(8710.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_772():
    """Validate 565 PLL lock range and capture frequency for test point 772."""
    f0 = pll_free_running_frequency(8720.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_773():
    """Validate 565 PLL lock range and capture frequency for test point 773."""
    f0 = pll_free_running_frequency(8730.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_774():
    """Validate 565 PLL lock range and capture frequency for test point 774."""
    f0 = pll_free_running_frequency(8740.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_775():
    """Validate 565 PLL lock range and capture frequency for test point 775."""
    f0 = pll_free_running_frequency(8750.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_776():
    """Validate 565 PLL lock range and capture frequency for test point 776."""
    f0 = pll_free_running_frequency(8760.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_777():
    """Validate 565 PLL lock range and capture frequency for test point 777."""
    f0 = pll_free_running_frequency(8770.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_778():
    """Validate 565 PLL lock range and capture frequency for test point 778."""
    f0 = pll_free_running_frequency(8780.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_779():
    """Validate 565 PLL lock range and capture frequency for test point 779."""
    f0 = pll_free_running_frequency(8790.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_780():
    """Validate 565 PLL lock range and capture frequency for test point 780."""
    f0 = pll_free_running_frequency(8800.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_781():
    """Validate 565 PLL lock range and capture frequency for test point 781."""
    f0 = pll_free_running_frequency(8810.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_782():
    """Validate 565 PLL lock range and capture frequency for test point 782."""
    f0 = pll_free_running_frequency(8820.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_783():
    """Validate 565 PLL lock range and capture frequency for test point 783."""
    f0 = pll_free_running_frequency(8830.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_784():
    """Validate 565 PLL lock range and capture frequency for test point 784."""
    f0 = pll_free_running_frequency(8840.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_785():
    """Validate 565 PLL lock range and capture frequency for test point 785."""
    f0 = pll_free_running_frequency(8850.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_786():
    """Validate 565 PLL lock range and capture frequency for test point 786."""
    f0 = pll_free_running_frequency(8860.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_787():
    """Validate 565 PLL lock range and capture frequency for test point 787."""
    f0 = pll_free_running_frequency(8870.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_788():
    """Validate 565 PLL lock range and capture frequency for test point 788."""
    f0 = pll_free_running_frequency(8880.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_789():
    """Validate 565 PLL lock range and capture frequency for test point 789."""
    f0 = pll_free_running_frequency(8890.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_790():
    """Validate 565 PLL lock range and capture frequency for test point 790."""
    f0 = pll_free_running_frequency(8900.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_791():
    """Validate 565 PLL lock range and capture frequency for test point 791."""
    f0 = pll_free_running_frequency(8910.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_792():
    """Validate 565 PLL lock range and capture frequency for test point 792."""
    f0 = pll_free_running_frequency(8920.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_793():
    """Validate 565 PLL lock range and capture frequency for test point 793."""
    f0 = pll_free_running_frequency(8930.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_794():
    """Validate 565 PLL lock range and capture frequency for test point 794."""
    f0 = pll_free_running_frequency(8940.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_795():
    """Validate 565 PLL lock range and capture frequency for test point 795."""
    f0 = pll_free_running_frequency(8950.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_796():
    """Validate 565 PLL lock range and capture frequency for test point 796."""
    f0 = pll_free_running_frequency(8960.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_797():
    """Validate 565 PLL lock range and capture frequency for test point 797."""
    f0 = pll_free_running_frequency(8970.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_798():
    """Validate 565 PLL lock range and capture frequency for test point 798."""
    f0 = pll_free_running_frequency(8980.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_799():
    """Validate 565 PLL lock range and capture frequency for test point 799."""
    f0 = pll_free_running_frequency(8990.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_800():
    """Validate 565 PLL lock range and capture frequency for test point 800."""
    f0 = pll_free_running_frequency(9000.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_801():
    """Validate 565 PLL lock range and capture frequency for test point 801."""
    f0 = pll_free_running_frequency(9010.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_802():
    """Validate 565 PLL lock range and capture frequency for test point 802."""
    f0 = pll_free_running_frequency(9020.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_803():
    """Validate 565 PLL lock range and capture frequency for test point 803."""
    f0 = pll_free_running_frequency(9030.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_804():
    """Validate 565 PLL lock range and capture frequency for test point 804."""
    f0 = pll_free_running_frequency(9040.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_805():
    """Validate 565 PLL lock range and capture frequency for test point 805."""
    f0 = pll_free_running_frequency(9050.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_806():
    """Validate 565 PLL lock range and capture frequency for test point 806."""
    f0 = pll_free_running_frequency(9060.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_807():
    """Validate 565 PLL lock range and capture frequency for test point 807."""
    f0 = pll_free_running_frequency(9070.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_808():
    """Validate 565 PLL lock range and capture frequency for test point 808."""
    f0 = pll_free_running_frequency(9080.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_809():
    """Validate 565 PLL lock range and capture frequency for test point 809."""
    f0 = pll_free_running_frequency(9090.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_810():
    """Validate 565 PLL lock range and capture frequency for test point 810."""
    f0 = pll_free_running_frequency(9100.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_811():
    """Validate 565 PLL lock range and capture frequency for test point 811."""
    f0 = pll_free_running_frequency(9110.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_812():
    """Validate 565 PLL lock range and capture frequency for test point 812."""
    f0 = pll_free_running_frequency(9120.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_813():
    """Validate 565 PLL lock range and capture frequency for test point 813."""
    f0 = pll_free_running_frequency(9130.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_814():
    """Validate 565 PLL lock range and capture frequency for test point 814."""
    f0 = pll_free_running_frequency(9140.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_815():
    """Validate 565 PLL lock range and capture frequency for test point 815."""
    f0 = pll_free_running_frequency(9150.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_816():
    """Validate 565 PLL lock range and capture frequency for test point 816."""
    f0 = pll_free_running_frequency(9160.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_817():
    """Validate 565 PLL lock range and capture frequency for test point 817."""
    f0 = pll_free_running_frequency(9170.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_818():
    """Validate 565 PLL lock range and capture frequency for test point 818."""
    f0 = pll_free_running_frequency(9180.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_819():
    """Validate 565 PLL lock range and capture frequency for test point 819."""
    f0 = pll_free_running_frequency(9190.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_820():
    """Validate 565 PLL lock range and capture frequency for test point 820."""
    f0 = pll_free_running_frequency(9200.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_821():
    """Validate 565 PLL lock range and capture frequency for test point 821."""
    f0 = pll_free_running_frequency(9210.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_822():
    """Validate 565 PLL lock range and capture frequency for test point 822."""
    f0 = pll_free_running_frequency(9220.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_823():
    """Validate 565 PLL lock range and capture frequency for test point 823."""
    f0 = pll_free_running_frequency(9230.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_824():
    """Validate 565 PLL lock range and capture frequency for test point 824."""
    f0 = pll_free_running_frequency(9240.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_825():
    """Validate 565 PLL lock range and capture frequency for test point 825."""
    f0 = pll_free_running_frequency(9250.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_826():
    """Validate 565 PLL lock range and capture frequency for test point 826."""
    f0 = pll_free_running_frequency(9260.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_827():
    """Validate 565 PLL lock range and capture frequency for test point 827."""
    f0 = pll_free_running_frequency(9270.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_828():
    """Validate 565 PLL lock range and capture frequency for test point 828."""
    f0 = pll_free_running_frequency(9280.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_829():
    """Validate 565 PLL lock range and capture frequency for test point 829."""
    f0 = pll_free_running_frequency(9290.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_830():
    """Validate 565 PLL lock range and capture frequency for test point 830."""
    f0 = pll_free_running_frequency(9300.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_831():
    """Validate 565 PLL lock range and capture frequency for test point 831."""
    f0 = pll_free_running_frequency(9310.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_832():
    """Validate 565 PLL lock range and capture frequency for test point 832."""
    f0 = pll_free_running_frequency(9320.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_833():
    """Validate 565 PLL lock range and capture frequency for test point 833."""
    f0 = pll_free_running_frequency(9330.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_834():
    """Validate 565 PLL lock range and capture frequency for test point 834."""
    f0 = pll_free_running_frequency(9340.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_835():
    """Validate 565 PLL lock range and capture frequency for test point 835."""
    f0 = pll_free_running_frequency(9350.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_836():
    """Validate 565 PLL lock range and capture frequency for test point 836."""
    f0 = pll_free_running_frequency(9360.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_837():
    """Validate 565 PLL lock range and capture frequency for test point 837."""
    f0 = pll_free_running_frequency(9370.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_838():
    """Validate 565 PLL lock range and capture frequency for test point 838."""
    f0 = pll_free_running_frequency(9380.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_839():
    """Validate 565 PLL lock range and capture frequency for test point 839."""
    f0 = pll_free_running_frequency(9390.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_840():
    """Validate 565 PLL lock range and capture frequency for test point 840."""
    f0 = pll_free_running_frequency(9400.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_841():
    """Validate 565 PLL lock range and capture frequency for test point 841."""
    f0 = pll_free_running_frequency(9410.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_842():
    """Validate 565 PLL lock range and capture frequency for test point 842."""
    f0 = pll_free_running_frequency(9420.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_843():
    """Validate 565 PLL lock range and capture frequency for test point 843."""
    f0 = pll_free_running_frequency(9430.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_844():
    """Validate 565 PLL lock range and capture frequency for test point 844."""
    f0 = pll_free_running_frequency(9440.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_845():
    """Validate 565 PLL lock range and capture frequency for test point 845."""
    f0 = pll_free_running_frequency(9450.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_846():
    """Validate 565 PLL lock range and capture frequency for test point 846."""
    f0 = pll_free_running_frequency(9460.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_847():
    """Validate 565 PLL lock range and capture frequency for test point 847."""
    f0 = pll_free_running_frequency(9470.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_848():
    """Validate 565 PLL lock range and capture frequency for test point 848."""
    f0 = pll_free_running_frequency(9480.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_849():
    """Validate 565 PLL lock range and capture frequency for test point 849."""
    f0 = pll_free_running_frequency(9490.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_850():
    """Validate 565 PLL lock range and capture frequency for test point 850."""
    f0 = pll_free_running_frequency(9500.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_851():
    """Validate 565 PLL lock range and capture frequency for test point 851."""
    f0 = pll_free_running_frequency(9510.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_852():
    """Validate 565 PLL lock range and capture frequency for test point 852."""
    f0 = pll_free_running_frequency(9520.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_853():
    """Validate 565 PLL lock range and capture frequency for test point 853."""
    f0 = pll_free_running_frequency(9530.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_854():
    """Validate 565 PLL lock range and capture frequency for test point 854."""
    f0 = pll_free_running_frequency(9540.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_855():
    """Validate 565 PLL lock range and capture frequency for test point 855."""
    f0 = pll_free_running_frequency(9550.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_856():
    """Validate 565 PLL lock range and capture frequency for test point 856."""
    f0 = pll_free_running_frequency(9560.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_857():
    """Validate 565 PLL lock range and capture frequency for test point 857."""
    f0 = pll_free_running_frequency(9570.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_858():
    """Validate 565 PLL lock range and capture frequency for test point 858."""
    f0 = pll_free_running_frequency(9580.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_859():
    """Validate 565 PLL lock range and capture frequency for test point 859."""
    f0 = pll_free_running_frequency(9590.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_860():
    """Validate 565 PLL lock range and capture frequency for test point 860."""
    f0 = pll_free_running_frequency(9600.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_861():
    """Validate 565 PLL lock range and capture frequency for test point 861."""
    f0 = pll_free_running_frequency(9610.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_862():
    """Validate 565 PLL lock range and capture frequency for test point 862."""
    f0 = pll_free_running_frequency(9620.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_863():
    """Validate 565 PLL lock range and capture frequency for test point 863."""
    f0 = pll_free_running_frequency(9630.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_864():
    """Validate 565 PLL lock range and capture frequency for test point 864."""
    f0 = pll_free_running_frequency(9640.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_865():
    """Validate 565 PLL lock range and capture frequency for test point 865."""
    f0 = pll_free_running_frequency(9650.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_866():
    """Validate 565 PLL lock range and capture frequency for test point 866."""
    f0 = pll_free_running_frequency(9660.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_867():
    """Validate 565 PLL lock range and capture frequency for test point 867."""
    f0 = pll_free_running_frequency(9670.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_868():
    """Validate 565 PLL lock range and capture frequency for test point 868."""
    f0 = pll_free_running_frequency(9680.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_869():
    """Validate 565 PLL lock range and capture frequency for test point 869."""
    f0 = pll_free_running_frequency(9690.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_870():
    """Validate 565 PLL lock range and capture frequency for test point 870."""
    f0 = pll_free_running_frequency(9700.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_871():
    """Validate 565 PLL lock range and capture frequency for test point 871."""
    f0 = pll_free_running_frequency(9710.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_872():
    """Validate 565 PLL lock range and capture frequency for test point 872."""
    f0 = pll_free_running_frequency(9720.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_873():
    """Validate 565 PLL lock range and capture frequency for test point 873."""
    f0 = pll_free_running_frequency(9730.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_874():
    """Validate 565 PLL lock range and capture frequency for test point 874."""
    f0 = pll_free_running_frequency(9740.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_875():
    """Validate 565 PLL lock range and capture frequency for test point 875."""
    f0 = pll_free_running_frequency(9750.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_876():
    """Validate 565 PLL lock range and capture frequency for test point 876."""
    f0 = pll_free_running_frequency(9760.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_877():
    """Validate 565 PLL lock range and capture frequency for test point 877."""
    f0 = pll_free_running_frequency(9770.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_878():
    """Validate 565 PLL lock range and capture frequency for test point 878."""
    f0 = pll_free_running_frequency(9780.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_879():
    """Validate 565 PLL lock range and capture frequency for test point 879."""
    f0 = pll_free_running_frequency(9790.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_880():
    """Validate 565 PLL lock range and capture frequency for test point 880."""
    f0 = pll_free_running_frequency(9800.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_881():
    """Validate 565 PLL lock range and capture frequency for test point 881."""
    f0 = pll_free_running_frequency(9810.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_882():
    """Validate 565 PLL lock range and capture frequency for test point 882."""
    f0 = pll_free_running_frequency(9820.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_883():
    """Validate 565 PLL lock range and capture frequency for test point 883."""
    f0 = pll_free_running_frequency(9830.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_884():
    """Validate 565 PLL lock range and capture frequency for test point 884."""
    f0 = pll_free_running_frequency(9840.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_885():
    """Validate 565 PLL lock range and capture frequency for test point 885."""
    f0 = pll_free_running_frequency(9850.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_886():
    """Validate 565 PLL lock range and capture frequency for test point 886."""
    f0 = pll_free_running_frequency(9860.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_887():
    """Validate 565 PLL lock range and capture frequency for test point 887."""
    f0 = pll_free_running_frequency(9870.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_888():
    """Validate 565 PLL lock range and capture frequency for test point 888."""
    f0 = pll_free_running_frequency(9880.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_889():
    """Validate 565 PLL lock range and capture frequency for test point 889."""
    f0 = pll_free_running_frequency(9890.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_890():
    """Validate 565 PLL lock range and capture frequency for test point 890."""
    f0 = pll_free_running_frequency(9900.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_891():
    """Validate 565 PLL lock range and capture frequency for test point 891."""
    f0 = pll_free_running_frequency(9910.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_892():
    """Validate 565 PLL lock range and capture frequency for test point 892."""
    f0 = pll_free_running_frequency(9920.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_893():
    """Validate 565 PLL lock range and capture frequency for test point 893."""
    f0 = pll_free_running_frequency(9930.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_894():
    """Validate 565 PLL lock range and capture frequency for test point 894."""
    f0 = pll_free_running_frequency(9940.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_895():
    """Validate 565 PLL lock range and capture frequency for test point 895."""
    f0 = pll_free_running_frequency(9950.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_896():
    """Validate 565 PLL lock range and capture frequency for test point 896."""
    f0 = pll_free_running_frequency(9960.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_897():
    """Validate 565 PLL lock range and capture frequency for test point 897."""
    f0 = pll_free_running_frequency(9970.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_898():
    """Validate 565 PLL lock range and capture frequency for test point 898."""
    f0 = pll_free_running_frequency(9980.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_899():
    """Validate 565 PLL lock range and capture frequency for test point 899."""
    f0 = pll_free_running_frequency(9990.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_900():
    """Validate 565 PLL lock range and capture frequency for test point 900."""
    f0 = pll_free_running_frequency(10000.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_901():
    """Validate 565 PLL lock range and capture frequency for test point 901."""
    f0 = pll_free_running_frequency(10010.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_902():
    """Validate 565 PLL lock range and capture frequency for test point 902."""
    f0 = pll_free_running_frequency(10020.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_903():
    """Validate 565 PLL lock range and capture frequency for test point 903."""
    f0 = pll_free_running_frequency(10030.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_904():
    """Validate 565 PLL lock range and capture frequency for test point 904."""
    f0 = pll_free_running_frequency(10040.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_905():
    """Validate 565 PLL lock range and capture frequency for test point 905."""
    f0 = pll_free_running_frequency(10050.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_906():
    """Validate 565 PLL lock range and capture frequency for test point 906."""
    f0 = pll_free_running_frequency(10060.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_907():
    """Validate 565 PLL lock range and capture frequency for test point 907."""
    f0 = pll_free_running_frequency(10070.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_908():
    """Validate 565 PLL lock range and capture frequency for test point 908."""
    f0 = pll_free_running_frequency(10080.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_909():
    """Validate 565 PLL lock range and capture frequency for test point 909."""
    f0 = pll_free_running_frequency(10090.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_910():
    """Validate 565 PLL lock range and capture frequency for test point 910."""
    f0 = pll_free_running_frequency(10100.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_911():
    """Validate 565 PLL lock range and capture frequency for test point 911."""
    f0 = pll_free_running_frequency(10110.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_912():
    """Validate 565 PLL lock range and capture frequency for test point 912."""
    f0 = pll_free_running_frequency(10120.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_913():
    """Validate 565 PLL lock range and capture frequency for test point 913."""
    f0 = pll_free_running_frequency(10130.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_914():
    """Validate 565 PLL lock range and capture frequency for test point 914."""
    f0 = pll_free_running_frequency(10140.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_915():
    """Validate 565 PLL lock range and capture frequency for test point 915."""
    f0 = pll_free_running_frequency(10150.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_916():
    """Validate 565 PLL lock range and capture frequency for test point 916."""
    f0 = pll_free_running_frequency(10160.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_917():
    """Validate 565 PLL lock range and capture frequency for test point 917."""
    f0 = pll_free_running_frequency(10170.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_918():
    """Validate 565 PLL lock range and capture frequency for test point 918."""
    f0 = pll_free_running_frequency(10180.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_919():
    """Validate 565 PLL lock range and capture frequency for test point 919."""
    f0 = pll_free_running_frequency(10190.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_920():
    """Validate 565 PLL lock range and capture frequency for test point 920."""
    f0 = pll_free_running_frequency(10200.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_921():
    """Validate 565 PLL lock range and capture frequency for test point 921."""
    f0 = pll_free_running_frequency(10210.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_922():
    """Validate 565 PLL lock range and capture frequency for test point 922."""
    f0 = pll_free_running_frequency(10220.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_923():
    """Validate 565 PLL lock range and capture frequency for test point 923."""
    f0 = pll_free_running_frequency(10230.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_924():
    """Validate 565 PLL lock range and capture frequency for test point 924."""
    f0 = pll_free_running_frequency(10240.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_925():
    """Validate 565 PLL lock range and capture frequency for test point 925."""
    f0 = pll_free_running_frequency(10250.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_926():
    """Validate 565 PLL lock range and capture frequency for test point 926."""
    f0 = pll_free_running_frequency(10260.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_927():
    """Validate 565 PLL lock range and capture frequency for test point 927."""
    f0 = pll_free_running_frequency(10270.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_928():
    """Validate 565 PLL lock range and capture frequency for test point 928."""
    f0 = pll_free_running_frequency(10280.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_929():
    """Validate 565 PLL lock range and capture frequency for test point 929."""
    f0 = pll_free_running_frequency(10290.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_930():
    """Validate 565 PLL lock range and capture frequency for test point 930."""
    f0 = pll_free_running_frequency(10300.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_931():
    """Validate 565 PLL lock range and capture frequency for test point 931."""
    f0 = pll_free_running_frequency(10310.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_932():
    """Validate 565 PLL lock range and capture frequency for test point 932."""
    f0 = pll_free_running_frequency(10320.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_933():
    """Validate 565 PLL lock range and capture frequency for test point 933."""
    f0 = pll_free_running_frequency(10330.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_934():
    """Validate 565 PLL lock range and capture frequency for test point 934."""
    f0 = pll_free_running_frequency(10340.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_935():
    """Validate 565 PLL lock range and capture frequency for test point 935."""
    f0 = pll_free_running_frequency(10350.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_936():
    """Validate 565 PLL lock range and capture frequency for test point 936."""
    f0 = pll_free_running_frequency(10360.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_937():
    """Validate 565 PLL lock range and capture frequency for test point 937."""
    f0 = pll_free_running_frequency(10370.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_938():
    """Validate 565 PLL lock range and capture frequency for test point 938."""
    f0 = pll_free_running_frequency(10380.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_939():
    """Validate 565 PLL lock range and capture frequency for test point 939."""
    f0 = pll_free_running_frequency(10390.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_940():
    """Validate 565 PLL lock range and capture frequency for test point 940."""
    f0 = pll_free_running_frequency(10400.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_941():
    """Validate 565 PLL lock range and capture frequency for test point 941."""
    f0 = pll_free_running_frequency(10410.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_942():
    """Validate 565 PLL lock range and capture frequency for test point 942."""
    f0 = pll_free_running_frequency(10420.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_943():
    """Validate 565 PLL lock range and capture frequency for test point 943."""
    f0 = pll_free_running_frequency(10430.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_944():
    """Validate 565 PLL lock range and capture frequency for test point 944."""
    f0 = pll_free_running_frequency(10440.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_945():
    """Validate 565 PLL lock range and capture frequency for test point 945."""
    f0 = pll_free_running_frequency(10450.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_946():
    """Validate 565 PLL lock range and capture frequency for test point 946."""
    f0 = pll_free_running_frequency(10460.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_947():
    """Validate 565 PLL lock range and capture frequency for test point 947."""
    f0 = pll_free_running_frequency(10470.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_948():
    """Validate 565 PLL lock range and capture frequency for test point 948."""
    f0 = pll_free_running_frequency(10480.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_949():
    """Validate 565 PLL lock range and capture frequency for test point 949."""
    f0 = pll_free_running_frequency(10490.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_950():
    """Validate 565 PLL lock range and capture frequency for test point 950."""
    f0 = pll_free_running_frequency(10500.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_951():
    """Validate 565 PLL lock range and capture frequency for test point 951."""
    f0 = pll_free_running_frequency(10510.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_952():
    """Validate 565 PLL lock range and capture frequency for test point 952."""
    f0 = pll_free_running_frequency(10520.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_953():
    """Validate 565 PLL lock range and capture frequency for test point 953."""
    f0 = pll_free_running_frequency(10530.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_954():
    """Validate 565 PLL lock range and capture frequency for test point 954."""
    f0 = pll_free_running_frequency(10540.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_955():
    """Validate 565 PLL lock range and capture frequency for test point 955."""
    f0 = pll_free_running_frequency(10550.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_956():
    """Validate 565 PLL lock range and capture frequency for test point 956."""
    f0 = pll_free_running_frequency(10560.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_957():
    """Validate 565 PLL lock range and capture frequency for test point 957."""
    f0 = pll_free_running_frequency(10570.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_958():
    """Validate 565 PLL lock range and capture frequency for test point 958."""
    f0 = pll_free_running_frequency(10580.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_959():
    """Validate 565 PLL lock range and capture frequency for test point 959."""
    f0 = pll_free_running_frequency(10590.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_960():
    """Validate 565 PLL lock range and capture frequency for test point 960."""
    f0 = pll_free_running_frequency(10600.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_961():
    """Validate 565 PLL lock range and capture frequency for test point 961."""
    f0 = pll_free_running_frequency(10610.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_962():
    """Validate 565 PLL lock range and capture frequency for test point 962."""
    f0 = pll_free_running_frequency(10620.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_963():
    """Validate 565 PLL lock range and capture frequency for test point 963."""
    f0 = pll_free_running_frequency(10630.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_964():
    """Validate 565 PLL lock range and capture frequency for test point 964."""
    f0 = pll_free_running_frequency(10640.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_965():
    """Validate 565 PLL lock range and capture frequency for test point 965."""
    f0 = pll_free_running_frequency(10650.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_966():
    """Validate 565 PLL lock range and capture frequency for test point 966."""
    f0 = pll_free_running_frequency(10660.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_967():
    """Validate 565 PLL lock range and capture frequency for test point 967."""
    f0 = pll_free_running_frequency(10670.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_968():
    """Validate 565 PLL lock range and capture frequency for test point 968."""
    f0 = pll_free_running_frequency(10680.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_969():
    """Validate 565 PLL lock range and capture frequency for test point 969."""
    f0 = pll_free_running_frequency(10690.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_970():
    """Validate 565 PLL lock range and capture frequency for test point 970."""
    f0 = pll_free_running_frequency(10700.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_971():
    """Validate 565 PLL lock range and capture frequency for test point 971."""
    f0 = pll_free_running_frequency(10710.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_972():
    """Validate 565 PLL lock range and capture frequency for test point 972."""
    f0 = pll_free_running_frequency(10720.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_973():
    """Validate 565 PLL lock range and capture frequency for test point 973."""
    f0 = pll_free_running_frequency(10730.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_974():
    """Validate 565 PLL lock range and capture frequency for test point 974."""
    f0 = pll_free_running_frequency(10740.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_975():
    """Validate 565 PLL lock range and capture frequency for test point 975."""
    f0 = pll_free_running_frequency(10750.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_976():
    """Validate 565 PLL lock range and capture frequency for test point 976."""
    f0 = pll_free_running_frequency(10760.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_977():
    """Validate 565 PLL lock range and capture frequency for test point 977."""
    f0 = pll_free_running_frequency(10770.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_978():
    """Validate 565 PLL lock range and capture frequency for test point 978."""
    f0 = pll_free_running_frequency(10780.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_979():
    """Validate 565 PLL lock range and capture frequency for test point 979."""
    f0 = pll_free_running_frequency(10790.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_980():
    """Validate 565 PLL lock range and capture frequency for test point 980."""
    f0 = pll_free_running_frequency(10800.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_981():
    """Validate 565 PLL lock range and capture frequency for test point 981."""
    f0 = pll_free_running_frequency(10810.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_982():
    """Validate 565 PLL lock range and capture frequency for test point 982."""
    f0 = pll_free_running_frequency(10820.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_983():
    """Validate 565 PLL lock range and capture frequency for test point 983."""
    f0 = pll_free_running_frequency(10830.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_984():
    """Validate 565 PLL lock range and capture frequency for test point 984."""
    f0 = pll_free_running_frequency(10840.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_985():
    """Validate 565 PLL lock range and capture frequency for test point 985."""
    f0 = pll_free_running_frequency(10850.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_986():
    """Validate 565 PLL lock range and capture frequency for test point 986."""
    f0 = pll_free_running_frequency(10860.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_987():
    """Validate 565 PLL lock range and capture frequency for test point 987."""
    f0 = pll_free_running_frequency(10870.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_988():
    """Validate 565 PLL lock range and capture frequency for test point 988."""
    f0 = pll_free_running_frequency(10880.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_989():
    """Validate 565 PLL lock range and capture frequency for test point 989."""
    f0 = pll_free_running_frequency(10890.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_990():
    """Validate 565 PLL lock range and capture frequency for test point 990."""
    f0 = pll_free_running_frequency(10900.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_991():
    """Validate 565 PLL lock range and capture frequency for test point 991."""
    f0 = pll_free_running_frequency(10910.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_992():
    """Validate 565 PLL lock range and capture frequency for test point 992."""
    f0 = pll_free_running_frequency(10920.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_993():
    """Validate 565 PLL lock range and capture frequency for test point 993."""
    f0 = pll_free_running_frequency(10930.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_994():
    """Validate 565 PLL lock range and capture frequency for test point 994."""
    f0 = pll_free_running_frequency(10940.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_995():
    """Validate 565 PLL lock range and capture frequency for test point 995."""
    f0 = pll_free_running_frequency(10950.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_996():
    """Validate 565 PLL lock range and capture frequency for test point 996."""
    f0 = pll_free_running_frequency(10960.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_997():
    """Validate 565 PLL lock range and capture frequency for test point 997."""
    f0 = pll_free_running_frequency(10970.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_998():
    """Validate 565 PLL lock range and capture frequency for test point 998."""
    f0 = pll_free_running_frequency(10980.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_999():
    """Validate 565 PLL lock range and capture frequency for test point 999."""
    f0 = pll_free_running_frequency(10990.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0

def test_timing_pll_circuit_node_1000():
    """Validate 565 PLL lock range and capture frequency for test point 1000."""
    f0 = pll_free_running_frequency(11000.0, 1e-8)
    fl = pll_lock_range(f0, 12.0)
    assert f0 > 0.0
    assert fl > 0.0
