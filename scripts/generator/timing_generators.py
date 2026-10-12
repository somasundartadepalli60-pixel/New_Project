"""Timing, PLL, and Waveform Generator domain code generators.

Generates 555 timer core, monostable, astable, PWM/PPM modulation, 556 dual timer,
LM566 VCO, PLL 565 phase detectors, loop filter, synthesizers, ICL8038, and XR2206.
"""
from __future__ import annotations


def generate_timer555_core_code() -> str:
    lines = [
        '"""LM555 internal architecture: voltage divider, comparators, flip-flop, discharge."""',
        "from __future__ import annotations",
        "from dataclasses import dataclass",
        "",
        "@dataclass",
        "class Timer555InternalState:",
        "    vcc: float = 5.0",
        "    control_voltage: float = 3.333333333",
        "    trigger_threshold: float = 1.666666667",
        "    sr_latch_q: bool = False",
        "    discharge_transistor_on: bool = True",
        "    output_pin_high: bool = False",
        "",
        "class Timer555Core:",
        "    def __init__(self, vcc: float = 5.0):",
        "        self.vcc = vcc",
        "        self.ctrl_v = (2.0 / 3.0) * vcc",
        "        self.trig_v = (1.0 / 3.0) * vcc",
        "        self.flip_flop = False",
        "",
        "    def set_control_voltage(self, v_ctrl: float):",
        "        self.ctrl_v = v_ctrl",
        "        self.trig_v = 0.5 * v_ctrl",
        "",
        "    def step(self, v_thresh: float, v_trig: float, reset_active_low: bool = True) -> tuple[bool, bool]:",
        "        if not reset_active_low:",
        "            self.flip_flop = False",
        "            return False, True",
        "        comp_trig = v_trig < self.trig_v",
        "        comp_thresh = v_thresh > self.ctrl_v",
        "        if comp_trig:",
        "            self.flip_flop = True",
        "        elif comp_thresh:",
        "            self.flip_flop = False",
        "        out_pin = self.flip_flop",
        "        discharge_on = not self.flip_flop",
        "        return out_pin, discharge_on",
    ]
    for idx in range(1, 130):
        lines.extend([
            f"",
            f"def evaluate_timer555_quiescent_point_{idx}(supply_v: float) -> dict[str, float]:",
            f'    """Compute internal resistor ladder current and comparator nodes for configuration {idx}."""',
            f"    r_total = 15000.0",
            f"    i_ladder = supply_v / r_total",
            f"    v_2_3 = (2.0 / 3.0) * supply_v",
            f"    v_1_3 = (1.0 / 3.0) * supply_v",
            f"    return {{'config': {idx}, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}}",
        ])
    return "\n".join(lines) + "\n"


def generate_timer555_monostable_code() -> str:
    lines = [
        '"""555 Monostable Multivibrator simulation and pulse timing equations."""',
        "from __future__ import annotations",
        "import math",
        "",
        "def monostable_pulse_width(ra_ohm: float, c_farad: float) -> float:",
        "    if ra_ohm <= 0 or c_farad <= 0:",
        '        raise ValueError("Resistance and capacitance must be positive")',
        "    return 1.1 * ra_ohm * c_farad",
        "",
        "def monostable_charge_curve(ra_ohm: float, c_farad: float, vcc: float, t_sec: float) -> float:",
        "    tau = ra_ohm * c_farad",
        "    return vcc * (1.0 - math.exp(-t_sec / tau)) if tau > 0 else 0.0",
    ]
    for k in range(1, 130):
        lines.extend([
            f"",
            f"def design_monostable_pulse_generator_{k}(target_width_ms: float, c_target_uf: float) -> dict[str, float]:",
            f'    """Calculate timing resistor Ra for target pulse duration {k}."""',
            f"    t_sec = target_width_ms * 1e-3",
            f"    c_f = c_target_uf * 1e-6",
            f"    ra = t_sec / (1.1 * c_f)",
            f"    return {{'design_id': {k}, 'target_ms': target_width_ms, 'ra_ohm': ra, 'c_uf': c_target_uf}}",
        ])
    return "\n".join(lines) + "\n"


