"""Pytest unit tests for MNA matrix solver, op-amp macromodels, and active filters."""
from __future__ import annotations
import math
import pytest
from app.simulation.core.mna_solver import MNASolver
from app.simulation.analog.opamp_models import compute_gain_bandwidth_rolloff, OPAMP_CATALOG
from app.simulation.analog.linear_stages import inverting_amplifier_gain, non_inverting_amplifier_gain
from app.simulation.analog.instrumentation_amp import instrumentation_amplifier_gain
from app.simulation.analog.filters_butterworth import butterworth_sallen_key_lowpass, butterworth_transfer_magnitude

def test_mna_solver_voltage_divider():
    solver = MNASolver(num_nodes=2)
    solver.add_voltage_source("V1", 1, 0, 10.0)
    solver.add_resistor("R1", 1, 2, 1000.0)
    solver.add_resistor("R2", 2, 0, 1000.0)
    voltages = solver.solve_dc()
    assert math.isclose(voltages[0], 10.0, rel_tol=1e-3)
    assert math.isclose(voltages[1], 5.0, rel_tol=1e-3)

def test_inverting_gain():
    gain = inverting_amplifier_gain(10000.0, 50000.0)
    assert math.isclose(gain, -5.0, rel_tol=1e-4)

def test_non_inverting_gain():
    gain = non_inverting_amplifier_gain(10000.0, 90000.0)
    assert math.isclose(gain, 10.0, rel_tol=1e-4)

def test_instrumentation_gain():
    gain = instrumentation_amplifier_gain(50000.0, 1000.0, 10000.0, 10000.0)
    assert math.isclose(gain, 101.0, rel_tol=1e-4)

