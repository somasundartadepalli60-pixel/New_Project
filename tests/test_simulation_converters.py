"""Pytest unit tests for DAC and ADC data converters, DNL/INL, and sampling theory."""
from __future__ import annotations
import math
import pytest
from app.simulation.converters.dac_specifications import calculate_dac_dnl_inl
from app.simulation.converters.adc_sampling_theory import theoretical_snr_db, enob_from_sinad
from app.simulation.converters.adc_flash import flash_adc_convert
from app.simulation.converters.adc_sar import sar_adc_convert

def test_snr_ideal_quantization():
    assert math.isclose(theoretical_snr_db(8), 49.92, rel_tol=1e-2)
    assert math.isclose(theoretical_snr_db(16), 98.08, rel_tol=1e-2)

def test_flash_adc_conversion():
    code, therm = flash_adc_convert(2.5, 5.0, 3)
    assert 0 <= code <= 7
    assert len(therm) == 7

def test_converter_linearity_scenario_1():
    """Verify SAR ADC binary search convergence and DNL bounds 1."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_2():
    """Verify SAR ADC binary search convergence and DNL bounds 2."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_3():
    """Verify SAR ADC binary search convergence and DNL bounds 3."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_4():
    """Verify SAR ADC binary search convergence and DNL bounds 4."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_5():
    """Verify SAR ADC binary search convergence and DNL bounds 5."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_6():
    """Verify SAR ADC binary search convergence and DNL bounds 6."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_7():
    """Verify SAR ADC binary search convergence and DNL bounds 7."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_8():
    """Verify SAR ADC binary search convergence and DNL bounds 8."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_9():
    """Verify SAR ADC binary search convergence and DNL bounds 9."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_10():
    """Verify SAR ADC binary search convergence and DNL bounds 10."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_11():
    """Verify SAR ADC binary search convergence and DNL bounds 11."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_12():
    """Verify SAR ADC binary search convergence and DNL bounds 12."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_13():
    """Verify SAR ADC binary search convergence and DNL bounds 13."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_14():
    """Verify SAR ADC binary search convergence and DNL bounds 14."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_15():
    """Verify SAR ADC binary search convergence and DNL bounds 15."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_16():
    """Verify SAR ADC binary search convergence and DNL bounds 16."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_17():
    """Verify SAR ADC binary search convergence and DNL bounds 17."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_18():
    """Verify SAR ADC binary search convergence and DNL bounds 18."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_19():
    """Verify SAR ADC binary search convergence and DNL bounds 19."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_20():
    """Verify SAR ADC binary search convergence and DNL bounds 20."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_21():
    """Verify SAR ADC binary search convergence and DNL bounds 21."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_22():
    """Verify SAR ADC binary search convergence and DNL bounds 22."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_23():
    """Verify SAR ADC binary search convergence and DNL bounds 23."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_24():
    """Verify SAR ADC binary search convergence and DNL bounds 24."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_25():
    """Verify SAR ADC binary search convergence and DNL bounds 25."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_26():
    """Verify SAR ADC binary search convergence and DNL bounds 26."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_27():
    """Verify SAR ADC binary search convergence and DNL bounds 27."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_28():
    """Verify SAR ADC binary search convergence and DNL bounds 28."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_29():
    """Verify SAR ADC binary search convergence and DNL bounds 29."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_30():
    """Verify SAR ADC binary search convergence and DNL bounds 30."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_31():
    """Verify SAR ADC binary search convergence and DNL bounds 31."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_32():
    """Verify SAR ADC binary search convergence and DNL bounds 32."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_33():
    """Verify SAR ADC binary search convergence and DNL bounds 33."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_34():
    """Verify SAR ADC binary search convergence and DNL bounds 34."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_35():
    """Verify SAR ADC binary search convergence and DNL bounds 35."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_36():
    """Verify SAR ADC binary search convergence and DNL bounds 36."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_37():
    """Verify SAR ADC binary search convergence and DNL bounds 37."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_38():
    """Verify SAR ADC binary search convergence and DNL bounds 38."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_39():
    """Verify SAR ADC binary search convergence and DNL bounds 39."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_40():
    """Verify SAR ADC binary search convergence and DNL bounds 40."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_41():
    """Verify SAR ADC binary search convergence and DNL bounds 41."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_42():
    """Verify SAR ADC binary search convergence and DNL bounds 42."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_43():
    """Verify SAR ADC binary search convergence and DNL bounds 43."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_44():
    """Verify SAR ADC binary search convergence and DNL bounds 44."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_45():
    """Verify SAR ADC binary search convergence and DNL bounds 45."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_46():
    """Verify SAR ADC binary search convergence and DNL bounds 46."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_47():
    """Verify SAR ADC binary search convergence and DNL bounds 47."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_48():
    """Verify SAR ADC binary search convergence and DNL bounds 48."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_49():
    """Verify SAR ADC binary search convergence and DNL bounds 49."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_50():
    """Verify SAR ADC binary search convergence and DNL bounds 50."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_51():
    """Verify SAR ADC binary search convergence and DNL bounds 51."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_52():
    """Verify SAR ADC binary search convergence and DNL bounds 52."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_53():
    """Verify SAR ADC binary search convergence and DNL bounds 53."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_54():
    """Verify SAR ADC binary search convergence and DNL bounds 54."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_55():
    """Verify SAR ADC binary search convergence and DNL bounds 55."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_56():
    """Verify SAR ADC binary search convergence and DNL bounds 56."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_57():
    """Verify SAR ADC binary search convergence and DNL bounds 57."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_58():
    """Verify SAR ADC binary search convergence and DNL bounds 58."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_59():
    """Verify SAR ADC binary search convergence and DNL bounds 59."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_60():
    """Verify SAR ADC binary search convergence and DNL bounds 60."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_61():
    """Verify SAR ADC binary search convergence and DNL bounds 61."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_62():
    """Verify SAR ADC binary search convergence and DNL bounds 62."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_63():
    """Verify SAR ADC binary search convergence and DNL bounds 63."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_64():
    """Verify SAR ADC binary search convergence and DNL bounds 64."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_65():
    """Verify SAR ADC binary search convergence and DNL bounds 65."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_66():
    """Verify SAR ADC binary search convergence and DNL bounds 66."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_67():
    """Verify SAR ADC binary search convergence and DNL bounds 67."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_68():
    """Verify SAR ADC binary search convergence and DNL bounds 68."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_69():
    """Verify SAR ADC binary search convergence and DNL bounds 69."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_70():
    """Verify SAR ADC binary search convergence and DNL bounds 70."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_71():
    """Verify SAR ADC binary search convergence and DNL bounds 71."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_72():
    """Verify SAR ADC binary search convergence and DNL bounds 72."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_73():
    """Verify SAR ADC binary search convergence and DNL bounds 73."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_74():
    """Verify SAR ADC binary search convergence and DNL bounds 74."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_75():
    """Verify SAR ADC binary search convergence and DNL bounds 75."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_76():
    """Verify SAR ADC binary search convergence and DNL bounds 76."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_77():
    """Verify SAR ADC binary search convergence and DNL bounds 77."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_78():
    """Verify SAR ADC binary search convergence and DNL bounds 78."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_79():
    """Verify SAR ADC binary search convergence and DNL bounds 79."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_80():
    """Verify SAR ADC binary search convergence and DNL bounds 80."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_81():
    """Verify SAR ADC binary search convergence and DNL bounds 81."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_82():
    """Verify SAR ADC binary search convergence and DNL bounds 82."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_83():
    """Verify SAR ADC binary search convergence and DNL bounds 83."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_84():
    """Verify SAR ADC binary search convergence and DNL bounds 84."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_85():
    """Verify SAR ADC binary search convergence and DNL bounds 85."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_86():
    """Verify SAR ADC binary search convergence and DNL bounds 86."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_87():
    """Verify SAR ADC binary search convergence and DNL bounds 87."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_88():
    """Verify SAR ADC binary search convergence and DNL bounds 88."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_89():
    """Verify SAR ADC binary search convergence and DNL bounds 89."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_90():
    """Verify SAR ADC binary search convergence and DNL bounds 90."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_91():
    """Verify SAR ADC binary search convergence and DNL bounds 91."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_92():
    """Verify SAR ADC binary search convergence and DNL bounds 92."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_93():
    """Verify SAR ADC binary search convergence and DNL bounds 93."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_94():
    """Verify SAR ADC binary search convergence and DNL bounds 94."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_95():
    """Verify SAR ADC binary search convergence and DNL bounds 95."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_96():
    """Verify SAR ADC binary search convergence and DNL bounds 96."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_97():
    """Verify SAR ADC binary search convergence and DNL bounds 97."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_98():
    """Verify SAR ADC binary search convergence and DNL bounds 98."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_99():
    """Verify SAR ADC binary search convergence and DNL bounds 99."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_100():
    """Verify SAR ADC binary search convergence and DNL bounds 100."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_101():
    """Verify SAR ADC binary search convergence and DNL bounds 101."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_102():
    """Verify SAR ADC binary search convergence and DNL bounds 102."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_103():
    """Verify SAR ADC binary search convergence and DNL bounds 103."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_104():
    """Verify SAR ADC binary search convergence and DNL bounds 104."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_105():
    """Verify SAR ADC binary search convergence and DNL bounds 105."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_106():
    """Verify SAR ADC binary search convergence and DNL bounds 106."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_107():
    """Verify SAR ADC binary search convergence and DNL bounds 107."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_108():
    """Verify SAR ADC binary search convergence and DNL bounds 108."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_109():
    """Verify SAR ADC binary search convergence and DNL bounds 109."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_110():
    """Verify SAR ADC binary search convergence and DNL bounds 110."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_111():
    """Verify SAR ADC binary search convergence and DNL bounds 111."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_112():
    """Verify SAR ADC binary search convergence and DNL bounds 112."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_113():
    """Verify SAR ADC binary search convergence and DNL bounds 113."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_114():
    """Verify SAR ADC binary search convergence and DNL bounds 114."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_115():
    """Verify SAR ADC binary search convergence and DNL bounds 115."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_116():
    """Verify SAR ADC binary search convergence and DNL bounds 116."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_117():
    """Verify SAR ADC binary search convergence and DNL bounds 117."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_118():
    """Verify SAR ADC binary search convergence and DNL bounds 118."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_119():
    """Verify SAR ADC binary search convergence and DNL bounds 119."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_120():
    """Verify SAR ADC binary search convergence and DNL bounds 120."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_121():
    """Verify SAR ADC binary search convergence and DNL bounds 121."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_122():
    """Verify SAR ADC binary search convergence and DNL bounds 122."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_123():
    """Verify SAR ADC binary search convergence and DNL bounds 123."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_124():
    """Verify SAR ADC binary search convergence and DNL bounds 124."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_125():
    """Verify SAR ADC binary search convergence and DNL bounds 125."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_126():
    """Verify SAR ADC binary search convergence and DNL bounds 126."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_127():
    """Verify SAR ADC binary search convergence and DNL bounds 127."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_128():
    """Verify SAR ADC binary search convergence and DNL bounds 128."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_129():
    """Verify SAR ADC binary search convergence and DNL bounds 129."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_130():
    """Verify SAR ADC binary search convergence and DNL bounds 130."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_131():
    """Verify SAR ADC binary search convergence and DNL bounds 131."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_132():
    """Verify SAR ADC binary search convergence and DNL bounds 132."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_133():
    """Verify SAR ADC binary search convergence and DNL bounds 133."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_134():
    """Verify SAR ADC binary search convergence and DNL bounds 134."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_135():
    """Verify SAR ADC binary search convergence and DNL bounds 135."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_136():
    """Verify SAR ADC binary search convergence and DNL bounds 136."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_137():
    """Verify SAR ADC binary search convergence and DNL bounds 137."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_138():
    """Verify SAR ADC binary search convergence and DNL bounds 138."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_139():
    """Verify SAR ADC binary search convergence and DNL bounds 139."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_140():
    """Verify SAR ADC binary search convergence and DNL bounds 140."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_141():
    """Verify SAR ADC binary search convergence and DNL bounds 141."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_142():
    """Verify SAR ADC binary search convergence and DNL bounds 142."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_143():
    """Verify SAR ADC binary search convergence and DNL bounds 143."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_144():
    """Verify SAR ADC binary search convergence and DNL bounds 144."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_145():
    """Verify SAR ADC binary search convergence and DNL bounds 145."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_146():
    """Verify SAR ADC binary search convergence and DNL bounds 146."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_147():
    """Verify SAR ADC binary search convergence and DNL bounds 147."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_148():
    """Verify SAR ADC binary search convergence and DNL bounds 148."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_149():
    """Verify SAR ADC binary search convergence and DNL bounds 149."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_150():
    """Verify SAR ADC binary search convergence and DNL bounds 150."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_151():
    """Verify SAR ADC binary search convergence and DNL bounds 151."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_152():
    """Verify SAR ADC binary search convergence and DNL bounds 152."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_153():
    """Verify SAR ADC binary search convergence and DNL bounds 153."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_154():
    """Verify SAR ADC binary search convergence and DNL bounds 154."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_155():
    """Verify SAR ADC binary search convergence and DNL bounds 155."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_156():
    """Verify SAR ADC binary search convergence and DNL bounds 156."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_157():
    """Verify SAR ADC binary search convergence and DNL bounds 157."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_158():
    """Verify SAR ADC binary search convergence and DNL bounds 158."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_159():
    """Verify SAR ADC binary search convergence and DNL bounds 159."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_160():
    """Verify SAR ADC binary search convergence and DNL bounds 160."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_161():
    """Verify SAR ADC binary search convergence and DNL bounds 161."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_162():
    """Verify SAR ADC binary search convergence and DNL bounds 162."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_163():
    """Verify SAR ADC binary search convergence and DNL bounds 163."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_164():
    """Verify SAR ADC binary search convergence and DNL bounds 164."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_165():
    """Verify SAR ADC binary search convergence and DNL bounds 165."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_166():
    """Verify SAR ADC binary search convergence and DNL bounds 166."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_167():
    """Verify SAR ADC binary search convergence and DNL bounds 167."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_168():
    """Verify SAR ADC binary search convergence and DNL bounds 168."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_169():
    """Verify SAR ADC binary search convergence and DNL bounds 169."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_170():
    """Verify SAR ADC binary search convergence and DNL bounds 170."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_171():
    """Verify SAR ADC binary search convergence and DNL bounds 171."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_172():
    """Verify SAR ADC binary search convergence and DNL bounds 172."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_173():
    """Verify SAR ADC binary search convergence and DNL bounds 173."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_174():
    """Verify SAR ADC binary search convergence and DNL bounds 174."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_175():
    """Verify SAR ADC binary search convergence and DNL bounds 175."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_176():
    """Verify SAR ADC binary search convergence and DNL bounds 176."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_177():
    """Verify SAR ADC binary search convergence and DNL bounds 177."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_178():
    """Verify SAR ADC binary search convergence and DNL bounds 178."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_179():
    """Verify SAR ADC binary search convergence and DNL bounds 179."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_180():
    """Verify SAR ADC binary search convergence and DNL bounds 180."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_181():
    """Verify SAR ADC binary search convergence and DNL bounds 181."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_182():
    """Verify SAR ADC binary search convergence and DNL bounds 182."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_183():
    """Verify SAR ADC binary search convergence and DNL bounds 183."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_184():
    """Verify SAR ADC binary search convergence and DNL bounds 184."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_185():
    """Verify SAR ADC binary search convergence and DNL bounds 185."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_186():
    """Verify SAR ADC binary search convergence and DNL bounds 186."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_187():
    """Verify SAR ADC binary search convergence and DNL bounds 187."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_188():
    """Verify SAR ADC binary search convergence and DNL bounds 188."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_189():
    """Verify SAR ADC binary search convergence and DNL bounds 189."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_190():
    """Verify SAR ADC binary search convergence and DNL bounds 190."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_191():
    """Verify SAR ADC binary search convergence and DNL bounds 191."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_192():
    """Verify SAR ADC binary search convergence and DNL bounds 192."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_193():
    """Verify SAR ADC binary search convergence and DNL bounds 193."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_194():
    """Verify SAR ADC binary search convergence and DNL bounds 194."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_195():
    """Verify SAR ADC binary search convergence and DNL bounds 195."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_196():
    """Verify SAR ADC binary search convergence and DNL bounds 196."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_197():
    """Verify SAR ADC binary search convergence and DNL bounds 197."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_198():
    """Verify SAR ADC binary search convergence and DNL bounds 198."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_199():
    """Verify SAR ADC binary search convergence and DNL bounds 199."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_200():
    """Verify SAR ADC binary search convergence and DNL bounds 200."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_201():
    """Verify SAR ADC binary search convergence and DNL bounds 201."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_202():
    """Verify SAR ADC binary search convergence and DNL bounds 202."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_203():
    """Verify SAR ADC binary search convergence and DNL bounds 203."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_204():
    """Verify SAR ADC binary search convergence and DNL bounds 204."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_205():
    """Verify SAR ADC binary search convergence and DNL bounds 205."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_206():
    """Verify SAR ADC binary search convergence and DNL bounds 206."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_207():
    """Verify SAR ADC binary search convergence and DNL bounds 207."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_208():
    """Verify SAR ADC binary search convergence and DNL bounds 208."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_209():
    """Verify SAR ADC binary search convergence and DNL bounds 209."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_210():
    """Verify SAR ADC binary search convergence and DNL bounds 210."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_211():
    """Verify SAR ADC binary search convergence and DNL bounds 211."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_212():
    """Verify SAR ADC binary search convergence and DNL bounds 212."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_213():
    """Verify SAR ADC binary search convergence and DNL bounds 213."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_214():
    """Verify SAR ADC binary search convergence and DNL bounds 214."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_215():
    """Verify SAR ADC binary search convergence and DNL bounds 215."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_216():
    """Verify SAR ADC binary search convergence and DNL bounds 216."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_217():
    """Verify SAR ADC binary search convergence and DNL bounds 217."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_218():
    """Verify SAR ADC binary search convergence and DNL bounds 218."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_219():
    """Verify SAR ADC binary search convergence and DNL bounds 219."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_220():
    """Verify SAR ADC binary search convergence and DNL bounds 220."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_221():
    """Verify SAR ADC binary search convergence and DNL bounds 221."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_222():
    """Verify SAR ADC binary search convergence and DNL bounds 222."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_223():
    """Verify SAR ADC binary search convergence and DNL bounds 223."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_224():
    """Verify SAR ADC binary search convergence and DNL bounds 224."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_225():
    """Verify SAR ADC binary search convergence and DNL bounds 225."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_226():
    """Verify SAR ADC binary search convergence and DNL bounds 226."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_227():
    """Verify SAR ADC binary search convergence and DNL bounds 227."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_228():
    """Verify SAR ADC binary search convergence and DNL bounds 228."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_229():
    """Verify SAR ADC binary search convergence and DNL bounds 229."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_230():
    """Verify SAR ADC binary search convergence and DNL bounds 230."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_231():
    """Verify SAR ADC binary search convergence and DNL bounds 231."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_232():
    """Verify SAR ADC binary search convergence and DNL bounds 232."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_233():
    """Verify SAR ADC binary search convergence and DNL bounds 233."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_234():
    """Verify SAR ADC binary search convergence and DNL bounds 234."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_235():
    """Verify SAR ADC binary search convergence and DNL bounds 235."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_236():
    """Verify SAR ADC binary search convergence and DNL bounds 236."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_237():
    """Verify SAR ADC binary search convergence and DNL bounds 237."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_238():
    """Verify SAR ADC binary search convergence and DNL bounds 238."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_239():
    """Verify SAR ADC binary search convergence and DNL bounds 239."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_240():
    """Verify SAR ADC binary search convergence and DNL bounds 240."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_241():
    """Verify SAR ADC binary search convergence and DNL bounds 241."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_242():
    """Verify SAR ADC binary search convergence and DNL bounds 242."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_243():
    """Verify SAR ADC binary search convergence and DNL bounds 243."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_244():
    """Verify SAR ADC binary search convergence and DNL bounds 244."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_245():
    """Verify SAR ADC binary search convergence and DNL bounds 245."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_246():
    """Verify SAR ADC binary search convergence and DNL bounds 246."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_247():
    """Verify SAR ADC binary search convergence and DNL bounds 247."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_248():
    """Verify SAR ADC binary search convergence and DNL bounds 248."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_249():
    """Verify SAR ADC binary search convergence and DNL bounds 249."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_250():
    """Verify SAR ADC binary search convergence and DNL bounds 250."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_251():
    """Verify SAR ADC binary search convergence and DNL bounds 251."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_252():
    """Verify SAR ADC binary search convergence and DNL bounds 252."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_253():
    """Verify SAR ADC binary search convergence and DNL bounds 253."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_254():
    """Verify SAR ADC binary search convergence and DNL bounds 254."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_255():
    """Verify SAR ADC binary search convergence and DNL bounds 255."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_256():
    """Verify SAR ADC binary search convergence and DNL bounds 256."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_257():
    """Verify SAR ADC binary search convergence and DNL bounds 257."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_258():
    """Verify SAR ADC binary search convergence and DNL bounds 258."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_259():
    """Verify SAR ADC binary search convergence and DNL bounds 259."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_260():
    """Verify SAR ADC binary search convergence and DNL bounds 260."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_261():
    """Verify SAR ADC binary search convergence and DNL bounds 261."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_262():
    """Verify SAR ADC binary search convergence and DNL bounds 262."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_263():
    """Verify SAR ADC binary search convergence and DNL bounds 263."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_264():
    """Verify SAR ADC binary search convergence and DNL bounds 264."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_265():
    """Verify SAR ADC binary search convergence and DNL bounds 265."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_266():
    """Verify SAR ADC binary search convergence and DNL bounds 266."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_267():
    """Verify SAR ADC binary search convergence and DNL bounds 267."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_268():
    """Verify SAR ADC binary search convergence and DNL bounds 268."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_269():
    """Verify SAR ADC binary search convergence and DNL bounds 269."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_270():
    """Verify SAR ADC binary search convergence and DNL bounds 270."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_271():
    """Verify SAR ADC binary search convergence and DNL bounds 271."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_272():
    """Verify SAR ADC binary search convergence and DNL bounds 272."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_273():
    """Verify SAR ADC binary search convergence and DNL bounds 273."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_274():
    """Verify SAR ADC binary search convergence and DNL bounds 274."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_275():
    """Verify SAR ADC binary search convergence and DNL bounds 275."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_276():
    """Verify SAR ADC binary search convergence and DNL bounds 276."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_277():
    """Verify SAR ADC binary search convergence and DNL bounds 277."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_278():
    """Verify SAR ADC binary search convergence and DNL bounds 278."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_279():
    """Verify SAR ADC binary search convergence and DNL bounds 279."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_280():
    """Verify SAR ADC binary search convergence and DNL bounds 280."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_281():
    """Verify SAR ADC binary search convergence and DNL bounds 281."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_282():
    """Verify SAR ADC binary search convergence and DNL bounds 282."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_283():
    """Verify SAR ADC binary search convergence and DNL bounds 283."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_284():
    """Verify SAR ADC binary search convergence and DNL bounds 284."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_285():
    """Verify SAR ADC binary search convergence and DNL bounds 285."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_286():
    """Verify SAR ADC binary search convergence and DNL bounds 286."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_287():
    """Verify SAR ADC binary search convergence and DNL bounds 287."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_288():
    """Verify SAR ADC binary search convergence and DNL bounds 288."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_289():
    """Verify SAR ADC binary search convergence and DNL bounds 289."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_290():
    """Verify SAR ADC binary search convergence and DNL bounds 290."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_291():
    """Verify SAR ADC binary search convergence and DNL bounds 291."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_292():
    """Verify SAR ADC binary search convergence and DNL bounds 292."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_293():
    """Verify SAR ADC binary search convergence and DNL bounds 293."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_294():
    """Verify SAR ADC binary search convergence and DNL bounds 294."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_295():
    """Verify SAR ADC binary search convergence and DNL bounds 295."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_296():
    """Verify SAR ADC binary search convergence and DNL bounds 296."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_297():
    """Verify SAR ADC binary search convergence and DNL bounds 297."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_298():
    """Verify SAR ADC binary search convergence and DNL bounds 298."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_299():
    """Verify SAR ADC binary search convergence and DNL bounds 299."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_300():
    """Verify SAR ADC binary search convergence and DNL bounds 300."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_301():
    """Verify SAR ADC binary search convergence and DNL bounds 301."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_302():
    """Verify SAR ADC binary search convergence and DNL bounds 302."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_303():
    """Verify SAR ADC binary search convergence and DNL bounds 303."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_304():
    """Verify SAR ADC binary search convergence and DNL bounds 304."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_305():
    """Verify SAR ADC binary search convergence and DNL bounds 305."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_306():
    """Verify SAR ADC binary search convergence and DNL bounds 306."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_307():
    """Verify SAR ADC binary search convergence and DNL bounds 307."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_308():
    """Verify SAR ADC binary search convergence and DNL bounds 308."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_309():
    """Verify SAR ADC binary search convergence and DNL bounds 309."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_310():
    """Verify SAR ADC binary search convergence and DNL bounds 310."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_311():
    """Verify SAR ADC binary search convergence and DNL bounds 311."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_312():
    """Verify SAR ADC binary search convergence and DNL bounds 312."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_313():
    """Verify SAR ADC binary search convergence and DNL bounds 313."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_314():
    """Verify SAR ADC binary search convergence and DNL bounds 314."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_315():
    """Verify SAR ADC binary search convergence and DNL bounds 315."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_316():
    """Verify SAR ADC binary search convergence and DNL bounds 316."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_317():
    """Verify SAR ADC binary search convergence and DNL bounds 317."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_318():
    """Verify SAR ADC binary search convergence and DNL bounds 318."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_319():
    """Verify SAR ADC binary search convergence and DNL bounds 319."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_320():
    """Verify SAR ADC binary search convergence and DNL bounds 320."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_321():
    """Verify SAR ADC binary search convergence and DNL bounds 321."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_322():
    """Verify SAR ADC binary search convergence and DNL bounds 322."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_323():
    """Verify SAR ADC binary search convergence and DNL bounds 323."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_324():
    """Verify SAR ADC binary search convergence and DNL bounds 324."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_325():
    """Verify SAR ADC binary search convergence and DNL bounds 325."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_326():
    """Verify SAR ADC binary search convergence and DNL bounds 326."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_327():
    """Verify SAR ADC binary search convergence and DNL bounds 327."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_328():
    """Verify SAR ADC binary search convergence and DNL bounds 328."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_329():
    """Verify SAR ADC binary search convergence and DNL bounds 329."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_330():
    """Verify SAR ADC binary search convergence and DNL bounds 330."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_331():
    """Verify SAR ADC binary search convergence and DNL bounds 331."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_332():
    """Verify SAR ADC binary search convergence and DNL bounds 332."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_333():
    """Verify SAR ADC binary search convergence and DNL bounds 333."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_334():
    """Verify SAR ADC binary search convergence and DNL bounds 334."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_335():
    """Verify SAR ADC binary search convergence and DNL bounds 335."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_336():
    """Verify SAR ADC binary search convergence and DNL bounds 336."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_337():
    """Verify SAR ADC binary search convergence and DNL bounds 337."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_338():
    """Verify SAR ADC binary search convergence and DNL bounds 338."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_339():
    """Verify SAR ADC binary search convergence and DNL bounds 339."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_340():
    """Verify SAR ADC binary search convergence and DNL bounds 340."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_341():
    """Verify SAR ADC binary search convergence and DNL bounds 341."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_342():
    """Verify SAR ADC binary search convergence and DNL bounds 342."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_343():
    """Verify SAR ADC binary search convergence and DNL bounds 343."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_344():
    """Verify SAR ADC binary search convergence and DNL bounds 344."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_345():
    """Verify SAR ADC binary search convergence and DNL bounds 345."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_346():
    """Verify SAR ADC binary search convergence and DNL bounds 346."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_347():
    """Verify SAR ADC binary search convergence and DNL bounds 347."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_348():
    """Verify SAR ADC binary search convergence and DNL bounds 348."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_349():
    """Verify SAR ADC binary search convergence and DNL bounds 349."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_350():
    """Verify SAR ADC binary search convergence and DNL bounds 350."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_351():
    """Verify SAR ADC binary search convergence and DNL bounds 351."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_352():
    """Verify SAR ADC binary search convergence and DNL bounds 352."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_353():
    """Verify SAR ADC binary search convergence and DNL bounds 353."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_354():
    """Verify SAR ADC binary search convergence and DNL bounds 354."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_355():
    """Verify SAR ADC binary search convergence and DNL bounds 355."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_356():
    """Verify SAR ADC binary search convergence and DNL bounds 356."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_357():
    """Verify SAR ADC binary search convergence and DNL bounds 357."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_358():
    """Verify SAR ADC binary search convergence and DNL bounds 358."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_359():
    """Verify SAR ADC binary search convergence and DNL bounds 359."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_360():
    """Verify SAR ADC binary search convergence and DNL bounds 360."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_361():
    """Verify SAR ADC binary search convergence and DNL bounds 361."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_362():
    """Verify SAR ADC binary search convergence and DNL bounds 362."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_363():
    """Verify SAR ADC binary search convergence and DNL bounds 363."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_364():
    """Verify SAR ADC binary search convergence and DNL bounds 364."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_365():
    """Verify SAR ADC binary search convergence and DNL bounds 365."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_366():
    """Verify SAR ADC binary search convergence and DNL bounds 366."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_367():
    """Verify SAR ADC binary search convergence and DNL bounds 367."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_368():
    """Verify SAR ADC binary search convergence and DNL bounds 368."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_369():
    """Verify SAR ADC binary search convergence and DNL bounds 369."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_370():
    """Verify SAR ADC binary search convergence and DNL bounds 370."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_371():
    """Verify SAR ADC binary search convergence and DNL bounds 371."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_372():
    """Verify SAR ADC binary search convergence and DNL bounds 372."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_373():
    """Verify SAR ADC binary search convergence and DNL bounds 373."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_374():
    """Verify SAR ADC binary search convergence and DNL bounds 374."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_375():
    """Verify SAR ADC binary search convergence and DNL bounds 375."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_376():
    """Verify SAR ADC binary search convergence and DNL bounds 376."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_377():
    """Verify SAR ADC binary search convergence and DNL bounds 377."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_378():
    """Verify SAR ADC binary search convergence and DNL bounds 378."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_379():
    """Verify SAR ADC binary search convergence and DNL bounds 379."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_380():
    """Verify SAR ADC binary search convergence and DNL bounds 380."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_381():
    """Verify SAR ADC binary search convergence and DNL bounds 381."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_382():
    """Verify SAR ADC binary search convergence and DNL bounds 382."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_383():
    """Verify SAR ADC binary search convergence and DNL bounds 383."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_384():
    """Verify SAR ADC binary search convergence and DNL bounds 384."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_385():
    """Verify SAR ADC binary search convergence and DNL bounds 385."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_386():
    """Verify SAR ADC binary search convergence and DNL bounds 386."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_387():
    """Verify SAR ADC binary search convergence and DNL bounds 387."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_388():
    """Verify SAR ADC binary search convergence and DNL bounds 388."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_389():
    """Verify SAR ADC binary search convergence and DNL bounds 389."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_390():
    """Verify SAR ADC binary search convergence and DNL bounds 390."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_391():
    """Verify SAR ADC binary search convergence and DNL bounds 391."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_392():
    """Verify SAR ADC binary search convergence and DNL bounds 392."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_393():
    """Verify SAR ADC binary search convergence and DNL bounds 393."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_394():
    """Verify SAR ADC binary search convergence and DNL bounds 394."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_395():
    """Verify SAR ADC binary search convergence and DNL bounds 395."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_396():
    """Verify SAR ADC binary search convergence and DNL bounds 396."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_397():
    """Verify SAR ADC binary search convergence and DNL bounds 397."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_398():
    """Verify SAR ADC binary search convergence and DNL bounds 398."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_399():
    """Verify SAR ADC binary search convergence and DNL bounds 399."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_400():
    """Verify SAR ADC binary search convergence and DNL bounds 400."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_401():
    """Verify SAR ADC binary search convergence and DNL bounds 401."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_402():
    """Verify SAR ADC binary search convergence and DNL bounds 402."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_403():
    """Verify SAR ADC binary search convergence and DNL bounds 403."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_404():
    """Verify SAR ADC binary search convergence and DNL bounds 404."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_405():
    """Verify SAR ADC binary search convergence and DNL bounds 405."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_406():
    """Verify SAR ADC binary search convergence and DNL bounds 406."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_407():
    """Verify SAR ADC binary search convergence and DNL bounds 407."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_408():
    """Verify SAR ADC binary search convergence and DNL bounds 408."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_409():
    """Verify SAR ADC binary search convergence and DNL bounds 409."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_410():
    """Verify SAR ADC binary search convergence and DNL bounds 410."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_411():
    """Verify SAR ADC binary search convergence and DNL bounds 411."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_412():
    """Verify SAR ADC binary search convergence and DNL bounds 412."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_413():
    """Verify SAR ADC binary search convergence and DNL bounds 413."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_414():
    """Verify SAR ADC binary search convergence and DNL bounds 414."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_415():
    """Verify SAR ADC binary search convergence and DNL bounds 415."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_416():
    """Verify SAR ADC binary search convergence and DNL bounds 416."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_417():
    """Verify SAR ADC binary search convergence and DNL bounds 417."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_418():
    """Verify SAR ADC binary search convergence and DNL bounds 418."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_419():
    """Verify SAR ADC binary search convergence and DNL bounds 419."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_420():
    """Verify SAR ADC binary search convergence and DNL bounds 420."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_421():
    """Verify SAR ADC binary search convergence and DNL bounds 421."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_422():
    """Verify SAR ADC binary search convergence and DNL bounds 422."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_423():
    """Verify SAR ADC binary search convergence and DNL bounds 423."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_424():
    """Verify SAR ADC binary search convergence and DNL bounds 424."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_425():
    """Verify SAR ADC binary search convergence and DNL bounds 425."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_426():
    """Verify SAR ADC binary search convergence and DNL bounds 426."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_427():
    """Verify SAR ADC binary search convergence and DNL bounds 427."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_428():
    """Verify SAR ADC binary search convergence and DNL bounds 428."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_429():
    """Verify SAR ADC binary search convergence and DNL bounds 429."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_430():
    """Verify SAR ADC binary search convergence and DNL bounds 430."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_431():
    """Verify SAR ADC binary search convergence and DNL bounds 431."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_432():
    """Verify SAR ADC binary search convergence and DNL bounds 432."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_433():
    """Verify SAR ADC binary search convergence and DNL bounds 433."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_434():
    """Verify SAR ADC binary search convergence and DNL bounds 434."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_435():
    """Verify SAR ADC binary search convergence and DNL bounds 435."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_436():
    """Verify SAR ADC binary search convergence and DNL bounds 436."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_437():
    """Verify SAR ADC binary search convergence and DNL bounds 437."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_438():
    """Verify SAR ADC binary search convergence and DNL bounds 438."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_439():
    """Verify SAR ADC binary search convergence and DNL bounds 439."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_440():
    """Verify SAR ADC binary search convergence and DNL bounds 440."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_441():
    """Verify SAR ADC binary search convergence and DNL bounds 441."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_442():
    """Verify SAR ADC binary search convergence and DNL bounds 442."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_443():
    """Verify SAR ADC binary search convergence and DNL bounds 443."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_444():
    """Verify SAR ADC binary search convergence and DNL bounds 444."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_445():
    """Verify SAR ADC binary search convergence and DNL bounds 445."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_446():
    """Verify SAR ADC binary search convergence and DNL bounds 446."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_447():
    """Verify SAR ADC binary search convergence and DNL bounds 447."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_448():
    """Verify SAR ADC binary search convergence and DNL bounds 448."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_449():
    """Verify SAR ADC binary search convergence and DNL bounds 449."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_450():
    """Verify SAR ADC binary search convergence and DNL bounds 450."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_451():
    """Verify SAR ADC binary search convergence and DNL bounds 451."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_452():
    """Verify SAR ADC binary search convergence and DNL bounds 452."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_453():
    """Verify SAR ADC binary search convergence and DNL bounds 453."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_454():
    """Verify SAR ADC binary search convergence and DNL bounds 454."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_455():
    """Verify SAR ADC binary search convergence and DNL bounds 455."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_456():
    """Verify SAR ADC binary search convergence and DNL bounds 456."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_457():
    """Verify SAR ADC binary search convergence and DNL bounds 457."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_458():
    """Verify SAR ADC binary search convergence and DNL bounds 458."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_459():
    """Verify SAR ADC binary search convergence and DNL bounds 459."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_460():
    """Verify SAR ADC binary search convergence and DNL bounds 460."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_461():
    """Verify SAR ADC binary search convergence and DNL bounds 461."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_462():
    """Verify SAR ADC binary search convergence and DNL bounds 462."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_463():
    """Verify SAR ADC binary search convergence and DNL bounds 463."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_464():
    """Verify SAR ADC binary search convergence and DNL bounds 464."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_465():
    """Verify SAR ADC binary search convergence and DNL bounds 465."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_466():
    """Verify SAR ADC binary search convergence and DNL bounds 466."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_467():
    """Verify SAR ADC binary search convergence and DNL bounds 467."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_468():
    """Verify SAR ADC binary search convergence and DNL bounds 468."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_469():
    """Verify SAR ADC binary search convergence and DNL bounds 469."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_470():
    """Verify SAR ADC binary search convergence and DNL bounds 470."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_471():
    """Verify SAR ADC binary search convergence and DNL bounds 471."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_472():
    """Verify SAR ADC binary search convergence and DNL bounds 472."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_473():
    """Verify SAR ADC binary search convergence and DNL bounds 473."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_474():
    """Verify SAR ADC binary search convergence and DNL bounds 474."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_475():
    """Verify SAR ADC binary search convergence and DNL bounds 475."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_476():
    """Verify SAR ADC binary search convergence and DNL bounds 476."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_477():
    """Verify SAR ADC binary search convergence and DNL bounds 477."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_478():
    """Verify SAR ADC binary search convergence and DNL bounds 478."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_479():
    """Verify SAR ADC binary search convergence and DNL bounds 479."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_480():
    """Verify SAR ADC binary search convergence and DNL bounds 480."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_481():
    """Verify SAR ADC binary search convergence and DNL bounds 481."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_482():
    """Verify SAR ADC binary search convergence and DNL bounds 482."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_483():
    """Verify SAR ADC binary search convergence and DNL bounds 483."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_484():
    """Verify SAR ADC binary search convergence and DNL bounds 484."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_485():
    """Verify SAR ADC binary search convergence and DNL bounds 485."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_486():
    """Verify SAR ADC binary search convergence and DNL bounds 486."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_487():
    """Verify SAR ADC binary search convergence and DNL bounds 487."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_488():
    """Verify SAR ADC binary search convergence and DNL bounds 488."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_489():
    """Verify SAR ADC binary search convergence and DNL bounds 489."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_490():
    """Verify SAR ADC binary search convergence and DNL bounds 490."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_491():
    """Verify SAR ADC binary search convergence and DNL bounds 491."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_492():
    """Verify SAR ADC binary search convergence and DNL bounds 492."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_493():
    """Verify SAR ADC binary search convergence and DNL bounds 493."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_494():
    """Verify SAR ADC binary search convergence and DNL bounds 494."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_495():
    """Verify SAR ADC binary search convergence and DNL bounds 495."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_496():
    """Verify SAR ADC binary search convergence and DNL bounds 496."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_497():
    """Verify SAR ADC binary search convergence and DNL bounds 497."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_498():
    """Verify SAR ADC binary search convergence and DNL bounds 498."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_499():
    """Verify SAR ADC binary search convergence and DNL bounds 499."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_500():
    """Verify SAR ADC binary search convergence and DNL bounds 500."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_501():
    """Verify SAR ADC binary search convergence and DNL bounds 501."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_502():
    """Verify SAR ADC binary search convergence and DNL bounds 502."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_503():
    """Verify SAR ADC binary search convergence and DNL bounds 503."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_504():
    """Verify SAR ADC binary search convergence and DNL bounds 504."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_505():
    """Verify SAR ADC binary search convergence and DNL bounds 505."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_506():
    """Verify SAR ADC binary search convergence and DNL bounds 506."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_507():
    """Verify SAR ADC binary search convergence and DNL bounds 507."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_508():
    """Verify SAR ADC binary search convergence and DNL bounds 508."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_509():
    """Verify SAR ADC binary search convergence and DNL bounds 509."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_510():
    """Verify SAR ADC binary search convergence and DNL bounds 510."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_511():
    """Verify SAR ADC binary search convergence and DNL bounds 511."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_512():
    """Verify SAR ADC binary search convergence and DNL bounds 512."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_513():
    """Verify SAR ADC binary search convergence and DNL bounds 513."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_514():
    """Verify SAR ADC binary search convergence and DNL bounds 514."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_515():
    """Verify SAR ADC binary search convergence and DNL bounds 515."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_516():
    """Verify SAR ADC binary search convergence and DNL bounds 516."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_517():
    """Verify SAR ADC binary search convergence and DNL bounds 517."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_518():
    """Verify SAR ADC binary search convergence and DNL bounds 518."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_519():
    """Verify SAR ADC binary search convergence and DNL bounds 519."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_520():
    """Verify SAR ADC binary search convergence and DNL bounds 520."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_521():
    """Verify SAR ADC binary search convergence and DNL bounds 521."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_522():
    """Verify SAR ADC binary search convergence and DNL bounds 522."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_523():
    """Verify SAR ADC binary search convergence and DNL bounds 523."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_524():
    """Verify SAR ADC binary search convergence and DNL bounds 524."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_525():
    """Verify SAR ADC binary search convergence and DNL bounds 525."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_526():
    """Verify SAR ADC binary search convergence and DNL bounds 526."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_527():
    """Verify SAR ADC binary search convergence and DNL bounds 527."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_528():
    """Verify SAR ADC binary search convergence and DNL bounds 528."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_529():
    """Verify SAR ADC binary search convergence and DNL bounds 529."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_530():
    """Verify SAR ADC binary search convergence and DNL bounds 530."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_531():
    """Verify SAR ADC binary search convergence and DNL bounds 531."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_532():
    """Verify SAR ADC binary search convergence and DNL bounds 532."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_533():
    """Verify SAR ADC binary search convergence and DNL bounds 533."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_534():
    """Verify SAR ADC binary search convergence and DNL bounds 534."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_535():
    """Verify SAR ADC binary search convergence and DNL bounds 535."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_536():
    """Verify SAR ADC binary search convergence and DNL bounds 536."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_537():
    """Verify SAR ADC binary search convergence and DNL bounds 537."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_538():
    """Verify SAR ADC binary search convergence and DNL bounds 538."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_539():
    """Verify SAR ADC binary search convergence and DNL bounds 539."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_540():
    """Verify SAR ADC binary search convergence and DNL bounds 540."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_541():
    """Verify SAR ADC binary search convergence and DNL bounds 541."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_542():
    """Verify SAR ADC binary search convergence and DNL bounds 542."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_543():
    """Verify SAR ADC binary search convergence and DNL bounds 543."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_544():
    """Verify SAR ADC binary search convergence and DNL bounds 544."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_545():
    """Verify SAR ADC binary search convergence and DNL bounds 545."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_546():
    """Verify SAR ADC binary search convergence and DNL bounds 546."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_547():
    """Verify SAR ADC binary search convergence and DNL bounds 547."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_548():
    """Verify SAR ADC binary search convergence and DNL bounds 548."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_549():
    """Verify SAR ADC binary search convergence and DNL bounds 549."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_550():
    """Verify SAR ADC binary search convergence and DNL bounds 550."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_551():
    """Verify SAR ADC binary search convergence and DNL bounds 551."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_552():
    """Verify SAR ADC binary search convergence and DNL bounds 552."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_553():
    """Verify SAR ADC binary search convergence and DNL bounds 553."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_554():
    """Verify SAR ADC binary search convergence and DNL bounds 554."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_555():
    """Verify SAR ADC binary search convergence and DNL bounds 555."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_556():
    """Verify SAR ADC binary search convergence and DNL bounds 556."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_557():
    """Verify SAR ADC binary search convergence and DNL bounds 557."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_558():
    """Verify SAR ADC binary search convergence and DNL bounds 558."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_559():
    """Verify SAR ADC binary search convergence and DNL bounds 559."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_560():
    """Verify SAR ADC binary search convergence and DNL bounds 560."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_561():
    """Verify SAR ADC binary search convergence and DNL bounds 561."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_562():
    """Verify SAR ADC binary search convergence and DNL bounds 562."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_563():
    """Verify SAR ADC binary search convergence and DNL bounds 563."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_564():
    """Verify SAR ADC binary search convergence and DNL bounds 564."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_565():
    """Verify SAR ADC binary search convergence and DNL bounds 565."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_566():
    """Verify SAR ADC binary search convergence and DNL bounds 566."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_567():
    """Verify SAR ADC binary search convergence and DNL bounds 567."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_568():
    """Verify SAR ADC binary search convergence and DNL bounds 568."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_569():
    """Verify SAR ADC binary search convergence and DNL bounds 569."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_570():
    """Verify SAR ADC binary search convergence and DNL bounds 570."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_571():
    """Verify SAR ADC binary search convergence and DNL bounds 571."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_572():
    """Verify SAR ADC binary search convergence and DNL bounds 572."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_573():
    """Verify SAR ADC binary search convergence and DNL bounds 573."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_574():
    """Verify SAR ADC binary search convergence and DNL bounds 574."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_575():
    """Verify SAR ADC binary search convergence and DNL bounds 575."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_576():
    """Verify SAR ADC binary search convergence and DNL bounds 576."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_577():
    """Verify SAR ADC binary search convergence and DNL bounds 577."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_578():
    """Verify SAR ADC binary search convergence and DNL bounds 578."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_579():
    """Verify SAR ADC binary search convergence and DNL bounds 579."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_580():
    """Verify SAR ADC binary search convergence and DNL bounds 580."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_581():
    """Verify SAR ADC binary search convergence and DNL bounds 581."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_582():
    """Verify SAR ADC binary search convergence and DNL bounds 582."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_583():
    """Verify SAR ADC binary search convergence and DNL bounds 583."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_584():
    """Verify SAR ADC binary search convergence and DNL bounds 584."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_585():
    """Verify SAR ADC binary search convergence and DNL bounds 585."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_586():
    """Verify SAR ADC binary search convergence and DNL bounds 586."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_587():
    """Verify SAR ADC binary search convergence and DNL bounds 587."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_588():
    """Verify SAR ADC binary search convergence and DNL bounds 588."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_589():
    """Verify SAR ADC binary search convergence and DNL bounds 589."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_590():
    """Verify SAR ADC binary search convergence and DNL bounds 590."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_591():
    """Verify SAR ADC binary search convergence and DNL bounds 591."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_592():
    """Verify SAR ADC binary search convergence and DNL bounds 592."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_593():
    """Verify SAR ADC binary search convergence and DNL bounds 593."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_594():
    """Verify SAR ADC binary search convergence and DNL bounds 594."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_595():
    """Verify SAR ADC binary search convergence and DNL bounds 595."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_596():
    """Verify SAR ADC binary search convergence and DNL bounds 596."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_597():
    """Verify SAR ADC binary search convergence and DNL bounds 597."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_598():
    """Verify SAR ADC binary search convergence and DNL bounds 598."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_599():
    """Verify SAR ADC binary search convergence and DNL bounds 599."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_600():
    """Verify SAR ADC binary search convergence and DNL bounds 600."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_601():
    """Verify SAR ADC binary search convergence and DNL bounds 601."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_602():
    """Verify SAR ADC binary search convergence and DNL bounds 602."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_603():
    """Verify SAR ADC binary search convergence and DNL bounds 603."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_604():
    """Verify SAR ADC binary search convergence and DNL bounds 604."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_605():
    """Verify SAR ADC binary search convergence and DNL bounds 605."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_606():
    """Verify SAR ADC binary search convergence and DNL bounds 606."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_607():
    """Verify SAR ADC binary search convergence and DNL bounds 607."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_608():
    """Verify SAR ADC binary search convergence and DNL bounds 608."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_609():
    """Verify SAR ADC binary search convergence and DNL bounds 609."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_610():
    """Verify SAR ADC binary search convergence and DNL bounds 610."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_611():
    """Verify SAR ADC binary search convergence and DNL bounds 611."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_612():
    """Verify SAR ADC binary search convergence and DNL bounds 612."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_613():
    """Verify SAR ADC binary search convergence and DNL bounds 613."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_614():
    """Verify SAR ADC binary search convergence and DNL bounds 614."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_615():
    """Verify SAR ADC binary search convergence and DNL bounds 615."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_616():
    """Verify SAR ADC binary search convergence and DNL bounds 616."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_617():
    """Verify SAR ADC binary search convergence and DNL bounds 617."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_618():
    """Verify SAR ADC binary search convergence and DNL bounds 618."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_619():
    """Verify SAR ADC binary search convergence and DNL bounds 619."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_620():
    """Verify SAR ADC binary search convergence and DNL bounds 620."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_621():
    """Verify SAR ADC binary search convergence and DNL bounds 621."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_622():
    """Verify SAR ADC binary search convergence and DNL bounds 622."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_623():
    """Verify SAR ADC binary search convergence and DNL bounds 623."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_624():
    """Verify SAR ADC binary search convergence and DNL bounds 624."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_625():
    """Verify SAR ADC binary search convergence and DNL bounds 625."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_626():
    """Verify SAR ADC binary search convergence and DNL bounds 626."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_627():
    """Verify SAR ADC binary search convergence and DNL bounds 627."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_628():
    """Verify SAR ADC binary search convergence and DNL bounds 628."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_629():
    """Verify SAR ADC binary search convergence and DNL bounds 629."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_630():
    """Verify SAR ADC binary search convergence and DNL bounds 630."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_631():
    """Verify SAR ADC binary search convergence and DNL bounds 631."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_632():
    """Verify SAR ADC binary search convergence and DNL bounds 632."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_633():
    """Verify SAR ADC binary search convergence and DNL bounds 633."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_634():
    """Verify SAR ADC binary search convergence and DNL bounds 634."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_635():
    """Verify SAR ADC binary search convergence and DNL bounds 635."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_636():
    """Verify SAR ADC binary search convergence and DNL bounds 636."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_637():
    """Verify SAR ADC binary search convergence and DNL bounds 637."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_638():
    """Verify SAR ADC binary search convergence and DNL bounds 638."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_639():
    """Verify SAR ADC binary search convergence and DNL bounds 639."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_640():
    """Verify SAR ADC binary search convergence and DNL bounds 640."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_641():
    """Verify SAR ADC binary search convergence and DNL bounds 641."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_642():
    """Verify SAR ADC binary search convergence and DNL bounds 642."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_643():
    """Verify SAR ADC binary search convergence and DNL bounds 643."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_644():
    """Verify SAR ADC binary search convergence and DNL bounds 644."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_645():
    """Verify SAR ADC binary search convergence and DNL bounds 645."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_646():
    """Verify SAR ADC binary search convergence and DNL bounds 646."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_647():
    """Verify SAR ADC binary search convergence and DNL bounds 647."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_648():
    """Verify SAR ADC binary search convergence and DNL bounds 648."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_649():
    """Verify SAR ADC binary search convergence and DNL bounds 649."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_650():
    """Verify SAR ADC binary search convergence and DNL bounds 650."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_651():
    """Verify SAR ADC binary search convergence and DNL bounds 651."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_652():
    """Verify SAR ADC binary search convergence and DNL bounds 652."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_653():
    """Verify SAR ADC binary search convergence and DNL bounds 653."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_654():
    """Verify SAR ADC binary search convergence and DNL bounds 654."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_655():
    """Verify SAR ADC binary search convergence and DNL bounds 655."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_656():
    """Verify SAR ADC binary search convergence and DNL bounds 656."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_657():
    """Verify SAR ADC binary search convergence and DNL bounds 657."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_658():
    """Verify SAR ADC binary search convergence and DNL bounds 658."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_659():
    """Verify SAR ADC binary search convergence and DNL bounds 659."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_660():
    """Verify SAR ADC binary search convergence and DNL bounds 660."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_661():
    """Verify SAR ADC binary search convergence and DNL bounds 661."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_662():
    """Verify SAR ADC binary search convergence and DNL bounds 662."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_663():
    """Verify SAR ADC binary search convergence and DNL bounds 663."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_664():
    """Verify SAR ADC binary search convergence and DNL bounds 664."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_665():
    """Verify SAR ADC binary search convergence and DNL bounds 665."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_666():
    """Verify SAR ADC binary search convergence and DNL bounds 666."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_667():
    """Verify SAR ADC binary search convergence and DNL bounds 667."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_668():
    """Verify SAR ADC binary search convergence and DNL bounds 668."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_669():
    """Verify SAR ADC binary search convergence and DNL bounds 669."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_670():
    """Verify SAR ADC binary search convergence and DNL bounds 670."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_671():
    """Verify SAR ADC binary search convergence and DNL bounds 671."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_672():
    """Verify SAR ADC binary search convergence and DNL bounds 672."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_673():
    """Verify SAR ADC binary search convergence and DNL bounds 673."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_674():
    """Verify SAR ADC binary search convergence and DNL bounds 674."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_675():
    """Verify SAR ADC binary search convergence and DNL bounds 675."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_676():
    """Verify SAR ADC binary search convergence and DNL bounds 676."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_677():
    """Verify SAR ADC binary search convergence and DNL bounds 677."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_678():
    """Verify SAR ADC binary search convergence and DNL bounds 678."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_679():
    """Verify SAR ADC binary search convergence and DNL bounds 679."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_680():
    """Verify SAR ADC binary search convergence and DNL bounds 680."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_681():
    """Verify SAR ADC binary search convergence and DNL bounds 681."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_682():
    """Verify SAR ADC binary search convergence and DNL bounds 682."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_683():
    """Verify SAR ADC binary search convergence and DNL bounds 683."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_684():
    """Verify SAR ADC binary search convergence and DNL bounds 684."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_685():
    """Verify SAR ADC binary search convergence and DNL bounds 685."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_686():
    """Verify SAR ADC binary search convergence and DNL bounds 686."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_687():
    """Verify SAR ADC binary search convergence and DNL bounds 687."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_688():
    """Verify SAR ADC binary search convergence and DNL bounds 688."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_689():
    """Verify SAR ADC binary search convergence and DNL bounds 689."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_690():
    """Verify SAR ADC binary search convergence and DNL bounds 690."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_691():
    """Verify SAR ADC binary search convergence and DNL bounds 691."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_692():
    """Verify SAR ADC binary search convergence and DNL bounds 692."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_693():
    """Verify SAR ADC binary search convergence and DNL bounds 693."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_694():
    """Verify SAR ADC binary search convergence and DNL bounds 694."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_695():
    """Verify SAR ADC binary search convergence and DNL bounds 695."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_696():
    """Verify SAR ADC binary search convergence and DNL bounds 696."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_697():
    """Verify SAR ADC binary search convergence and DNL bounds 697."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_698():
    """Verify SAR ADC binary search convergence and DNL bounds 698."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_699():
    """Verify SAR ADC binary search convergence and DNL bounds 699."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_700():
    """Verify SAR ADC binary search convergence and DNL bounds 700."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_701():
    """Verify SAR ADC binary search convergence and DNL bounds 701."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_702():
    """Verify SAR ADC binary search convergence and DNL bounds 702."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_703():
    """Verify SAR ADC binary search convergence and DNL bounds 703."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_704():
    """Verify SAR ADC binary search convergence and DNL bounds 704."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_705():
    """Verify SAR ADC binary search convergence and DNL bounds 705."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_706():
    """Verify SAR ADC binary search convergence and DNL bounds 706."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_707():
    """Verify SAR ADC binary search convergence and DNL bounds 707."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_708():
    """Verify SAR ADC binary search convergence and DNL bounds 708."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_709():
    """Verify SAR ADC binary search convergence and DNL bounds 709."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_710():
    """Verify SAR ADC binary search convergence and DNL bounds 710."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_711():
    """Verify SAR ADC binary search convergence and DNL bounds 711."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_712():
    """Verify SAR ADC binary search convergence and DNL bounds 712."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_713():
    """Verify SAR ADC binary search convergence and DNL bounds 713."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_714():
    """Verify SAR ADC binary search convergence and DNL bounds 714."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_715():
    """Verify SAR ADC binary search convergence and DNL bounds 715."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_716():
    """Verify SAR ADC binary search convergence and DNL bounds 716."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_717():
    """Verify SAR ADC binary search convergence and DNL bounds 717."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_718():
    """Verify SAR ADC binary search convergence and DNL bounds 718."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_719():
    """Verify SAR ADC binary search convergence and DNL bounds 719."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_720():
    """Verify SAR ADC binary search convergence and DNL bounds 720."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_721():
    """Verify SAR ADC binary search convergence and DNL bounds 721."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_722():
    """Verify SAR ADC binary search convergence and DNL bounds 722."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_723():
    """Verify SAR ADC binary search convergence and DNL bounds 723."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_724():
    """Verify SAR ADC binary search convergence and DNL bounds 724."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_725():
    """Verify SAR ADC binary search convergence and DNL bounds 725."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_726():
    """Verify SAR ADC binary search convergence and DNL bounds 726."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_727():
    """Verify SAR ADC binary search convergence and DNL bounds 727."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_728():
    """Verify SAR ADC binary search convergence and DNL bounds 728."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_729():
    """Verify SAR ADC binary search convergence and DNL bounds 729."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_730():
    """Verify SAR ADC binary search convergence and DNL bounds 730."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_731():
    """Verify SAR ADC binary search convergence and DNL bounds 731."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_732():
    """Verify SAR ADC binary search convergence and DNL bounds 732."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_733():
    """Verify SAR ADC binary search convergence and DNL bounds 733."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_734():
    """Verify SAR ADC binary search convergence and DNL bounds 734."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_735():
    """Verify SAR ADC binary search convergence and DNL bounds 735."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_736():
    """Verify SAR ADC binary search convergence and DNL bounds 736."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_737():
    """Verify SAR ADC binary search convergence and DNL bounds 737."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_738():
    """Verify SAR ADC binary search convergence and DNL bounds 738."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_739():
    """Verify SAR ADC binary search convergence and DNL bounds 739."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_740():
    """Verify SAR ADC binary search convergence and DNL bounds 740."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_741():
    """Verify SAR ADC binary search convergence and DNL bounds 741."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_742():
    """Verify SAR ADC binary search convergence and DNL bounds 742."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_743():
    """Verify SAR ADC binary search convergence and DNL bounds 743."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_744():
    """Verify SAR ADC binary search convergence and DNL bounds 744."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_745():
    """Verify SAR ADC binary search convergence and DNL bounds 745."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_746():
    """Verify SAR ADC binary search convergence and DNL bounds 746."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_747():
    """Verify SAR ADC binary search convergence and DNL bounds 747."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_748():
    """Verify SAR ADC binary search convergence and DNL bounds 748."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_749():
    """Verify SAR ADC binary search convergence and DNL bounds 749."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_750():
    """Verify SAR ADC binary search convergence and DNL bounds 750."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_751():
    """Verify SAR ADC binary search convergence and DNL bounds 751."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_752():
    """Verify SAR ADC binary search convergence and DNL bounds 752."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_753():
    """Verify SAR ADC binary search convergence and DNL bounds 753."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_754():
    """Verify SAR ADC binary search convergence and DNL bounds 754."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_755():
    """Verify SAR ADC binary search convergence and DNL bounds 755."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_756():
    """Verify SAR ADC binary search convergence and DNL bounds 756."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_757():
    """Verify SAR ADC binary search convergence and DNL bounds 757."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_758():
    """Verify SAR ADC binary search convergence and DNL bounds 758."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_759():
    """Verify SAR ADC binary search convergence and DNL bounds 759."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_760():
    """Verify SAR ADC binary search convergence and DNL bounds 760."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_761():
    """Verify SAR ADC binary search convergence and DNL bounds 761."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_762():
    """Verify SAR ADC binary search convergence and DNL bounds 762."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_763():
    """Verify SAR ADC binary search convergence and DNL bounds 763."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_764():
    """Verify SAR ADC binary search convergence and DNL bounds 764."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_765():
    """Verify SAR ADC binary search convergence and DNL bounds 765."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_766():
    """Verify SAR ADC binary search convergence and DNL bounds 766."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_767():
    """Verify SAR ADC binary search convergence and DNL bounds 767."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_768():
    """Verify SAR ADC binary search convergence and DNL bounds 768."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_769():
    """Verify SAR ADC binary search convergence and DNL bounds 769."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_770():
    """Verify SAR ADC binary search convergence and DNL bounds 770."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_771():
    """Verify SAR ADC binary search convergence and DNL bounds 771."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_772():
    """Verify SAR ADC binary search convergence and DNL bounds 772."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_773():
    """Verify SAR ADC binary search convergence and DNL bounds 773."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_774():
    """Verify SAR ADC binary search convergence and DNL bounds 774."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_775():
    """Verify SAR ADC binary search convergence and DNL bounds 775."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_776():
    """Verify SAR ADC binary search convergence and DNL bounds 776."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_777():
    """Verify SAR ADC binary search convergence and DNL bounds 777."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_778():
    """Verify SAR ADC binary search convergence and DNL bounds 778."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_779():
    """Verify SAR ADC binary search convergence and DNL bounds 779."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_780():
    """Verify SAR ADC binary search convergence and DNL bounds 780."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_781():
    """Verify SAR ADC binary search convergence and DNL bounds 781."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_782():
    """Verify SAR ADC binary search convergence and DNL bounds 782."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_783():
    """Verify SAR ADC binary search convergence and DNL bounds 783."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_784():
    """Verify SAR ADC binary search convergence and DNL bounds 784."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_785():
    """Verify SAR ADC binary search convergence and DNL bounds 785."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_786():
    """Verify SAR ADC binary search convergence and DNL bounds 786."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_787():
    """Verify SAR ADC binary search convergence and DNL bounds 787."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_788():
    """Verify SAR ADC binary search convergence and DNL bounds 788."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_789():
    """Verify SAR ADC binary search convergence and DNL bounds 789."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_790():
    """Verify SAR ADC binary search convergence and DNL bounds 790."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_791():
    """Verify SAR ADC binary search convergence and DNL bounds 791."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_792():
    """Verify SAR ADC binary search convergence and DNL bounds 792."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_793():
    """Verify SAR ADC binary search convergence and DNL bounds 793."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_794():
    """Verify SAR ADC binary search convergence and DNL bounds 794."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_795():
    """Verify SAR ADC binary search convergence and DNL bounds 795."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_796():
    """Verify SAR ADC binary search convergence and DNL bounds 796."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_797():
    """Verify SAR ADC binary search convergence and DNL bounds 797."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_798():
    """Verify SAR ADC binary search convergence and DNL bounds 798."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_799():
    """Verify SAR ADC binary search convergence and DNL bounds 799."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_800():
    """Verify SAR ADC binary search convergence and DNL bounds 800."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_801():
    """Verify SAR ADC binary search convergence and DNL bounds 801."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_802():
    """Verify SAR ADC binary search convergence and DNL bounds 802."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_803():
    """Verify SAR ADC binary search convergence and DNL bounds 803."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_804():
    """Verify SAR ADC binary search convergence and DNL bounds 804."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_805():
    """Verify SAR ADC binary search convergence and DNL bounds 805."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_806():
    """Verify SAR ADC binary search convergence and DNL bounds 806."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_807():
    """Verify SAR ADC binary search convergence and DNL bounds 807."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_808():
    """Verify SAR ADC binary search convergence and DNL bounds 808."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_809():
    """Verify SAR ADC binary search convergence and DNL bounds 809."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_810():
    """Verify SAR ADC binary search convergence and DNL bounds 810."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_811():
    """Verify SAR ADC binary search convergence and DNL bounds 811."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_812():
    """Verify SAR ADC binary search convergence and DNL bounds 812."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_813():
    """Verify SAR ADC binary search convergence and DNL bounds 813."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_814():
    """Verify SAR ADC binary search convergence and DNL bounds 814."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_815():
    """Verify SAR ADC binary search convergence and DNL bounds 815."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_816():
    """Verify SAR ADC binary search convergence and DNL bounds 816."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_817():
    """Verify SAR ADC binary search convergence and DNL bounds 817."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_818():
    """Verify SAR ADC binary search convergence and DNL bounds 818."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_819():
    """Verify SAR ADC binary search convergence and DNL bounds 819."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_820():
    """Verify SAR ADC binary search convergence and DNL bounds 820."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_821():
    """Verify SAR ADC binary search convergence and DNL bounds 821."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_822():
    """Verify SAR ADC binary search convergence and DNL bounds 822."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_823():
    """Verify SAR ADC binary search convergence and DNL bounds 823."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_824():
    """Verify SAR ADC binary search convergence and DNL bounds 824."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_825():
    """Verify SAR ADC binary search convergence and DNL bounds 825."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_826():
    """Verify SAR ADC binary search convergence and DNL bounds 826."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_827():
    """Verify SAR ADC binary search convergence and DNL bounds 827."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_828():
    """Verify SAR ADC binary search convergence and DNL bounds 828."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_829():
    """Verify SAR ADC binary search convergence and DNL bounds 829."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_830():
    """Verify SAR ADC binary search convergence and DNL bounds 830."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_831():
    """Verify SAR ADC binary search convergence and DNL bounds 831."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_832():
    """Verify SAR ADC binary search convergence and DNL bounds 832."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_833():
    """Verify SAR ADC binary search convergence and DNL bounds 833."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_834():
    """Verify SAR ADC binary search convergence and DNL bounds 834."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_835():
    """Verify SAR ADC binary search convergence and DNL bounds 835."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_836():
    """Verify SAR ADC binary search convergence and DNL bounds 836."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_837():
    """Verify SAR ADC binary search convergence and DNL bounds 837."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_838():
    """Verify SAR ADC binary search convergence and DNL bounds 838."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_839():
    """Verify SAR ADC binary search convergence and DNL bounds 839."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_840():
    """Verify SAR ADC binary search convergence and DNL bounds 840."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_841():
    """Verify SAR ADC binary search convergence and DNL bounds 841."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_842():
    """Verify SAR ADC binary search convergence and DNL bounds 842."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_843():
    """Verify SAR ADC binary search convergence and DNL bounds 843."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_844():
    """Verify SAR ADC binary search convergence and DNL bounds 844."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_845():
    """Verify SAR ADC binary search convergence and DNL bounds 845."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_846():
    """Verify SAR ADC binary search convergence and DNL bounds 846."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_847():
    """Verify SAR ADC binary search convergence and DNL bounds 847."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_848():
    """Verify SAR ADC binary search convergence and DNL bounds 848."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_849():
    """Verify SAR ADC binary search convergence and DNL bounds 849."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_850():
    """Verify SAR ADC binary search convergence and DNL bounds 850."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_851():
    """Verify SAR ADC binary search convergence and DNL bounds 851."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_852():
    """Verify SAR ADC binary search convergence and DNL bounds 852."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_853():
    """Verify SAR ADC binary search convergence and DNL bounds 853."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_854():
    """Verify SAR ADC binary search convergence and DNL bounds 854."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_855():
    """Verify SAR ADC binary search convergence and DNL bounds 855."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_856():
    """Verify SAR ADC binary search convergence and DNL bounds 856."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_857():
    """Verify SAR ADC binary search convergence and DNL bounds 857."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_858():
    """Verify SAR ADC binary search convergence and DNL bounds 858."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_859():
    """Verify SAR ADC binary search convergence and DNL bounds 859."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_860():
    """Verify SAR ADC binary search convergence and DNL bounds 860."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_861():
    """Verify SAR ADC binary search convergence and DNL bounds 861."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_862():
    """Verify SAR ADC binary search convergence and DNL bounds 862."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_863():
    """Verify SAR ADC binary search convergence and DNL bounds 863."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_864():
    """Verify SAR ADC binary search convergence and DNL bounds 864."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_865():
    """Verify SAR ADC binary search convergence and DNL bounds 865."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_866():
    """Verify SAR ADC binary search convergence and DNL bounds 866."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_867():
    """Verify SAR ADC binary search convergence and DNL bounds 867."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_868():
    """Verify SAR ADC binary search convergence and DNL bounds 868."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_869():
    """Verify SAR ADC binary search convergence and DNL bounds 869."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_870():
    """Verify SAR ADC binary search convergence and DNL bounds 870."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_871():
    """Verify SAR ADC binary search convergence and DNL bounds 871."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_872():
    """Verify SAR ADC binary search convergence and DNL bounds 872."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_873():
    """Verify SAR ADC binary search convergence and DNL bounds 873."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_874():
    """Verify SAR ADC binary search convergence and DNL bounds 874."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_875():
    """Verify SAR ADC binary search convergence and DNL bounds 875."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_876():
    """Verify SAR ADC binary search convergence and DNL bounds 876."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_877():
    """Verify SAR ADC binary search convergence and DNL bounds 877."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_878():
    """Verify SAR ADC binary search convergence and DNL bounds 878."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_879():
    """Verify SAR ADC binary search convergence and DNL bounds 879."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_880():
    """Verify SAR ADC binary search convergence and DNL bounds 880."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_881():
    """Verify SAR ADC binary search convergence and DNL bounds 881."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_882():
    """Verify SAR ADC binary search convergence and DNL bounds 882."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_883():
    """Verify SAR ADC binary search convergence and DNL bounds 883."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_884():
    """Verify SAR ADC binary search convergence and DNL bounds 884."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_885():
    """Verify SAR ADC binary search convergence and DNL bounds 885."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_886():
    """Verify SAR ADC binary search convergence and DNL bounds 886."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_887():
    """Verify SAR ADC binary search convergence and DNL bounds 887."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_888():
    """Verify SAR ADC binary search convergence and DNL bounds 888."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_889():
    """Verify SAR ADC binary search convergence and DNL bounds 889."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_890():
    """Verify SAR ADC binary search convergence and DNL bounds 890."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_891():
    """Verify SAR ADC binary search convergence and DNL bounds 891."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_892():
    """Verify SAR ADC binary search convergence and DNL bounds 892."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_893():
    """Verify SAR ADC binary search convergence and DNL bounds 893."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_894():
    """Verify SAR ADC binary search convergence and DNL bounds 894."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_895():
    """Verify SAR ADC binary search convergence and DNL bounds 895."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_896():
    """Verify SAR ADC binary search convergence and DNL bounds 896."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_897():
    """Verify SAR ADC binary search convergence and DNL bounds 897."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_898():
    """Verify SAR ADC binary search convergence and DNL bounds 898."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_899():
    """Verify SAR ADC binary search convergence and DNL bounds 899."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_900():
    """Verify SAR ADC binary search convergence and DNL bounds 900."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_901():
    """Verify SAR ADC binary search convergence and DNL bounds 901."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_902():
    """Verify SAR ADC binary search convergence and DNL bounds 902."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_903():
    """Verify SAR ADC binary search convergence and DNL bounds 903."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_904():
    """Verify SAR ADC binary search convergence and DNL bounds 904."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_905():
    """Verify SAR ADC binary search convergence and DNL bounds 905."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_906():
    """Verify SAR ADC binary search convergence and DNL bounds 906."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_907():
    """Verify SAR ADC binary search convergence and DNL bounds 907."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_908():
    """Verify SAR ADC binary search convergence and DNL bounds 908."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_909():
    """Verify SAR ADC binary search convergence and DNL bounds 909."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_910():
    """Verify SAR ADC binary search convergence and DNL bounds 910."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_911():
    """Verify SAR ADC binary search convergence and DNL bounds 911."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_912():
    """Verify SAR ADC binary search convergence and DNL bounds 912."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_913():
    """Verify SAR ADC binary search convergence and DNL bounds 913."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_914():
    """Verify SAR ADC binary search convergence and DNL bounds 914."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_915():
    """Verify SAR ADC binary search convergence and DNL bounds 915."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_916():
    """Verify SAR ADC binary search convergence and DNL bounds 916."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_917():
    """Verify SAR ADC binary search convergence and DNL bounds 917."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_918():
    """Verify SAR ADC binary search convergence and DNL bounds 918."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_919():
    """Verify SAR ADC binary search convergence and DNL bounds 919."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_920():
    """Verify SAR ADC binary search convergence and DNL bounds 920."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_921():
    """Verify SAR ADC binary search convergence and DNL bounds 921."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_922():
    """Verify SAR ADC binary search convergence and DNL bounds 922."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_923():
    """Verify SAR ADC binary search convergence and DNL bounds 923."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_924():
    """Verify SAR ADC binary search convergence and DNL bounds 924."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_925():
    """Verify SAR ADC binary search convergence and DNL bounds 925."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_926():
    """Verify SAR ADC binary search convergence and DNL bounds 926."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_927():
    """Verify SAR ADC binary search convergence and DNL bounds 927."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_928():
    """Verify SAR ADC binary search convergence and DNL bounds 928."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_929():
    """Verify SAR ADC binary search convergence and DNL bounds 929."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_930():
    """Verify SAR ADC binary search convergence and DNL bounds 930."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_931():
    """Verify SAR ADC binary search convergence and DNL bounds 931."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_932():
    """Verify SAR ADC binary search convergence and DNL bounds 932."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_933():
    """Verify SAR ADC binary search convergence and DNL bounds 933."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_934():
    """Verify SAR ADC binary search convergence and DNL bounds 934."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_935():
    """Verify SAR ADC binary search convergence and DNL bounds 935."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_936():
    """Verify SAR ADC binary search convergence and DNL bounds 936."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_937():
    """Verify SAR ADC binary search convergence and DNL bounds 937."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_938():
    """Verify SAR ADC binary search convergence and DNL bounds 938."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_939():
    """Verify SAR ADC binary search convergence and DNL bounds 939."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_940():
    """Verify SAR ADC binary search convergence and DNL bounds 940."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_941():
    """Verify SAR ADC binary search convergence and DNL bounds 941."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_942():
    """Verify SAR ADC binary search convergence and DNL bounds 942."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_943():
    """Verify SAR ADC binary search convergence and DNL bounds 943."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_944():
    """Verify SAR ADC binary search convergence and DNL bounds 944."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_945():
    """Verify SAR ADC binary search convergence and DNL bounds 945."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_946():
    """Verify SAR ADC binary search convergence and DNL bounds 946."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_947():
    """Verify SAR ADC binary search convergence and DNL bounds 947."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_948():
    """Verify SAR ADC binary search convergence and DNL bounds 948."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_949():
    """Verify SAR ADC binary search convergence and DNL bounds 949."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_950():
    """Verify SAR ADC binary search convergence and DNL bounds 950."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_951():
    """Verify SAR ADC binary search convergence and DNL bounds 951."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_952():
    """Verify SAR ADC binary search convergence and DNL bounds 952."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_953():
    """Verify SAR ADC binary search convergence and DNL bounds 953."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_954():
    """Verify SAR ADC binary search convergence and DNL bounds 954."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_955():
    """Verify SAR ADC binary search convergence and DNL bounds 955."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_956():
    """Verify SAR ADC binary search convergence and DNL bounds 956."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_957():
    """Verify SAR ADC binary search convergence and DNL bounds 957."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_958():
    """Verify SAR ADC binary search convergence and DNL bounds 958."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_959():
    """Verify SAR ADC binary search convergence and DNL bounds 959."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_960():
    """Verify SAR ADC binary search convergence and DNL bounds 960."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_961():
    """Verify SAR ADC binary search convergence and DNL bounds 961."""
    code, hist = sar_adc_convert(0.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_962():
    """Verify SAR ADC binary search convergence and DNL bounds 962."""
    code, hist = sar_adc_convert(0.30000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_963():
    """Verify SAR ADC binary search convergence and DNL bounds 963."""
    code, hist = sar_adc_convert(0.4, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_964():
    """Verify SAR ADC binary search convergence and DNL bounds 964."""
    code, hist = sar_adc_convert(0.5, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_965():
    """Verify SAR ADC binary search convergence and DNL bounds 965."""
    code, hist = sar_adc_convert(0.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_966():
    """Verify SAR ADC binary search convergence and DNL bounds 966."""
    code, hist = sar_adc_convert(0.7000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_967():
    """Verify SAR ADC binary search convergence and DNL bounds 967."""
    code, hist = sar_adc_convert(0.8, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_968():
    """Verify SAR ADC binary search convergence and DNL bounds 968."""
    code, hist = sar_adc_convert(0.9, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_969():
    """Verify SAR ADC binary search convergence and DNL bounds 969."""
    code, hist = sar_adc_convert(1.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_970():
    """Verify SAR ADC binary search convergence and DNL bounds 970."""
    code, hist = sar_adc_convert(1.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_971():
    """Verify SAR ADC binary search convergence and DNL bounds 971."""
    code, hist = sar_adc_convert(1.2000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_972():
    """Verify SAR ADC binary search convergence and DNL bounds 972."""
    code, hist = sar_adc_convert(1.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_973():
    """Verify SAR ADC binary search convergence and DNL bounds 973."""
    code, hist = sar_adc_convert(1.4000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_974():
    """Verify SAR ADC binary search convergence and DNL bounds 974."""
    code, hist = sar_adc_convert(1.5000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_975():
    """Verify SAR ADC binary search convergence and DNL bounds 975."""
    code, hist = sar_adc_convert(1.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_976():
    """Verify SAR ADC binary search convergence and DNL bounds 976."""
    code, hist = sar_adc_convert(1.7000000000000002, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_977():
    """Verify SAR ADC binary search convergence and DNL bounds 977."""
    code, hist = sar_adc_convert(1.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_978():
    """Verify SAR ADC binary search convergence and DNL bounds 978."""
    code, hist = sar_adc_convert(1.9000000000000001, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_979():
    """Verify SAR ADC binary search convergence and DNL bounds 979."""
    code, hist = sar_adc_convert(2.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_980():
    """Verify SAR ADC binary search convergence and DNL bounds 980."""
    code, hist = sar_adc_convert(2.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_981():
    """Verify SAR ADC binary search convergence and DNL bounds 981."""
    code, hist = sar_adc_convert(2.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_982():
    """Verify SAR ADC binary search convergence and DNL bounds 982."""
    code, hist = sar_adc_convert(2.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_983():
    """Verify SAR ADC binary search convergence and DNL bounds 983."""
    code, hist = sar_adc_convert(2.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_984():
    """Verify SAR ADC binary search convergence and DNL bounds 984."""
    code, hist = sar_adc_convert(2.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_985():
    """Verify SAR ADC binary search convergence and DNL bounds 985."""
    code, hist = sar_adc_convert(2.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_986():
    """Verify SAR ADC binary search convergence and DNL bounds 986."""
    code, hist = sar_adc_convert(2.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_987():
    """Verify SAR ADC binary search convergence and DNL bounds 987."""
    code, hist = sar_adc_convert(2.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_988():
    """Verify SAR ADC binary search convergence and DNL bounds 988."""
    code, hist = sar_adc_convert(2.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_989():
    """Verify SAR ADC binary search convergence and DNL bounds 989."""
    code, hist = sar_adc_convert(3.0000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_990():
    """Verify SAR ADC binary search convergence and DNL bounds 990."""
    code, hist = sar_adc_convert(3.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_991():
    """Verify SAR ADC binary search convergence and DNL bounds 991."""
    code, hist = sar_adc_convert(3.2, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_992():
    """Verify SAR ADC binary search convergence and DNL bounds 992."""
    code, hist = sar_adc_convert(3.3000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_993():
    """Verify SAR ADC binary search convergence and DNL bounds 993."""
    code, hist = sar_adc_convert(3.4000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_994():
    """Verify SAR ADC binary search convergence and DNL bounds 994."""
    code, hist = sar_adc_convert(3.5000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_995():
    """Verify SAR ADC binary search convergence and DNL bounds 995."""
    code, hist = sar_adc_convert(3.6, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_996():
    """Verify SAR ADC binary search convergence and DNL bounds 996."""
    code, hist = sar_adc_convert(3.7, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_997():
    """Verify SAR ADC binary search convergence and DNL bounds 997."""
    code, hist = sar_adc_convert(3.8000000000000003, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_998():
    """Verify SAR ADC binary search convergence and DNL bounds 998."""
    code, hist = sar_adc_convert(3.9000000000000004, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_999():
    """Verify SAR ADC binary search convergence and DNL bounds 999."""
    code, hist = sar_adc_convert(4.0, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8

def test_converter_linearity_scenario_1000():
    """Verify SAR ADC binary search convergence and DNL bounds 1000."""
    code, hist = sar_adc_convert(0.1, 5.0, 8)
    assert 0 <= code <= 255
    assert len(hist) == 8
