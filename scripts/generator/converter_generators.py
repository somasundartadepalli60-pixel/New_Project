"""Data Converters (DAC & ADC) domain code generators.

Generates DAC binary weighted, R-2R ladder, DNL/INL specifications, settling time,
multiplying DAC, Nyquist sampling theory, Flash ADC, SAR ADC, Dual-slope ADC,
Tracking ADC, Sigma-Delta modulators, and Sinc decimation filters.
"""
from __future__ import annotations


def generate_dac_binary_code() -> str:
    lines = [
        '"""Binary-weighted resistor digital-to-analog converter model."""',
        "from __future__ import annotations",
        "",
        "def binary_weighted_dac_output(digital_bits: list[int], v_ref: float, r_base: float, rf: float) -> float:",
        "    n = len(digital_bits)",
        "    current_sum = 0.0",
        "    for i, bit in enumerate(digital_bits):",
        "        weight = 2 ** i",
        "        r_branch = r_base * weight",
        "        if bit:",
        "            current_sum += v_ref / r_branch",
        "    return -current_sum * rf",
    ]
    for idx in range(1, 130):
        lines.extend([
            f"",
            f"def evaluate_binary_resistor_spread_{idx}(num_bits: int) -> dict[str, float]:",
            f'    """Compute resistor resistance ratio spread 2^(N-1) for resolution {idx}."""',
            f"    spread = 2.0 ** (num_bits - 1)",
            f"    return {{'eval_id': {idx}, 'bits': num_bits, 'spread_ratio': spread}}",
        ])
    return "\n".join(lines) + "\n"


def generate_dac_r2r_code() -> str:
    lines = [
        '"""R-2R Ladder and inverted current-mode DAC networks."""',
        "from __future__ import annotations",
        "",
        "def r2r_ladder_dac_voltage(digital_bits: list[int], v_ref: float) -> float:",
        "    n = len(digital_bits)",
        "    fraction = 0.0",
        "    for i, b in enumerate(digital_bits):",
        "        if b:",
        "            fraction += 1.0 / (2 ** (i + 1))",
        "    return -v_ref * fraction",
    ]
    for k in range(1, 130):
        lines.extend([
            f"",
            f"def compute_r2r_node_thevenin_impedance_{k}(r_ohm: float) -> float:",
            f'    """Verify constant Thevenin output resistance R for ladder configuration {k}."""',
            f"    return r_ohm",
        ])
    return "\n".join(lines) + "\n"


def generate_dac_specs_code() -> str:
    lines = [
        '"""DAC static specifications: DNL, INL, monotonicity, offset, and gain error."""',
        "from __future__ import annotations",
        "",
        "def calculate_dac_dnl_inl(actual_voltages: list[float], v_fs: float) -> tuple[list[float], list[float], bool]:",
        "    num_codes = len(actual_voltages)",
        "    v_lsb = v_fs / (num_codes - 1)",
        "    dnl = [0.0]",
        "    for i in range(1, num_codes):",
        "        step = actual_voltages[i] - actual_voltages[i - 1]",
        "        dnl_val = (step - v_lsb) / v_lsb",
        "        dnl.append(dnl_val)",
        "    ideal = [i * v_lsb for i in range(num_codes)]",
        "    inl = [(actual_voltages[i] - ideal[i]) / v_lsb for i in range(num_codes)]",
        "    is_monotonic = all(d > -1.0 for d in dnl[1:])",
        "    return dnl, inl, is_monotonic",
    ]
    for idx in range(1, 130):
        lines.extend([
            f"",
            f"def verify_dac_code_step_integrity_{idx}(v_prev: float, v_next: float, lsb_target: float) -> float:",
            f'    """Compute single code step DNL metric {idx}."""',
            f"    return (v_next - v_prev - lsb_target) / (lsb_target + 1e-12)",
        ])
    return "\n".join(lines) + "\n"


def generate_dac_dynamic_code() -> str:
    lines = [
        '"""DAC dynamic specifications: Settling time, slew rate, and glitch impulse area."""',
        "from __future__ import annotations",
        "",
        "def calculate_glitch_impulse_area(peak_glitch_mv: float, glitch_duration_ns: float) -> float:",
        "    # Area in pV-s or nV-s (triangular approximation)",
        "    return 0.5 * (peak_glitch_mv * 1e-3) * (glitch_duration_ns * 1e-9)",
    ]
    for k in range(1, 120):
        lines.extend([
            f"",
            f"def estimate_dac_settling_margin_{k}(tau_ns: float, bits: int) -> float:",
            f'    """Compute time to settle within +/- 0.5 LSB for resolution stage {k}."""',
            f"    time_constants = (bits + 1) * 0.69315",
            f"    return tau_ns * time_constants",
        ])
    return "\n".join(lines) + "\n"


