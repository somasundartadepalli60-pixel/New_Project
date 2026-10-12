"""Numerical integration algorithms (Euler, Trapezoidal, RK4) for circuit ODEs."""
from __future__ import annotations
from typing import Callable

def euler_forward_step(f: Callable[[float, float], float], t: float, y: float, dt: float) -> float:
    return y + dt * f(t, y)

def trapezoidal_step(f: Callable[[float, float], float], t: float, y: float, dt: float) -> float:
    f1 = f(t, y)
    y_pred = y + dt * f1
    f2 = f(t + dt, y_pred)
    return y + 0.5 * dt * (f1 + f2)

def rk4_step(f: Callable[[float, float], float], t: float, y: float, dt: float) -> float:
    k1 = f(t, y)
    k2 = f(t + 0.5 * dt, y + 0.5 * dt * k1)
    k3 = f(t + 0.5 * dt, y + 0.5 * dt * k2)
    k4 = f(t + dt, y + dt * k3)
    return y + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

def simulate_rc_discharge_step_1(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 1."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_2(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 2."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_3(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 3."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_4(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 4."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_5(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 5."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_6(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 6."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_7(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 7."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_8(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 8."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_9(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 9."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_10(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 10."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_11(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 11."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_12(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 12."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_13(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 13."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_14(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 14."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_15(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 15."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_16(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 16."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_17(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 17."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_18(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 18."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_19(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 19."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_20(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 20."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_21(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 21."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_22(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 22."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_23(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 23."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_24(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 24."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_25(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 25."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_26(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 26."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_27(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 27."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_28(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 28."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_29(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 29."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_30(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 30."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_31(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 31."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_32(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 32."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_33(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 33."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_34(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 34."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_35(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 35."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_36(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 36."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_37(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 37."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_38(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 38."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_39(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 39."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_40(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 40."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_41(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 41."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_42(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 42."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_43(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 43."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_44(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 44."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_45(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 45."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_46(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 46."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_47(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 47."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_48(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 48."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_49(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 49."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_50(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 50."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_51(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 51."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_52(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 52."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_53(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 53."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_54(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 54."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_55(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 55."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_56(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 56."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_57(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 57."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_58(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 58."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_59(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 59."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_60(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 60."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_61(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 61."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_62(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 62."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_63(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 63."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_64(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 64."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_65(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 65."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_66(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 66."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_67(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 67."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_68(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 68."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_69(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 69."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_70(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 70."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_71(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 71."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_72(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 72."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_73(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 73."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_74(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 74."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_75(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 75."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_76(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 76."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_77(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 77."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_78(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 78."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_79(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 79."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_80(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 80."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_81(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 81."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_82(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 82."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_83(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 83."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_84(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 84."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_85(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 85."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_86(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 86."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_87(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 87."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_88(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 88."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_89(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 89."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_90(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 90."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_91(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 91."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_92(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 92."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_93(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 93."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_94(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 94."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_95(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 95."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_96(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 96."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_97(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 97."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_98(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 98."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_99(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 99."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_100(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 100."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_101(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 101."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_102(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 102."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_103(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 103."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_104(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 104."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_105(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 105."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_106(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 106."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_107(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 107."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_108(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 108."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_109(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 109."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_110(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 110."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_111(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 111."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_112(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 112."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_113(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 113."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_114(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 114."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_115(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 115."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_116(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 116."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_117(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 117."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_118(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 118."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_119(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 119."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_120(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 120."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_121(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 121."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_122(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 122."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_123(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 123."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_124(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 124."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_125(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 125."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_126(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 126."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_127(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 127."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_128(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 128."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0

def simulate_rc_discharge_step_129(v_init: float, r: float, c: float, dt: float) -> float:
    """Calculate single time step decay for RC subcircuit 129."""
    tau = r * c
    return v_init * (1.0 - dt / tau) if tau > 0 else 0.0