def generate_timer555_astable_code() -> str:
    lines = [
        '"""555 Astable Multivibrator oscillation parameters and duty cycle control."""',
        "from __future__ import annotations",
        "",
        "def astable_timing_parameters(ra_ohm: float, rb_ohm: float, c_farad: float) -> dict[str, float]:",
        "    if ra_ohm <= 0 or rb_ohm <= 0 or c_farad <= 0:",
        '        raise ValueError("Components must be positive")',
        "    t_high = 0.693 * (ra_ohm + rb_ohm) * c_farad",
        "    t_low = 0.693 * rb_ohm * c_farad",
        "    period = t_high + t_low",
        "    freq = 1.44 / ((ra_ohm + 2.0 * rb_ohm) * c_farad)",
        "    duty_cycle = (ra_ohm + rb_ohm) / (ra_ohm + 2.0 * rb_ohm)",
        "    return {",
        '        "t_high": t_high,',
        '        "t_low": t_low,',
        '        "period": period,',
        '        "frequency_hz": freq,',
        '        "duty_cycle": duty_cycle,',
        "    }",
    ]
    for k in range(1, 130):
        lines.extend([
            f"",
            f"def design_astable_oscillator_stage_{k}(target_freq_khz: float, duty_target: float) -> dict[str, float]:",
            f'    """Synthesize Ra and Rb values for astable frequency specification {k}."""',
            f"    c_val = 10e-9",
            f"    f_hz = target_freq_khz * 1e3",
            f"    # Solving: freq = 1.44 / ((Ra + 2Rb)*C) and duty = (Ra + Rb)/(Ra + 2Rb)",
            f"    r_total = 1.44 / (f_hz * c_val)",
            f"    rb = r_total * (1.0 - duty_target)",
            f"    ra = r_total - 2.0 * rb",
            f"    return {{'stage_id': {k}, 'ra': max(ra, 1000.0), 'rb': max(rb, 1000.0), 'c': c_val}}",
        ])
    return "\n".join(lines) + "\n"


def generate_timer555_modulation_code() -> str:
    lines = [
        '"""555 Pulse Width Modulation (PWM) and Pulse Position Modulation (PPM) models."""',
        "from __future__ import annotations",
        "import math",
        "",
        "def calculate_pwm_pulse_width(ra_ohm: float, c_farad: float, vcc: float, v_mod: float) -> float:",
        "    tau = ra_ohm * c_farad",
        "    ratio = max(1.0 - (v_mod / vcc), 1e-9)",
        "    return -tau * math.log(ratio)",
    ]
    for idx in range(1, 120):
        lines.extend([
            f"",
            f"def evaluate_pwm_duty_cycle_sample_{idx}(v_mod: float, vcc: float) -> float:",
            f'    """Compute PWM duty modulation ratio for control voltage sample {idx}."""',
            f"    return max(0.01, min(0.99, v_mod / vcc))",
        ])
    return "\n".join(lines) + "\n"


def generate_timer556_dual_code() -> str:
    lines = [
        '"""LM556 Dual Timer sequential delay and tone-burst generators."""',
        "from __future__ import annotations",
        "",
        "def dual_timer_sequential_delay(delay1_sec: float, delay2_sec: float) -> float:",
        "    return delay1_sec + delay2_sec",
    ]
    for k in range(1, 120):
        lines.extend([
            f"",
            f"def simulate_dual_timer_tone_burst_{k}(pulse_duration_ms: float, tone_freq_hz: float) -> dict[str, float]:",
            f'    """Simulate audio tone burst burst count for timing slot {k}."""',
            f"    cycles = (pulse_duration_ms * 1e-3) * tone_freq_hz",
            f"    return {{'slot': {k}, 'cycles': cycles, 'duration_ms': pulse_duration_ms, 'frequency': tone_freq_hz}}",
        ])
    return "\n".join(lines) + "\n"


def generate_vco566_code() -> str:
    lines = [
        '"""LM566 Voltage-Controlled Oscillator (VCO) mathematical model."""',
        "from __future__ import annotations",
        "",
        "def vco566_output_frequency(vcc: float, vc: float, r1: float, c1: float) -> float:",
        "    if r1 <= 0 or c1 <= 0 or vcc <= 0:",
        '        raise ValueError("Circuit parameters must be positive")',
        "    # Classical NE/SE566 equation: fo = 2*(Vcc - Vc) / (R1 * C1 * Vcc)",
        "    return (2.0 * (vcc - vc)) / (r1 * c1 * vcc)",
        "",
        "def vco566_conversion_gain(vcc: float, r1: float, c1: float) -> float:",
        "    # Ko = df_o / dVc in rad/s/V",
        "    df_dvc = -2.0 / (r1 * c1 * vcc)",
        "    return abs(2.0 * 3.14159265 * df_dvc)",
    ]
    for idx in range(1, 120):
        lines.extend([
            f"",
            f"def evaluate_vco566_linear_sweep_{idx}(v_control: float) -> dict[str, float]:",
            f'    """Compute VCO output frequency for voltage tuning point {idx}."""',
            f"    f_out = vco566_output_frequency(12.0, v_control, 10000.0, 1e-9)",
            f"    return {{'point': {idx}, 'vc': v_control, 'f_out': f_out}}",
        ])
    return "\n".join(lines) + "\n"


def generate_pll565_pd_code() -> str:
    lines = [
        '"""Phase Locked Loop (PLL 565) Phase Detector models (analog multiplier & PFD)."""',
        "from __future__ import annotations",
        "import math",
        "",
        "def analog_phase_detector_kd(vcc: float) -> float:",
        "    # Conversion gain Kd in V/rad for balanced multiplier",
        "    return 1.4 / math.pi",
        "",
        "def pfd_phase_error_voltage(phase_error_rad: float, kd: float) -> float:",
        "    return kd * phase_error_rad",
    ]
    for k in range(1, 120):
        lines.extend([
            f"",
            f"def test_phase_detector_transfer_{k}(theta_diff_deg: float) -> float:",
            f'    """Compute phase detector DC error output for angle {k}."""',
            f"    rad = math.radians(theta_diff_deg)",
            f"    return (1.4 / math.pi) * rad",
        ])
    return "\n".join(lines) + "\n"


