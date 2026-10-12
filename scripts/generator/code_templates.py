"""Code templates and generators for the LDICA Enterprise Architecture.

Dispatches code generation to modular generator engines.
"""
from __future__ import annotations

from pathlib import Path

from scripts.generator.analog_generators import *
from scripts.generator.timing_generators import *
from scripts.generator.converter_generators import *
from scripts.generator.digital_generators import *
from scripts.generator.memory_hdl_generators import *
from scripts.generator.problem_bank_generators import *
from scripts.generator.test_suite_generators import *
from scripts.generator.docs_generators import *

ROOT = Path(__file__).resolve().parents[2]
APP = ROOT / "app"
SIM = APP / "simulation"
HDL = APP / "hdl"
PROBLEMS = APP / "content" / "problem_bank"
MANUALS = APP / "manuals"
TESTS = ROOT / "tests"


def ensure_init_files():
    """Ensure all package directories have __init__.py files."""
    dirs = [
        SIM,
        SIM / "core",
        SIM / "analog",
        SIM / "timing",
        SIM / "converters",
        SIM / "digital",
        SIM / "memory",
        HDL,
        HDL / "verilog",
        HDL / "vhdl",
        PROBLEMS,
        MANUALS,
        TESTS,
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        init_file = d / "__init__.py"
        if not init_file.exists():
            init_file.write_text(f'"""Package initialization for {d.name}."""\n', encoding="utf-8")


def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def generate_for_pr(pr_id: int):
    """Generate files corresponding to PR pr_id."""
    ensure_init_files()

    if pr_id == 1:
        write_file(SIM / "core" / "mna_solver.py", generate_mna_solver_code())
        write_file(SIM / "core" / "matrix_utils.py", generate_matrix_utils_code())
        write_file(SIM / "core" / "integrators.py", generate_integrators_code())

    elif pr_id == 2:
        write_file(SIM / "analog" / "opamp_models.py", generate_opamp_models_code())

    elif pr_id == 3:
        write_file(SIM / "analog" / "linear_stages.py", generate_linear_stages_code())

    elif pr_id == 4:
        write_file(SIM / "analog" / "instrumentation_amp.py", generate_instrumentation_amp_code())

    elif pr_id == 5:
        write_file(SIM / "analog" / "filters_butterworth.py", generate_butterworth_code())

    elif pr_id == 6:
        write_file(SIM / "analog" / "filters_chebyshev_bessel.py", generate_chebyshev_bessel_code())

    elif pr_id == 7:
        write_file(SIM / "analog" / "filters_state_variable.py", generate_state_variable_code())

    elif pr_id == 8:
        write_file(SIM / "analog" / "switched_capacitor_filters.py", generate_switched_capacitor_code())

    elif pr_id == 9:
        write_file(SIM / "analog" / "precision_rectifiers.py", generate_precision_rectifiers_code())

    elif pr_id == 10:
        write_file(SIM / "analog" / "log_antilog.py", generate_log_antilog_code())

    elif pr_id == 11:
        write_file(SIM / "analog" / "analog_multipliers.py", generate_analog_multipliers_code())

    elif pr_id == 12:
        write_file(SIM / "analog" / "schmitt_triggers.py", generate_schmitt_triggers_code())

    elif pr_id == 13:
        write_file(SIM / "analog" / "sample_and_hold.py", generate_sample_and_hold_code())

    elif pr_id == 14:
        write_file(SIM / "analog" / "peak_detectors.py", generate_peak_detectors_code())

    elif pr_id == 15:
        write_file(SIM / "timing" / "timer555_core.py", generate_timer555_core_code())

    elif pr_id == 16:
        write_file(SIM / "timing" / "timer555_monostable.py", generate_timer555_monostable_code())

    elif pr_id == 17:
        write_file(SIM / "timing" / "timer555_astable.py", generate_timer555_astable_code())

    elif pr_id == 18:
        write_file(SIM / "timing" / "timer555_modulation.py", generate_timer555_modulation_code())

    elif pr_id == 19:
        write_file(SIM / "timing" / "timer556_dual.py", generate_timer556_dual_code())

    elif pr_id == 20:
        write_file(SIM / "timing" / "vco566.py", generate_vco566_code())

    elif pr_id == 21:
        write_file(SIM / "timing" / "pll565_phase_detector.py", generate_pll565_pd_code())

    elif pr_id == 22:
        write_file(SIM / "timing" / "pll565_loop_filter.py", generate_pll565_filter_code())

    elif pr_id == 23:
        write_file(SIM / "timing" / "pll_frequency_synthesis.py", generate_pll_synth_code())

    elif pr_id == 24:
        write_file(SIM / "timing" / "pll_demodulation.py", generate_pll_demod_code())

    elif pr_id == 25:
        write_file(SIM / "timing" / "icl8038_generator.py", generate_icl8038_code())

    elif pr_id == 26:
        write_file(SIM / "timing" / "xr2206_generator.py", generate_xr2206_code())

    elif pr_id == 27:
        write_file(SIM / "converters" / "dac_binary_weighted.py", generate_dac_binary_code())

    elif pr_id == 28:
        write_file(SIM / "converters" / "dac_r2r_ladder.py", generate_dac_r2r_code())

    elif pr_id == 29:
        write_file(SIM / "converters" / "dac_specifications.py", generate_dac_specs_code())

    elif pr_id == 30:
        write_file(SIM / "converters" / "dac_dynamic_metrics.py", generate_dac_dynamic_code())

    elif pr_id == 31:
        write_file(SIM / "converters" / "dac_multiplying.py", generate_dac_multiplying_code())

    elif pr_id == 32:
        write_file(SIM / "converters" / "adc_sampling_theory.py", generate_adc_sampling_code())

    elif pr_id == 33:
        write_file(SIM / "converters" / "adc_flash.py", generate_adc_flash_code())

    elif pr_id == 34:
        write_file(SIM / "converters" / "adc_sar.py", generate_adc_sar_code())

    elif pr_id == 35:
        write_file(SIM / "converters" / "adc_dual_slope.py", generate_adc_dual_slope_code())

    elif pr_id == 36:
        write_file(SIM / "converters" / "adc_tracking_counter.py", generate_adc_tracking_code())

    elif pr_id == 37:
        write_file(SIM / "converters" / "adc_sigma_delta.py", generate_adc_sigma_delta_code())

    elif pr_id == 38:
        write_file(SIM / "converters" / "adc_decimation_filter.py", generate_adc_decimation_code())

    elif pr_id == 39:
        write_file(SIM / "digital" / "logic_families.py", generate_logic_families_code())

    elif pr_id == 40:
        write_file(SIM / "digital" / "ic_gates_basic.py", generate_ic_gates_basic_code())

    elif pr_id == 41:
        write_file(SIM / "digital" / "ic_gates_multi.py", generate_ic_gates_multi_code())

    elif pr_id == 42:
        write_file(SIM / "digital" / "ic_decoders_74138_139.py", generate_ic_decoders_code())

    elif pr_id == 43:
        write_file(SIM / "digital" / "ic_decoder_74154.py", generate_ic_decoder_74154_code())

    elif pr_id == 44:
        write_file(SIM / "digital" / "ic_encoders_74147_148.py", generate_ic_encoders_code())

    elif pr_id == 45:
        write_file(SIM / "digital" / "ic_mux_74151_153.py", generate_ic_mux_code())

    elif pr_id == 46:
        write_file(SIM / "digital" / "ic_mux_74157.py", generate_ic_mux_74157_code())

    elif pr_id == 47:
        write_file(SIM / "digital" / "ic_display_7447_7448.py", generate_ic_display_code())

    elif pr_id == 48:
        write_file(SIM / "digital" / "ic_adder_7483.py", generate_ic_adder_7483_code())

    elif pr_id == 49:
        write_file(SIM / "digital" / "ic_comparator_7485.py", generate_ic_comparator_7485_code())

    elif pr_id == 50:
        write_file(SIM / "digital" / "ic_parity_74180.py", generate_ic_parity_74180_code())

    elif pr_id == 51:
        write_file(SIM / "digital" / "ic_alu_74181.py", generate_ic_alu_74181_code())

    elif pr_id == 52:
        write_file(SIM / "digital" / "flip_flops_core.py", generate_flip_flops_core_code())

    elif pr_id == 53:
        write_file(SIM / "digital" / "ic_flipflops_7474_7476.py", generate_ic_flipflops_code())

    elif pr_id == 54:
        write_file(SIM / "digital" / "shift_registers_core.py", generate_shift_registers_core_code())

    elif pr_id == 55:
        write_file(SIM / "digital" / "ic_shift_74194.py", generate_ic_shift_74194_code())

    elif pr_id == 56:
        write_file(SIM / "digital" / "ring_johnson_counters.py", generate_ring_johnson_code())

    elif pr_id == 57:
        write_file(SIM / "digital" / "ic_ripple_counters_7490_93.py", generate_ic_ripple_counters_code())

    elif pr_id == 58:
        write_file(SIM / "digital" / "ic_sync_counters_74160_163.py", generate_ic_sync_counters_code())

    elif pr_id == 59:
        write_file(SIM / "digital" / "ic_updown_counters_74190_191.py", generate_ic_updown_counters_code())

    elif pr_id == 60:
        write_file(SIM / "digital" / "ic_bus_transceivers_74244_245.py", generate_ic_bus_transceivers_code())

    elif pr_id == 61:
        write_file(SIM / "digital" / "ic_latches_74373_374.py", generate_ic_latches_code())

    elif pr_id == 62:
        write_file(SIM / "memory" / "sram_architecture.py", generate_sram_code())

    elif pr_id == 63:
        write_file(SIM / "memory" / "dram_architecture.py", generate_dram_code())

    elif pr_id == 64:
        write_file(SIM / "memory" / "non_volatile_memory.py", generate_rom_eprom_code())

    elif pr_id == 65:
        write_file(SIM / "memory" / "flash_memory.py", generate_flash_memory_code())

    elif pr_id == 66:
        write_file(SIM / "memory" / "memory_expansion.py", generate_memory_expansion_code())

    elif pr_id == 67:
        write_file(HDL / "verilog" / "combinational_circuits.v", generate_verilog_combinational_code())
        write_file(HDL / "verilog" / "decoders.v", generate_verilog_decoders_code())
        write_file(HDL / "verilog" / "multiplexers.v", generate_verilog_multiplexers_code())
        write_file(HDL / "verilog" / "adders.v", generate_verilog_adders_code())

    elif pr_id == 68:
        write_file(HDL / "verilog" / "sequential_circuits.v", generate_verilog_sequential_code())
        write_file(HDL / "verilog" / "registers.v", generate_verilog_registers_code())
        write_file(HDL / "verilog" / "counters.v", generate_verilog_counters_code())

    elif pr_id == 69:
        write_file(HDL / "verilog" / "ic74xx_library.v", generate_verilog_74xx_library_code())
        write_file(HDL / "verilog" / "tb_ic74xx.v", generate_verilog_tb_74xx_code())

    elif pr_id == 70:
        write_file(HDL / "vhdl" / "ldica_digital_pkg.vhd", generate_vhdl_pkg_code())
        write_file(HDL / "vhdl" / "gates.vhd", generate_vhdl_gates_code())
        write_file(HDL / "vhdl" / "arithmetic.vhd", generate_vhdl_arithmetic_code())

    elif pr_id == 71:
        write_file(PROBLEMS / "unit1_problems.py", generate_problem_bank_unit(1, "Operational Amplifiers & Linear ICs", 3300))

    elif pr_id == 72:
        write_file(PROBLEMS / "unit2_problems.py", generate_problem_bank_unit(2, "Timers, PLLs & Waveform Generators", 3300))

    elif pr_id == 73:
        write_file(PROBLEMS / "unit3_problems.py", generate_problem_bank_unit(3, "D/A & A/D Converters", 3300))

    elif pr_id == 74:
        write_file(PROBLEMS / "unit4_problems.py", generate_problem_bank_unit(4, "Combinational Logic & Digital ICs", 3300))

    elif pr_id == 75:
        write_file(PROBLEMS / "unit5_problems.py", generate_problem_bank_unit(5, "Sequential Circuits & Semiconductor Memories", 3300))

    elif pr_id == 76:
        write_file(TESTS / "test_simulation_analog.py", generate_test_analog_suite())

    elif pr_id == 77:
        write_file(TESTS / "test_simulation_timing.py", generate_test_timing_suite())

    elif pr_id == 78:
        write_file(TESTS / "test_simulation_converters.py", generate_test_converters_suite())

    elif pr_id == 79:
        write_file(TESTS / "test_simulation_combinational.py", generate_test_combinational_suite())

    elif pr_id == 80:
        write_file(TESTS / "test_simulation_sequential_memory.py", generate_test_sequential_suite())

    elif pr_id == 81:
        write_file(TESTS / "test_hdl_netlists.py", generate_test_hdl_suite())

    elif pr_id == 82:
        write_file(MANUALS / "lab_manuals.py", generate_lab_manuals_code())

    elif pr_id == 83:
        write_file(SIM / "api_bridge.py", generate_api_bridge_code())

    elif pr_id == 84:
        write_file(APP / "content" / "extended_graph_matrix.py", generate_graph_matrix_code())

    elif pr_id == 85:
        write_file(TESTS / "test_enterprise_verification.py", generate_enterprise_verification_code())
        update_readme_and_changelog()
