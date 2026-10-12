"""Switched-capacitor filter equivalence and clocking dynamics."""
from __future__ import annotations

def sc_equivalent_resistance(c_val: float, f_clock: float) -> float:
    if c_val <= 0 or f_clock <= 0:
        raise ValueError("Capacitance and clock frequency must be positive")
    return 1.0 / (c_val * f_clock)

def evaluate_sc_integrator_spec_1(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 1."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 1, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_2(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 2."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 2, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_3(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 3."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 3, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_4(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 4."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 4, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_5(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 5."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 5, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_6(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 6."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 6, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_7(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 7."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 7, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_8(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 8."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 8, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_9(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 9."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 9, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_10(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 10."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 10, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_11(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 11."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 11, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_12(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 12."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 12, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_13(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 13."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 13, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_14(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 14."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 14, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_15(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 15."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 15, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_16(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 16."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 16, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_17(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 17."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 17, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_18(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 18."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 18, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_19(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 19."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 19, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_20(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 20."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 20, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_21(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 21."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 21, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_22(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 22."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 22, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_23(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 23."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 23, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_24(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 24."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 24, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_25(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 25."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 25, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_26(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 26."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 26, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_27(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 27."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 27, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_28(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 28."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 28, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_29(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 29."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 29, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_30(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 30."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 30, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_31(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 31."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 31, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_32(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 32."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 32, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_33(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 33."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 33, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_34(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 34."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 34, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_35(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 35."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 35, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_36(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 36."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 36, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_37(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 37."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 37, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_38(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 38."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 38, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_39(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 39."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 39, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_40(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 40."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 40, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_41(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 41."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 41, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_42(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 42."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 42, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_43(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 43."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 43, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_44(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 44."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 44, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_45(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 45."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 45, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_46(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 46."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 46, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_47(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 47."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 47, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_48(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 48."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 48, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_49(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 49."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 49, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_50(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 50."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 50, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_51(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 51."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 51, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_52(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 52."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 52, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_53(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 53."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 53, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_54(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 54."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 54, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_55(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 55."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 55, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_56(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 56."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 56, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_57(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 57."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 57, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_58(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 58."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 58, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_59(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 59."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 59, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_60(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 60."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 60, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_61(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 61."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 61, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_62(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 62."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 62, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_63(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 63."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 63, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_64(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 64."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 64, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_65(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 65."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 65, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_66(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 66."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 66, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_67(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 67."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 67, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_68(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 68."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 68, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_69(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 69."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 69, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_70(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 70."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 70, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_71(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 71."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 71, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_72(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 72."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 72, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_73(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 73."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 73, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_74(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 74."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 74, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_75(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 75."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 75, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_76(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 76."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 76, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_77(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 77."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 77, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_78(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 78."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 78, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_79(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 79."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 79, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_80(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 80."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 80, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_81(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 81."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 81, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_82(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 82."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 82, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_83(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 83."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 83, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_84(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 84."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 84, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_85(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 85."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 85, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_86(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 86."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 86, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_87(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 87."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 87, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_88(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 88."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 88, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_89(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 89."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 89, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_90(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 90."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 90, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_91(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 91."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 91, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_92(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 92."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 92, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_93(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 93."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 93, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_94(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 94."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 94, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_95(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 95."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 95, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_96(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 96."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 96, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_97(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 97."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 97, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_98(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 98."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 98, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_99(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 99."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 99, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_100(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 100."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 100, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_101(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 101."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 101, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_102(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 102."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 102, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_103(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 103."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 103, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_104(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 104."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 104, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_105(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 105."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 105, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_106(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 106."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 106, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_107(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 107."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 107, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_108(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 108."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 108, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_109(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 109."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 109, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_110(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 110."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 110, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_111(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 111."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 111, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_112(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 112."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 112, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_113(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 113."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 113, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_114(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 114."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 114, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_115(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 115."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 115, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_116(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 116."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 116, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_117(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 117."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 117, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_118(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 118."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 118, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}

def evaluate_sc_integrator_spec_119(c_in: float, c_int: float, f_clk: float) -> dict[str, float]:
    """Compute equivalent integration time constant for SC cell 119."""
    req = 1.0 / (c_in * f_clk)
    tau = req * c_int
    unity_gain_freq = 1.0 / (2.0 * 3.14159265 * tau)
    return {'cell_id': 119, 'req': req, 'tau': tau, 'f_unity': unity_gain_freq}
