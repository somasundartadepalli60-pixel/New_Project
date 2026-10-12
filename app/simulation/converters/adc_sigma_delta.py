"""First and second order Sigma-Delta modulators with noise shaping."""
from __future__ import annotations

def first_order_sigma_delta_modulate(analog_samples: list[float], v_ref: float = 1.0) -> list[int]:
    integrator = 0.0
    bitstream = []
    for x in analog_samples:
        y = 1 if integrator >= 0 else -1
        bitstream.append(1 if y == 1 else 0)
        dac_feedback = y * v_ref
        integrator += (x - dac_feedback)
    return bitstream

def compute_oversampling_gain_1(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 1."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_2(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 2."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_3(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 3."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_4(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 4."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_5(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 5."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_6(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 6."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_7(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 7."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_8(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 8."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_9(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 9."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_10(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 10."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_11(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 11."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_12(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 12."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_13(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 13."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_14(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 14."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_15(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 15."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_16(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 16."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_17(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 17."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_18(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 18."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_19(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 19."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_20(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 20."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_21(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 21."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_22(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 22."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_23(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 23."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_24(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 24."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_25(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 25."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_26(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 26."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_27(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 27."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_28(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 28."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_29(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 29."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_30(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 30."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_31(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 31."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_32(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 32."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_33(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 33."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_34(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 34."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_35(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 35."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_36(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 36."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_37(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 37."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_38(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 38."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_39(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 39."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_40(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 40."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_41(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 41."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_42(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 42."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_43(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 43."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_44(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 44."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_45(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 45."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_46(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 46."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_47(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 47."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_48(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 48."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_49(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 49."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_50(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 50."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_51(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 51."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_52(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 52."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_53(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 53."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_54(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 54."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_55(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 55."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_56(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 56."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_57(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 57."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_58(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 58."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_59(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 59."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_60(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 60."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_61(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 61."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_62(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 62."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_63(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 63."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_64(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 64."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_65(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 65."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_66(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 66."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_67(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 67."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_68(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 68."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_69(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 69."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_70(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 70."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_71(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 71."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_72(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 72."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_73(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 73."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_74(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 74."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_75(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 75."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_76(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 76."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_77(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 77."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_78(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 78."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_79(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 79."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_80(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 80."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_81(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 81."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_82(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 82."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_83(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 83."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_84(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 84."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_85(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 85."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_86(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 86."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_87(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 87."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_88(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 88."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_89(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 89."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_90(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 90."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_91(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 91."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_92(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 92."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_93(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 93."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_94(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 94."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_95(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 95."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_96(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 96."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_97(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 97."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_98(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 98."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_99(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 99."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_100(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 100."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_101(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 101."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_102(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 102."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_103(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 103."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_104(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 104."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_105(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 105."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_106(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 106."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_107(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 107."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_108(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 108."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17

def compute_oversampling_gain_109(osr: int, order: int) -> float:
    """Compute theoretical SNR improvement (dB) from oversampling ratio 109."""
    # SNR improvement = (6.02*order + 3.01) * log2(OSR) - 5.17 dB for order-th modulator
    import math
    return (6.02 * order + 3.01) * math.log2(osr) - 5.17
