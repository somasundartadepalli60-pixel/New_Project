"""Binary-weighted resistor digital-to-analog converter model."""
from __future__ import annotations

def binary_weighted_dac_output(digital_bits: list[int], v_ref: float, r_base: float, rf: float) -> float:
    n = len(digital_bits)
    current_sum = 0.0
    for i, bit in enumerate(digital_bits):
        weight = 2 ** i
        r_branch = r_base * weight
        if bit:
            current_sum += v_ref / r_branch
    return -current_sum * rf

def evaluate_binary_resistor_spread_1(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 1."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 1, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_2(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 2."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 2, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_3(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 3."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 3, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_4(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 4."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 4, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_5(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 5."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 5, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_6(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 6."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 6, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_7(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 7."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 7, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_8(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 8."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 8, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_9(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 9."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 9, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_10(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 10."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 10, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_11(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 11."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 11, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_12(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 12."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 12, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_13(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 13."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 13, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_14(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 14."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 14, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_15(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 15."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 15, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_16(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 16."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 16, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_17(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 17."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 17, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_18(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 18."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 18, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_19(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 19."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 19, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_20(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 20."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 20, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_21(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 21."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 21, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_22(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 22."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 22, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_23(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 23."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 23, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_24(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 24."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 24, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_25(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 25."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 25, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_26(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 26."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 26, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_27(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 27."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 27, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_28(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 28."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 28, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_29(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 29."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 29, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_30(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 30."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 30, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_31(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 31."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 31, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_32(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 32."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 32, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_33(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 33."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 33, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_34(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 34."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 34, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_35(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 35."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 35, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_36(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 36."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 36, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_37(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 37."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 37, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_38(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 38."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 38, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_39(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 39."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 39, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_40(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 40."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 40, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_41(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 41."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 41, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_42(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 42."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 42, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_43(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 43."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 43, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_44(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 44."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 44, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_45(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 45."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 45, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_46(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 46."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 46, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_47(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 47."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 47, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_48(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 48."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 48, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_49(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 49."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 49, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_50(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 50."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 50, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_51(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 51."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 51, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_52(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 52."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 52, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_53(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 53."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 53, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_54(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 54."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 54, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_55(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 55."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 55, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_56(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 56."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 56, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_57(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 57."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 57, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_58(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 58."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 58, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_59(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 59."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 59, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_60(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 60."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 60, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_61(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 61."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 61, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_62(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 62."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 62, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_63(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 63."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 63, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_64(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 64."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 64, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_65(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 65."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 65, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_66(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 66."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 66, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_67(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 67."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 67, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_68(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 68."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 68, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_69(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 69."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 69, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_70(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 70."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 70, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_71(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 71."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 71, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_72(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 72."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 72, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_73(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 73."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 73, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_74(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 74."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 74, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_75(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 75."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 75, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_76(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 76."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 76, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_77(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 77."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 77, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_78(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 78."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 78, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_79(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 79."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 79, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_80(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 80."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 80, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_81(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 81."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 81, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_82(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 82."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 82, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_83(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 83."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 83, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_84(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 84."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 84, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_85(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 85."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 85, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_86(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 86."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 86, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_87(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 87."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 87, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_88(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 88."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 88, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_89(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 89."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 89, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_90(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 90."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 90, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_91(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 91."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 91, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_92(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 92."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 92, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_93(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 93."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 93, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_94(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 94."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 94, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_95(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 95."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 95, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_96(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 96."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 96, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_97(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 97."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 97, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_98(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 98."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 98, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_99(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 99."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 99, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_100(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 100."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 100, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_101(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 101."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 101, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_102(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 102."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 102, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_103(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 103."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 103, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_104(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 104."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 104, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_105(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 105."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 105, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_106(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 106."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 106, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_107(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 107."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 107, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_108(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 108."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 108, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_109(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 109."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 109, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_110(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 110."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 110, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_111(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 111."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 111, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_112(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 112."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 112, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_113(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 113."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 113, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_114(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 114."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 114, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_115(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 115."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 115, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_116(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 116."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 116, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_117(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 117."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 117, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_118(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 118."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 118, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_119(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 119."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 119, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_120(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 120."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 120, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_121(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 121."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 121, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_122(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 122."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 122, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_123(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 123."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 123, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_124(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 124."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 124, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_125(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 125."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 125, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_126(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 126."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 126, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_127(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 127."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 127, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_128(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 128."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 128, 'bits': num_bits, 'spread_ratio': spread}

def evaluate_binary_resistor_spread_129(num_bits: int) -> dict[str, float]:
    """Compute resistor resistance ratio spread 2^(N-1) for resolution 129."""
    spread = 2.0 ** (num_bits - 1)
    return {'eval_id': 129, 'bits': num_bits, 'spread_ratio': spread}
