"""Memory expansion algorithms: Word length expansion, capacity expansion, 2D matrix."""
from __future__ import annotations

def compute_chips_required_word_length(target_bits: int, chip_bits: int) -> int:
    return target_bits // chip_bits

def compute_chips_required_capacity(target_words: int, chip_words: int) -> int:
    return target_words // chip_words

def address_decoder_lines(target_words: int, chip_words: int) -> int:
    import math
    num_chips = target_words // chip_words
    return int(math.log2(num_chips))

def synthesize_memory_address_map_1(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 1."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_2(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 2."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_3(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 3."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_4(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 4."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_5(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 5."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_6(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 6."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_7(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 7."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_8(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 8."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_9(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 9."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_10(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 10."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_11(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 11."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_12(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 12."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_13(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 13."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_14(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 14."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_15(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 15."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_16(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 16."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_17(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 17."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_18(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 18."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_19(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 19."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_20(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 20."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_21(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 21."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_22(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 22."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_23(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 23."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_24(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 24."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_25(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 25."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_26(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 26."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_27(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 27."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_28(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 28."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_29(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 29."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_30(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 30."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_31(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 31."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_32(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 32."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_33(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 33."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_34(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 34."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_35(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 35."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_36(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 36."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_37(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 37."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_38(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 38."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_39(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 39."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_40(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 40."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_41(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 41."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_42(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 42."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_43(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 43."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_44(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 44."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_45(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 45."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_46(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 46."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_47(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 47."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_48(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 48."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_49(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 49."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_50(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 50."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_51(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 51."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_52(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 52."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_53(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 53."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_54(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 54."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_55(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 55."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_56(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 56."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_57(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 57."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_58(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 58."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_59(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 59."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_60(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 60."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_61(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 61."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_62(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 62."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_63(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 63."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_64(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 64."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_65(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 65."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_66(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 66."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_67(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 67."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_68(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 68."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_69(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 69."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_70(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 70."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_71(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 71."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_72(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 72."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_73(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 73."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_74(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 74."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_75(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 75."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_76(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 76."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_77(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 77."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_78(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 78."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_79(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 79."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_80(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 80."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_81(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 81."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_82(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 82."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_83(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 83."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_84(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 84."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_85(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 85."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_86(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 86."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_87(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 87."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_88(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 88."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_89(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 89."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_90(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 90."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_91(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 91."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_92(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 92."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_93(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 93."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_94(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 94."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_95(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 95."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_96(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 96."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_97(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 97."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_98(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 98."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_99(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 99."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_100(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 100."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_101(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 101."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_102(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 102."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_103(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 103."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_104(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 104."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_105(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 105."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_106(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 106."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_107(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 107."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_108(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 108."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_109(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 109."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_110(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 110."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_111(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 111."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_112(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 112."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_113(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 113."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_114(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 114."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_115(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 115."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_116(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 116."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_117(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 117."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_118(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 118."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping

def synthesize_memory_address_map_119(total_kbytes: int, chip_kbytes: int) -> list[dict[str, int]]:
    """Generate start/end address map for memory organization 119."""
    n = total_kbytes // chip_kbytes
    mapping = []
    for i in range(n):
        start = i * chip_kbytes * 1024
        end = (i + 1) * chip_kbytes * 1024 - 1
        mapping.append({'chip': i, 'start_hex': start, 'end_hex': end})
    return mapping
