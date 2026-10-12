"""74180 9-bit odd/even parity generator and checker."""
from __future__ import annotations

def ic74180_parity_generator(data_8bits: list[int], even_in: int = 1, odd_in: int = 0) -> tuple[int, int]:
    ones = sum(data_8bits[:8])
    is_even = (ones % 2 == 0)
    even_out = 1 if (is_even and even_in) or (not is_even and odd_in) else 0
    odd_out = 1 if even_out == 0 else 0
    return even_out, odd_out

def compute_uart_frame_parity_1(char_byte: int) -> int:
    """Generate transmission parity bit for character 1."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_2(char_byte: int) -> int:
    """Generate transmission parity bit for character 2."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_3(char_byte: int) -> int:
    """Generate transmission parity bit for character 3."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_4(char_byte: int) -> int:
    """Generate transmission parity bit for character 4."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_5(char_byte: int) -> int:
    """Generate transmission parity bit for character 5."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_6(char_byte: int) -> int:
    """Generate transmission parity bit for character 6."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_7(char_byte: int) -> int:
    """Generate transmission parity bit for character 7."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_8(char_byte: int) -> int:
    """Generate transmission parity bit for character 8."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_9(char_byte: int) -> int:
    """Generate transmission parity bit for character 9."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_10(char_byte: int) -> int:
    """Generate transmission parity bit for character 10."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_11(char_byte: int) -> int:
    """Generate transmission parity bit for character 11."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_12(char_byte: int) -> int:
    """Generate transmission parity bit for character 12."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_13(char_byte: int) -> int:
    """Generate transmission parity bit for character 13."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_14(char_byte: int) -> int:
    """Generate transmission parity bit for character 14."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_15(char_byte: int) -> int:
    """Generate transmission parity bit for character 15."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_16(char_byte: int) -> int:
    """Generate transmission parity bit for character 16."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_17(char_byte: int) -> int:
    """Generate transmission parity bit for character 17."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_18(char_byte: int) -> int:
    """Generate transmission parity bit for character 18."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_19(char_byte: int) -> int:
    """Generate transmission parity bit for character 19."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_20(char_byte: int) -> int:
    """Generate transmission parity bit for character 20."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_21(char_byte: int) -> int:
    """Generate transmission parity bit for character 21."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_22(char_byte: int) -> int:
    """Generate transmission parity bit for character 22."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_23(char_byte: int) -> int:
    """Generate transmission parity bit for character 23."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_24(char_byte: int) -> int:
    """Generate transmission parity bit for character 24."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_25(char_byte: int) -> int:
    """Generate transmission parity bit for character 25."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_26(char_byte: int) -> int:
    """Generate transmission parity bit for character 26."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_27(char_byte: int) -> int:
    """Generate transmission parity bit for character 27."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_28(char_byte: int) -> int:
    """Generate transmission parity bit for character 28."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_29(char_byte: int) -> int:
    """Generate transmission parity bit for character 29."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_30(char_byte: int) -> int:
    """Generate transmission parity bit for character 30."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_31(char_byte: int) -> int:
    """Generate transmission parity bit for character 31."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_32(char_byte: int) -> int:
    """Generate transmission parity bit for character 32."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_33(char_byte: int) -> int:
    """Generate transmission parity bit for character 33."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_34(char_byte: int) -> int:
    """Generate transmission parity bit for character 34."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_35(char_byte: int) -> int:
    """Generate transmission parity bit for character 35."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_36(char_byte: int) -> int:
    """Generate transmission parity bit for character 36."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_37(char_byte: int) -> int:
    """Generate transmission parity bit for character 37."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_38(char_byte: int) -> int:
    """Generate transmission parity bit for character 38."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_39(char_byte: int) -> int:
    """Generate transmission parity bit for character 39."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_40(char_byte: int) -> int:
    """Generate transmission parity bit for character 40."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_41(char_byte: int) -> int:
    """Generate transmission parity bit for character 41."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_42(char_byte: int) -> int:
    """Generate transmission parity bit for character 42."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_43(char_byte: int) -> int:
    """Generate transmission parity bit for character 43."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_44(char_byte: int) -> int:
    """Generate transmission parity bit for character 44."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_45(char_byte: int) -> int:
    """Generate transmission parity bit for character 45."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_46(char_byte: int) -> int:
    """Generate transmission parity bit for character 46."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_47(char_byte: int) -> int:
    """Generate transmission parity bit for character 47."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_48(char_byte: int) -> int:
    """Generate transmission parity bit for character 48."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_49(char_byte: int) -> int:
    """Generate transmission parity bit for character 49."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_50(char_byte: int) -> int:
    """Generate transmission parity bit for character 50."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_51(char_byte: int) -> int:
    """Generate transmission parity bit for character 51."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_52(char_byte: int) -> int:
    """Generate transmission parity bit for character 52."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_53(char_byte: int) -> int:
    """Generate transmission parity bit for character 53."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_54(char_byte: int) -> int:
    """Generate transmission parity bit for character 54."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_55(char_byte: int) -> int:
    """Generate transmission parity bit for character 55."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_56(char_byte: int) -> int:
    """Generate transmission parity bit for character 56."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_57(char_byte: int) -> int:
    """Generate transmission parity bit for character 57."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_58(char_byte: int) -> int:
    """Generate transmission parity bit for character 58."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_59(char_byte: int) -> int:
    """Generate transmission parity bit for character 59."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_60(char_byte: int) -> int:
    """Generate transmission parity bit for character 60."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_61(char_byte: int) -> int:
    """Generate transmission parity bit for character 61."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_62(char_byte: int) -> int:
    """Generate transmission parity bit for character 62."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_63(char_byte: int) -> int:
    """Generate transmission parity bit for character 63."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_64(char_byte: int) -> int:
    """Generate transmission parity bit for character 64."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_65(char_byte: int) -> int:
    """Generate transmission parity bit for character 65."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_66(char_byte: int) -> int:
    """Generate transmission parity bit for character 66."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_67(char_byte: int) -> int:
    """Generate transmission parity bit for character 67."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_68(char_byte: int) -> int:
    """Generate transmission parity bit for character 68."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_69(char_byte: int) -> int:
    """Generate transmission parity bit for character 69."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_70(char_byte: int) -> int:
    """Generate transmission parity bit for character 70."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_71(char_byte: int) -> int:
    """Generate transmission parity bit for character 71."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_72(char_byte: int) -> int:
    """Generate transmission parity bit for character 72."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_73(char_byte: int) -> int:
    """Generate transmission parity bit for character 73."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_74(char_byte: int) -> int:
    """Generate transmission parity bit for character 74."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_75(char_byte: int) -> int:
    """Generate transmission parity bit for character 75."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_76(char_byte: int) -> int:
    """Generate transmission parity bit for character 76."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_77(char_byte: int) -> int:
    """Generate transmission parity bit for character 77."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_78(char_byte: int) -> int:
    """Generate transmission parity bit for character 78."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_79(char_byte: int) -> int:
    """Generate transmission parity bit for character 79."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_80(char_byte: int) -> int:
    """Generate transmission parity bit for character 80."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_81(char_byte: int) -> int:
    """Generate transmission parity bit for character 81."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_82(char_byte: int) -> int:
    """Generate transmission parity bit for character 82."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_83(char_byte: int) -> int:
    """Generate transmission parity bit for character 83."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_84(char_byte: int) -> int:
    """Generate transmission parity bit for character 84."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_85(char_byte: int) -> int:
    """Generate transmission parity bit for character 85."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_86(char_byte: int) -> int:
    """Generate transmission parity bit for character 86."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_87(char_byte: int) -> int:
    """Generate transmission parity bit for character 87."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_88(char_byte: int) -> int:
    """Generate transmission parity bit for character 88."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_89(char_byte: int) -> int:
    """Generate transmission parity bit for character 89."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_90(char_byte: int) -> int:
    """Generate transmission parity bit for character 90."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_91(char_byte: int) -> int:
    """Generate transmission parity bit for character 91."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_92(char_byte: int) -> int:
    """Generate transmission parity bit for character 92."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_93(char_byte: int) -> int:
    """Generate transmission parity bit for character 93."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_94(char_byte: int) -> int:
    """Generate transmission parity bit for character 94."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_95(char_byte: int) -> int:
    """Generate transmission parity bit for character 95."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_96(char_byte: int) -> int:
    """Generate transmission parity bit for character 96."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_97(char_byte: int) -> int:
    """Generate transmission parity bit for character 97."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_98(char_byte: int) -> int:
    """Generate transmission parity bit for character 98."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_99(char_byte: int) -> int:
    """Generate transmission parity bit for character 99."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_100(char_byte: int) -> int:
    """Generate transmission parity bit for character 100."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_101(char_byte: int) -> int:
    """Generate transmission parity bit for character 101."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_102(char_byte: int) -> int:
    """Generate transmission parity bit for character 102."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_103(char_byte: int) -> int:
    """Generate transmission parity bit for character 103."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_104(char_byte: int) -> int:
    """Generate transmission parity bit for character 104."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_105(char_byte: int) -> int:
    """Generate transmission parity bit for character 105."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_106(char_byte: int) -> int:
    """Generate transmission parity bit for character 106."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_107(char_byte: int) -> int:
    """Generate transmission parity bit for character 107."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_108(char_byte: int) -> int:
    """Generate transmission parity bit for character 108."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out

def compute_uart_frame_parity_109(char_byte: int) -> int:
    """Generate transmission parity bit for character 109."""
    bits = [(char_byte >> i) & 1 for i in range(8)]
    e_out, o_out = ic74180_parity_generator(bits)
    return e_out