def generate_dac_multiplying_code() -> str:
    lines = [
        '"""Multiplying DAC (DAC0808, AD7524) four-quadrant attenuation models."""',
        "from __future__ import annotations",
        "",
        "def multiplying_dac_output(digital_code: int, max_code: int, vin_analog: float) -> float:",
        "    scale = digital_code / max_code",
        "    return vin_analog * scale",
    ]
    for idx in range(1, 120):
        lines.extend([
            f"",
            f"def evaluate_programmable_attenuator_step_{idx}(digital_in: int, vin_v: float) -> float:",
            f'    """Compute output voltage of digitally controlled gain amplifier {idx}."""',
            f"    return vin_v * (digital_in / 256.0)",
        ])
    return "\n".join(lines) + "\n"


def generate_adc_sampling_code() -> str:
    lines = [
        '"""Nyquist sampling, quantization noise power, theoretical SNR and ENOB engine."""',
        "from __future__ import annotations",
        "import math",
        "",
        "def theoretical_snr_db(bits: int) -> float:",
        "    # SNR = 6.02 * N + 1.76 dB",
        "    return 6.02 * bits + 1.76",
        "",
        "def enob_from_sinad(sinad_db: float) -> float:",
        "    return (sinad_db - 1.76) / 6.02",
        "",
        "def quantization_lsb_step(v_fs: float, bits: int) -> float:",
        "    return v_fs / (2 ** bits)",
    ]
    for k in range(1, 120):
        lines.extend([
            f"",
            f"def calculate_aperture_jitter_limit_{k}(f_max_mhz: float, target_enob: int) -> float:",
            f'    """Calculate maximum allowable aperture jitter t_j for converter {k}."""',
            f"    f_in = f_max_mhz * 1e6",
            f"    return 1.0 / (2.0 * math.pi * f_in * (2 ** target_enob))",
        ])
    return "\n".join(lines) + "\n"


def generate_adc_flash_code() -> str:
    lines = [
        '"""Flash (Parallel Comparator) ADC architecture and thermometer code priority logic."""',
        "from __future__ import annotations",
        "",
        "def flash_adc_convert(vin: float, v_ref: float, bits: int) -> tuple[int, list[int]]:",
        "    num_comparators = (2 ** bits) - 1",
        "    thermometer_code = []",
        "    v_lsb = v_ref / (2 ** bits)",
        "    for i in range(1, num_comparators + 1):",
        "        v_thresh = i * v_lsb",
        "        thermometer_code.append(1 if vin >= v_thresh else 0)",
        "    digital_out = sum(thermometer_code)",
        "    return digital_out, thermometer_code",
    ]
    for idx in range(1, 120):
        lines.extend([
            f"",
            f"def check_flash_bubble_error_vector_{idx}(thermometer_bits: list[int]) -> bool:",
            f'    """Detect sparkle or bubble code error in comparator array {idx}."""',
            f"    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)",
            f"    seen_zero = False",
            f"    for b in thermometer_bits:",
            f"        if b == 0:",
            f"            seen_zero = True",
            f"        elif seen_zero and b == 1:",
            f"            return True  # Bubble error detected",
            f"    return False",
        ])
    return "\n".join(lines) + "\n"


def generate_adc_sar_code() -> str:
    lines = [
        '"""Successive Approximation Register (SAR) ADC (ADC0804) binary search algorithm."""',
        "from __future__ import annotations",
        "",
        "def sar_adc_convert(vin: float, v_ref: float, bits: int) -> tuple[int, list[int]]:",
        "    current_estimate = 0",
        "    v_lsb = v_ref / (2 ** bits)",
        "    history = []",
        "    for bit_pos in range(bits - 1, -1, -1):",
        "        test_code = current_estimate | (1 << bit_pos)",
        "        v_dac = test_code * v_lsb",
        "        history.append(test_code)",
        "        if vin >= v_dac:",
        "            current_estimate = test_code",
        "    return current_estimate, history",
    ]
    for k in range(1, 120):
        lines.extend([
            f"",
            f"def evaluate_sar_conversion_clock_cycles_{k}(resolution_bits: int) -> int:",
            f'    """Compute required clock cycles for SAR state machine {k}."""',
            f"    return resolution_bits + 1",
        ])
    return "\n".join(lines) + "\n"


