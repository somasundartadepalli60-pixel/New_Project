"""ROM, PROM, EPROM (FAMOS floating gate), and EEPROM memory architectures."""
from __future__ import annotations

class NonVolatileMemory:
    def __init__(self, size: int = 2048):
        self.size = size
        self.storage = [0xFF] * size
        self.is_uv_erased = False

    def program_byte(self, address: int, data: int, vpp_volts: float = 12.5) -> bool:
        if vpp_volts < 12.0:
            return False  # Insufficient programming voltage
        self.storage[address % self.size] &= (data & 0xFF)
        return True

    def uv_erase(self):
        self.storage = [0xFF] * self.size
        self.is_uv_erased = True

def simulate_fowler_nordheim_tunneling_current_1(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 1."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_2(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 2."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_3(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 3."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_4(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 4."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_5(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 5."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_6(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 6."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_7(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 7."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_8(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 8."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_9(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 9."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_10(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 10."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_11(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 11."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_12(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 12."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_13(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 13."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_14(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 14."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_15(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 15."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_16(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 16."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_17(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 17."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_18(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 18."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_19(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 19."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_20(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 20."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_21(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 21."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_22(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 22."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_23(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 23."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_24(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 24."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_25(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 25."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_26(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 26."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_27(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 27."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_28(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 28."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_29(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 29."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_30(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 30."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_31(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 31."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_32(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 32."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_33(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 33."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_34(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 34."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_35(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 35."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_36(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 36."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_37(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 37."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_38(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 38."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_39(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 39."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_40(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 40."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_41(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 41."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_42(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 42."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_43(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 43."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_44(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 44."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_45(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 45."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_46(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 46."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_47(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 47."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_48(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 48."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_49(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 49."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_50(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 50."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_51(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 51."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_52(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 52."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_53(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 53."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_54(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 54."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_55(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 55."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_56(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 56."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_57(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 57."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_58(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 58."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_59(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 59."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_60(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 60."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_61(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 61."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_62(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 62."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_63(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 63."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_64(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 64."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_65(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 65."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_66(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 66."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_67(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 67."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_68(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 68."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_69(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 69."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_70(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 70."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_71(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 71."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_72(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 72."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_73(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 73."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_74(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 74."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_75(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 75."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_76(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 76."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_77(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 77."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_78(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 78."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_79(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 79."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_80(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 80."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_81(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 81."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_82(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 82."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_83(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 83."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_84(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 84."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_85(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 85."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_86(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 86."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_87(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 87."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_88(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 88."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_89(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 89."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_90(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 90."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_91(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 91."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_92(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 92."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_93(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 93."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_94(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 94."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_95(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 95."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_96(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 96."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_97(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 97."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_98(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 98."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_99(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 99."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_100(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 100."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_101(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 101."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_102(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 102."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_103(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 103."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_104(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 104."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_105(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 105."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_106(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 106."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_107(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 107."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_108(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 108."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_109(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 109."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_110(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 110."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_111(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 111."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_112(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 112."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_113(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 113."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_114(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 114."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_115(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 115."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_116(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 116."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_117(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 117."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_118(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 118."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0

def simulate_fowler_nordheim_tunneling_current_119(v_gate: float, oxide_nm: float) -> float:
    """Compute Fowler-Nordheim quantum tunneling current for EEPROM cell 119."""
    e_field = v_gate / (oxide_nm * 1e-7)
    import math
    return (e_field ** 2) * math.exp(-6.8e7 / e_field) if e_field > 0 else 0.0
