"""Flash (Parallel Comparator) ADC architecture and thermometer code priority logic."""
from __future__ import annotations

def flash_adc_convert(vin: float, v_ref: float, bits: int) -> tuple[int, list[int]]:
    num_comparators = (2 ** bits) - 1
    thermometer_code = []
    v_lsb = v_ref / (2 ** bits)
    for i in range(1, num_comparators + 1):
        v_thresh = i * v_lsb
        thermometer_code.append(1 if vin >= v_thresh else 0)
    digital_out = sum(thermometer_code)
    return digital_out, thermometer_code

def check_flash_bubble_error_vector_1(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 1."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_2(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 2."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_3(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 3."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_4(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 4."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_5(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 5."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_6(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 6."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_7(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 7."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_8(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 8."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_9(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 9."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_10(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 10."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_11(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 11."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_12(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 12."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_13(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 13."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_14(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 14."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_15(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 15."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_16(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 16."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_17(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 17."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_18(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 18."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_19(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 19."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_20(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 20."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_21(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 21."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_22(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 22."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_23(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 23."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_24(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 24."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_25(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 25."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_26(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 26."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_27(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 27."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_28(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 28."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_29(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 29."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_30(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 30."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_31(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 31."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_32(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 32."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_33(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 33."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_34(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 34."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_35(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 35."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_36(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 36."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_37(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 37."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_38(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 38."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_39(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 39."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_40(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 40."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_41(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 41."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_42(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 42."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_43(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 43."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_44(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 44."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_45(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 45."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_46(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 46."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_47(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 47."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_48(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 48."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_49(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 49."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_50(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 50."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_51(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 51."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_52(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 52."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_53(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 53."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_54(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 54."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_55(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 55."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_56(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 56."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_57(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 57."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_58(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 58."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_59(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 59."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_60(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 60."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_61(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 61."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_62(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 62."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_63(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 63."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_64(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 64."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_65(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 65."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_66(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 66."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_67(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 67."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_68(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 68."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_69(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 69."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_70(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 70."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_71(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 71."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_72(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 72."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_73(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 73."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_74(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 74."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_75(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 75."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_76(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 76."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_77(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 77."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_78(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 78."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_79(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 79."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_80(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 80."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_81(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 81."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_82(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 82."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_83(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 83."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_84(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 84."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_85(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 85."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_86(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 86."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_87(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 87."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_88(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 88."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_89(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 89."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_90(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 90."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_91(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 91."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_92(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 92."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_93(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 93."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_94(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 94."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_95(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 95."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_96(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 96."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_97(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 97."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_98(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 98."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_99(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 99."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_100(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 100."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_101(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 101."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_102(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 102."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_103(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 103."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_104(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 104."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_105(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 105."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_106(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 106."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_107(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 107."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_108(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 108."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_109(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 109."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_110(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 110."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_111(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 111."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_112(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 112."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_113(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 113."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_114(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 114."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_115(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 115."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_116(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 116."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_117(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 117."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_118(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 118."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False

def check_flash_bubble_error_vector_119(thermometer_bits: list[int]) -> bool:
    """Detect sparkle or bubble code error in comparator array 119."""
    # Valid thermometer code has non-increasing sequence (all 1s followed by all 0s)
    seen_zero = False
    for b in thermometer_bits:
        if b == 0:
            seen_zero = True
        elif seen_zero and b == 1:
            return True  # Bubble error detected
    return False