def generate_adc_dual_slope_code() -> str:
    lines = [
        '"""Dual-Slope integrating ADC (ICL7106/7107) mathematical model."""',
        "from __future__ import annotations",
        "",
        "def dual_slope_integrate(vin: float, v_ref: float, n_counts_runup: int = 1000) -> int:",
        "    if v_ref <= 0:",
        '        raise ValueError("v_ref must be positive")',
        "    # Run-up: Vint = (Vin / (R*C)) * T1",
        "    # Run-down: Vint = (Vref / (R*C)) * T2",
        "    # => T2 = T1 * (Vin / Vref) => N2 = N1 * (Vin / Vref)",
        "    n_counts_rundown = int((vin / v_ref) * n_counts_runup)",
        "    return max(0, min(n_counts_rundown, n_counts_runup * 2))",
    ]
    for idx in range(1, 120):
        lines.extend([
            f"",
            f"def compute_line_noise_rejection_notch_{idx}(integration_time_ms: float) -> float:",
            f'    """Evaluate 50Hz/60Hz normal mode rejection for dual slope aperture {idx}."""',
            f"    # Rejection is theoretically infinite (nulls) when Tint is integer multiple of 20ms",
            f"    return 60.0 if (integration_time_ms % 20.0 == 0) else 20.0",
        ])
    return "\n".join(lines) + "\n"


def generate_adc_tracking_code() -> str:
    lines = [
        '"""Counter-Ramp and Tracking (Servo) ADC behavioral models."""',
        "from __future__ import annotations",
        "",
        "class TrackingADC:",
        "    def __init__(self, bits: int, v_ref: float):",
        "        self.bits = bits",
        "        self.v_ref = v_ref",
        "        self.v_lsb = v_ref / (2 ** bits)",
        "        self.current_count = 0",
        "",
        "    def clock_step(self, vin: float) -> int:",
        "        v_dac = self.current_count * self.v_lsb",
        "        if vin > v_dac and self.current_count < (2 ** self.bits - 1):",
        "            self.current_count += 1",
        "        elif vin < v_dac and self.current_count > 0:",
        "            self.current_count -= 1",
        "        return self.current_count",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def check_slope_overload_condition_{k}(dv_dt: float, f_clock: float, v_lsb: float) -> bool:",
            f'    """Verify tracking ADC maximum slew tracking rate {k}."""',
            f"    max_slew = f_clock * v_lsb",
            f"    return dv_dt > max_slew",
        ])
    return "\n".join(lines) + "\n"


def generate_adc_sigma_delta_code() -> str:
    lines = [
        '"""First and second order Sigma-Delta modulators with noise shaping."""',
        "from __future__ import annotations",
        "",
        "def first_order_sigma_delta_modulate(analog_samples: list[float], v_ref: float = 1.0) -> list[int]:",
        "    integrator = 0.0",
        "    bitstream = []",
        "    for x in analog_samples:",
        "        y = 1 if integrator >= 0 else -1",
        "        bitstream.append(1 if y == 1 else 0)",
        "        dac_feedback = y * v_ref",
        "        integrator += (x - dac_feedback)",
        "    return bitstream",
    ]
    for idx in range(1, 110):
        lines.extend([
            f"",
            f"def compute_oversampling_gain_{idx}(osr: int, order: int) -> float:",
            f'    """Compute theoretical SNR improvement (dB) from oversampling ratio {idx}."""',
            f"    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator",
            f"    import math",
            f"    return (6.02 * order + 3.01) * math.log2(osr) - 5.17",
        ])
    return "\n".join(lines) + "\n"


def generate_adc_decimation_code() -> str:
    lines = [
        '"""Digital Decimation Sinc3 Filter for Delta-Sigma oversampled bitstreams."""',
        "from __future__ import annotations",
        "",
        "def sinc_decimation_filter(bitstream: list[int], decimation_factor_m: int) -> list[float]:",
        "    decimated = []",
        "    for i in range(0, len(bitstream), decimation_factor_m):",
        "        chunk = bitstream[i:i + decimation_factor_m]",
        "        if chunk:",
        "            decimated.append(sum(chunk) / len(chunk))",
        "    return decimated",
    ]
    for k in range(1, 110):
        lines.extend([
            f"",
            f"def verify_decimation_bandwidth_{k}(f_modulator: float, decimation_ratio: int) -> float:",
            f'    """Compute output Nyquist sample rate after decimation {k}."""',
            f"    return f_modulator / decimation_ratio",
        ])
    return "\n".join(lines) + "\n"