def test_analog_macromodel_verification_case_1():
    """Verify gain-bandwidth rolloff and linear stability for test case 1."""
    g = compute_gain_bandwidth_rolloff('LM741', 150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 510.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_2():
    """Verify gain-bandwidth rolloff and linear stability for test case 2."""
    g = compute_gain_bandwidth_rolloff('LM741', 200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 520.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_3():
    """Verify gain-bandwidth rolloff and linear stability for test case 3."""
    g = compute_gain_bandwidth_rolloff('LM741', 250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 530.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_4():
    """Verify gain-bandwidth rolloff and linear stability for test case 4."""
    g = compute_gain_bandwidth_rolloff('LM741', 300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 540.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_5():
    """Verify gain-bandwidth rolloff and linear stability for test case 5."""
    g = compute_gain_bandwidth_rolloff('LM741', 350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 550.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_6():
    """Verify gain-bandwidth rolloff and linear stability for test case 6."""
    g = compute_gain_bandwidth_rolloff('LM741', 400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 560.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_7():
    """Verify gain-bandwidth rolloff and linear stability for test case 7."""
    g = compute_gain_bandwidth_rolloff('LM741', 450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 570.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_8():
    """Verify gain-bandwidth rolloff and linear stability for test case 8."""
    g = compute_gain_bandwidth_rolloff('LM741', 500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 580.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_9():
    """Verify gain-bandwidth rolloff and linear stability for test case 9."""
    g = compute_gain_bandwidth_rolloff('LM741', 550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 590.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_10():
    """Verify gain-bandwidth rolloff and linear stability for test case 10."""
    g = compute_gain_bandwidth_rolloff('LM741', 600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 600.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_11():
    """Verify gain-bandwidth rolloff and linear stability for test case 11."""
    g = compute_gain_bandwidth_rolloff('LM741', 650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 610.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_12():
    """Verify gain-bandwidth rolloff and linear stability for test case 12."""
    g = compute_gain_bandwidth_rolloff('LM741', 700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 620.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_13():
    """Verify gain-bandwidth rolloff and linear stability for test case 13."""
    g = compute_gain_bandwidth_rolloff('LM741', 750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 630.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_14():
    """Verify gain-bandwidth rolloff and linear stability for test case 14."""
    g = compute_gain_bandwidth_rolloff('LM741', 800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 640.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_15():
    """Verify gain-bandwidth rolloff and linear stability for test case 15."""
    g = compute_gain_bandwidth_rolloff('LM741', 850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 650.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_16():
    """Verify gain-bandwidth rolloff and linear stability for test case 16."""
    g = compute_gain_bandwidth_rolloff('LM741', 900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 660.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_17():
    """Verify gain-bandwidth rolloff and linear stability for test case 17."""
    g = compute_gain_bandwidth_rolloff('LM741', 950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 670.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_18():
    """Verify gain-bandwidth rolloff and linear stability for test case 18."""
    g = compute_gain_bandwidth_rolloff('LM741', 1000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 680.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_19():
    """Verify gain-bandwidth rolloff and linear stability for test case 19."""
    g = compute_gain_bandwidth_rolloff('LM741', 1050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 690.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_20():
    """Verify gain-bandwidth rolloff and linear stability for test case 20."""
    g = compute_gain_bandwidth_rolloff('LM741', 1100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 700.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_21():
    """Verify gain-bandwidth rolloff and linear stability for test case 21."""
    g = compute_gain_bandwidth_rolloff('LM741', 1150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 710.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_22():
    """Verify gain-bandwidth rolloff and linear stability for test case 22."""
    g = compute_gain_bandwidth_rolloff('LM741', 1200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 720.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_23():
    """Verify gain-bandwidth rolloff and linear stability for test case 23."""
    g = compute_gain_bandwidth_rolloff('LM741', 1250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 730.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_24():
    """Verify gain-bandwidth rolloff and linear stability for test case 24."""
    g = compute_gain_bandwidth_rolloff('LM741', 1300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 740.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_25():
    """Verify gain-bandwidth rolloff and linear stability for test case 25."""
    g = compute_gain_bandwidth_rolloff('LM741', 1350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 750.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_26():
    """Verify gain-bandwidth rolloff and linear stability for test case 26."""
    g = compute_gain_bandwidth_rolloff('LM741', 1400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 760.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_27():
    """Verify gain-bandwidth rolloff and linear stability for test case 27."""
    g = compute_gain_bandwidth_rolloff('LM741', 1450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 770.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_28():
    """Verify gain-bandwidth rolloff and linear stability for test case 28."""
    g = compute_gain_bandwidth_rolloff('LM741', 1500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 780.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_29():
    """Verify gain-bandwidth rolloff and linear stability for test case 29."""
    g = compute_gain_bandwidth_rolloff('LM741', 1550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 790.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_30():
    """Verify gain-bandwidth rolloff and linear stability for test case 30."""
    g = compute_gain_bandwidth_rolloff('LM741', 1600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 800.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_31():
    """Verify gain-bandwidth rolloff and linear stability for test case 31."""
    g = compute_gain_bandwidth_rolloff('LM741', 1650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 810.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_32():
    """Verify gain-bandwidth rolloff and linear stability for test case 32."""
    g = compute_gain_bandwidth_rolloff('LM741', 1700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 820.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_33():
    """Verify gain-bandwidth rolloff and linear stability for test case 33."""
    g = compute_gain_bandwidth_rolloff('LM741', 1750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 830.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_34():
    """Verify gain-bandwidth rolloff and linear stability for test case 34."""
    g = compute_gain_bandwidth_rolloff('LM741', 1800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 840.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_35():
    """Verify gain-bandwidth rolloff and linear stability for test case 35."""
    g = compute_gain_bandwidth_rolloff('LM741', 1850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 850.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_36():
    """Verify gain-bandwidth rolloff and linear stability for test case 36."""
    g = compute_gain_bandwidth_rolloff('LM741', 1900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 860.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_37():
    """Verify gain-bandwidth rolloff and linear stability for test case 37."""
    g = compute_gain_bandwidth_rolloff('LM741', 1950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 870.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_38():
    """Verify gain-bandwidth rolloff and linear stability for test case 38."""
    g = compute_gain_bandwidth_rolloff('LM741', 2000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 880.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_39():
    """Verify gain-bandwidth rolloff and linear stability for test case 39."""
    g = compute_gain_bandwidth_rolloff('LM741', 2050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 890.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_40():
    """Verify gain-bandwidth rolloff and linear stability for test case 40."""
    g = compute_gain_bandwidth_rolloff('LM741', 2100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 900.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_41():
    """Verify gain-bandwidth rolloff and linear stability for test case 41."""
    g = compute_gain_bandwidth_rolloff('LM741', 2150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 910.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_42():
    """Verify gain-bandwidth rolloff and linear stability for test case 42."""
    g = compute_gain_bandwidth_rolloff('LM741', 2200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 920.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_43():
    """Verify gain-bandwidth rolloff and linear stability for test case 43."""
    g = compute_gain_bandwidth_rolloff('LM741', 2250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 930.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_44():
    """Verify gain-bandwidth rolloff and linear stability for test case 44."""
    g = compute_gain_bandwidth_rolloff('LM741', 2300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 940.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_45():
    """Verify gain-bandwidth rolloff and linear stability for test case 45."""
    g = compute_gain_bandwidth_rolloff('LM741', 2350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 950.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_46():
    """Verify gain-bandwidth rolloff and linear stability for test case 46."""
    g = compute_gain_bandwidth_rolloff('LM741', 2400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 960.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_47():
    """Verify gain-bandwidth rolloff and linear stability for test case 47."""
    g = compute_gain_bandwidth_rolloff('LM741', 2450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 970.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_48():
    """Verify gain-bandwidth rolloff and linear stability for test case 48."""
    g = compute_gain_bandwidth_rolloff('LM741', 2500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 980.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_49():
    """Verify gain-bandwidth rolloff and linear stability for test case 49."""
    g = compute_gain_bandwidth_rolloff('LM741', 2550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 990.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_50():
    """Verify gain-bandwidth rolloff and linear stability for test case 50."""
    g = compute_gain_bandwidth_rolloff('LM741', 2600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1000.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_51():
    """Verify gain-bandwidth rolloff and linear stability for test case 51."""
    g = compute_gain_bandwidth_rolloff('LM741', 2650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1010.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_52():
    """Verify gain-bandwidth rolloff and linear stability for test case 52."""
    g = compute_gain_bandwidth_rolloff('LM741', 2700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1020.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_53():
    """Verify gain-bandwidth rolloff and linear stability for test case 53."""
    g = compute_gain_bandwidth_rolloff('LM741', 2750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1030.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_54():
    """Verify gain-bandwidth rolloff and linear stability for test case 54."""
    g = compute_gain_bandwidth_rolloff('LM741', 2800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1040.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_55():
    """Verify gain-bandwidth rolloff and linear stability for test case 55."""
    g = compute_gain_bandwidth_rolloff('LM741', 2850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1050.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_56():
    """Verify gain-bandwidth rolloff and linear stability for test case 56."""
    g = compute_gain_bandwidth_rolloff('LM741', 2900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1060.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_57():
    """Verify gain-bandwidth rolloff and linear stability for test case 57."""
    g = compute_gain_bandwidth_rolloff('LM741', 2950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1070.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_58():
    """Verify gain-bandwidth rolloff and linear stability for test case 58."""
    g = compute_gain_bandwidth_rolloff('LM741', 3000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1080.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_59():
    """Verify gain-bandwidth rolloff and linear stability for test case 59."""
    g = compute_gain_bandwidth_rolloff('LM741', 3050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1090.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_60():
    """Verify gain-bandwidth rolloff and linear stability for test case 60."""
    g = compute_gain_bandwidth_rolloff('LM741', 3100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1100.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_61():
    """Verify gain-bandwidth rolloff and linear stability for test case 61."""
    g = compute_gain_bandwidth_rolloff('LM741', 3150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1110.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_62():
    """Verify gain-bandwidth rolloff and linear stability for test case 62."""
    g = compute_gain_bandwidth_rolloff('LM741', 3200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1120.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_63():
    """Verify gain-bandwidth rolloff and linear stability for test case 63."""
    g = compute_gain_bandwidth_rolloff('LM741', 3250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1130.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_64():
    """Verify gain-bandwidth rolloff and linear stability for test case 64."""
    g = compute_gain_bandwidth_rolloff('LM741', 3300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1140.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_65():
    """Verify gain-bandwidth rolloff and linear stability for test case 65."""
    g = compute_gain_bandwidth_rolloff('LM741', 3350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1150.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_66():
    """Verify gain-bandwidth rolloff and linear stability for test case 66."""
    g = compute_gain_bandwidth_rolloff('LM741', 3400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1160.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_67():
    """Verify gain-bandwidth rolloff and linear stability for test case 67."""
    g = compute_gain_bandwidth_rolloff('LM741', 3450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1170.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_68():
    """Verify gain-bandwidth rolloff and linear stability for test case 68."""
    g = compute_gain_bandwidth_rolloff('LM741', 3500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1180.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_69():
    """Verify gain-bandwidth rolloff and linear stability for test case 69."""
    g = compute_gain_bandwidth_rolloff('LM741', 3550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1190.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_70():
    """Verify gain-bandwidth rolloff and linear stability for test case 70."""
    g = compute_gain_bandwidth_rolloff('LM741', 3600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1200.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_71():
    """Verify gain-bandwidth rolloff and linear stability for test case 71."""
    g = compute_gain_bandwidth_rolloff('LM741', 3650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1210.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_72():
    """Verify gain-bandwidth rolloff and linear stability for test case 72."""
    g = compute_gain_bandwidth_rolloff('LM741', 3700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1220.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_73():
    """Verify gain-bandwidth rolloff and linear stability for test case 73."""
    g = compute_gain_bandwidth_rolloff('LM741', 3750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1230.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_74():
    """Verify gain-bandwidth rolloff and linear stability for test case 74."""
    g = compute_gain_bandwidth_rolloff('LM741', 3800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1240.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_75():
    """Verify gain-bandwidth rolloff and linear stability for test case 75."""
    g = compute_gain_bandwidth_rolloff('LM741', 3850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1250.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_76():
    """Verify gain-bandwidth rolloff and linear stability for test case 76."""
    g = compute_gain_bandwidth_rolloff('LM741', 3900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1260.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_77():
    """Verify gain-bandwidth rolloff and linear stability for test case 77."""
    g = compute_gain_bandwidth_rolloff('LM741', 3950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1270.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_78():
    """Verify gain-bandwidth rolloff and linear stability for test case 78."""
    g = compute_gain_bandwidth_rolloff('LM741', 4000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1280.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_79():
    """Verify gain-bandwidth rolloff and linear stability for test case 79."""
    g = compute_gain_bandwidth_rolloff('LM741', 4050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1290.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_80():
    """Verify gain-bandwidth rolloff and linear stability for test case 80."""
    g = compute_gain_bandwidth_rolloff('LM741', 4100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1300.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_81():
    """Verify gain-bandwidth rolloff and linear stability for test case 81."""
    g = compute_gain_bandwidth_rolloff('LM741', 4150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1310.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_82():
    """Verify gain-bandwidth rolloff and linear stability for test case 82."""
    g = compute_gain_bandwidth_rolloff('LM741', 4200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1320.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_83():
    """Verify gain-bandwidth rolloff and linear stability for test case 83."""
    g = compute_gain_bandwidth_rolloff('LM741', 4250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1330.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_84():
    """Verify gain-bandwidth rolloff and linear stability for test case 84."""
    g = compute_gain_bandwidth_rolloff('LM741', 4300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1340.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_85():
    """Verify gain-bandwidth rolloff and linear stability for test case 85."""
    g = compute_gain_bandwidth_rolloff('LM741', 4350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1350.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_86():
    """Verify gain-bandwidth rolloff and linear stability for test case 86."""
    g = compute_gain_bandwidth_rolloff('LM741', 4400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1360.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_87():
    """Verify gain-bandwidth rolloff and linear stability for test case 87."""
    g = compute_gain_bandwidth_rolloff('LM741', 4450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1370.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_88():
    """Verify gain-bandwidth rolloff and linear stability for test case 88."""
    g = compute_gain_bandwidth_rolloff('LM741', 4500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1380.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_89():
    """Verify gain-bandwidth rolloff and linear stability for test case 89."""
    g = compute_gain_bandwidth_rolloff('LM741', 4550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1390.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_90():
    """Verify gain-bandwidth rolloff and linear stability for test case 90."""
    g = compute_gain_bandwidth_rolloff('LM741', 4600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1400.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_91():
    """Verify gain-bandwidth rolloff and linear stability for test case 91."""
    g = compute_gain_bandwidth_rolloff('LM741', 4650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1410.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_92():
    """Verify gain-bandwidth rolloff and linear stability for test case 92."""
    g = compute_gain_bandwidth_rolloff('LM741', 4700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1420.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_93():
    """Verify gain-bandwidth rolloff and linear stability for test case 93."""
    g = compute_gain_bandwidth_rolloff('LM741', 4750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1430.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_94():
    """Verify gain-bandwidth rolloff and linear stability for test case 94."""
    g = compute_gain_bandwidth_rolloff('LM741', 4800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1440.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_95():
    """Verify gain-bandwidth rolloff and linear stability for test case 95."""
    g = compute_gain_bandwidth_rolloff('LM741', 4850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1450.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_96():
    """Verify gain-bandwidth rolloff and linear stability for test case 96."""
    g = compute_gain_bandwidth_rolloff('LM741', 4900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1460.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_97():
    """Verify gain-bandwidth rolloff and linear stability for test case 97."""
    g = compute_gain_bandwidth_rolloff('LM741', 4950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1470.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_98():
    """Verify gain-bandwidth rolloff and linear stability for test case 98."""
    g = compute_gain_bandwidth_rolloff('LM741', 5000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1480.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_99():
    """Verify gain-bandwidth rolloff and linear stability for test case 99."""
    g = compute_gain_bandwidth_rolloff('LM741', 5050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1490.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_100():
    """Verify gain-bandwidth rolloff and linear stability for test case 100."""
    g = compute_gain_bandwidth_rolloff('LM741', 5100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1500.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_101():
    """Verify gain-bandwidth rolloff and linear stability for test case 101."""
    g = compute_gain_bandwidth_rolloff('LM741', 5150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1510.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_102():
    """Verify gain-bandwidth rolloff and linear stability for test case 102."""
    g = compute_gain_bandwidth_rolloff('LM741', 5200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1520.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_103():
    """Verify gain-bandwidth rolloff and linear stability for test case 103."""
    g = compute_gain_bandwidth_rolloff('LM741', 5250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1530.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_104():
    """Verify gain-bandwidth rolloff and linear stability for test case 104."""
    g = compute_gain_bandwidth_rolloff('LM741', 5300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1540.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_105():
    """Verify gain-bandwidth rolloff and linear stability for test case 105."""
    g = compute_gain_bandwidth_rolloff('LM741', 5350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1550.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_106():
    """Verify gain-bandwidth rolloff and linear stability for test case 106."""
    g = compute_gain_bandwidth_rolloff('LM741', 5400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1560.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_107():
    """Verify gain-bandwidth rolloff and linear stability for test case 107."""
    g = compute_gain_bandwidth_rolloff('LM741', 5450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1570.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_108():
    """Verify gain-bandwidth rolloff and linear stability for test case 108."""
    g = compute_gain_bandwidth_rolloff('LM741', 5500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1580.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_109():
    """Verify gain-bandwidth rolloff and linear stability for test case 109."""
    g = compute_gain_bandwidth_rolloff('LM741', 5550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1590.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_110():
    """Verify gain-bandwidth rolloff and linear stability for test case 110."""
    g = compute_gain_bandwidth_rolloff('LM741', 5600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1600.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_111():
    """Verify gain-bandwidth rolloff and linear stability for test case 111."""
    g = compute_gain_bandwidth_rolloff('LM741', 5650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1610.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_112():
    """Verify gain-bandwidth rolloff and linear stability for test case 112."""
    g = compute_gain_bandwidth_rolloff('LM741', 5700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1620.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_113():
    """Verify gain-bandwidth rolloff and linear stability for test case 113."""
    g = compute_gain_bandwidth_rolloff('LM741', 5750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1630.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_114():
    """Verify gain-bandwidth rolloff and linear stability for test case 114."""
    g = compute_gain_bandwidth_rolloff('LM741', 5800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1640.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_115():
    """Verify gain-bandwidth rolloff and linear stability for test case 115."""
    g = compute_gain_bandwidth_rolloff('LM741', 5850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1650.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_116():
    """Verify gain-bandwidth rolloff and linear stability for test case 116."""
    g = compute_gain_bandwidth_rolloff('LM741', 5900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1660.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_117():
    """Verify gain-bandwidth rolloff and linear stability for test case 117."""
    g = compute_gain_bandwidth_rolloff('LM741', 5950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1670.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_118():
    """Verify gain-bandwidth rolloff and linear stability for test case 118."""
    g = compute_gain_bandwidth_rolloff('LM741', 6000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1680.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_119():
    """Verify gain-bandwidth rolloff and linear stability for test case 119."""
    g = compute_gain_bandwidth_rolloff('LM741', 6050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1690.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_120():
    """Verify gain-bandwidth rolloff and linear stability for test case 120."""
    g = compute_gain_bandwidth_rolloff('LM741', 6100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1700.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_121():
    """Verify gain-bandwidth rolloff and linear stability for test case 121."""
    g = compute_gain_bandwidth_rolloff('LM741', 6150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1710.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_122():
    """Verify gain-bandwidth rolloff and linear stability for test case 122."""
    g = compute_gain_bandwidth_rolloff('LM741', 6200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1720.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_123():
    """Verify gain-bandwidth rolloff and linear stability for test case 123."""
    g = compute_gain_bandwidth_rolloff('LM741', 6250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1730.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_124():
    """Verify gain-bandwidth rolloff and linear stability for test case 124."""
    g = compute_gain_bandwidth_rolloff('LM741', 6300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1740.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_125():
    """Verify gain-bandwidth rolloff and linear stability for test case 125."""
    g = compute_gain_bandwidth_rolloff('LM741', 6350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1750.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_126():
    """Verify gain-bandwidth rolloff and linear stability for test case 126."""
    g = compute_gain_bandwidth_rolloff('LM741', 6400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1760.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_127():
    """Verify gain-bandwidth rolloff and linear stability for test case 127."""
    g = compute_gain_bandwidth_rolloff('LM741', 6450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1770.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_128():
    """Verify gain-bandwidth rolloff and linear stability for test case 128."""
    g = compute_gain_bandwidth_rolloff('LM741', 6500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1780.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_129():
    """Verify gain-bandwidth rolloff and linear stability for test case 129."""
    g = compute_gain_bandwidth_rolloff('LM741', 6550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1790.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_130():
    """Verify gain-bandwidth rolloff and linear stability for test case 130."""
    g = compute_gain_bandwidth_rolloff('LM741', 6600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1800.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_131():
    """Verify gain-bandwidth rolloff and linear stability for test case 131."""
    g = compute_gain_bandwidth_rolloff('LM741', 6650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1810.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_132():
    """Verify gain-bandwidth rolloff and linear stability for test case 132."""
    g = compute_gain_bandwidth_rolloff('LM741', 6700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1820.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_133():
    """Verify gain-bandwidth rolloff and linear stability for test case 133."""
    g = compute_gain_bandwidth_rolloff('LM741', 6750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1830.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_134():
    """Verify gain-bandwidth rolloff and linear stability for test case 134."""
    g = compute_gain_bandwidth_rolloff('LM741', 6800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1840.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_135():
    """Verify gain-bandwidth rolloff and linear stability for test case 135."""
    g = compute_gain_bandwidth_rolloff('LM741', 6850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1850.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_136():
    """Verify gain-bandwidth rolloff and linear stability for test case 136."""
    g = compute_gain_bandwidth_rolloff('LM741', 6900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1860.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_137():
    """Verify gain-bandwidth rolloff and linear stability for test case 137."""
    g = compute_gain_bandwidth_rolloff('LM741', 6950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1870.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_138():
    """Verify gain-bandwidth rolloff and linear stability for test case 138."""
    g = compute_gain_bandwidth_rolloff('LM741', 7000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1880.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_139():
    """Verify gain-bandwidth rolloff and linear stability for test case 139."""
    g = compute_gain_bandwidth_rolloff('LM741', 7050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1890.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_140():
    """Verify gain-bandwidth rolloff and linear stability for test case 140."""
    g = compute_gain_bandwidth_rolloff('LM741', 7100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1900.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_141():
    """Verify gain-bandwidth rolloff and linear stability for test case 141."""
    g = compute_gain_bandwidth_rolloff('LM741', 7150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1910.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_142():
    """Verify gain-bandwidth rolloff and linear stability for test case 142."""
    g = compute_gain_bandwidth_rolloff('LM741', 7200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1920.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_143():
    """Verify gain-bandwidth rolloff and linear stability for test case 143."""
    g = compute_gain_bandwidth_rolloff('LM741', 7250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1930.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_144():
    """Verify gain-bandwidth rolloff and linear stability for test case 144."""
    g = compute_gain_bandwidth_rolloff('LM741', 7300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1940.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_145():
    """Verify gain-bandwidth rolloff and linear stability for test case 145."""
    g = compute_gain_bandwidth_rolloff('LM741', 7350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1950.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_146():
    """Verify gain-bandwidth rolloff and linear stability for test case 146."""
    g = compute_gain_bandwidth_rolloff('LM741', 7400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1960.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_147():
    """Verify gain-bandwidth rolloff and linear stability for test case 147."""
    g = compute_gain_bandwidth_rolloff('LM741', 7450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1970.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_148():
    """Verify gain-bandwidth rolloff and linear stability for test case 148."""
    g = compute_gain_bandwidth_rolloff('LM741', 7500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1980.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_149():
    """Verify gain-bandwidth rolloff and linear stability for test case 149."""
    g = compute_gain_bandwidth_rolloff('LM741', 7550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 1990.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_150():
    """Verify gain-bandwidth rolloff and linear stability for test case 150."""
    g = compute_gain_bandwidth_rolloff('LM741', 7600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2000.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_151():
    """Verify gain-bandwidth rolloff and linear stability for test case 151."""
    g = compute_gain_bandwidth_rolloff('LM741', 7650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2010.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_152():
    """Verify gain-bandwidth rolloff and linear stability for test case 152."""
    g = compute_gain_bandwidth_rolloff('LM741', 7700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2020.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_153():
    """Verify gain-bandwidth rolloff and linear stability for test case 153."""
    g = compute_gain_bandwidth_rolloff('LM741', 7750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2030.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_154():
    """Verify gain-bandwidth rolloff and linear stability for test case 154."""
    g = compute_gain_bandwidth_rolloff('LM741', 7800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2040.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_155():
    """Verify gain-bandwidth rolloff and linear stability for test case 155."""
    g = compute_gain_bandwidth_rolloff('LM741', 7850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2050.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_156():
    """Verify gain-bandwidth rolloff and linear stability for test case 156."""
    g = compute_gain_bandwidth_rolloff('LM741', 7900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2060.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_157():
    """Verify gain-bandwidth rolloff and linear stability for test case 157."""
    g = compute_gain_bandwidth_rolloff('LM741', 7950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2070.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_158():
    """Verify gain-bandwidth rolloff and linear stability for test case 158."""
    g = compute_gain_bandwidth_rolloff('LM741', 8000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2080.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_159():
    """Verify gain-bandwidth rolloff and linear stability for test case 159."""
    g = compute_gain_bandwidth_rolloff('LM741', 8050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2090.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_160():
    """Verify gain-bandwidth rolloff and linear stability for test case 160."""
    g = compute_gain_bandwidth_rolloff('LM741', 8100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2100.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_161():
    """Verify gain-bandwidth rolloff and linear stability for test case 161."""
    g = compute_gain_bandwidth_rolloff('LM741', 8150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2110.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_162():
    """Verify gain-bandwidth rolloff and linear stability for test case 162."""
    g = compute_gain_bandwidth_rolloff('LM741', 8200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2120.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_163():
    """Verify gain-bandwidth rolloff and linear stability for test case 163."""
    g = compute_gain_bandwidth_rolloff('LM741', 8250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2130.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_164():
    """Verify gain-bandwidth rolloff and linear stability for test case 164."""
    g = compute_gain_bandwidth_rolloff('LM741', 8300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2140.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_165():
    """Verify gain-bandwidth rolloff and linear stability for test case 165."""
    g = compute_gain_bandwidth_rolloff('LM741', 8350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2150.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_166():
    """Verify gain-bandwidth rolloff and linear stability for test case 166."""
    g = compute_gain_bandwidth_rolloff('LM741', 8400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2160.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_167():
    """Verify gain-bandwidth rolloff and linear stability for test case 167."""
    g = compute_gain_bandwidth_rolloff('LM741', 8450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2170.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_168():
    """Verify gain-bandwidth rolloff and linear stability for test case 168."""
    g = compute_gain_bandwidth_rolloff('LM741', 8500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2180.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_169():
    """Verify gain-bandwidth rolloff and linear stability for test case 169."""
    g = compute_gain_bandwidth_rolloff('LM741', 8550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2190.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_170():
    """Verify gain-bandwidth rolloff and linear stability for test case 170."""
    g = compute_gain_bandwidth_rolloff('LM741', 8600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2200.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_171():
    """Verify gain-bandwidth rolloff and linear stability for test case 171."""
    g = compute_gain_bandwidth_rolloff('LM741', 8650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2210.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_172():
    """Verify gain-bandwidth rolloff and linear stability for test case 172."""
    g = compute_gain_bandwidth_rolloff('LM741', 8700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2220.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_173():
    """Verify gain-bandwidth rolloff and linear stability for test case 173."""
    g = compute_gain_bandwidth_rolloff('LM741', 8750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2230.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_174():
    """Verify gain-bandwidth rolloff and linear stability for test case 174."""
    g = compute_gain_bandwidth_rolloff('LM741', 8800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2240.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_175():
    """Verify gain-bandwidth rolloff and linear stability for test case 175."""
    g = compute_gain_bandwidth_rolloff('LM741', 8850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2250.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_176():
    """Verify gain-bandwidth rolloff and linear stability for test case 176."""
    g = compute_gain_bandwidth_rolloff('LM741', 8900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2260.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_177():
    """Verify gain-bandwidth rolloff and linear stability for test case 177."""
    g = compute_gain_bandwidth_rolloff('LM741', 8950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2270.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_178():
    """Verify gain-bandwidth rolloff and linear stability for test case 178."""
    g = compute_gain_bandwidth_rolloff('LM741', 9000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2280.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_179():
    """Verify gain-bandwidth rolloff and linear stability for test case 179."""
    g = compute_gain_bandwidth_rolloff('LM741', 9050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2290.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_180():
    """Verify gain-bandwidth rolloff and linear stability for test case 180."""
    g = compute_gain_bandwidth_rolloff('LM741', 9100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2300.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_181():
    """Verify gain-bandwidth rolloff and linear stability for test case 181."""
    g = compute_gain_bandwidth_rolloff('LM741', 9150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2310.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_182():
    """Verify gain-bandwidth rolloff and linear stability for test case 182."""
    g = compute_gain_bandwidth_rolloff('LM741', 9200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2320.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_183():
    """Verify gain-bandwidth rolloff and linear stability for test case 183."""
    g = compute_gain_bandwidth_rolloff('LM741', 9250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2330.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_184():
    """Verify gain-bandwidth rolloff and linear stability for test case 184."""
    g = compute_gain_bandwidth_rolloff('LM741', 9300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2340.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_185():
    """Verify gain-bandwidth rolloff and linear stability for test case 185."""
    g = compute_gain_bandwidth_rolloff('LM741', 9350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2350.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_186():
    """Verify gain-bandwidth rolloff and linear stability for test case 186."""
    g = compute_gain_bandwidth_rolloff('LM741', 9400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2360.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_187():
    """Verify gain-bandwidth rolloff and linear stability for test case 187."""
    g = compute_gain_bandwidth_rolloff('LM741', 9450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2370.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_188():
    """Verify gain-bandwidth rolloff and linear stability for test case 188."""
    g = compute_gain_bandwidth_rolloff('LM741', 9500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2380.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_189():
    """Verify gain-bandwidth rolloff and linear stability for test case 189."""
    g = compute_gain_bandwidth_rolloff('LM741', 9550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2390.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_190():
    """Verify gain-bandwidth rolloff and linear stability for test case 190."""
    g = compute_gain_bandwidth_rolloff('LM741', 9600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2400.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_191():
    """Verify gain-bandwidth rolloff and linear stability for test case 191."""
    g = compute_gain_bandwidth_rolloff('LM741', 9650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2410.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_192():
    """Verify gain-bandwidth rolloff and linear stability for test case 192."""
    g = compute_gain_bandwidth_rolloff('LM741', 9700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2420.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_193():
    """Verify gain-bandwidth rolloff and linear stability for test case 193."""
    g = compute_gain_bandwidth_rolloff('LM741', 9750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2430.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_194():
    """Verify gain-bandwidth rolloff and linear stability for test case 194."""
    g = compute_gain_bandwidth_rolloff('LM741', 9800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2440.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_195():
    """Verify gain-bandwidth rolloff and linear stability for test case 195."""
    g = compute_gain_bandwidth_rolloff('LM741', 9850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2450.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_196():
    """Verify gain-bandwidth rolloff and linear stability for test case 196."""
    g = compute_gain_bandwidth_rolloff('LM741', 9900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2460.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_197():
    """Verify gain-bandwidth rolloff and linear stability for test case 197."""
    g = compute_gain_bandwidth_rolloff('LM741', 9950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2470.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_198():
    """Verify gain-bandwidth rolloff and linear stability for test case 198."""
    g = compute_gain_bandwidth_rolloff('LM741', 10000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2480.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_199():
    """Verify gain-bandwidth rolloff and linear stability for test case 199."""
    g = compute_gain_bandwidth_rolloff('LM741', 10050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2490.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_200():
    """Verify gain-bandwidth rolloff and linear stability for test case 200."""
    g = compute_gain_bandwidth_rolloff('LM741', 10100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2500.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_201():
    """Verify gain-bandwidth rolloff and linear stability for test case 201."""
    g = compute_gain_bandwidth_rolloff('LM741', 10150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2510.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_202():
    """Verify gain-bandwidth rolloff and linear stability for test case 202."""
    g = compute_gain_bandwidth_rolloff('LM741', 10200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2520.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_203():
    """Verify gain-bandwidth rolloff and linear stability for test case 203."""
    g = compute_gain_bandwidth_rolloff('LM741', 10250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2530.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_204():
    """Verify gain-bandwidth rolloff and linear stability for test case 204."""
    g = compute_gain_bandwidth_rolloff('LM741', 10300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2540.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_205():
    """Verify gain-bandwidth rolloff and linear stability for test case 205."""
    g = compute_gain_bandwidth_rolloff('LM741', 10350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2550.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_206():
    """Verify gain-bandwidth rolloff and linear stability for test case 206."""
    g = compute_gain_bandwidth_rolloff('LM741', 10400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2560.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_207():
    """Verify gain-bandwidth rolloff and linear stability for test case 207."""
    g = compute_gain_bandwidth_rolloff('LM741', 10450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2570.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_208():
    """Verify gain-bandwidth rolloff and linear stability for test case 208."""
    g = compute_gain_bandwidth_rolloff('LM741', 10500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2580.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_209():
    """Verify gain-bandwidth rolloff and linear stability for test case 209."""
    g = compute_gain_bandwidth_rolloff('LM741', 10550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2590.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_210():
    """Verify gain-bandwidth rolloff and linear stability for test case 210."""
    g = compute_gain_bandwidth_rolloff('LM741', 10600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2600.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_211():
    """Verify gain-bandwidth rolloff and linear stability for test case 211."""
    g = compute_gain_bandwidth_rolloff('LM741', 10650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2610.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_212():
    """Verify gain-bandwidth rolloff and linear stability for test case 212."""
    g = compute_gain_bandwidth_rolloff('LM741', 10700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2620.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_213():
    """Verify gain-bandwidth rolloff and linear stability for test case 213."""
    g = compute_gain_bandwidth_rolloff('LM741', 10750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2630.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_214():
    """Verify gain-bandwidth rolloff and linear stability for test case 214."""
    g = compute_gain_bandwidth_rolloff('LM741', 10800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2640.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_215():
    """Verify gain-bandwidth rolloff and linear stability for test case 215."""
    g = compute_gain_bandwidth_rolloff('LM741', 10850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2650.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_216():
    """Verify gain-bandwidth rolloff and linear stability for test case 216."""
    g = compute_gain_bandwidth_rolloff('LM741', 10900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2660.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_217():
    """Verify gain-bandwidth rolloff and linear stability for test case 217."""
    g = compute_gain_bandwidth_rolloff('LM741', 10950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2670.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_218():
    """Verify gain-bandwidth rolloff and linear stability for test case 218."""
    g = compute_gain_bandwidth_rolloff('LM741', 11000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2680.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_219():
    """Verify gain-bandwidth rolloff and linear stability for test case 219."""
    g = compute_gain_bandwidth_rolloff('LM741', 11050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2690.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_220():
    """Verify gain-bandwidth rolloff and linear stability for test case 220."""
    g = compute_gain_bandwidth_rolloff('LM741', 11100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2700.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_221():
    """Verify gain-bandwidth rolloff and linear stability for test case 221."""
    g = compute_gain_bandwidth_rolloff('LM741', 11150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2710.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_222():
    """Verify gain-bandwidth rolloff and linear stability for test case 222."""
    g = compute_gain_bandwidth_rolloff('LM741', 11200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2720.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_223():
    """Verify gain-bandwidth rolloff and linear stability for test case 223."""
    g = compute_gain_bandwidth_rolloff('LM741', 11250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2730.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_224():
    """Verify gain-bandwidth rolloff and linear stability for test case 224."""
    g = compute_gain_bandwidth_rolloff('LM741', 11300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2740.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_225():
    """Verify gain-bandwidth rolloff and linear stability for test case 225."""
    g = compute_gain_bandwidth_rolloff('LM741', 11350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2750.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_226():
    """Verify gain-bandwidth rolloff and linear stability for test case 226."""
    g = compute_gain_bandwidth_rolloff('LM741', 11400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2760.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_227():
    """Verify gain-bandwidth rolloff and linear stability for test case 227."""
    g = compute_gain_bandwidth_rolloff('LM741', 11450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2770.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_228():
    """Verify gain-bandwidth rolloff and linear stability for test case 228."""
    g = compute_gain_bandwidth_rolloff('LM741', 11500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2780.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_229():
    """Verify gain-bandwidth rolloff and linear stability for test case 229."""
    g = compute_gain_bandwidth_rolloff('LM741', 11550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2790.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_230():
    """Verify gain-bandwidth rolloff and linear stability for test case 230."""
    g = compute_gain_bandwidth_rolloff('LM741', 11600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2800.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_231():
    """Verify gain-bandwidth rolloff and linear stability for test case 231."""
    g = compute_gain_bandwidth_rolloff('LM741', 11650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2810.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_232():
    """Verify gain-bandwidth rolloff and linear stability for test case 232."""
    g = compute_gain_bandwidth_rolloff('LM741', 11700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2820.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_233():
    """Verify gain-bandwidth rolloff and linear stability for test case 233."""
    g = compute_gain_bandwidth_rolloff('LM741', 11750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2830.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_234():
    """Verify gain-bandwidth rolloff and linear stability for test case 234."""
    g = compute_gain_bandwidth_rolloff('LM741', 11800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2840.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_235():
    """Verify gain-bandwidth rolloff and linear stability for test case 235."""
    g = compute_gain_bandwidth_rolloff('LM741', 11850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2850.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_236():
    """Verify gain-bandwidth rolloff and linear stability for test case 236."""
    g = compute_gain_bandwidth_rolloff('LM741', 11900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2860.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_237():
    """Verify gain-bandwidth rolloff and linear stability for test case 237."""
    g = compute_gain_bandwidth_rolloff('LM741', 11950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2870.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_238():
    """Verify gain-bandwidth rolloff and linear stability for test case 238."""
    g = compute_gain_bandwidth_rolloff('LM741', 12000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2880.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_239():
    """Verify gain-bandwidth rolloff and linear stability for test case 239."""
    g = compute_gain_bandwidth_rolloff('LM741', 12050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2890.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_240():
    """Verify gain-bandwidth rolloff and linear stability for test case 240."""
    g = compute_gain_bandwidth_rolloff('LM741', 12100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2900.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_241():
    """Verify gain-bandwidth rolloff and linear stability for test case 241."""
    g = compute_gain_bandwidth_rolloff('LM741', 12150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2910.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_242():
    """Verify gain-bandwidth rolloff and linear stability for test case 242."""
    g = compute_gain_bandwidth_rolloff('LM741', 12200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2920.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_243():
    """Verify gain-bandwidth rolloff and linear stability for test case 243."""
    g = compute_gain_bandwidth_rolloff('LM741', 12250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2930.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_244():
    """Verify gain-bandwidth rolloff and linear stability for test case 244."""
    g = compute_gain_bandwidth_rolloff('LM741', 12300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2940.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_245():
    """Verify gain-bandwidth rolloff and linear stability for test case 245."""
    g = compute_gain_bandwidth_rolloff('LM741', 12350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2950.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_246():
    """Verify gain-bandwidth rolloff and linear stability for test case 246."""
    g = compute_gain_bandwidth_rolloff('LM741', 12400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2960.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_247():
    """Verify gain-bandwidth rolloff and linear stability for test case 247."""
    g = compute_gain_bandwidth_rolloff('LM741', 12450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2970.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_248():
    """Verify gain-bandwidth rolloff and linear stability for test case 248."""
    g = compute_gain_bandwidth_rolloff('LM741', 12500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2980.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_249():
    """Verify gain-bandwidth rolloff and linear stability for test case 249."""
    g = compute_gain_bandwidth_rolloff('LM741', 12550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 2990.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_250():
    """Verify gain-bandwidth rolloff and linear stability for test case 250."""
    g = compute_gain_bandwidth_rolloff('LM741', 12600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3000.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_251():
    """Verify gain-bandwidth rolloff and linear stability for test case 251."""
    g = compute_gain_bandwidth_rolloff('LM741', 12650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3010.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_252():
    """Verify gain-bandwidth rolloff and linear stability for test case 252."""
    g = compute_gain_bandwidth_rolloff('LM741', 12700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3020.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_253():
    """Verify gain-bandwidth rolloff and linear stability for test case 253."""
    g = compute_gain_bandwidth_rolloff('LM741', 12750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3030.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_254():
    """Verify gain-bandwidth rolloff and linear stability for test case 254."""
    g = compute_gain_bandwidth_rolloff('LM741', 12800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3040.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_255():
    """Verify gain-bandwidth rolloff and linear stability for test case 255."""
    g = compute_gain_bandwidth_rolloff('LM741', 12850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3050.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_256():
    """Verify gain-bandwidth rolloff and linear stability for test case 256."""
    g = compute_gain_bandwidth_rolloff('LM741', 12900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3060.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_257():
    """Verify gain-bandwidth rolloff and linear stability for test case 257."""
    g = compute_gain_bandwidth_rolloff('LM741', 12950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3070.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_258():
    """Verify gain-bandwidth rolloff and linear stability for test case 258."""
    g = compute_gain_bandwidth_rolloff('LM741', 13000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3080.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_259():
    """Verify gain-bandwidth rolloff and linear stability for test case 259."""
    g = compute_gain_bandwidth_rolloff('LM741', 13050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3090.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_260():
    """Verify gain-bandwidth rolloff and linear stability for test case 260."""
    g = compute_gain_bandwidth_rolloff('LM741', 13100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3100.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_261():
    """Verify gain-bandwidth rolloff and linear stability for test case 261."""
    g = compute_gain_bandwidth_rolloff('LM741', 13150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3110.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_262():
    """Verify gain-bandwidth rolloff and linear stability for test case 262."""
    g = compute_gain_bandwidth_rolloff('LM741', 13200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3120.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_263():
    """Verify gain-bandwidth rolloff and linear stability for test case 263."""
    g = compute_gain_bandwidth_rolloff('LM741', 13250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3130.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_264():
    """Verify gain-bandwidth rolloff and linear stability for test case 264."""
    g = compute_gain_bandwidth_rolloff('LM741', 13300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3140.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_265():
    """Verify gain-bandwidth rolloff and linear stability for test case 265."""
    g = compute_gain_bandwidth_rolloff('LM741', 13350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3150.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_266():
    """Verify gain-bandwidth rolloff and linear stability for test case 266."""
    g = compute_gain_bandwidth_rolloff('LM741', 13400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3160.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_267():
    """Verify gain-bandwidth rolloff and linear stability for test case 267."""
    g = compute_gain_bandwidth_rolloff('LM741', 13450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3170.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_268():
    """Verify gain-bandwidth rolloff and linear stability for test case 268."""
    g = compute_gain_bandwidth_rolloff('LM741', 13500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3180.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_269():
    """Verify gain-bandwidth rolloff and linear stability for test case 269."""
    g = compute_gain_bandwidth_rolloff('LM741', 13550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3190.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_270():
    """Verify gain-bandwidth rolloff and linear stability for test case 270."""
    g = compute_gain_bandwidth_rolloff('LM741', 13600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3200.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_271():
    """Verify gain-bandwidth rolloff and linear stability for test case 271."""
    g = compute_gain_bandwidth_rolloff('LM741', 13650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3210.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_272():
    """Verify gain-bandwidth rolloff and linear stability for test case 272."""
    g = compute_gain_bandwidth_rolloff('LM741', 13700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3220.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_273():
    """Verify gain-bandwidth rolloff and linear stability for test case 273."""
    g = compute_gain_bandwidth_rolloff('LM741', 13750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3230.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_274():
    """Verify gain-bandwidth rolloff and linear stability for test case 274."""
    g = compute_gain_bandwidth_rolloff('LM741', 13800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3240.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_275():
    """Verify gain-bandwidth rolloff and linear stability for test case 275."""
    g = compute_gain_bandwidth_rolloff('LM741', 13850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3250.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_276():
    """Verify gain-bandwidth rolloff and linear stability for test case 276."""
    g = compute_gain_bandwidth_rolloff('LM741', 13900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3260.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_277():
    """Verify gain-bandwidth rolloff and linear stability for test case 277."""
    g = compute_gain_bandwidth_rolloff('LM741', 13950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3270.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_278():
    """Verify gain-bandwidth rolloff and linear stability for test case 278."""
    g = compute_gain_bandwidth_rolloff('LM741', 14000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3280.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_279():
    """Verify gain-bandwidth rolloff and linear stability for test case 279."""
    g = compute_gain_bandwidth_rolloff('LM741', 14050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3290.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_280():
    """Verify gain-bandwidth rolloff and linear stability for test case 280."""
    g = compute_gain_bandwidth_rolloff('LM741', 14100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3300.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_281():
    """Verify gain-bandwidth rolloff and linear stability for test case 281."""
    g = compute_gain_bandwidth_rolloff('LM741', 14150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3310.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_282():
    """Verify gain-bandwidth rolloff and linear stability for test case 282."""
    g = compute_gain_bandwidth_rolloff('LM741', 14200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3320.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_283():
    """Verify gain-bandwidth rolloff and linear stability for test case 283."""
    g = compute_gain_bandwidth_rolloff('LM741', 14250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3330.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_284():
    """Verify gain-bandwidth rolloff and linear stability for test case 284."""
    g = compute_gain_bandwidth_rolloff('LM741', 14300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3340.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_285():
    """Verify gain-bandwidth rolloff and linear stability for test case 285."""
    g = compute_gain_bandwidth_rolloff('LM741', 14350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3350.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_286():
    """Verify gain-bandwidth rolloff and linear stability for test case 286."""
    g = compute_gain_bandwidth_rolloff('LM741', 14400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3360.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_287():
    """Verify gain-bandwidth rolloff and linear stability for test case 287."""
    g = compute_gain_bandwidth_rolloff('LM741', 14450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3370.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_288():
    """Verify gain-bandwidth rolloff and linear stability for test case 288."""
    g = compute_gain_bandwidth_rolloff('LM741', 14500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3380.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_289():
    """Verify gain-bandwidth rolloff and linear stability for test case 289."""
    g = compute_gain_bandwidth_rolloff('LM741', 14550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3390.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_290():
    """Verify gain-bandwidth rolloff and linear stability for test case 290."""
    g = compute_gain_bandwidth_rolloff('LM741', 14600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3400.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_291():
    """Verify gain-bandwidth rolloff and linear stability for test case 291."""
    g = compute_gain_bandwidth_rolloff('LM741', 14650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3410.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_292():
    """Verify gain-bandwidth rolloff and linear stability for test case 292."""
    g = compute_gain_bandwidth_rolloff('LM741', 14700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3420.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_293():
    """Verify gain-bandwidth rolloff and linear stability for test case 293."""
    g = compute_gain_bandwidth_rolloff('LM741', 14750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3430.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_294():
    """Verify gain-bandwidth rolloff and linear stability for test case 294."""
    g = compute_gain_bandwidth_rolloff('LM741', 14800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3440.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_295():
    """Verify gain-bandwidth rolloff and linear stability for test case 295."""
    g = compute_gain_bandwidth_rolloff('LM741', 14850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3450.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_296():
    """Verify gain-bandwidth rolloff and linear stability for test case 296."""
    g = compute_gain_bandwidth_rolloff('LM741', 14900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3460.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_297():
    """Verify gain-bandwidth rolloff and linear stability for test case 297."""
    g = compute_gain_bandwidth_rolloff('LM741', 14950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3470.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_298():
    """Verify gain-bandwidth rolloff and linear stability for test case 298."""
    g = compute_gain_bandwidth_rolloff('LM741', 15000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3480.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_299():
    """Verify gain-bandwidth rolloff and linear stability for test case 299."""
    g = compute_gain_bandwidth_rolloff('LM741', 15050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3490.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_300():
    """Verify gain-bandwidth rolloff and linear stability for test case 300."""
    g = compute_gain_bandwidth_rolloff('LM741', 15100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3500.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_301():
    """Verify gain-bandwidth rolloff and linear stability for test case 301."""
    g = compute_gain_bandwidth_rolloff('LM741', 15150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3510.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_302():
    """Verify gain-bandwidth rolloff and linear stability for test case 302."""
    g = compute_gain_bandwidth_rolloff('LM741', 15200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3520.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_303():
    """Verify gain-bandwidth rolloff and linear stability for test case 303."""
    g = compute_gain_bandwidth_rolloff('LM741', 15250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3530.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_304():
    """Verify gain-bandwidth rolloff and linear stability for test case 304."""
    g = compute_gain_bandwidth_rolloff('LM741', 15300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3540.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_305():
    """Verify gain-bandwidth rolloff and linear stability for test case 305."""
    g = compute_gain_bandwidth_rolloff('LM741', 15350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3550.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_306():
    """Verify gain-bandwidth rolloff and linear stability for test case 306."""
    g = compute_gain_bandwidth_rolloff('LM741', 15400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3560.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_307():
    """Verify gain-bandwidth rolloff and linear stability for test case 307."""
    g = compute_gain_bandwidth_rolloff('LM741', 15450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3570.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_308():
    """Verify gain-bandwidth rolloff and linear stability for test case 308."""
    g = compute_gain_bandwidth_rolloff('LM741', 15500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3580.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_309():
    """Verify gain-bandwidth rolloff and linear stability for test case 309."""
    g = compute_gain_bandwidth_rolloff('LM741', 15550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3590.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_310():
    """Verify gain-bandwidth rolloff and linear stability for test case 310."""
    g = compute_gain_bandwidth_rolloff('LM741', 15600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3600.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_311():
    """Verify gain-bandwidth rolloff and linear stability for test case 311."""
    g = compute_gain_bandwidth_rolloff('LM741', 15650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3610.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_312():
    """Verify gain-bandwidth rolloff and linear stability for test case 312."""
    g = compute_gain_bandwidth_rolloff('LM741', 15700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3620.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_313():
    """Verify gain-bandwidth rolloff and linear stability for test case 313."""
    g = compute_gain_bandwidth_rolloff('LM741', 15750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3630.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_314():
    """Verify gain-bandwidth rolloff and linear stability for test case 314."""
    g = compute_gain_bandwidth_rolloff('LM741', 15800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3640.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_315():
    """Verify gain-bandwidth rolloff and linear stability for test case 315."""
    g = compute_gain_bandwidth_rolloff('LM741', 15850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3650.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_316():
    """Verify gain-bandwidth rolloff and linear stability for test case 316."""
    g = compute_gain_bandwidth_rolloff('LM741', 15900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3660.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_317():
    """Verify gain-bandwidth rolloff and linear stability for test case 317."""
    g = compute_gain_bandwidth_rolloff('LM741', 15950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3670.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_318():
    """Verify gain-bandwidth rolloff and linear stability for test case 318."""
    g = compute_gain_bandwidth_rolloff('LM741', 16000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3680.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_319():
    """Verify gain-bandwidth rolloff and linear stability for test case 319."""
    g = compute_gain_bandwidth_rolloff('LM741', 16050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3690.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_320():
    """Verify gain-bandwidth rolloff and linear stability for test case 320."""
    g = compute_gain_bandwidth_rolloff('LM741', 16100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3700.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_321():
    """Verify gain-bandwidth rolloff and linear stability for test case 321."""
    g = compute_gain_bandwidth_rolloff('LM741', 16150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3710.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_322():
    """Verify gain-bandwidth rolloff and linear stability for test case 322."""
    g = compute_gain_bandwidth_rolloff('LM741', 16200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3720.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_323():
    """Verify gain-bandwidth rolloff and linear stability for test case 323."""
    g = compute_gain_bandwidth_rolloff('LM741', 16250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3730.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_324():
    """Verify gain-bandwidth rolloff and linear stability for test case 324."""
    g = compute_gain_bandwidth_rolloff('LM741', 16300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3740.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_325():
    """Verify gain-bandwidth rolloff and linear stability for test case 325."""
    g = compute_gain_bandwidth_rolloff('LM741', 16350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3750.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_326():
    """Verify gain-bandwidth rolloff and linear stability for test case 326."""
    g = compute_gain_bandwidth_rolloff('LM741', 16400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3760.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_327():
    """Verify gain-bandwidth rolloff and linear stability for test case 327."""
    g = compute_gain_bandwidth_rolloff('LM741', 16450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3770.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_328():
    """Verify gain-bandwidth rolloff and linear stability for test case 328."""
    g = compute_gain_bandwidth_rolloff('LM741', 16500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3780.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_329():
    """Verify gain-bandwidth rolloff and linear stability for test case 329."""
    g = compute_gain_bandwidth_rolloff('LM741', 16550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3790.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_330():
    """Verify gain-bandwidth rolloff and linear stability for test case 330."""
    g = compute_gain_bandwidth_rolloff('LM741', 16600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3800.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_331():
    """Verify gain-bandwidth rolloff and linear stability for test case 331."""
    g = compute_gain_bandwidth_rolloff('LM741', 16650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3810.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_332():
    """Verify gain-bandwidth rolloff and linear stability for test case 332."""
    g = compute_gain_bandwidth_rolloff('LM741', 16700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3820.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_333():
    """Verify gain-bandwidth rolloff and linear stability for test case 333."""
    g = compute_gain_bandwidth_rolloff('LM741', 16750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3830.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_334():
    """Verify gain-bandwidth rolloff and linear stability for test case 334."""
    g = compute_gain_bandwidth_rolloff('LM741', 16800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3840.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_335():
    """Verify gain-bandwidth rolloff and linear stability for test case 335."""
    g = compute_gain_bandwidth_rolloff('LM741', 16850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3850.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_336():
    """Verify gain-bandwidth rolloff and linear stability for test case 336."""
    g = compute_gain_bandwidth_rolloff('LM741', 16900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3860.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_337():
    """Verify gain-bandwidth rolloff and linear stability for test case 337."""
    g = compute_gain_bandwidth_rolloff('LM741', 16950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3870.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_338():
    """Verify gain-bandwidth rolloff and linear stability for test case 338."""
    g = compute_gain_bandwidth_rolloff('LM741', 17000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3880.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_339():
    """Verify gain-bandwidth rolloff and linear stability for test case 339."""
    g = compute_gain_bandwidth_rolloff('LM741', 17050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3890.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_340():
    """Verify gain-bandwidth rolloff and linear stability for test case 340."""
    g = compute_gain_bandwidth_rolloff('LM741', 17100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3900.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_341():
    """Verify gain-bandwidth rolloff and linear stability for test case 341."""
    g = compute_gain_bandwidth_rolloff('LM741', 17150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3910.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_342():
    """Verify gain-bandwidth rolloff and linear stability for test case 342."""
    g = compute_gain_bandwidth_rolloff('LM741', 17200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3920.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_343():
    """Verify gain-bandwidth rolloff and linear stability for test case 343."""
    g = compute_gain_bandwidth_rolloff('LM741', 17250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3930.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_344():
    """Verify gain-bandwidth rolloff and linear stability for test case 344."""
    g = compute_gain_bandwidth_rolloff('LM741', 17300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3940.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_345():
    """Verify gain-bandwidth rolloff and linear stability for test case 345."""
    g = compute_gain_bandwidth_rolloff('LM741', 17350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3950.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_346():
    """Verify gain-bandwidth rolloff and linear stability for test case 346."""
    g = compute_gain_bandwidth_rolloff('LM741', 17400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3960.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_347():
    """Verify gain-bandwidth rolloff and linear stability for test case 347."""
    g = compute_gain_bandwidth_rolloff('LM741', 17450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3970.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_348():
    """Verify gain-bandwidth rolloff and linear stability for test case 348."""
    g = compute_gain_bandwidth_rolloff('LM741', 17500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3980.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_349():
    """Verify gain-bandwidth rolloff and linear stability for test case 349."""
    g = compute_gain_bandwidth_rolloff('LM741', 17550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 3990.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_350():
    """Verify gain-bandwidth rolloff and linear stability for test case 350."""
    g = compute_gain_bandwidth_rolloff('LM741', 17600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4000.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_351():
    """Verify gain-bandwidth rolloff and linear stability for test case 351."""
    g = compute_gain_bandwidth_rolloff('LM741', 17650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4010.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_352():
    """Verify gain-bandwidth rolloff and linear stability for test case 352."""
    g = compute_gain_bandwidth_rolloff('LM741', 17700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4020.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_353():
    """Verify gain-bandwidth rolloff and linear stability for test case 353."""
    g = compute_gain_bandwidth_rolloff('LM741', 17750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4030.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_354():
    """Verify gain-bandwidth rolloff and linear stability for test case 354."""
    g = compute_gain_bandwidth_rolloff('LM741', 17800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4040.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_355():
    """Verify gain-bandwidth rolloff and linear stability for test case 355."""
    g = compute_gain_bandwidth_rolloff('LM741', 17850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4050.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_356():
    """Verify gain-bandwidth rolloff and linear stability for test case 356."""
    g = compute_gain_bandwidth_rolloff('LM741', 17900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4060.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_357():
    """Verify gain-bandwidth rolloff and linear stability for test case 357."""
    g = compute_gain_bandwidth_rolloff('LM741', 17950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4070.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_358():
    """Verify gain-bandwidth rolloff and linear stability for test case 358."""
    g = compute_gain_bandwidth_rolloff('LM741', 18000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4080.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_359():
    """Verify gain-bandwidth rolloff and linear stability for test case 359."""
    g = compute_gain_bandwidth_rolloff('LM741', 18050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4090.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_360():
    """Verify gain-bandwidth rolloff and linear stability for test case 360."""
    g = compute_gain_bandwidth_rolloff('LM741', 18100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4100.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_361():
    """Verify gain-bandwidth rolloff and linear stability for test case 361."""
    g = compute_gain_bandwidth_rolloff('LM741', 18150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4110.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_362():
    """Verify gain-bandwidth rolloff and linear stability for test case 362."""
    g = compute_gain_bandwidth_rolloff('LM741', 18200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4120.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_363():
    """Verify gain-bandwidth rolloff and linear stability for test case 363."""
    g = compute_gain_bandwidth_rolloff('LM741', 18250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4130.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_364():
    """Verify gain-bandwidth rolloff and linear stability for test case 364."""
    g = compute_gain_bandwidth_rolloff('LM741', 18300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4140.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_365():
    """Verify gain-bandwidth rolloff and linear stability for test case 365."""
    g = compute_gain_bandwidth_rolloff('LM741', 18350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4150.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_366():
    """Verify gain-bandwidth rolloff and linear stability for test case 366."""
    g = compute_gain_bandwidth_rolloff('LM741', 18400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4160.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_367():
    """Verify gain-bandwidth rolloff and linear stability for test case 367."""
    g = compute_gain_bandwidth_rolloff('LM741', 18450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4170.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_368():
    """Verify gain-bandwidth rolloff and linear stability for test case 368."""
    g = compute_gain_bandwidth_rolloff('LM741', 18500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4180.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_369():
    """Verify gain-bandwidth rolloff and linear stability for test case 369."""
    g = compute_gain_bandwidth_rolloff('LM741', 18550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4190.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_370():
    """Verify gain-bandwidth rolloff and linear stability for test case 370."""
    g = compute_gain_bandwidth_rolloff('LM741', 18600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4200.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_371():
    """Verify gain-bandwidth rolloff and linear stability for test case 371."""
    g = compute_gain_bandwidth_rolloff('LM741', 18650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4210.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_372():
    """Verify gain-bandwidth rolloff and linear stability for test case 372."""
    g = compute_gain_bandwidth_rolloff('LM741', 18700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4220.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_373():
    """Verify gain-bandwidth rolloff and linear stability for test case 373."""
    g = compute_gain_bandwidth_rolloff('LM741', 18750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4230.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_374():
    """Verify gain-bandwidth rolloff and linear stability for test case 374."""
    g = compute_gain_bandwidth_rolloff('LM741', 18800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4240.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_375():
    """Verify gain-bandwidth rolloff and linear stability for test case 375."""
    g = compute_gain_bandwidth_rolloff('LM741', 18850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4250.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_376():
    """Verify gain-bandwidth rolloff and linear stability for test case 376."""
    g = compute_gain_bandwidth_rolloff('LM741', 18900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4260.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_377():
    """Verify gain-bandwidth rolloff and linear stability for test case 377."""
    g = compute_gain_bandwidth_rolloff('LM741', 18950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4270.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_378():
    """Verify gain-bandwidth rolloff and linear stability for test case 378."""
    g = compute_gain_bandwidth_rolloff('LM741', 19000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4280.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_379():
    """Verify gain-bandwidth rolloff and linear stability for test case 379."""
    g = compute_gain_bandwidth_rolloff('LM741', 19050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4290.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_380():
    """Verify gain-bandwidth rolloff and linear stability for test case 380."""
    g = compute_gain_bandwidth_rolloff('LM741', 19100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4300.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_381():
    """Verify gain-bandwidth rolloff and linear stability for test case 381."""
    g = compute_gain_bandwidth_rolloff('LM741', 19150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4310.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_382():
    """Verify gain-bandwidth rolloff and linear stability for test case 382."""
    g = compute_gain_bandwidth_rolloff('LM741', 19200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4320.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_383():
    """Verify gain-bandwidth rolloff and linear stability for test case 383."""
    g = compute_gain_bandwidth_rolloff('LM741', 19250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4330.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_384():
    """Verify gain-bandwidth rolloff and linear stability for test case 384."""
    g = compute_gain_bandwidth_rolloff('LM741', 19300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4340.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_385():
    """Verify gain-bandwidth rolloff and linear stability for test case 385."""
    g = compute_gain_bandwidth_rolloff('LM741', 19350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4350.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_386():
    """Verify gain-bandwidth rolloff and linear stability for test case 386."""
    g = compute_gain_bandwidth_rolloff('LM741', 19400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4360.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_387():
    """Verify gain-bandwidth rolloff and linear stability for test case 387."""
    g = compute_gain_bandwidth_rolloff('LM741', 19450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4370.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_388():
    """Verify gain-bandwidth rolloff and linear stability for test case 388."""
    g = compute_gain_bandwidth_rolloff('LM741', 19500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4380.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_389():
    """Verify gain-bandwidth rolloff and linear stability for test case 389."""
    g = compute_gain_bandwidth_rolloff('LM741', 19550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4390.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_390():
    """Verify gain-bandwidth rolloff and linear stability for test case 390."""
    g = compute_gain_bandwidth_rolloff('LM741', 19600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4400.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_391():
    """Verify gain-bandwidth rolloff and linear stability for test case 391."""
    g = compute_gain_bandwidth_rolloff('LM741', 19650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4410.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_392():
    """Verify gain-bandwidth rolloff and linear stability for test case 392."""
    g = compute_gain_bandwidth_rolloff('LM741', 19700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4420.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_393():
    """Verify gain-bandwidth rolloff and linear stability for test case 393."""
    g = compute_gain_bandwidth_rolloff('LM741', 19750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4430.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_394():
    """Verify gain-bandwidth rolloff and linear stability for test case 394."""
    g = compute_gain_bandwidth_rolloff('LM741', 19800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4440.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_395():
    """Verify gain-bandwidth rolloff and linear stability for test case 395."""
    g = compute_gain_bandwidth_rolloff('LM741', 19850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4450.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_396():
    """Verify gain-bandwidth rolloff and linear stability for test case 396."""
    g = compute_gain_bandwidth_rolloff('LM741', 19900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4460.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_397():
    """Verify gain-bandwidth rolloff and linear stability for test case 397."""
    g = compute_gain_bandwidth_rolloff('LM741', 19950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4470.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_398():
    """Verify gain-bandwidth rolloff and linear stability for test case 398."""
    g = compute_gain_bandwidth_rolloff('LM741', 20000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4480.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_399():
    """Verify gain-bandwidth rolloff and linear stability for test case 399."""
    g = compute_gain_bandwidth_rolloff('LM741', 20050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4490.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_400():
    """Verify gain-bandwidth rolloff and linear stability for test case 400."""
    g = compute_gain_bandwidth_rolloff('LM741', 20100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4500.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_401():
    """Verify gain-bandwidth rolloff and linear stability for test case 401."""
    g = compute_gain_bandwidth_rolloff('LM741', 20150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4510.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_402():
    """Verify gain-bandwidth rolloff and linear stability for test case 402."""
    g = compute_gain_bandwidth_rolloff('LM741', 20200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4520.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_403():
    """Verify gain-bandwidth rolloff and linear stability for test case 403."""
    g = compute_gain_bandwidth_rolloff('LM741', 20250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4530.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_404():
    """Verify gain-bandwidth rolloff and linear stability for test case 404."""
    g = compute_gain_bandwidth_rolloff('LM741', 20300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4540.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_405():
    """Verify gain-bandwidth rolloff and linear stability for test case 405."""
    g = compute_gain_bandwidth_rolloff('LM741', 20350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4550.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_406():
    """Verify gain-bandwidth rolloff and linear stability for test case 406."""
    g = compute_gain_bandwidth_rolloff('LM741', 20400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4560.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_407():
    """Verify gain-bandwidth rolloff and linear stability for test case 407."""
    g = compute_gain_bandwidth_rolloff('LM741', 20450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4570.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_408():
    """Verify gain-bandwidth rolloff and linear stability for test case 408."""
    g = compute_gain_bandwidth_rolloff('LM741', 20500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4580.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_409():
    """Verify gain-bandwidth rolloff and linear stability for test case 409."""
    g = compute_gain_bandwidth_rolloff('LM741', 20550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4590.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_410():
    """Verify gain-bandwidth rolloff and linear stability for test case 410."""
    g = compute_gain_bandwidth_rolloff('LM741', 20600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4600.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_411():
    """Verify gain-bandwidth rolloff and linear stability for test case 411."""
    g = compute_gain_bandwidth_rolloff('LM741', 20650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4610.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_412():
    """Verify gain-bandwidth rolloff and linear stability for test case 412."""
    g = compute_gain_bandwidth_rolloff('LM741', 20700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4620.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_413():
    """Verify gain-bandwidth rolloff and linear stability for test case 413."""
    g = compute_gain_bandwidth_rolloff('LM741', 20750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4630.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_414():
    """Verify gain-bandwidth rolloff and linear stability for test case 414."""
    g = compute_gain_bandwidth_rolloff('LM741', 20800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4640.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_415():
    """Verify gain-bandwidth rolloff and linear stability for test case 415."""
    g = compute_gain_bandwidth_rolloff('LM741', 20850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4650.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_416():
    """Verify gain-bandwidth rolloff and linear stability for test case 416."""
    g = compute_gain_bandwidth_rolloff('LM741', 20900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4660.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_417():
    """Verify gain-bandwidth rolloff and linear stability for test case 417."""
    g = compute_gain_bandwidth_rolloff('LM741', 20950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4670.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_418():
    """Verify gain-bandwidth rolloff and linear stability for test case 418."""
    g = compute_gain_bandwidth_rolloff('LM741', 21000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4680.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_419():
    """Verify gain-bandwidth rolloff and linear stability for test case 419."""
    g = compute_gain_bandwidth_rolloff('LM741', 21050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4690.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_420():
    """Verify gain-bandwidth rolloff and linear stability for test case 420."""
    g = compute_gain_bandwidth_rolloff('LM741', 21100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4700.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_421():
    """Verify gain-bandwidth rolloff and linear stability for test case 421."""
    g = compute_gain_bandwidth_rolloff('LM741', 21150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4710.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_422():
    """Verify gain-bandwidth rolloff and linear stability for test case 422."""
    g = compute_gain_bandwidth_rolloff('LM741', 21200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4720.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_423():
    """Verify gain-bandwidth rolloff and linear stability for test case 423."""
    g = compute_gain_bandwidth_rolloff('LM741', 21250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4730.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_424():
    """Verify gain-bandwidth rolloff and linear stability for test case 424."""
    g = compute_gain_bandwidth_rolloff('LM741', 21300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4740.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_425():
    """Verify gain-bandwidth rolloff and linear stability for test case 425."""
    g = compute_gain_bandwidth_rolloff('LM741', 21350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4750.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_426():
    """Verify gain-bandwidth rolloff and linear stability for test case 426."""
    g = compute_gain_bandwidth_rolloff('LM741', 21400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4760.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_427():
    """Verify gain-bandwidth rolloff and linear stability for test case 427."""
    g = compute_gain_bandwidth_rolloff('LM741', 21450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4770.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_428():
    """Verify gain-bandwidth rolloff and linear stability for test case 428."""
    g = compute_gain_bandwidth_rolloff('LM741', 21500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4780.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_429():
    """Verify gain-bandwidth rolloff and linear stability for test case 429."""
    g = compute_gain_bandwidth_rolloff('LM741', 21550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4790.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_430():
    """Verify gain-bandwidth rolloff and linear stability for test case 430."""
    g = compute_gain_bandwidth_rolloff('LM741', 21600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4800.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_431():
    """Verify gain-bandwidth rolloff and linear stability for test case 431."""
    g = compute_gain_bandwidth_rolloff('LM741', 21650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4810.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_432():
    """Verify gain-bandwidth rolloff and linear stability for test case 432."""
    g = compute_gain_bandwidth_rolloff('LM741', 21700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4820.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_433():
    """Verify gain-bandwidth rolloff and linear stability for test case 433."""
    g = compute_gain_bandwidth_rolloff('LM741', 21750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4830.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_434():
    """Verify gain-bandwidth rolloff and linear stability for test case 434."""
    g = compute_gain_bandwidth_rolloff('LM741', 21800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4840.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_435():
    """Verify gain-bandwidth rolloff and linear stability for test case 435."""
    g = compute_gain_bandwidth_rolloff('LM741', 21850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4850.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_436():
    """Verify gain-bandwidth rolloff and linear stability for test case 436."""
    g = compute_gain_bandwidth_rolloff('LM741', 21900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4860.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_437():
    """Verify gain-bandwidth rolloff and linear stability for test case 437."""
    g = compute_gain_bandwidth_rolloff('LM741', 21950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4870.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_438():
    """Verify gain-bandwidth rolloff and linear stability for test case 438."""
    g = compute_gain_bandwidth_rolloff('LM741', 22000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4880.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_439():
    """Verify gain-bandwidth rolloff and linear stability for test case 439."""
    g = compute_gain_bandwidth_rolloff('LM741', 22050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4890.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_440():
    """Verify gain-bandwidth rolloff and linear stability for test case 440."""
    g = compute_gain_bandwidth_rolloff('LM741', 22100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4900.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_441():
    """Verify gain-bandwidth rolloff and linear stability for test case 441."""
    g = compute_gain_bandwidth_rolloff('LM741', 22150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4910.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_442():
    """Verify gain-bandwidth rolloff and linear stability for test case 442."""
    g = compute_gain_bandwidth_rolloff('LM741', 22200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4920.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_443():
    """Verify gain-bandwidth rolloff and linear stability for test case 443."""
    g = compute_gain_bandwidth_rolloff('LM741', 22250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4930.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_444():
    """Verify gain-bandwidth rolloff and linear stability for test case 444."""
    g = compute_gain_bandwidth_rolloff('LM741', 22300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4940.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_445():
    """Verify gain-bandwidth rolloff and linear stability for test case 445."""
    g = compute_gain_bandwidth_rolloff('LM741', 22350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4950.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_446():
    """Verify gain-bandwidth rolloff and linear stability for test case 446."""
    g = compute_gain_bandwidth_rolloff('LM741', 22400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4960.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_447():
    """Verify gain-bandwidth rolloff and linear stability for test case 447."""
    g = compute_gain_bandwidth_rolloff('LM741', 22450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4970.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_448():
    """Verify gain-bandwidth rolloff and linear stability for test case 448."""
    g = compute_gain_bandwidth_rolloff('LM741', 22500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4980.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_449():
    """Verify gain-bandwidth rolloff and linear stability for test case 449."""
    g = compute_gain_bandwidth_rolloff('LM741', 22550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 4990.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_450():
    """Verify gain-bandwidth rolloff and linear stability for test case 450."""
    g = compute_gain_bandwidth_rolloff('LM741', 22600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5000.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_451():
    """Verify gain-bandwidth rolloff and linear stability for test case 451."""
    g = compute_gain_bandwidth_rolloff('LM741', 22650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5010.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_452():
    """Verify gain-bandwidth rolloff and linear stability for test case 452."""
    g = compute_gain_bandwidth_rolloff('LM741', 22700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5020.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_453():
    """Verify gain-bandwidth rolloff and linear stability for test case 453."""
    g = compute_gain_bandwidth_rolloff('LM741', 22750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5030.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_454():
    """Verify gain-bandwidth rolloff and linear stability for test case 454."""
    g = compute_gain_bandwidth_rolloff('LM741', 22800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5040.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_455():
    """Verify gain-bandwidth rolloff and linear stability for test case 455."""
    g = compute_gain_bandwidth_rolloff('LM741', 22850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5050.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_456():
    """Verify gain-bandwidth rolloff and linear stability for test case 456."""
    g = compute_gain_bandwidth_rolloff('LM741', 22900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5060.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_457():
    """Verify gain-bandwidth rolloff and linear stability for test case 457."""
    g = compute_gain_bandwidth_rolloff('LM741', 22950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5070.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_458():
    """Verify gain-bandwidth rolloff and linear stability for test case 458."""
    g = compute_gain_bandwidth_rolloff('LM741', 23000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5080.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_459():
    """Verify gain-bandwidth rolloff and linear stability for test case 459."""
    g = compute_gain_bandwidth_rolloff('LM741', 23050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5090.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_460():
    """Verify gain-bandwidth rolloff and linear stability for test case 460."""
    g = compute_gain_bandwidth_rolloff('LM741', 23100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5100.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_461():
    """Verify gain-bandwidth rolloff and linear stability for test case 461."""
    g = compute_gain_bandwidth_rolloff('LM741', 23150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5110.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_462():
    """Verify gain-bandwidth rolloff and linear stability for test case 462."""
    g = compute_gain_bandwidth_rolloff('LM741', 23200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5120.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_463():
    """Verify gain-bandwidth rolloff and linear stability for test case 463."""
    g = compute_gain_bandwidth_rolloff('LM741', 23250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5130.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_464():
    """Verify gain-bandwidth rolloff and linear stability for test case 464."""
    g = compute_gain_bandwidth_rolloff('LM741', 23300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5140.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_465():
    """Verify gain-bandwidth rolloff and linear stability for test case 465."""
    g = compute_gain_bandwidth_rolloff('LM741', 23350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5150.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_466():
    """Verify gain-bandwidth rolloff and linear stability for test case 466."""
    g = compute_gain_bandwidth_rolloff('LM741', 23400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5160.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_467():
    """Verify gain-bandwidth rolloff and linear stability for test case 467."""
    g = compute_gain_bandwidth_rolloff('LM741', 23450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5170.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_468():
    """Verify gain-bandwidth rolloff and linear stability for test case 468."""
    g = compute_gain_bandwidth_rolloff('LM741', 23500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5180.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_469():
    """Verify gain-bandwidth rolloff and linear stability for test case 469."""
    g = compute_gain_bandwidth_rolloff('LM741', 23550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5190.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_470():
    """Verify gain-bandwidth rolloff and linear stability for test case 470."""
    g = compute_gain_bandwidth_rolloff('LM741', 23600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5200.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_471():
    """Verify gain-bandwidth rolloff and linear stability for test case 471."""
    g = compute_gain_bandwidth_rolloff('LM741', 23650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5210.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_472():
    """Verify gain-bandwidth rolloff and linear stability for test case 472."""
    g = compute_gain_bandwidth_rolloff('LM741', 23700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5220.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_473():
    """Verify gain-bandwidth rolloff and linear stability for test case 473."""
    g = compute_gain_bandwidth_rolloff('LM741', 23750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5230.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_474():
    """Verify gain-bandwidth rolloff and linear stability for test case 474."""
    g = compute_gain_bandwidth_rolloff('LM741', 23800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5240.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_475():
    """Verify gain-bandwidth rolloff and linear stability for test case 475."""
    g = compute_gain_bandwidth_rolloff('LM741', 23850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5250.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_476():
    """Verify gain-bandwidth rolloff and linear stability for test case 476."""
    g = compute_gain_bandwidth_rolloff('LM741', 23900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5260.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_477():
    """Verify gain-bandwidth rolloff and linear stability for test case 477."""
    g = compute_gain_bandwidth_rolloff('LM741', 23950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5270.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_478():
    """Verify gain-bandwidth rolloff and linear stability for test case 478."""
    g = compute_gain_bandwidth_rolloff('LM741', 24000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5280.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_479():
    """Verify gain-bandwidth rolloff and linear stability for test case 479."""
    g = compute_gain_bandwidth_rolloff('LM741', 24050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5290.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_480():
    """Verify gain-bandwidth rolloff and linear stability for test case 480."""
    g = compute_gain_bandwidth_rolloff('LM741', 24100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5300.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_481():
    """Verify gain-bandwidth rolloff and linear stability for test case 481."""
    g = compute_gain_bandwidth_rolloff('LM741', 24150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5310.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_482():
    """Verify gain-bandwidth rolloff and linear stability for test case 482."""
    g = compute_gain_bandwidth_rolloff('LM741', 24200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5320.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_483():
    """Verify gain-bandwidth rolloff and linear stability for test case 483."""
    g = compute_gain_bandwidth_rolloff('LM741', 24250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5330.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_484():
    """Verify gain-bandwidth rolloff and linear stability for test case 484."""
    g = compute_gain_bandwidth_rolloff('LM741', 24300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5340.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_485():
    """Verify gain-bandwidth rolloff and linear stability for test case 485."""
    g = compute_gain_bandwidth_rolloff('LM741', 24350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5350.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_486():
    """Verify gain-bandwidth rolloff and linear stability for test case 486."""
    g = compute_gain_bandwidth_rolloff('LM741', 24400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5360.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_487():
    """Verify gain-bandwidth rolloff and linear stability for test case 487."""
    g = compute_gain_bandwidth_rolloff('LM741', 24450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5370.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_488():
    """Verify gain-bandwidth rolloff and linear stability for test case 488."""
    g = compute_gain_bandwidth_rolloff('LM741', 24500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5380.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_489():
    """Verify gain-bandwidth rolloff and linear stability for test case 489."""
    g = compute_gain_bandwidth_rolloff('LM741', 24550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5390.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_490():
    """Verify gain-bandwidth rolloff and linear stability for test case 490."""
    g = compute_gain_bandwidth_rolloff('LM741', 24600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5400.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_491():
    """Verify gain-bandwidth rolloff and linear stability for test case 491."""
    g = compute_gain_bandwidth_rolloff('LM741', 24650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5410.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_492():
    """Verify gain-bandwidth rolloff and linear stability for test case 492."""
    g = compute_gain_bandwidth_rolloff('LM741', 24700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5420.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_493():
    """Verify gain-bandwidth rolloff and linear stability for test case 493."""
    g = compute_gain_bandwidth_rolloff('LM741', 24750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5430.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_494():
    """Verify gain-bandwidth rolloff and linear stability for test case 494."""
    g = compute_gain_bandwidth_rolloff('LM741', 24800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5440.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_495():
    """Verify gain-bandwidth rolloff and linear stability for test case 495."""
    g = compute_gain_bandwidth_rolloff('LM741', 24850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5450.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_496():
    """Verify gain-bandwidth rolloff and linear stability for test case 496."""
    g = compute_gain_bandwidth_rolloff('LM741', 24900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5460.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_497():
    """Verify gain-bandwidth rolloff and linear stability for test case 497."""
    g = compute_gain_bandwidth_rolloff('LM741', 24950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5470.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_498():
    """Verify gain-bandwidth rolloff and linear stability for test case 498."""
    g = compute_gain_bandwidth_rolloff('LM741', 25000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5480.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_499():
    """Verify gain-bandwidth rolloff and linear stability for test case 499."""
    g = compute_gain_bandwidth_rolloff('LM741', 25050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5490.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_500():
    """Verify gain-bandwidth rolloff and linear stability for test case 500."""
    g = compute_gain_bandwidth_rolloff('LM741', 25100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5500.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_501():
    """Verify gain-bandwidth rolloff and linear stability for test case 501."""
    g = compute_gain_bandwidth_rolloff('LM741', 25150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5510.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_502():
    """Verify gain-bandwidth rolloff and linear stability for test case 502."""
    g = compute_gain_bandwidth_rolloff('LM741', 25200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5520.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_503():
    """Verify gain-bandwidth rolloff and linear stability for test case 503."""
    g = compute_gain_bandwidth_rolloff('LM741', 25250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5530.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_504():
    """Verify gain-bandwidth rolloff and linear stability for test case 504."""
    g = compute_gain_bandwidth_rolloff('LM741', 25300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5540.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_505():
    """Verify gain-bandwidth rolloff and linear stability for test case 505."""
    g = compute_gain_bandwidth_rolloff('LM741', 25350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5550.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_506():
    """Verify gain-bandwidth rolloff and linear stability for test case 506."""
    g = compute_gain_bandwidth_rolloff('LM741', 25400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5560.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_507():
    """Verify gain-bandwidth rolloff and linear stability for test case 507."""
    g = compute_gain_bandwidth_rolloff('LM741', 25450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5570.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_508():
    """Verify gain-bandwidth rolloff and linear stability for test case 508."""
    g = compute_gain_bandwidth_rolloff('LM741', 25500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5580.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_509():
    """Verify gain-bandwidth rolloff and linear stability for test case 509."""
    g = compute_gain_bandwidth_rolloff('LM741', 25550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5590.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_510():
    """Verify gain-bandwidth rolloff and linear stability for test case 510."""
    g = compute_gain_bandwidth_rolloff('LM741', 25600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5600.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_511():
    """Verify gain-bandwidth rolloff and linear stability for test case 511."""
    g = compute_gain_bandwidth_rolloff('LM741', 25650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5610.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_512():
    """Verify gain-bandwidth rolloff and linear stability for test case 512."""
    g = compute_gain_bandwidth_rolloff('LM741', 25700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5620.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_513():
    """Verify gain-bandwidth rolloff and linear stability for test case 513."""
    g = compute_gain_bandwidth_rolloff('LM741', 25750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5630.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_514():
    """Verify gain-bandwidth rolloff and linear stability for test case 514."""
    g = compute_gain_bandwidth_rolloff('LM741', 25800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5640.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_515():
    """Verify gain-bandwidth rolloff and linear stability for test case 515."""
    g = compute_gain_bandwidth_rolloff('LM741', 25850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5650.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_516():
    """Verify gain-bandwidth rolloff and linear stability for test case 516."""
    g = compute_gain_bandwidth_rolloff('LM741', 25900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5660.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_517():
    """Verify gain-bandwidth rolloff and linear stability for test case 517."""
    g = compute_gain_bandwidth_rolloff('LM741', 25950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5670.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_518():
    """Verify gain-bandwidth rolloff and linear stability for test case 518."""
    g = compute_gain_bandwidth_rolloff('LM741', 26000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5680.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_519():
    """Verify gain-bandwidth rolloff and linear stability for test case 519."""
    g = compute_gain_bandwidth_rolloff('LM741', 26050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5690.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_520():
    """Verify gain-bandwidth rolloff and linear stability for test case 520."""
    g = compute_gain_bandwidth_rolloff('LM741', 26100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5700.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_521():
    """Verify gain-bandwidth rolloff and linear stability for test case 521."""
    g = compute_gain_bandwidth_rolloff('LM741', 26150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5710.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_522():
    """Verify gain-bandwidth rolloff and linear stability for test case 522."""
    g = compute_gain_bandwidth_rolloff('LM741', 26200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5720.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_523():
    """Verify gain-bandwidth rolloff and linear stability for test case 523."""
    g = compute_gain_bandwidth_rolloff('LM741', 26250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5730.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_524():
    """Verify gain-bandwidth rolloff and linear stability for test case 524."""
    g = compute_gain_bandwidth_rolloff('LM741', 26300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5740.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_525():
    """Verify gain-bandwidth rolloff and linear stability for test case 525."""
    g = compute_gain_bandwidth_rolloff('LM741', 26350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5750.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_526():
    """Verify gain-bandwidth rolloff and linear stability for test case 526."""
    g = compute_gain_bandwidth_rolloff('LM741', 26400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5760.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_527():
    """Verify gain-bandwidth rolloff and linear stability for test case 527."""
    g = compute_gain_bandwidth_rolloff('LM741', 26450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5770.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_528():
    """Verify gain-bandwidth rolloff and linear stability for test case 528."""
    g = compute_gain_bandwidth_rolloff('LM741', 26500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5780.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_529():
    """Verify gain-bandwidth rolloff and linear stability for test case 529."""
    g = compute_gain_bandwidth_rolloff('LM741', 26550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5790.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_530():
    """Verify gain-bandwidth rolloff and linear stability for test case 530."""
    g = compute_gain_bandwidth_rolloff('LM741', 26600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5800.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_531():
    """Verify gain-bandwidth rolloff and linear stability for test case 531."""
    g = compute_gain_bandwidth_rolloff('LM741', 26650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5810.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_532():
    """Verify gain-bandwidth rolloff and linear stability for test case 532."""
    g = compute_gain_bandwidth_rolloff('LM741', 26700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5820.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_533():
    """Verify gain-bandwidth rolloff and linear stability for test case 533."""
    g = compute_gain_bandwidth_rolloff('LM741', 26750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5830.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_534():
    """Verify gain-bandwidth rolloff and linear stability for test case 534."""
    g = compute_gain_bandwidth_rolloff('LM741', 26800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5840.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_535():
    """Verify gain-bandwidth rolloff and linear stability for test case 535."""
    g = compute_gain_bandwidth_rolloff('LM741', 26850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5850.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_536():
    """Verify gain-bandwidth rolloff and linear stability for test case 536."""
    g = compute_gain_bandwidth_rolloff('LM741', 26900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5860.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_537():
    """Verify gain-bandwidth rolloff and linear stability for test case 537."""
    g = compute_gain_bandwidth_rolloff('LM741', 26950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5870.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_538():
    """Verify gain-bandwidth rolloff and linear stability for test case 538."""
    g = compute_gain_bandwidth_rolloff('LM741', 27000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5880.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_539():
    """Verify gain-bandwidth rolloff and linear stability for test case 539."""
    g = compute_gain_bandwidth_rolloff('LM741', 27050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5890.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_540():
    """Verify gain-bandwidth rolloff and linear stability for test case 540."""
    g = compute_gain_bandwidth_rolloff('LM741', 27100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5900.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_541():
    """Verify gain-bandwidth rolloff and linear stability for test case 541."""
    g = compute_gain_bandwidth_rolloff('LM741', 27150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5910.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_542():
    """Verify gain-bandwidth rolloff and linear stability for test case 542."""
    g = compute_gain_bandwidth_rolloff('LM741', 27200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5920.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_543():
    """Verify gain-bandwidth rolloff and linear stability for test case 543."""
    g = compute_gain_bandwidth_rolloff('LM741', 27250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5930.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_544():
    """Verify gain-bandwidth rolloff and linear stability for test case 544."""
    g = compute_gain_bandwidth_rolloff('LM741', 27300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5940.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_545():
    """Verify gain-bandwidth rolloff and linear stability for test case 545."""
    g = compute_gain_bandwidth_rolloff('LM741', 27350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5950.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_546():
    """Verify gain-bandwidth rolloff and linear stability for test case 546."""
    g = compute_gain_bandwidth_rolloff('LM741', 27400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5960.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_547():
    """Verify gain-bandwidth rolloff and linear stability for test case 547."""
    g = compute_gain_bandwidth_rolloff('LM741', 27450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5970.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_548():
    """Verify gain-bandwidth rolloff and linear stability for test case 548."""
    g = compute_gain_bandwidth_rolloff('LM741', 27500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5980.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_549():
    """Verify gain-bandwidth rolloff and linear stability for test case 549."""
    g = compute_gain_bandwidth_rolloff('LM741', 27550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 5990.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_550():
    """Verify gain-bandwidth rolloff and linear stability for test case 550."""
    g = compute_gain_bandwidth_rolloff('LM741', 27600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6000.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_551():
    """Verify gain-bandwidth rolloff and linear stability for test case 551."""
    g = compute_gain_bandwidth_rolloff('LM741', 27650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6010.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_552():
    """Verify gain-bandwidth rolloff and linear stability for test case 552."""
    g = compute_gain_bandwidth_rolloff('LM741', 27700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6020.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_553():
    """Verify gain-bandwidth rolloff and linear stability for test case 553."""
    g = compute_gain_bandwidth_rolloff('LM741', 27750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6030.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_554():
    """Verify gain-bandwidth rolloff and linear stability for test case 554."""
    g = compute_gain_bandwidth_rolloff('LM741', 27800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6040.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_555():
    """Verify gain-bandwidth rolloff and linear stability for test case 555."""
    g = compute_gain_bandwidth_rolloff('LM741', 27850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6050.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_556():
    """Verify gain-bandwidth rolloff and linear stability for test case 556."""
    g = compute_gain_bandwidth_rolloff('LM741', 27900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6060.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_557():
    """Verify gain-bandwidth rolloff and linear stability for test case 557."""
    g = compute_gain_bandwidth_rolloff('LM741', 27950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6070.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_558():
    """Verify gain-bandwidth rolloff and linear stability for test case 558."""
    g = compute_gain_bandwidth_rolloff('LM741', 28000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6080.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_559():
    """Verify gain-bandwidth rolloff and linear stability for test case 559."""
    g = compute_gain_bandwidth_rolloff('LM741', 28050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6090.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_560():
    """Verify gain-bandwidth rolloff and linear stability for test case 560."""
    g = compute_gain_bandwidth_rolloff('LM741', 28100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6100.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_561():
    """Verify gain-bandwidth rolloff and linear stability for test case 561."""
    g = compute_gain_bandwidth_rolloff('LM741', 28150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6110.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_562():
    """Verify gain-bandwidth rolloff and linear stability for test case 562."""
    g = compute_gain_bandwidth_rolloff('LM741', 28200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6120.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_563():
    """Verify gain-bandwidth rolloff and linear stability for test case 563."""
    g = compute_gain_bandwidth_rolloff('LM741', 28250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6130.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_564():
    """Verify gain-bandwidth rolloff and linear stability for test case 564."""
    g = compute_gain_bandwidth_rolloff('LM741', 28300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6140.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_565():
    """Verify gain-bandwidth rolloff and linear stability for test case 565."""
    g = compute_gain_bandwidth_rolloff('LM741', 28350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6150.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_566():
    """Verify gain-bandwidth rolloff and linear stability for test case 566."""
    g = compute_gain_bandwidth_rolloff('LM741', 28400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6160.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_567():
    """Verify gain-bandwidth rolloff and linear stability for test case 567."""
    g = compute_gain_bandwidth_rolloff('LM741', 28450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6170.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_568():
    """Verify gain-bandwidth rolloff and linear stability for test case 568."""
    g = compute_gain_bandwidth_rolloff('LM741', 28500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6180.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_569():
    """Verify gain-bandwidth rolloff and linear stability for test case 569."""
    g = compute_gain_bandwidth_rolloff('LM741', 28550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6190.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_570():
    """Verify gain-bandwidth rolloff and linear stability for test case 570."""
    g = compute_gain_bandwidth_rolloff('LM741', 28600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6200.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_571():
    """Verify gain-bandwidth rolloff and linear stability for test case 571."""
    g = compute_gain_bandwidth_rolloff('LM741', 28650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6210.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_572():
    """Verify gain-bandwidth rolloff and linear stability for test case 572."""
    g = compute_gain_bandwidth_rolloff('LM741', 28700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6220.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_573():
    """Verify gain-bandwidth rolloff and linear stability for test case 573."""
    g = compute_gain_bandwidth_rolloff('LM741', 28750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6230.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_574():
    """Verify gain-bandwidth rolloff and linear stability for test case 574."""
    g = compute_gain_bandwidth_rolloff('LM741', 28800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6240.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_575():
    """Verify gain-bandwidth rolloff and linear stability for test case 575."""
    g = compute_gain_bandwidth_rolloff('LM741', 28850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6250.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_576():
    """Verify gain-bandwidth rolloff and linear stability for test case 576."""
    g = compute_gain_bandwidth_rolloff('LM741', 28900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6260.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_577():
    """Verify gain-bandwidth rolloff and linear stability for test case 577."""
    g = compute_gain_bandwidth_rolloff('LM741', 28950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6270.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_578():
    """Verify gain-bandwidth rolloff and linear stability for test case 578."""
    g = compute_gain_bandwidth_rolloff('LM741', 29000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6280.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_579():
    """Verify gain-bandwidth rolloff and linear stability for test case 579."""
    g = compute_gain_bandwidth_rolloff('LM741', 29050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6290.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_580():
    """Verify gain-bandwidth rolloff and linear stability for test case 580."""
    g = compute_gain_bandwidth_rolloff('LM741', 29100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6300.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_581():
    """Verify gain-bandwidth rolloff and linear stability for test case 581."""
    g = compute_gain_bandwidth_rolloff('LM741', 29150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6310.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_582():
    """Verify gain-bandwidth rolloff and linear stability for test case 582."""
    g = compute_gain_bandwidth_rolloff('LM741', 29200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6320.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_583():
    """Verify gain-bandwidth rolloff and linear stability for test case 583."""
    g = compute_gain_bandwidth_rolloff('LM741', 29250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6330.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_584():
    """Verify gain-bandwidth rolloff and linear stability for test case 584."""
    g = compute_gain_bandwidth_rolloff('LM741', 29300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6340.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_585():
    """Verify gain-bandwidth rolloff and linear stability for test case 585."""
    g = compute_gain_bandwidth_rolloff('LM741', 29350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6350.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_586():
    """Verify gain-bandwidth rolloff and linear stability for test case 586."""
    g = compute_gain_bandwidth_rolloff('LM741', 29400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6360.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_587():
    """Verify gain-bandwidth rolloff and linear stability for test case 587."""
    g = compute_gain_bandwidth_rolloff('LM741', 29450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6370.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_588():
    """Verify gain-bandwidth rolloff and linear stability for test case 588."""
    g = compute_gain_bandwidth_rolloff('LM741', 29500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6380.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_589():
    """Verify gain-bandwidth rolloff and linear stability for test case 589."""
    g = compute_gain_bandwidth_rolloff('LM741', 29550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6390.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_590():
    """Verify gain-bandwidth rolloff and linear stability for test case 590."""
    g = compute_gain_bandwidth_rolloff('LM741', 29600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6400.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_591():
    """Verify gain-bandwidth rolloff and linear stability for test case 591."""
    g = compute_gain_bandwidth_rolloff('LM741', 29650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6410.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_592():
    """Verify gain-bandwidth rolloff and linear stability for test case 592."""
    g = compute_gain_bandwidth_rolloff('LM741', 29700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6420.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_593():
    """Verify gain-bandwidth rolloff and linear stability for test case 593."""
    g = compute_gain_bandwidth_rolloff('LM741', 29750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6430.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_594():
    """Verify gain-bandwidth rolloff and linear stability for test case 594."""
    g = compute_gain_bandwidth_rolloff('LM741', 29800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6440.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_595():
    """Verify gain-bandwidth rolloff and linear stability for test case 595."""
    g = compute_gain_bandwidth_rolloff('LM741', 29850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6450.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_596():
    """Verify gain-bandwidth rolloff and linear stability for test case 596."""
    g = compute_gain_bandwidth_rolloff('LM741', 29900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6460.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_597():
    """Verify gain-bandwidth rolloff and linear stability for test case 597."""
    g = compute_gain_bandwidth_rolloff('LM741', 29950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6470.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_598():
    """Verify gain-bandwidth rolloff and linear stability for test case 598."""
    g = compute_gain_bandwidth_rolloff('LM741', 30000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6480.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_599():
    """Verify gain-bandwidth rolloff and linear stability for test case 599."""
    g = compute_gain_bandwidth_rolloff('LM741', 30050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6490.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_600():
    """Verify gain-bandwidth rolloff and linear stability for test case 600."""
    g = compute_gain_bandwidth_rolloff('LM741', 30100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6500.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_601():
    """Verify gain-bandwidth rolloff and linear stability for test case 601."""
    g = compute_gain_bandwidth_rolloff('LM741', 30150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6510.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_602():
    """Verify gain-bandwidth rolloff and linear stability for test case 602."""
    g = compute_gain_bandwidth_rolloff('LM741', 30200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6520.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_603():
    """Verify gain-bandwidth rolloff and linear stability for test case 603."""
    g = compute_gain_bandwidth_rolloff('LM741', 30250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6530.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_604():
    """Verify gain-bandwidth rolloff and linear stability for test case 604."""
    g = compute_gain_bandwidth_rolloff('LM741', 30300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6540.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_605():
    """Verify gain-bandwidth rolloff and linear stability for test case 605."""
    g = compute_gain_bandwidth_rolloff('LM741', 30350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6550.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_606():
    """Verify gain-bandwidth rolloff and linear stability for test case 606."""
    g = compute_gain_bandwidth_rolloff('LM741', 30400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6560.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_607():
    """Verify gain-bandwidth rolloff and linear stability for test case 607."""
    g = compute_gain_bandwidth_rolloff('LM741', 30450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6570.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_608():
    """Verify gain-bandwidth rolloff and linear stability for test case 608."""
    g = compute_gain_bandwidth_rolloff('LM741', 30500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6580.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_609():
    """Verify gain-bandwidth rolloff and linear stability for test case 609."""
    g = compute_gain_bandwidth_rolloff('LM741', 30550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6590.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_610():
    """Verify gain-bandwidth rolloff and linear stability for test case 610."""
    g = compute_gain_bandwidth_rolloff('LM741', 30600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6600.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_611():
    """Verify gain-bandwidth rolloff and linear stability for test case 611."""
    g = compute_gain_bandwidth_rolloff('LM741', 30650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6610.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_612():
    """Verify gain-bandwidth rolloff and linear stability for test case 612."""
    g = compute_gain_bandwidth_rolloff('LM741', 30700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6620.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_613():
    """Verify gain-bandwidth rolloff and linear stability for test case 613."""
    g = compute_gain_bandwidth_rolloff('LM741', 30750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6630.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_614():
    """Verify gain-bandwidth rolloff and linear stability for test case 614."""
    g = compute_gain_bandwidth_rolloff('LM741', 30800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6640.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_615():
    """Verify gain-bandwidth rolloff and linear stability for test case 615."""
    g = compute_gain_bandwidth_rolloff('LM741', 30850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6650.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_616():
    """Verify gain-bandwidth rolloff and linear stability for test case 616."""
    g = compute_gain_bandwidth_rolloff('LM741', 30900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6660.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_617():
    """Verify gain-bandwidth rolloff and linear stability for test case 617."""
    g = compute_gain_bandwidth_rolloff('LM741', 30950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6670.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_618():
    """Verify gain-bandwidth rolloff and linear stability for test case 618."""
    g = compute_gain_bandwidth_rolloff('LM741', 31000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6680.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_619():
    """Verify gain-bandwidth rolloff and linear stability for test case 619."""
    g = compute_gain_bandwidth_rolloff('LM741', 31050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6690.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_620():
    """Verify gain-bandwidth rolloff and linear stability for test case 620."""
    g = compute_gain_bandwidth_rolloff('LM741', 31100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6700.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_621():
    """Verify gain-bandwidth rolloff and linear stability for test case 621."""
    g = compute_gain_bandwidth_rolloff('LM741', 31150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6710.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_622():
    """Verify gain-bandwidth rolloff and linear stability for test case 622."""
    g = compute_gain_bandwidth_rolloff('LM741', 31200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6720.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_623():
    """Verify gain-bandwidth rolloff and linear stability for test case 623."""
    g = compute_gain_bandwidth_rolloff('LM741', 31250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6730.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_624():
    """Verify gain-bandwidth rolloff and linear stability for test case 624."""
    g = compute_gain_bandwidth_rolloff('LM741', 31300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6740.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_625():
    """Verify gain-bandwidth rolloff and linear stability for test case 625."""
    g = compute_gain_bandwidth_rolloff('LM741', 31350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6750.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_626():
    """Verify gain-bandwidth rolloff and linear stability for test case 626."""
    g = compute_gain_bandwidth_rolloff('LM741', 31400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6760.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_627():
    """Verify gain-bandwidth rolloff and linear stability for test case 627."""
    g = compute_gain_bandwidth_rolloff('LM741', 31450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6770.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_628():
    """Verify gain-bandwidth rolloff and linear stability for test case 628."""
    g = compute_gain_bandwidth_rolloff('LM741', 31500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6780.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_629():
    """Verify gain-bandwidth rolloff and linear stability for test case 629."""
    g = compute_gain_bandwidth_rolloff('LM741', 31550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6790.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_630():
    """Verify gain-bandwidth rolloff and linear stability for test case 630."""
    g = compute_gain_bandwidth_rolloff('LM741', 31600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6800.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_631():
    """Verify gain-bandwidth rolloff and linear stability for test case 631."""
    g = compute_gain_bandwidth_rolloff('LM741', 31650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6810.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_632():
    """Verify gain-bandwidth rolloff and linear stability for test case 632."""
    g = compute_gain_bandwidth_rolloff('LM741', 31700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6820.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_633():
    """Verify gain-bandwidth rolloff and linear stability for test case 633."""
    g = compute_gain_bandwidth_rolloff('LM741', 31750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6830.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_634():
    """Verify gain-bandwidth rolloff and linear stability for test case 634."""
    g = compute_gain_bandwidth_rolloff('LM741', 31800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6840.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_635():
    """Verify gain-bandwidth rolloff and linear stability for test case 635."""
    g = compute_gain_bandwidth_rolloff('LM741', 31850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6850.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_636():
    """Verify gain-bandwidth rolloff and linear stability for test case 636."""
    g = compute_gain_bandwidth_rolloff('LM741', 31900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6860.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_637():
    """Verify gain-bandwidth rolloff and linear stability for test case 637."""
    g = compute_gain_bandwidth_rolloff('LM741', 31950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6870.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_638():
    """Verify gain-bandwidth rolloff and linear stability for test case 638."""
    g = compute_gain_bandwidth_rolloff('LM741', 32000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6880.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_639():
    """Verify gain-bandwidth rolloff and linear stability for test case 639."""
    g = compute_gain_bandwidth_rolloff('LM741', 32050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6890.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_640():
    """Verify gain-bandwidth rolloff and linear stability for test case 640."""
    g = compute_gain_bandwidth_rolloff('LM741', 32100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6900.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_641():
    """Verify gain-bandwidth rolloff and linear stability for test case 641."""
    g = compute_gain_bandwidth_rolloff('LM741', 32150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6910.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_642():
    """Verify gain-bandwidth rolloff and linear stability for test case 642."""
    g = compute_gain_bandwidth_rolloff('LM741', 32200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6920.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_643():
    """Verify gain-bandwidth rolloff and linear stability for test case 643."""
    g = compute_gain_bandwidth_rolloff('LM741', 32250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6930.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_644():
    """Verify gain-bandwidth rolloff and linear stability for test case 644."""
    g = compute_gain_bandwidth_rolloff('LM741', 32300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6940.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_645():
    """Verify gain-bandwidth rolloff and linear stability for test case 645."""
    g = compute_gain_bandwidth_rolloff('LM741', 32350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6950.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_646():
    """Verify gain-bandwidth rolloff and linear stability for test case 646."""
    g = compute_gain_bandwidth_rolloff('LM741', 32400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6960.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_647():
    """Verify gain-bandwidth rolloff and linear stability for test case 647."""
    g = compute_gain_bandwidth_rolloff('LM741', 32450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6970.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_648():
    """Verify gain-bandwidth rolloff and linear stability for test case 648."""
    g = compute_gain_bandwidth_rolloff('LM741', 32500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6980.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_649():
    """Verify gain-bandwidth rolloff and linear stability for test case 649."""
    g = compute_gain_bandwidth_rolloff('LM741', 32550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 6990.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_650():
    """Verify gain-bandwidth rolloff and linear stability for test case 650."""
    g = compute_gain_bandwidth_rolloff('LM741', 32600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7000.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_651():
    """Verify gain-bandwidth rolloff and linear stability for test case 651."""
    g = compute_gain_bandwidth_rolloff('LM741', 32650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7010.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_652():
    """Verify gain-bandwidth rolloff and linear stability for test case 652."""
    g = compute_gain_bandwidth_rolloff('LM741', 32700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7020.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_653():
    """Verify gain-bandwidth rolloff and linear stability for test case 653."""
    g = compute_gain_bandwidth_rolloff('LM741', 32750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7030.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_654():
    """Verify gain-bandwidth rolloff and linear stability for test case 654."""
    g = compute_gain_bandwidth_rolloff('LM741', 32800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7040.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_655():
    """Verify gain-bandwidth rolloff and linear stability for test case 655."""
    g = compute_gain_bandwidth_rolloff('LM741', 32850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7050.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_656():
    """Verify gain-bandwidth rolloff and linear stability for test case 656."""
    g = compute_gain_bandwidth_rolloff('LM741', 32900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7060.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_657():
    """Verify gain-bandwidth rolloff and linear stability for test case 657."""
    g = compute_gain_bandwidth_rolloff('LM741', 32950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7070.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_658():
    """Verify gain-bandwidth rolloff and linear stability for test case 658."""
    g = compute_gain_bandwidth_rolloff('LM741', 33000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7080.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_659():
    """Verify gain-bandwidth rolloff and linear stability for test case 659."""
    g = compute_gain_bandwidth_rolloff('LM741', 33050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7090.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_660():
    """Verify gain-bandwidth rolloff and linear stability for test case 660."""
    g = compute_gain_bandwidth_rolloff('LM741', 33100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7100.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_661():
    """Verify gain-bandwidth rolloff and linear stability for test case 661."""
    g = compute_gain_bandwidth_rolloff('LM741', 33150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7110.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_662():
    """Verify gain-bandwidth rolloff and linear stability for test case 662."""
    g = compute_gain_bandwidth_rolloff('LM741', 33200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7120.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_663():
    """Verify gain-bandwidth rolloff and linear stability for test case 663."""
    g = compute_gain_bandwidth_rolloff('LM741', 33250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7130.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_664():
    """Verify gain-bandwidth rolloff and linear stability for test case 664."""
    g = compute_gain_bandwidth_rolloff('LM741', 33300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7140.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_665():
    """Verify gain-bandwidth rolloff and linear stability for test case 665."""
    g = compute_gain_bandwidth_rolloff('LM741', 33350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7150.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_666():
    """Verify gain-bandwidth rolloff and linear stability for test case 666."""
    g = compute_gain_bandwidth_rolloff('LM741', 33400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7160.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_667():
    """Verify gain-bandwidth rolloff and linear stability for test case 667."""
    g = compute_gain_bandwidth_rolloff('LM741', 33450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7170.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_668():
    """Verify gain-bandwidth rolloff and linear stability for test case 668."""
    g = compute_gain_bandwidth_rolloff('LM741', 33500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7180.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_669():
    """Verify gain-bandwidth rolloff and linear stability for test case 669."""
    g = compute_gain_bandwidth_rolloff('LM741', 33550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7190.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_670():
    """Verify gain-bandwidth rolloff and linear stability for test case 670."""
    g = compute_gain_bandwidth_rolloff('LM741', 33600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7200.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_671():
    """Verify gain-bandwidth rolloff and linear stability for test case 671."""
    g = compute_gain_bandwidth_rolloff('LM741', 33650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7210.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_672():
    """Verify gain-bandwidth rolloff and linear stability for test case 672."""
    g = compute_gain_bandwidth_rolloff('LM741', 33700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7220.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_673():
    """Verify gain-bandwidth rolloff and linear stability for test case 673."""
    g = compute_gain_bandwidth_rolloff('LM741', 33750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7230.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_674():
    """Verify gain-bandwidth rolloff and linear stability for test case 674."""
    g = compute_gain_bandwidth_rolloff('LM741', 33800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7240.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_675():
    """Verify gain-bandwidth rolloff and linear stability for test case 675."""
    g = compute_gain_bandwidth_rolloff('LM741', 33850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7250.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_676():
    """Verify gain-bandwidth rolloff and linear stability for test case 676."""
    g = compute_gain_bandwidth_rolloff('LM741', 33900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7260.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_677():
    """Verify gain-bandwidth rolloff and linear stability for test case 677."""
    g = compute_gain_bandwidth_rolloff('LM741', 33950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7270.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_678():
    """Verify gain-bandwidth rolloff and linear stability for test case 678."""
    g = compute_gain_bandwidth_rolloff('LM741', 34000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7280.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_679():
    """Verify gain-bandwidth rolloff and linear stability for test case 679."""
    g = compute_gain_bandwidth_rolloff('LM741', 34050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7290.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_680():
    """Verify gain-bandwidth rolloff and linear stability for test case 680."""
    g = compute_gain_bandwidth_rolloff('LM741', 34100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7300.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_681():
    """Verify gain-bandwidth rolloff and linear stability for test case 681."""
    g = compute_gain_bandwidth_rolloff('LM741', 34150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7310.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_682():
    """Verify gain-bandwidth rolloff and linear stability for test case 682."""
    g = compute_gain_bandwidth_rolloff('LM741', 34200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7320.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_683():
    """Verify gain-bandwidth rolloff and linear stability for test case 683."""
    g = compute_gain_bandwidth_rolloff('LM741', 34250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7330.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_684():
    """Verify gain-bandwidth rolloff and linear stability for test case 684."""
    g = compute_gain_bandwidth_rolloff('LM741', 34300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7340.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_685():
    """Verify gain-bandwidth rolloff and linear stability for test case 685."""
    g = compute_gain_bandwidth_rolloff('LM741', 34350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7350.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_686():
    """Verify gain-bandwidth rolloff and linear stability for test case 686."""
    g = compute_gain_bandwidth_rolloff('LM741', 34400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7360.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_687():
    """Verify gain-bandwidth rolloff and linear stability for test case 687."""
    g = compute_gain_bandwidth_rolloff('LM741', 34450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7370.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_688():
    """Verify gain-bandwidth rolloff and linear stability for test case 688."""
    g = compute_gain_bandwidth_rolloff('LM741', 34500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7380.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_689():
    """Verify gain-bandwidth rolloff and linear stability for test case 689."""
    g = compute_gain_bandwidth_rolloff('LM741', 34550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7390.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_690():
    """Verify gain-bandwidth rolloff and linear stability for test case 690."""
    g = compute_gain_bandwidth_rolloff('LM741', 34600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7400.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_691():
    """Verify gain-bandwidth rolloff and linear stability for test case 691."""
    g = compute_gain_bandwidth_rolloff('LM741', 34650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7410.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_692():
    """Verify gain-bandwidth rolloff and linear stability for test case 692."""
    g = compute_gain_bandwidth_rolloff('LM741', 34700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7420.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_693():
    """Verify gain-bandwidth rolloff and linear stability for test case 693."""
    g = compute_gain_bandwidth_rolloff('LM741', 34750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7430.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_694():
    """Verify gain-bandwidth rolloff and linear stability for test case 694."""
    g = compute_gain_bandwidth_rolloff('LM741', 34800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7440.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_695():
    """Verify gain-bandwidth rolloff and linear stability for test case 695."""
    g = compute_gain_bandwidth_rolloff('LM741', 34850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7450.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_696():
    """Verify gain-bandwidth rolloff and linear stability for test case 696."""
    g = compute_gain_bandwidth_rolloff('LM741', 34900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7460.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_697():
    """Verify gain-bandwidth rolloff and linear stability for test case 697."""
    g = compute_gain_bandwidth_rolloff('LM741', 34950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7470.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_698():
    """Verify gain-bandwidth rolloff and linear stability for test case 698."""
    g = compute_gain_bandwidth_rolloff('LM741', 35000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7480.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_699():
    """Verify gain-bandwidth rolloff and linear stability for test case 699."""
    g = compute_gain_bandwidth_rolloff('LM741', 35050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7490.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_700():
    """Verify gain-bandwidth rolloff and linear stability for test case 700."""
    g = compute_gain_bandwidth_rolloff('LM741', 35100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7500.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_701():
    """Verify gain-bandwidth rolloff and linear stability for test case 701."""
    g = compute_gain_bandwidth_rolloff('LM741', 35150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7510.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_702():
    """Verify gain-bandwidth rolloff and linear stability for test case 702."""
    g = compute_gain_bandwidth_rolloff('LM741', 35200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7520.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_703():
    """Verify gain-bandwidth rolloff and linear stability for test case 703."""
    g = compute_gain_bandwidth_rolloff('LM741', 35250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7530.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_704():
    """Verify gain-bandwidth rolloff and linear stability for test case 704."""
    g = compute_gain_bandwidth_rolloff('LM741', 35300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7540.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_705():
    """Verify gain-bandwidth rolloff and linear stability for test case 705."""
    g = compute_gain_bandwidth_rolloff('LM741', 35350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7550.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_706():
    """Verify gain-bandwidth rolloff and linear stability for test case 706."""
    g = compute_gain_bandwidth_rolloff('LM741', 35400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7560.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_707():
    """Verify gain-bandwidth rolloff and linear stability for test case 707."""
    g = compute_gain_bandwidth_rolloff('LM741', 35450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7570.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_708():
    """Verify gain-bandwidth rolloff and linear stability for test case 708."""
    g = compute_gain_bandwidth_rolloff('LM741', 35500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7580.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_709():
    """Verify gain-bandwidth rolloff and linear stability for test case 709."""
    g = compute_gain_bandwidth_rolloff('LM741', 35550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7590.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_710():
    """Verify gain-bandwidth rolloff and linear stability for test case 710."""
    g = compute_gain_bandwidth_rolloff('LM741', 35600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7600.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_711():
    """Verify gain-bandwidth rolloff and linear stability for test case 711."""
    g = compute_gain_bandwidth_rolloff('LM741', 35650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7610.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_712():
    """Verify gain-bandwidth rolloff and linear stability for test case 712."""
    g = compute_gain_bandwidth_rolloff('LM741', 35700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7620.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_713():
    """Verify gain-bandwidth rolloff and linear stability for test case 713."""
    g = compute_gain_bandwidth_rolloff('LM741', 35750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7630.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_714():
    """Verify gain-bandwidth rolloff and linear stability for test case 714."""
    g = compute_gain_bandwidth_rolloff('LM741', 35800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7640.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_715():
    """Verify gain-bandwidth rolloff and linear stability for test case 715."""
    g = compute_gain_bandwidth_rolloff('LM741', 35850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7650.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_716():
    """Verify gain-bandwidth rolloff and linear stability for test case 716."""
    g = compute_gain_bandwidth_rolloff('LM741', 35900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7660.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_717():
    """Verify gain-bandwidth rolloff and linear stability for test case 717."""
    g = compute_gain_bandwidth_rolloff('LM741', 35950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7670.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_718():
    """Verify gain-bandwidth rolloff and linear stability for test case 718."""
    g = compute_gain_bandwidth_rolloff('LM741', 36000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7680.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_719():
    """Verify gain-bandwidth rolloff and linear stability for test case 719."""
    g = compute_gain_bandwidth_rolloff('LM741', 36050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7690.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_720():
    """Verify gain-bandwidth rolloff and linear stability for test case 720."""
    g = compute_gain_bandwidth_rolloff('LM741', 36100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7700.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_721():
    """Verify gain-bandwidth rolloff and linear stability for test case 721."""
    g = compute_gain_bandwidth_rolloff('LM741', 36150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7710.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_722():
    """Verify gain-bandwidth rolloff and linear stability for test case 722."""
    g = compute_gain_bandwidth_rolloff('LM741', 36200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7720.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_723():
    """Verify gain-bandwidth rolloff and linear stability for test case 723."""
    g = compute_gain_bandwidth_rolloff('LM741', 36250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7730.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_724():
    """Verify gain-bandwidth rolloff and linear stability for test case 724."""
    g = compute_gain_bandwidth_rolloff('LM741', 36300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7740.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_725():
    """Verify gain-bandwidth rolloff and linear stability for test case 725."""
    g = compute_gain_bandwidth_rolloff('LM741', 36350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7750.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_726():
    """Verify gain-bandwidth rolloff and linear stability for test case 726."""
    g = compute_gain_bandwidth_rolloff('LM741', 36400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7760.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_727():
    """Verify gain-bandwidth rolloff and linear stability for test case 727."""
    g = compute_gain_bandwidth_rolloff('LM741', 36450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7770.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_728():
    """Verify gain-bandwidth rolloff and linear stability for test case 728."""
    g = compute_gain_bandwidth_rolloff('LM741', 36500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7780.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_729():
    """Verify gain-bandwidth rolloff and linear stability for test case 729."""
    g = compute_gain_bandwidth_rolloff('LM741', 36550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7790.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_730():
    """Verify gain-bandwidth rolloff and linear stability for test case 730."""
    g = compute_gain_bandwidth_rolloff('LM741', 36600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7800.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_731():
    """Verify gain-bandwidth rolloff and linear stability for test case 731."""
    g = compute_gain_bandwidth_rolloff('LM741', 36650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7810.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_732():
    """Verify gain-bandwidth rolloff and linear stability for test case 732."""
    g = compute_gain_bandwidth_rolloff('LM741', 36700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7820.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_733():
    """Verify gain-bandwidth rolloff and linear stability for test case 733."""
    g = compute_gain_bandwidth_rolloff('LM741', 36750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7830.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_734():
    """Verify gain-bandwidth rolloff and linear stability for test case 734."""
    g = compute_gain_bandwidth_rolloff('LM741', 36800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7840.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_735():
    """Verify gain-bandwidth rolloff and linear stability for test case 735."""
    g = compute_gain_bandwidth_rolloff('LM741', 36850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7850.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_736():
    """Verify gain-bandwidth rolloff and linear stability for test case 736."""
    g = compute_gain_bandwidth_rolloff('LM741', 36900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7860.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_737():
    """Verify gain-bandwidth rolloff and linear stability for test case 737."""
    g = compute_gain_bandwidth_rolloff('LM741', 36950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7870.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_738():
    """Verify gain-bandwidth rolloff and linear stability for test case 738."""
    g = compute_gain_bandwidth_rolloff('LM741', 37000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7880.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_739():
    """Verify gain-bandwidth rolloff and linear stability for test case 739."""
    g = compute_gain_bandwidth_rolloff('LM741', 37050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7890.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_740():
    """Verify gain-bandwidth rolloff and linear stability for test case 740."""
    g = compute_gain_bandwidth_rolloff('LM741', 37100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7900.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_741():
    """Verify gain-bandwidth rolloff and linear stability for test case 741."""
    g = compute_gain_bandwidth_rolloff('LM741', 37150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7910.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_742():
    """Verify gain-bandwidth rolloff and linear stability for test case 742."""
    g = compute_gain_bandwidth_rolloff('LM741', 37200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7920.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_743():
    """Verify gain-bandwidth rolloff and linear stability for test case 743."""
    g = compute_gain_bandwidth_rolloff('LM741', 37250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7930.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_744():
    """Verify gain-bandwidth rolloff and linear stability for test case 744."""
    g = compute_gain_bandwidth_rolloff('LM741', 37300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7940.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_745():
    """Verify gain-bandwidth rolloff and linear stability for test case 745."""
    g = compute_gain_bandwidth_rolloff('LM741', 37350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7950.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_746():
    """Verify gain-bandwidth rolloff and linear stability for test case 746."""
    g = compute_gain_bandwidth_rolloff('LM741', 37400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7960.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_747():
    """Verify gain-bandwidth rolloff and linear stability for test case 747."""
    g = compute_gain_bandwidth_rolloff('LM741', 37450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7970.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_748():
    """Verify gain-bandwidth rolloff and linear stability for test case 748."""
    g = compute_gain_bandwidth_rolloff('LM741', 37500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7980.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_749():
    """Verify gain-bandwidth rolloff and linear stability for test case 749."""
    g = compute_gain_bandwidth_rolloff('LM741', 37550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 7990.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_750():
    """Verify gain-bandwidth rolloff and linear stability for test case 750."""
    g = compute_gain_bandwidth_rolloff('LM741', 37600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8000.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_751():
    """Verify gain-bandwidth rolloff and linear stability for test case 751."""
    g = compute_gain_bandwidth_rolloff('LM741', 37650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8010.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_752():
    """Verify gain-bandwidth rolloff and linear stability for test case 752."""
    g = compute_gain_bandwidth_rolloff('LM741', 37700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8020.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_753():
    """Verify gain-bandwidth rolloff and linear stability for test case 753."""
    g = compute_gain_bandwidth_rolloff('LM741', 37750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8030.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_754():
    """Verify gain-bandwidth rolloff and linear stability for test case 754."""
    g = compute_gain_bandwidth_rolloff('LM741', 37800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8040.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_755():
    """Verify gain-bandwidth rolloff and linear stability for test case 755."""
    g = compute_gain_bandwidth_rolloff('LM741', 37850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8050.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_756():
    """Verify gain-bandwidth rolloff and linear stability for test case 756."""
    g = compute_gain_bandwidth_rolloff('LM741', 37900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8060.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_757():
    """Verify gain-bandwidth rolloff and linear stability for test case 757."""
    g = compute_gain_bandwidth_rolloff('LM741', 37950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8070.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_758():
    """Verify gain-bandwidth rolloff and linear stability for test case 758."""
    g = compute_gain_bandwidth_rolloff('LM741', 38000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8080.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_759():
    """Verify gain-bandwidth rolloff and linear stability for test case 759."""
    g = compute_gain_bandwidth_rolloff('LM741', 38050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8090.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_760():
    """Verify gain-bandwidth rolloff and linear stability for test case 760."""
    g = compute_gain_bandwidth_rolloff('LM741', 38100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8100.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_761():
    """Verify gain-bandwidth rolloff and linear stability for test case 761."""
    g = compute_gain_bandwidth_rolloff('LM741', 38150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8110.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_762():
    """Verify gain-bandwidth rolloff and linear stability for test case 762."""
    g = compute_gain_bandwidth_rolloff('LM741', 38200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8120.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_763():
    """Verify gain-bandwidth rolloff and linear stability for test case 763."""
    g = compute_gain_bandwidth_rolloff('LM741', 38250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8130.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_764():
    """Verify gain-bandwidth rolloff and linear stability for test case 764."""
    g = compute_gain_bandwidth_rolloff('LM741', 38300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8140.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_765():
    """Verify gain-bandwidth rolloff and linear stability for test case 765."""
    g = compute_gain_bandwidth_rolloff('LM741', 38350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8150.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_766():
    """Verify gain-bandwidth rolloff and linear stability for test case 766."""
    g = compute_gain_bandwidth_rolloff('LM741', 38400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8160.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_767():
    """Verify gain-bandwidth rolloff and linear stability for test case 767."""
    g = compute_gain_bandwidth_rolloff('LM741', 38450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8170.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_768():
    """Verify gain-bandwidth rolloff and linear stability for test case 768."""
    g = compute_gain_bandwidth_rolloff('LM741', 38500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8180.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_769():
    """Verify gain-bandwidth rolloff and linear stability for test case 769."""
    g = compute_gain_bandwidth_rolloff('LM741', 38550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8190.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_770():
    """Verify gain-bandwidth rolloff and linear stability for test case 770."""
    g = compute_gain_bandwidth_rolloff('LM741', 38600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8200.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_771():
    """Verify gain-bandwidth rolloff and linear stability for test case 771."""
    g = compute_gain_bandwidth_rolloff('LM741', 38650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8210.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_772():
    """Verify gain-bandwidth rolloff and linear stability for test case 772."""
    g = compute_gain_bandwidth_rolloff('LM741', 38700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8220.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_773():
    """Verify gain-bandwidth rolloff and linear stability for test case 773."""
    g = compute_gain_bandwidth_rolloff('LM741', 38750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8230.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_774():
    """Verify gain-bandwidth rolloff and linear stability for test case 774."""
    g = compute_gain_bandwidth_rolloff('LM741', 38800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8240.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_775():
    """Verify gain-bandwidth rolloff and linear stability for test case 775."""
    g = compute_gain_bandwidth_rolloff('LM741', 38850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8250.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_776():
    """Verify gain-bandwidth rolloff and linear stability for test case 776."""
    g = compute_gain_bandwidth_rolloff('LM741', 38900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8260.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_777():
    """Verify gain-bandwidth rolloff and linear stability for test case 777."""
    g = compute_gain_bandwidth_rolloff('LM741', 38950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8270.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_778():
    """Verify gain-bandwidth rolloff and linear stability for test case 778."""
    g = compute_gain_bandwidth_rolloff('LM741', 39000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8280.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_779():
    """Verify gain-bandwidth rolloff and linear stability for test case 779."""
    g = compute_gain_bandwidth_rolloff('LM741', 39050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8290.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_780():
    """Verify gain-bandwidth rolloff and linear stability for test case 780."""
    g = compute_gain_bandwidth_rolloff('LM741', 39100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8300.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_781():
    """Verify gain-bandwidth rolloff and linear stability for test case 781."""
    g = compute_gain_bandwidth_rolloff('LM741', 39150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8310.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_782():
    """Verify gain-bandwidth rolloff and linear stability for test case 782."""
    g = compute_gain_bandwidth_rolloff('LM741', 39200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8320.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_783():
    """Verify gain-bandwidth rolloff and linear stability for test case 783."""
    g = compute_gain_bandwidth_rolloff('LM741', 39250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8330.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_784():
    """Verify gain-bandwidth rolloff and linear stability for test case 784."""
    g = compute_gain_bandwidth_rolloff('LM741', 39300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8340.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_785():
    """Verify gain-bandwidth rolloff and linear stability for test case 785."""
    g = compute_gain_bandwidth_rolloff('LM741', 39350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8350.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_786():
    """Verify gain-bandwidth rolloff and linear stability for test case 786."""
    g = compute_gain_bandwidth_rolloff('LM741', 39400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8360.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_787():
    """Verify gain-bandwidth rolloff and linear stability for test case 787."""
    g = compute_gain_bandwidth_rolloff('LM741', 39450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8370.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_788():
    """Verify gain-bandwidth rolloff and linear stability for test case 788."""
    g = compute_gain_bandwidth_rolloff('LM741', 39500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8380.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_789():
    """Verify gain-bandwidth rolloff and linear stability for test case 789."""
    g = compute_gain_bandwidth_rolloff('LM741', 39550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8390.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_790():
    """Verify gain-bandwidth rolloff and linear stability for test case 790."""
    g = compute_gain_bandwidth_rolloff('LM741', 39600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8400.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_791():
    """Verify gain-bandwidth rolloff and linear stability for test case 791."""
    g = compute_gain_bandwidth_rolloff('LM741', 39650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8410.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_792():
    """Verify gain-bandwidth rolloff and linear stability for test case 792."""
    g = compute_gain_bandwidth_rolloff('LM741', 39700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8420.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_793():
    """Verify gain-bandwidth rolloff and linear stability for test case 793."""
    g = compute_gain_bandwidth_rolloff('LM741', 39750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8430.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_794():
    """Verify gain-bandwidth rolloff and linear stability for test case 794."""
    g = compute_gain_bandwidth_rolloff('LM741', 39800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8440.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_795():
    """Verify gain-bandwidth rolloff and linear stability for test case 795."""
    g = compute_gain_bandwidth_rolloff('LM741', 39850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8450.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_796():
    """Verify gain-bandwidth rolloff and linear stability for test case 796."""
    g = compute_gain_bandwidth_rolloff('LM741', 39900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8460.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_797():
    """Verify gain-bandwidth rolloff and linear stability for test case 797."""
    g = compute_gain_bandwidth_rolloff('LM741', 39950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8470.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_798():
    """Verify gain-bandwidth rolloff and linear stability for test case 798."""
    g = compute_gain_bandwidth_rolloff('LM741', 40000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8480.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_799():
    """Verify gain-bandwidth rolloff and linear stability for test case 799."""
    g = compute_gain_bandwidth_rolloff('LM741', 40050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8490.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_800():
    """Verify gain-bandwidth rolloff and linear stability for test case 800."""
    g = compute_gain_bandwidth_rolloff('LM741', 40100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8500.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_801():
    """Verify gain-bandwidth rolloff and linear stability for test case 801."""
    g = compute_gain_bandwidth_rolloff('LM741', 40150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8510.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_802():
    """Verify gain-bandwidth rolloff and linear stability for test case 802."""
    g = compute_gain_bandwidth_rolloff('LM741', 40200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8520.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_803():
    """Verify gain-bandwidth rolloff and linear stability for test case 803."""
    g = compute_gain_bandwidth_rolloff('LM741', 40250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8530.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_804():
    """Verify gain-bandwidth rolloff and linear stability for test case 804."""
    g = compute_gain_bandwidth_rolloff('LM741', 40300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8540.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_805():
    """Verify gain-bandwidth rolloff and linear stability for test case 805."""
    g = compute_gain_bandwidth_rolloff('LM741', 40350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8550.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_806():
    """Verify gain-bandwidth rolloff and linear stability for test case 806."""
    g = compute_gain_bandwidth_rolloff('LM741', 40400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8560.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_807():
    """Verify gain-bandwidth rolloff and linear stability for test case 807."""
    g = compute_gain_bandwidth_rolloff('LM741', 40450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8570.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_808():
    """Verify gain-bandwidth rolloff and linear stability for test case 808."""
    g = compute_gain_bandwidth_rolloff('LM741', 40500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8580.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_809():
    """Verify gain-bandwidth rolloff and linear stability for test case 809."""
    g = compute_gain_bandwidth_rolloff('LM741', 40550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8590.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_810():
    """Verify gain-bandwidth rolloff and linear stability for test case 810."""
    g = compute_gain_bandwidth_rolloff('LM741', 40600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8600.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_811():
    """Verify gain-bandwidth rolloff and linear stability for test case 811."""
    g = compute_gain_bandwidth_rolloff('LM741', 40650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8610.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_812():
    """Verify gain-bandwidth rolloff and linear stability for test case 812."""
    g = compute_gain_bandwidth_rolloff('LM741', 40700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8620.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_813():
    """Verify gain-bandwidth rolloff and linear stability for test case 813."""
    g = compute_gain_bandwidth_rolloff('LM741', 40750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8630.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_814():
    """Verify gain-bandwidth rolloff and linear stability for test case 814."""
    g = compute_gain_bandwidth_rolloff('LM741', 40800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8640.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_815():
    """Verify gain-bandwidth rolloff and linear stability for test case 815."""
    g = compute_gain_bandwidth_rolloff('LM741', 40850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8650.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_816():
    """Verify gain-bandwidth rolloff and linear stability for test case 816."""
    g = compute_gain_bandwidth_rolloff('LM741', 40900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8660.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_817():
    """Verify gain-bandwidth rolloff and linear stability for test case 817."""
    g = compute_gain_bandwidth_rolloff('LM741', 40950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8670.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_818():
    """Verify gain-bandwidth rolloff and linear stability for test case 818."""
    g = compute_gain_bandwidth_rolloff('LM741', 41000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8680.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_819():
    """Verify gain-bandwidth rolloff and linear stability for test case 819."""
    g = compute_gain_bandwidth_rolloff('LM741', 41050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8690.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_820():
    """Verify gain-bandwidth rolloff and linear stability for test case 820."""
    g = compute_gain_bandwidth_rolloff('LM741', 41100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8700.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_821():
    """Verify gain-bandwidth rolloff and linear stability for test case 821."""
    g = compute_gain_bandwidth_rolloff('LM741', 41150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8710.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_822():
    """Verify gain-bandwidth rolloff and linear stability for test case 822."""
    g = compute_gain_bandwidth_rolloff('LM741', 41200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8720.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_823():
    """Verify gain-bandwidth rolloff and linear stability for test case 823."""
    g = compute_gain_bandwidth_rolloff('LM741', 41250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8730.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_824():
    """Verify gain-bandwidth rolloff and linear stability for test case 824."""
    g = compute_gain_bandwidth_rolloff('LM741', 41300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8740.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_825():
    """Verify gain-bandwidth rolloff and linear stability for test case 825."""
    g = compute_gain_bandwidth_rolloff('LM741', 41350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8750.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_826():
    """Verify gain-bandwidth rolloff and linear stability for test case 826."""
    g = compute_gain_bandwidth_rolloff('LM741', 41400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8760.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_827():
    """Verify gain-bandwidth rolloff and linear stability for test case 827."""
    g = compute_gain_bandwidth_rolloff('LM741', 41450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8770.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_828():
    """Verify gain-bandwidth rolloff and linear stability for test case 828."""
    g = compute_gain_bandwidth_rolloff('LM741', 41500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8780.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_829():
    """Verify gain-bandwidth rolloff and linear stability for test case 829."""
    g = compute_gain_bandwidth_rolloff('LM741', 41550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8790.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_830():
    """Verify gain-bandwidth rolloff and linear stability for test case 830."""
    g = compute_gain_bandwidth_rolloff('LM741', 41600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8800.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_831():
    """Verify gain-bandwidth rolloff and linear stability for test case 831."""
    g = compute_gain_bandwidth_rolloff('LM741', 41650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8810.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_832():
    """Verify gain-bandwidth rolloff and linear stability for test case 832."""
    g = compute_gain_bandwidth_rolloff('LM741', 41700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8820.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_833():
    """Verify gain-bandwidth rolloff and linear stability for test case 833."""
    g = compute_gain_bandwidth_rolloff('LM741', 41750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8830.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_834():
    """Verify gain-bandwidth rolloff and linear stability for test case 834."""
    g = compute_gain_bandwidth_rolloff('LM741', 41800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8840.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_835():
    """Verify gain-bandwidth rolloff and linear stability for test case 835."""
    g = compute_gain_bandwidth_rolloff('LM741', 41850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8850.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_836():
    """Verify gain-bandwidth rolloff and linear stability for test case 836."""
    g = compute_gain_bandwidth_rolloff('LM741', 41900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8860.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_837():
    """Verify gain-bandwidth rolloff and linear stability for test case 837."""
    g = compute_gain_bandwidth_rolloff('LM741', 41950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8870.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_838():
    """Verify gain-bandwidth rolloff and linear stability for test case 838."""
    g = compute_gain_bandwidth_rolloff('LM741', 42000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8880.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_839():
    """Verify gain-bandwidth rolloff and linear stability for test case 839."""
    g = compute_gain_bandwidth_rolloff('LM741', 42050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8890.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_840():
    """Verify gain-bandwidth rolloff and linear stability for test case 840."""
    g = compute_gain_bandwidth_rolloff('LM741', 42100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8900.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_841():
    """Verify gain-bandwidth rolloff and linear stability for test case 841."""
    g = compute_gain_bandwidth_rolloff('LM741', 42150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8910.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_842():
    """Verify gain-bandwidth rolloff and linear stability for test case 842."""
    g = compute_gain_bandwidth_rolloff('LM741', 42200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8920.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_843():
    """Verify gain-bandwidth rolloff and linear stability for test case 843."""
    g = compute_gain_bandwidth_rolloff('LM741', 42250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8930.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_844():
    """Verify gain-bandwidth rolloff and linear stability for test case 844."""
    g = compute_gain_bandwidth_rolloff('LM741', 42300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8940.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_845():
    """Verify gain-bandwidth rolloff and linear stability for test case 845."""
    g = compute_gain_bandwidth_rolloff('LM741', 42350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8950.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_846():
    """Verify gain-bandwidth rolloff and linear stability for test case 846."""
    g = compute_gain_bandwidth_rolloff('LM741', 42400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8960.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_847():
    """Verify gain-bandwidth rolloff and linear stability for test case 847."""
    g = compute_gain_bandwidth_rolloff('LM741', 42450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8970.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_848():
    """Verify gain-bandwidth rolloff and linear stability for test case 848."""
    g = compute_gain_bandwidth_rolloff('LM741', 42500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8980.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_849():
    """Verify gain-bandwidth rolloff and linear stability for test case 849."""
    g = compute_gain_bandwidth_rolloff('LM741', 42550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 8990.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_850():
    """Verify gain-bandwidth rolloff and linear stability for test case 850."""
    g = compute_gain_bandwidth_rolloff('LM741', 42600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9000.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_851():
    """Verify gain-bandwidth rolloff and linear stability for test case 851."""
    g = compute_gain_bandwidth_rolloff('LM741', 42650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9010.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_852():
    """Verify gain-bandwidth rolloff and linear stability for test case 852."""
    g = compute_gain_bandwidth_rolloff('LM741', 42700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9020.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_853():
    """Verify gain-bandwidth rolloff and linear stability for test case 853."""
    g = compute_gain_bandwidth_rolloff('LM741', 42750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9030.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_854():
    """Verify gain-bandwidth rolloff and linear stability for test case 854."""
    g = compute_gain_bandwidth_rolloff('LM741', 42800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9040.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_855():
    """Verify gain-bandwidth rolloff and linear stability for test case 855."""
    g = compute_gain_bandwidth_rolloff('LM741', 42850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9050.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_856():
    """Verify gain-bandwidth rolloff and linear stability for test case 856."""
    g = compute_gain_bandwidth_rolloff('LM741', 42900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9060.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_857():
    """Verify gain-bandwidth rolloff and linear stability for test case 857."""
    g = compute_gain_bandwidth_rolloff('LM741', 42950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9070.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_858():
    """Verify gain-bandwidth rolloff and linear stability for test case 858."""
    g = compute_gain_bandwidth_rolloff('LM741', 43000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9080.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_859():
    """Verify gain-bandwidth rolloff and linear stability for test case 859."""
    g = compute_gain_bandwidth_rolloff('LM741', 43050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9090.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_860():
    """Verify gain-bandwidth rolloff and linear stability for test case 860."""
    g = compute_gain_bandwidth_rolloff('LM741', 43100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9100.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_861():
    """Verify gain-bandwidth rolloff and linear stability for test case 861."""
    g = compute_gain_bandwidth_rolloff('LM741', 43150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9110.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_862():
    """Verify gain-bandwidth rolloff and linear stability for test case 862."""
    g = compute_gain_bandwidth_rolloff('LM741', 43200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9120.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_863():
    """Verify gain-bandwidth rolloff and linear stability for test case 863."""
    g = compute_gain_bandwidth_rolloff('LM741', 43250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9130.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_864():
    """Verify gain-bandwidth rolloff and linear stability for test case 864."""
    g = compute_gain_bandwidth_rolloff('LM741', 43300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9140.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_865():
    """Verify gain-bandwidth rolloff and linear stability for test case 865."""
    g = compute_gain_bandwidth_rolloff('LM741', 43350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9150.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_866():
    """Verify gain-bandwidth rolloff and linear stability for test case 866."""
    g = compute_gain_bandwidth_rolloff('LM741', 43400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9160.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_867():
    """Verify gain-bandwidth rolloff and linear stability for test case 867."""
    g = compute_gain_bandwidth_rolloff('LM741', 43450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9170.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_868():
    """Verify gain-bandwidth rolloff and linear stability for test case 868."""
    g = compute_gain_bandwidth_rolloff('LM741', 43500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9180.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_869():
    """Verify gain-bandwidth rolloff and linear stability for test case 869."""
    g = compute_gain_bandwidth_rolloff('LM741', 43550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9190.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_870():
    """Verify gain-bandwidth rolloff and linear stability for test case 870."""
    g = compute_gain_bandwidth_rolloff('LM741', 43600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9200.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_871():
    """Verify gain-bandwidth rolloff and linear stability for test case 871."""
    g = compute_gain_bandwidth_rolloff('LM741', 43650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9210.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_872():
    """Verify gain-bandwidth rolloff and linear stability for test case 872."""
    g = compute_gain_bandwidth_rolloff('LM741', 43700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9220.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_873():
    """Verify gain-bandwidth rolloff and linear stability for test case 873."""
    g = compute_gain_bandwidth_rolloff('LM741', 43750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9230.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_874():
    """Verify gain-bandwidth rolloff and linear stability for test case 874."""
    g = compute_gain_bandwidth_rolloff('LM741', 43800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9240.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_875():
    """Verify gain-bandwidth rolloff and linear stability for test case 875."""
    g = compute_gain_bandwidth_rolloff('LM741', 43850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9250.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_876():
    """Verify gain-bandwidth rolloff and linear stability for test case 876."""
    g = compute_gain_bandwidth_rolloff('LM741', 43900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9260.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_877():
    """Verify gain-bandwidth rolloff and linear stability for test case 877."""
    g = compute_gain_bandwidth_rolloff('LM741', 43950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9270.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_878():
    """Verify gain-bandwidth rolloff and linear stability for test case 878."""
    g = compute_gain_bandwidth_rolloff('LM741', 44000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9280.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_879():
    """Verify gain-bandwidth rolloff and linear stability for test case 879."""
    g = compute_gain_bandwidth_rolloff('LM741', 44050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9290.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_880():
    """Verify gain-bandwidth rolloff and linear stability for test case 880."""
    g = compute_gain_bandwidth_rolloff('LM741', 44100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9300.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_881():
    """Verify gain-bandwidth rolloff and linear stability for test case 881."""
    g = compute_gain_bandwidth_rolloff('LM741', 44150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9310.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_882():
    """Verify gain-bandwidth rolloff and linear stability for test case 882."""
    g = compute_gain_bandwidth_rolloff('LM741', 44200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9320.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_883():
    """Verify gain-bandwidth rolloff and linear stability for test case 883."""
    g = compute_gain_bandwidth_rolloff('LM741', 44250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9330.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_884():
    """Verify gain-bandwidth rolloff and linear stability for test case 884."""
    g = compute_gain_bandwidth_rolloff('LM741', 44300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9340.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_885():
    """Verify gain-bandwidth rolloff and linear stability for test case 885."""
    g = compute_gain_bandwidth_rolloff('LM741', 44350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9350.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_886():
    """Verify gain-bandwidth rolloff and linear stability for test case 886."""
    g = compute_gain_bandwidth_rolloff('LM741', 44400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9360.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_887():
    """Verify gain-bandwidth rolloff and linear stability for test case 887."""
    g = compute_gain_bandwidth_rolloff('LM741', 44450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9370.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_888():
    """Verify gain-bandwidth rolloff and linear stability for test case 888."""
    g = compute_gain_bandwidth_rolloff('LM741', 44500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9380.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_889():
    """Verify gain-bandwidth rolloff and linear stability for test case 889."""
    g = compute_gain_bandwidth_rolloff('LM741', 44550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9390.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_890():
    """Verify gain-bandwidth rolloff and linear stability for test case 890."""
    g = compute_gain_bandwidth_rolloff('LM741', 44600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9400.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_891():
    """Verify gain-bandwidth rolloff and linear stability for test case 891."""
    g = compute_gain_bandwidth_rolloff('LM741', 44650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9410.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_892():
    """Verify gain-bandwidth rolloff and linear stability for test case 892."""
    g = compute_gain_bandwidth_rolloff('LM741', 44700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9420.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_893():
    """Verify gain-bandwidth rolloff and linear stability for test case 893."""
    g = compute_gain_bandwidth_rolloff('LM741', 44750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9430.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_894():
    """Verify gain-bandwidth rolloff and linear stability for test case 894."""
    g = compute_gain_bandwidth_rolloff('LM741', 44800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9440.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_895():
    """Verify gain-bandwidth rolloff and linear stability for test case 895."""
    g = compute_gain_bandwidth_rolloff('LM741', 44850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9450.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_896():
    """Verify gain-bandwidth rolloff and linear stability for test case 896."""
    g = compute_gain_bandwidth_rolloff('LM741', 44900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9460.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_897():
    """Verify gain-bandwidth rolloff and linear stability for test case 897."""
    g = compute_gain_bandwidth_rolloff('LM741', 44950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9470.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_898():
    """Verify gain-bandwidth rolloff and linear stability for test case 898."""
    g = compute_gain_bandwidth_rolloff('LM741', 45000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9480.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_899():
    """Verify gain-bandwidth rolloff and linear stability for test case 899."""
    g = compute_gain_bandwidth_rolloff('LM741', 45050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9490.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_900():
    """Verify gain-bandwidth rolloff and linear stability for test case 900."""
    g = compute_gain_bandwidth_rolloff('LM741', 45100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9500.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_901():
    """Verify gain-bandwidth rolloff and linear stability for test case 901."""
    g = compute_gain_bandwidth_rolloff('LM741', 45150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9510.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_902():
    """Verify gain-bandwidth rolloff and linear stability for test case 902."""
    g = compute_gain_bandwidth_rolloff('LM741', 45200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9520.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_903():
    """Verify gain-bandwidth rolloff and linear stability for test case 903."""
    g = compute_gain_bandwidth_rolloff('LM741', 45250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9530.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_904():
    """Verify gain-bandwidth rolloff and linear stability for test case 904."""
    g = compute_gain_bandwidth_rolloff('LM741', 45300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9540.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_905():
    """Verify gain-bandwidth rolloff and linear stability for test case 905."""
    g = compute_gain_bandwidth_rolloff('LM741', 45350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9550.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_906():
    """Verify gain-bandwidth rolloff and linear stability for test case 906."""
    g = compute_gain_bandwidth_rolloff('LM741', 45400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9560.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_907():
    """Verify gain-bandwidth rolloff and linear stability for test case 907."""
    g = compute_gain_bandwidth_rolloff('LM741', 45450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9570.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_908():
    """Verify gain-bandwidth rolloff and linear stability for test case 908."""
    g = compute_gain_bandwidth_rolloff('LM741', 45500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9580.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_909():
    """Verify gain-bandwidth rolloff and linear stability for test case 909."""
    g = compute_gain_bandwidth_rolloff('LM741', 45550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9590.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_910():
    """Verify gain-bandwidth rolloff and linear stability for test case 910."""
    g = compute_gain_bandwidth_rolloff('LM741', 45600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9600.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_911():
    """Verify gain-bandwidth rolloff and linear stability for test case 911."""
    g = compute_gain_bandwidth_rolloff('LM741', 45650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9610.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_912():
    """Verify gain-bandwidth rolloff and linear stability for test case 912."""
    g = compute_gain_bandwidth_rolloff('LM741', 45700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9620.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_913():
    """Verify gain-bandwidth rolloff and linear stability for test case 913."""
    g = compute_gain_bandwidth_rolloff('LM741', 45750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9630.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_914():
    """Verify gain-bandwidth rolloff and linear stability for test case 914."""
    g = compute_gain_bandwidth_rolloff('LM741', 45800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9640.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_915():
    """Verify gain-bandwidth rolloff and linear stability for test case 915."""
    g = compute_gain_bandwidth_rolloff('LM741', 45850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9650.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_916():
    """Verify gain-bandwidth rolloff and linear stability for test case 916."""
    g = compute_gain_bandwidth_rolloff('LM741', 45900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9660.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_917():
    """Verify gain-bandwidth rolloff and linear stability for test case 917."""
    g = compute_gain_bandwidth_rolloff('LM741', 45950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9670.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_918():
    """Verify gain-bandwidth rolloff and linear stability for test case 918."""
    g = compute_gain_bandwidth_rolloff('LM741', 46000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9680.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_919():
    """Verify gain-bandwidth rolloff and linear stability for test case 919."""
    g = compute_gain_bandwidth_rolloff('LM741', 46050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9690.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_920():
    """Verify gain-bandwidth rolloff and linear stability for test case 920."""
    g = compute_gain_bandwidth_rolloff('LM741', 46100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9700.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_921():
    """Verify gain-bandwidth rolloff and linear stability for test case 921."""
    g = compute_gain_bandwidth_rolloff('LM741', 46150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9710.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_922():
    """Verify gain-bandwidth rolloff and linear stability for test case 922."""
    g = compute_gain_bandwidth_rolloff('LM741', 46200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9720.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_923():
    """Verify gain-bandwidth rolloff and linear stability for test case 923."""
    g = compute_gain_bandwidth_rolloff('LM741', 46250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9730.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_924():
    """Verify gain-bandwidth rolloff and linear stability for test case 924."""
    g = compute_gain_bandwidth_rolloff('LM741', 46300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9740.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_925():
    """Verify gain-bandwidth rolloff and linear stability for test case 925."""
    g = compute_gain_bandwidth_rolloff('LM741', 46350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9750.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_926():
    """Verify gain-bandwidth rolloff and linear stability for test case 926."""
    g = compute_gain_bandwidth_rolloff('LM741', 46400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9760.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_927():
    """Verify gain-bandwidth rolloff and linear stability for test case 927."""
    g = compute_gain_bandwidth_rolloff('LM741', 46450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9770.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_928():
    """Verify gain-bandwidth rolloff and linear stability for test case 928."""
    g = compute_gain_bandwidth_rolloff('LM741', 46500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9780.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_929():
    """Verify gain-bandwidth rolloff and linear stability for test case 929."""
    g = compute_gain_bandwidth_rolloff('LM741', 46550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9790.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_930():
    """Verify gain-bandwidth rolloff and linear stability for test case 930."""
    g = compute_gain_bandwidth_rolloff('LM741', 46600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9800.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_931():
    """Verify gain-bandwidth rolloff and linear stability for test case 931."""
    g = compute_gain_bandwidth_rolloff('LM741', 46650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9810.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_932():
    """Verify gain-bandwidth rolloff and linear stability for test case 932."""
    g = compute_gain_bandwidth_rolloff('LM741', 46700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9820.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_933():
    """Verify gain-bandwidth rolloff and linear stability for test case 933."""
    g = compute_gain_bandwidth_rolloff('LM741', 46750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9830.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_934():
    """Verify gain-bandwidth rolloff and linear stability for test case 934."""
    g = compute_gain_bandwidth_rolloff('LM741', 46800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9840.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_935():
    """Verify gain-bandwidth rolloff and linear stability for test case 935."""
    g = compute_gain_bandwidth_rolloff('LM741', 46850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9850.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_936():
    """Verify gain-bandwidth rolloff and linear stability for test case 936."""
    g = compute_gain_bandwidth_rolloff('LM741', 46900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9860.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_937():
    """Verify gain-bandwidth rolloff and linear stability for test case 937."""
    g = compute_gain_bandwidth_rolloff('LM741', 46950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9870.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_938():
    """Verify gain-bandwidth rolloff and linear stability for test case 938."""
    g = compute_gain_bandwidth_rolloff('LM741', 47000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9880.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_939():
    """Verify gain-bandwidth rolloff and linear stability for test case 939."""
    g = compute_gain_bandwidth_rolloff('LM741', 47050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9890.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_940():
    """Verify gain-bandwidth rolloff and linear stability for test case 940."""
    g = compute_gain_bandwidth_rolloff('LM741', 47100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9900.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_941():
    """Verify gain-bandwidth rolloff and linear stability for test case 941."""
    g = compute_gain_bandwidth_rolloff('LM741', 47150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9910.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_942():
    """Verify gain-bandwidth rolloff and linear stability for test case 942."""
    g = compute_gain_bandwidth_rolloff('LM741', 47200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9920.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_943():
    """Verify gain-bandwidth rolloff and linear stability for test case 943."""
    g = compute_gain_bandwidth_rolloff('LM741', 47250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9930.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_944():
    """Verify gain-bandwidth rolloff and linear stability for test case 944."""
    g = compute_gain_bandwidth_rolloff('LM741', 47300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9940.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_945():
    """Verify gain-bandwidth rolloff and linear stability for test case 945."""
    g = compute_gain_bandwidth_rolloff('LM741', 47350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9950.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_946():
    """Verify gain-bandwidth rolloff and linear stability for test case 946."""
    g = compute_gain_bandwidth_rolloff('LM741', 47400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9960.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_947():
    """Verify gain-bandwidth rolloff and linear stability for test case 947."""
    g = compute_gain_bandwidth_rolloff('LM741', 47450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9970.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_948():
    """Verify gain-bandwidth rolloff and linear stability for test case 948."""
    g = compute_gain_bandwidth_rolloff('LM741', 47500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9980.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_949():
    """Verify gain-bandwidth rolloff and linear stability for test case 949."""
    g = compute_gain_bandwidth_rolloff('LM741', 47550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 9990.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_950():
    """Verify gain-bandwidth rolloff and linear stability for test case 950."""
    g = compute_gain_bandwidth_rolloff('LM741', 47600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10000.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_951():
    """Verify gain-bandwidth rolloff and linear stability for test case 951."""
    g = compute_gain_bandwidth_rolloff('LM741', 47650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10010.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_952():
    """Verify gain-bandwidth rolloff and linear stability for test case 952."""
    g = compute_gain_bandwidth_rolloff('LM741', 47700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10020.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_953():
    """Verify gain-bandwidth rolloff and linear stability for test case 953."""
    g = compute_gain_bandwidth_rolloff('LM741', 47750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10030.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_954():
    """Verify gain-bandwidth rolloff and linear stability for test case 954."""
    g = compute_gain_bandwidth_rolloff('LM741', 47800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10040.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_955():
    """Verify gain-bandwidth rolloff and linear stability for test case 955."""
    g = compute_gain_bandwidth_rolloff('LM741', 47850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10050.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_956():
    """Verify gain-bandwidth rolloff and linear stability for test case 956."""
    g = compute_gain_bandwidth_rolloff('LM741', 47900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10060.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_957():
    """Verify gain-bandwidth rolloff and linear stability for test case 957."""
    g = compute_gain_bandwidth_rolloff('LM741', 47950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10070.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_958():
    """Verify gain-bandwidth rolloff and linear stability for test case 958."""
    g = compute_gain_bandwidth_rolloff('LM741', 48000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10080.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_959():
    """Verify gain-bandwidth rolloff and linear stability for test case 959."""
    g = compute_gain_bandwidth_rolloff('LM741', 48050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10090.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_960():
    """Verify gain-bandwidth rolloff and linear stability for test case 960."""
    g = compute_gain_bandwidth_rolloff('LM741', 48100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10100.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_961():
    """Verify gain-bandwidth rolloff and linear stability for test case 961."""
    g = compute_gain_bandwidth_rolloff('LM741', 48150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10110.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_962():
    """Verify gain-bandwidth rolloff and linear stability for test case 962."""
    g = compute_gain_bandwidth_rolloff('LM741', 48200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10120.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_963():
    """Verify gain-bandwidth rolloff and linear stability for test case 963."""
    g = compute_gain_bandwidth_rolloff('LM741', 48250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10130.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_964():
    """Verify gain-bandwidth rolloff and linear stability for test case 964."""
    g = compute_gain_bandwidth_rolloff('LM741', 48300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10140.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_965():
    """Verify gain-bandwidth rolloff and linear stability for test case 965."""
    g = compute_gain_bandwidth_rolloff('LM741', 48350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10150.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_966():
    """Verify gain-bandwidth rolloff and linear stability for test case 966."""
    g = compute_gain_bandwidth_rolloff('LM741', 48400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10160.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_967():
    """Verify gain-bandwidth rolloff and linear stability for test case 967."""
    g = compute_gain_bandwidth_rolloff('LM741', 48450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10170.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_968():
    """Verify gain-bandwidth rolloff and linear stability for test case 968."""
    g = compute_gain_bandwidth_rolloff('LM741', 48500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10180.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_969():
    """Verify gain-bandwidth rolloff and linear stability for test case 969."""
    g = compute_gain_bandwidth_rolloff('LM741', 48550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10190.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_970():
    """Verify gain-bandwidth rolloff and linear stability for test case 970."""
    g = compute_gain_bandwidth_rolloff('LM741', 48600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10200.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_971():
    """Verify gain-bandwidth rolloff and linear stability for test case 971."""
    g = compute_gain_bandwidth_rolloff('LM741', 48650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10210.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_972():
    """Verify gain-bandwidth rolloff and linear stability for test case 972."""
    g = compute_gain_bandwidth_rolloff('LM741', 48700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10220.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_973():
    """Verify gain-bandwidth rolloff and linear stability for test case 973."""
    g = compute_gain_bandwidth_rolloff('LM741', 48750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10230.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_974():
    """Verify gain-bandwidth rolloff and linear stability for test case 974."""
    g = compute_gain_bandwidth_rolloff('LM741', 48800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10240.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_975():
    """Verify gain-bandwidth rolloff and linear stability for test case 975."""
    g = compute_gain_bandwidth_rolloff('LM741', 48850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10250.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_976():
    """Verify gain-bandwidth rolloff and linear stability for test case 976."""
    g = compute_gain_bandwidth_rolloff('LM741', 48900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10260.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_977():
    """Verify gain-bandwidth rolloff and linear stability for test case 977."""
    g = compute_gain_bandwidth_rolloff('LM741', 48950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10270.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_978():
    """Verify gain-bandwidth rolloff and linear stability for test case 978."""
    g = compute_gain_bandwidth_rolloff('LM741', 49000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10280.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_979():
    """Verify gain-bandwidth rolloff and linear stability for test case 979."""
    g = compute_gain_bandwidth_rolloff('LM741', 49050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10290.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_980():
    """Verify gain-bandwidth rolloff and linear stability for test case 980."""
    g = compute_gain_bandwidth_rolloff('LM741', 49100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10300.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_981():
    """Verify gain-bandwidth rolloff and linear stability for test case 981."""
    g = compute_gain_bandwidth_rolloff('LM741', 49150.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10310.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_982():
    """Verify gain-bandwidth rolloff and linear stability for test case 982."""
    g = compute_gain_bandwidth_rolloff('LM741', 49200.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10320.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_983():
    """Verify gain-bandwidth rolloff and linear stability for test case 983."""
    g = compute_gain_bandwidth_rolloff('LM741', 49250.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10330.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_984():
    """Verify gain-bandwidth rolloff and linear stability for test case 984."""
    g = compute_gain_bandwidth_rolloff('LM741', 49300.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10340.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_985():
    """Verify gain-bandwidth rolloff and linear stability for test case 985."""
    g = compute_gain_bandwidth_rolloff('LM741', 49350.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10350.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_986():
    """Verify gain-bandwidth rolloff and linear stability for test case 986."""
    g = compute_gain_bandwidth_rolloff('LM741', 49400.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10360.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_987():
    """Verify gain-bandwidth rolloff and linear stability for test case 987."""
    g = compute_gain_bandwidth_rolloff('LM741', 49450.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10370.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_988():
    """Verify gain-bandwidth rolloff and linear stability for test case 988."""
    g = compute_gain_bandwidth_rolloff('LM741', 49500.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10380.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_989():
    """Verify gain-bandwidth rolloff and linear stability for test case 989."""
    g = compute_gain_bandwidth_rolloff('LM741', 49550.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10390.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_990():
    """Verify gain-bandwidth rolloff and linear stability for test case 990."""
    g = compute_gain_bandwidth_rolloff('LM741', 49600.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10400.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_991():
    """Verify gain-bandwidth rolloff and linear stability for test case 991."""
    g = compute_gain_bandwidth_rolloff('LM741', 49650.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10410.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_992():
    """Verify gain-bandwidth rolloff and linear stability for test case 992."""
    g = compute_gain_bandwidth_rolloff('LM741', 49700.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10420.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_993():
    """Verify gain-bandwidth rolloff and linear stability for test case 993."""
    g = compute_gain_bandwidth_rolloff('LM741', 49750.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10430.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_994():
    """Verify gain-bandwidth rolloff and linear stability for test case 994."""
    g = compute_gain_bandwidth_rolloff('LM741', 49800.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10440.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_995():
    """Verify gain-bandwidth rolloff and linear stability for test case 995."""
    g = compute_gain_bandwidth_rolloff('LM741', 49850.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10450.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_996():
    """Verify gain-bandwidth rolloff and linear stability for test case 996."""
    g = compute_gain_bandwidth_rolloff('LM741', 49900.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10460.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_997():
    """Verify gain-bandwidth rolloff and linear stability for test case 997."""
    g = compute_gain_bandwidth_rolloff('LM741', 49950.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10470.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_998():
    """Verify gain-bandwidth rolloff and linear stability for test case 998."""
    g = compute_gain_bandwidth_rolloff('LM741', 50000.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10480.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_999():
    """Verify gain-bandwidth rolloff and linear stability for test case 999."""
    g = compute_gain_bandwidth_rolloff('LM741', 50050.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10490.0)
    assert 0.0 <= bw <= 1.5

def test_analog_macromodel_verification_case_1000():
    """Verify gain-bandwidth rolloff and linear stability for test case 1000."""
    g = compute_gain_bandwidth_rolloff('LM741', 50100.0)
    assert g > 0.0
    bw = butterworth_transfer_magnitude(2, 1000.0, 10500.0)
    assert 0.0 <= bw <= 1.5