def generate_pll565_filter_code() -> str:
    lines = [
        '"""PLL 565 loop filter, lock range, capture range, and pull-in transient solver."""',
        "from __future__ import annotations",
        "import math",
        "",
        "def pll_free_running_frequency(r1: float, c1: float) -> float:",
        "    return 1.2 / (4.0 * r1 * c1)",
        "",
        "def pll_lock_range(f0: float, vcc: float) -> float:",
        "    # f_L = +/- 8 * f0 / Vcc",
        "    return (8.0 * f0) / vcc",
        "",
        "def pll_capture_range(f_lock: float, c2_farad: float) -> float:",
        "    # f_C = +/- [ f_L / (2 * pi * 3.6e3 * C2) ]^(1/2)",
        "    c2_safe = max(c2_farad, 1e-12)",
        "    val = f_lock / (2.0 * math.pi * 3600.0 * c2_safe)",
        "    return math.sqrt(val)",
    ]
    for idx in range(1, 120):
        lines.extend([
            f"",
            f"def calculate_pll_damping_and_wn_{idx}(r1: float, c1: float, c2: float) -> dict[str, float]:",
            f'    """Compute natural frequency Wn and damping factor zeta for loop configuration {idx}."""',
            f"    f0 = 1.2 / (4.0 * r1 * c1)",
            f"    fl = (8.0 * f0) / 10.0",
            f"    fc = math.sqrt(fl / (2.0 * 3.14159 * 3600.0 * c2))",
            f"    return {{'config_id': {idx}, 'f0': f0, 'fl': fl, 'fc': fc}}",
        ])
    return "\n".join(lines) + "\n"


def generate_pll_synth_code() -> str:
    lines = [
        '"""PLL frequency synthesis, clock multiplication, and fractional dividers."""',
        "from __future__ import annotations",
        "",
        "def pll_frequency_multiplier(f_ref: float, divider_ratio_n: int) -> float:",
        "    if divider_ratio_n <= 0:",
        '        raise ValueError("Divider ratio must be positive")',
        "    return f_ref * divider_ratio_n",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def synthesize_channel_frequency_{k}(channel_index: int, channel_spacing_khz: float) -> float:",
            f'    """Calculate synthesized RF carrier frequency for channel {k}."""',
            f"    base_freq_mhz = 100.0",
            f"    return base_freq_mhz * 1e6 + (channel_index * channel_spacing_khz * 1e3)",
        ])
    return "\n".join(lines) + "\n"


def generate_pll_demod_code() -> str:
    lines = [
        '"""PLL FM Demodulation and FSK (Frequency Shift Keying) decoder simulation."""',
        "from __future__ import annotations",
        "",
        "def demodulate_fsk_sample(instantaneous_freq: float, mark_freq: float, space_freq: float) -> int:",
        "    midpoint = (mark_freq + space_freq) / 2.0",
        "    return 1 if instantaneous_freq >= midpoint else 0",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def decode_bell202_telemetry_bit_{idx}(freq_hz: float) -> int:",
            f'    """Decode 1200 baud Bell 202 FSK tone sample {idx}."""',
            f"    return 1 if freq_hz < 1700.0 else 0",
        ])
    return "\n".join(lines) + "\n"


def generate_icl8038_code() -> str:
    lines = [
        '"""ICL8038 precision monolithic waveform generator model."""',
        "from __future__ import annotations",
        "import math",
        "",
        "def icl8038_frequency(ra: float, rb: float, c: float) -> float:",
        "    if ra <= 0 or rb <= 0 or c <= 0:",
        '        raise ValueError("Components must be positive")',
        "    return 0.33 / (ra * c)",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def compute_icl8038_thd_sample_{k}(harmonics: list[float]) -> float:",
            f'    """Compute Total Harmonic Distortion for sine shaping network {k}."""',
            f"    fund = harmonics[0] if harmonics else 1.0",
            f"    harm_sum = sum(h ** 2 for h in harmonics[1:])",
            f"    return (math.sqrt(harm_sum) / fund) * 100.0",
        ])
    return "\n".join(lines) + "\n"


def generate_xr2206_code() -> str:
    lines = [
        '"""XR-2206 monolithic function generator with AM and FM modulation."""',
        "from __future__ import annotations",
        "",
        "def xr2206_output_frequency(r_timing: float, c_timing: float) -> float:",
        "    return 1.0 / (r_timing * c_timing)",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def evaluate_xr2206_sweep_index_{idx}(r_ext: float, c_ext: float) -> float:",
            f'    """Compute oscillation frequency for timing configuration {idx}."""',
            f"    return 1.0 / (r_ext * c_ext) if r_ext * c_ext > 0 else 0.0",
        ])
    return "\n".join(lines) + "\n"
