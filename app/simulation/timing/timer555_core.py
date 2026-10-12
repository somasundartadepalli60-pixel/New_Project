"""LM555 internal architecture: voltage divider, comparators, flip-flop, discharge."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Timer555InternalState:
    vcc: float = 5.0
    control_voltage: float = 3.333333333
    trigger_threshold: float = 1.666666667
    sr_latch_q: bool = False
    discharge_transistor_on: bool = True
    output_pin_high: bool = False

class Timer555Core:
    def __init__(self, vcc: float = 5.0):
        self.vcc = vcc
        self.ctrl_v = (2.0 / 3.0) * vcc
        self.trig_v = (1.0 / 3.0) * vcc
        self.flip_flop = False

    def set_control_voltage(self, v_ctrl: float):
        self.ctrl_v = v_ctrl
        self.trig_v = 0.5 * v_ctrl

    def step(self, v_thresh: float, v_trig: float, reset_active_low: bool = True) -> tuple[bool, bool]:
        if not reset_active_low:
            self.flip_flop = False
            return False, True
        comp_trig = v_trig < self.trig_v
        comp_thresh = v_thresh > self.ctrl_v
        if comp_trig:
            self.flip_flop = True
        elif comp_thresh:
            self.flip_flop = False
        out_pin = self.flip_flop
        discharge_on = not self.flip_flop
        return out_pin, discharge_on

def evaluate_timer555_quiescent_point_1(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 1."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 1, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_2(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 2."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 2, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_3(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 3."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 3, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_4(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 4."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 4, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_5(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 5."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 5, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_6(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 6."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 6, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_7(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 7."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 7, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_8(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 8."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 8, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_9(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 9."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 9, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_10(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 10."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 10, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_11(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 11."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 11, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_12(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 12."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 12, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_13(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 13."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 13, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_14(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 14."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 14, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_15(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 15."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 15, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_16(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 16."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 16, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_17(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 17."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 17, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_18(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 18."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 18, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_19(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 19."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 19, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_20(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 20."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 20, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_21(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 21."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 21, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_22(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 22."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 22, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_23(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 23."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 23, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_24(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 24."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 24, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_25(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 25."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 25, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_26(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 26."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 26, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_27(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 27."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 27, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_28(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 28."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 28, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_29(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 29."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 29, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_30(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 30."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 30, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_31(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 31."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 31, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_32(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 32."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 32, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_33(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 33."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 33, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_34(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 34."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 34, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_35(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 35."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 35, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_36(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 36."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 36, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_37(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 37."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 37, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_38(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 38."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 38, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_39(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 39."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 39, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_40(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 40."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 40, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_41(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 41."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 41, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_42(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 42."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 42, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_43(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 43."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 43, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_44(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 44."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 44, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_45(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 45."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 45, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_46(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 46."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 46, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_47(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 47."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 47, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_48(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 48."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 48, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_49(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 49."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 49, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_50(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 50."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 50, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_51(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 51."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 51, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_52(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 52."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 52, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_53(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 53."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 53, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_54(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 54."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 54, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_55(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 55."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 55, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_56(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 56."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 56, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_57(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 57."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 57, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_58(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 58."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 58, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_59(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 59."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 59, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_60(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 60."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 60, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_61(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 61."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 61, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_62(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 62."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 62, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_63(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 63."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 63, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_64(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 64."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 64, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_65(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 65."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 65, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_66(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 66."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 66, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_67(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 67."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 67, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_68(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 68."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 68, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_69(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 69."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 69, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_70(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 70."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 70, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_71(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 71."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 71, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_72(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 72."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 72, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_73(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 73."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 73, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_74(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 74."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 74, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_75(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 75."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 75, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_76(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 76."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 76, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_77(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 77."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 77, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_78(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 78."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 78, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_79(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 79."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 79, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_80(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 80."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 80, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_81(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 81."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 81, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_82(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 82."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 82, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_83(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 83."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 83, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_84(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 84."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 84, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_85(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 85."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 85, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_86(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 86."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 86, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_87(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 87."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 87, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_88(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 88."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 88, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_89(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 89."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 89, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_90(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 90."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 90, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_91(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 91."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 91, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_92(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 92."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 92, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_93(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 93."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 93, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_94(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 94."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 94, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_95(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 95."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 95, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_96(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 96."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 96, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_97(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 97."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 97, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_98(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 98."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 98, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_99(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 99."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 99, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_100(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 100."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 100, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_101(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 101."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 101, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_102(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 102."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 102, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_103(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 103."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 103, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_104(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 104."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 104, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_105(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 105."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 105, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_106(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 106."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 106, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_107(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 107."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 107, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_108(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 108."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 108, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_109(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 109."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 109, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_110(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 110."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 110, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_111(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 111."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 111, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_112(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 112."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 112, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_113(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 113."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 113, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_114(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 114."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 114, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_115(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 115."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 115, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_116(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 116."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 116, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_117(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 117."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 117, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_118(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 118."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 118, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_119(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 119."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 119, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_120(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 120."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 120, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_121(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 121."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 121, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_122(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 122."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 122, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_123(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 123."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 123, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_124(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 124."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 124, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_125(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 125."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 125, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_126(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 126."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 126, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_127(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 127."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 127, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_128(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 128."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 128, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}

def evaluate_timer555_quiescent_point_129(supply_v: float) -> dict[str, float]:
    """Compute internal resistor ladder current and comparator nodes for configuration 129."""
    r_total = 15000.0
    i_ladder = supply_v / r_total
    v_2_3 = (2.0 / 3.0) * supply_v
    v_1_3 = (1.0 / 3.0) * supply_v
    return {'config': 129, 'i_ladder': i_ladder, 'v_upper': v_2_3, 'v_lower': v_1_3}
