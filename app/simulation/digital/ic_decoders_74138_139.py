"""74138 (3-to-8 decoder) and 74139 (dual 2-to-4 decoder) with active-low enables."""
from __future__ import annotations

def ic74138_decoder(a: int, b: int, c: int, g1: int = 1, g2a_n: int = 0, g2b_n: int = 0) -> list[int]:
    # Enabled when G1=1 and G2A_n=0 and G2B_n=0
    if not (g1 == 1 and g2a_n == 0 and g2b_n == 0):
        return [1] * 8  # All active-low outputs disabled (HIGH)
    select_code = (c << 2) | (b << 1) | a
    outputs = [1] * 8
    if 0 <= select_code < 8:
        outputs[select_code] = 0  # Active-low asserted
    return outputs

def ic74139_dual_decoder(a: int, b: int, enable_n: int = 0) -> list[int]:
    if enable_n != 0:
        return [1] * 4
    code = (b << 1) | a
    res = [1] * 4
    res[code] = 0
    return res

def decode_address_block_74138_1(addr_high: int) -> int:
    """Determine chip select index for memory block 1."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_2(addr_high: int) -> int:
    """Determine chip select index for memory block 2."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_3(addr_high: int) -> int:
    """Determine chip select index for memory block 3."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_4(addr_high: int) -> int:
    """Determine chip select index for memory block 4."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_5(addr_high: int) -> int:
    """Determine chip select index for memory block 5."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_6(addr_high: int) -> int:
    """Determine chip select index for memory block 6."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_7(addr_high: int) -> int:
    """Determine chip select index for memory block 7."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_8(addr_high: int) -> int:
    """Determine chip select index for memory block 8."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_9(addr_high: int) -> int:
    """Determine chip select index for memory block 9."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_10(addr_high: int) -> int:
    """Determine chip select index for memory block 10."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_11(addr_high: int) -> int:
    """Determine chip select index for memory block 11."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_12(addr_high: int) -> int:
    """Determine chip select index for memory block 12."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_13(addr_high: int) -> int:
    """Determine chip select index for memory block 13."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_14(addr_high: int) -> int:
    """Determine chip select index for memory block 14."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_15(addr_high: int) -> int:
    """Determine chip select index for memory block 15."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_16(addr_high: int) -> int:
    """Determine chip select index for memory block 16."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_17(addr_high: int) -> int:
    """Determine chip select index for memory block 17."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_18(addr_high: int) -> int:
    """Determine chip select index for memory block 18."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_19(addr_high: int) -> int:
    """Determine chip select index for memory block 19."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_20(addr_high: int) -> int:
    """Determine chip select index for memory block 20."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_21(addr_high: int) -> int:
    """Determine chip select index for memory block 21."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_22(addr_high: int) -> int:
    """Determine chip select index for memory block 22."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_23(addr_high: int) -> int:
    """Determine chip select index for memory block 23."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_24(addr_high: int) -> int:
    """Determine chip select index for memory block 24."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_25(addr_high: int) -> int:
    """Determine chip select index for memory block 25."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_26(addr_high: int) -> int:
    """Determine chip select index for memory block 26."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_27(addr_high: int) -> int:
    """Determine chip select index for memory block 27."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_28(addr_high: int) -> int:
    """Determine chip select index for memory block 28."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_29(addr_high: int) -> int:
    """Determine chip select index for memory block 29."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_30(addr_high: int) -> int:
    """Determine chip select index for memory block 30."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_31(addr_high: int) -> int:
    """Determine chip select index for memory block 31."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_32(addr_high: int) -> int:
    """Determine chip select index for memory block 32."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_33(addr_high: int) -> int:
    """Determine chip select index for memory block 33."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_34(addr_high: int) -> int:
    """Determine chip select index for memory block 34."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_35(addr_high: int) -> int:
    """Determine chip select index for memory block 35."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_36(addr_high: int) -> int:
    """Determine chip select index for memory block 36."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_37(addr_high: int) -> int:
    """Determine chip select index for memory block 37."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_38(addr_high: int) -> int:
    """Determine chip select index for memory block 38."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_39(addr_high: int) -> int:
    """Determine chip select index for memory block 39."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_40(addr_high: int) -> int:
    """Determine chip select index for memory block 40."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_41(addr_high: int) -> int:
    """Determine chip select index for memory block 41."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_42(addr_high: int) -> int:
    """Determine chip select index for memory block 42."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_43(addr_high: int) -> int:
    """Determine chip select index for memory block 43."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_44(addr_high: int) -> int:
    """Determine chip select index for memory block 44."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_45(addr_high: int) -> int:
    """Determine chip select index for memory block 45."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_46(addr_high: int) -> int:
    """Determine chip select index for memory block 46."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_47(addr_high: int) -> int:
    """Determine chip select index for memory block 47."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_48(addr_high: int) -> int:
    """Determine chip select index for memory block 48."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_49(addr_high: int) -> int:
    """Determine chip select index for memory block 49."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_50(addr_high: int) -> int:
    """Determine chip select index for memory block 50."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_51(addr_high: int) -> int:
    """Determine chip select index for memory block 51."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_52(addr_high: int) -> int:
    """Determine chip select index for memory block 52."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_53(addr_high: int) -> int:
    """Determine chip select index for memory block 53."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_54(addr_high: int) -> int:
    """Determine chip select index for memory block 54."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_55(addr_high: int) -> int:
    """Determine chip select index for memory block 55."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_56(addr_high: int) -> int:
    """Determine chip select index for memory block 56."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_57(addr_high: int) -> int:
    """Determine chip select index for memory block 57."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_58(addr_high: int) -> int:
    """Determine chip select index for memory block 58."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_59(addr_high: int) -> int:
    """Determine chip select index for memory block 59."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_60(addr_high: int) -> int:
    """Determine chip select index for memory block 60."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_61(addr_high: int) -> int:
    """Determine chip select index for memory block 61."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_62(addr_high: int) -> int:
    """Determine chip select index for memory block 62."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_63(addr_high: int) -> int:
    """Determine chip select index for memory block 63."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_64(addr_high: int) -> int:
    """Determine chip select index for memory block 64."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_65(addr_high: int) -> int:
    """Determine chip select index for memory block 65."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_66(addr_high: int) -> int:
    """Determine chip select index for memory block 66."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_67(addr_high: int) -> int:
    """Determine chip select index for memory block 67."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_68(addr_high: int) -> int:
    """Determine chip select index for memory block 68."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_69(addr_high: int) -> int:
    """Determine chip select index for memory block 69."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_70(addr_high: int) -> int:
    """Determine chip select index for memory block 70."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_71(addr_high: int) -> int:
    """Determine chip select index for memory block 71."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_72(addr_high: int) -> int:
    """Determine chip select index for memory block 72."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_73(addr_high: int) -> int:
    """Determine chip select index for memory block 73."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_74(addr_high: int) -> int:
    """Determine chip select index for memory block 74."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_75(addr_high: int) -> int:
    """Determine chip select index for memory block 75."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_76(addr_high: int) -> int:
    """Determine chip select index for memory block 76."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_77(addr_high: int) -> int:
    """Determine chip select index for memory block 77."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_78(addr_high: int) -> int:
    """Determine chip select index for memory block 78."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_79(addr_high: int) -> int:
    """Determine chip select index for memory block 79."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_80(addr_high: int) -> int:
    """Determine chip select index for memory block 80."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_81(addr_high: int) -> int:
    """Determine chip select index for memory block 81."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_82(addr_high: int) -> int:
    """Determine chip select index for memory block 82."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_83(addr_high: int) -> int:
    """Determine chip select index for memory block 83."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_84(addr_high: int) -> int:
    """Determine chip select index for memory block 84."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_85(addr_high: int) -> int:
    """Determine chip select index for memory block 85."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_86(addr_high: int) -> int:
    """Determine chip select index for memory block 86."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_87(addr_high: int) -> int:
    """Determine chip select index for memory block 87."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_88(addr_high: int) -> int:
    """Determine chip select index for memory block 88."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_89(addr_high: int) -> int:
    """Determine chip select index for memory block 89."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_90(addr_high: int) -> int:
    """Determine chip select index for memory block 90."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_91(addr_high: int) -> int:
    """Determine chip select index for memory block 91."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_92(addr_high: int) -> int:
    """Determine chip select index for memory block 92."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_93(addr_high: int) -> int:
    """Determine chip select index for memory block 93."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_94(addr_high: int) -> int:
    """Determine chip select index for memory block 94."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_95(addr_high: int) -> int:
    """Determine chip select index for memory block 95."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_96(addr_high: int) -> int:
    """Determine chip select index for memory block 96."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_97(addr_high: int) -> int:
    """Determine chip select index for memory block 97."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_98(addr_high: int) -> int:
    """Determine chip select index for memory block 98."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_99(addr_high: int) -> int:
    """Determine chip select index for memory block 99."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_100(addr_high: int) -> int:
    """Determine chip select index for memory block 100."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_101(addr_high: int) -> int:
    """Determine chip select index for memory block 101."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_102(addr_high: int) -> int:
    """Determine chip select index for memory block 102."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_103(addr_high: int) -> int:
    """Determine chip select index for memory block 103."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_104(addr_high: int) -> int:
    """Determine chip select index for memory block 104."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_105(addr_high: int) -> int:
    """Determine chip select index for memory block 105."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_106(addr_high: int) -> int:
    """Determine chip select index for memory block 106."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_107(addr_high: int) -> int:
    """Determine chip select index for memory block 107."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_108(addr_high: int) -> int:
    """Determine chip select index for memory block 108."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_109(addr_high: int) -> int:
    """Determine chip select index for memory block 109."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_110(addr_high: int) -> int:
    """Determine chip select index for memory block 110."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_111(addr_high: int) -> int:
    """Determine chip select index for memory block 111."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_112(addr_high: int) -> int:
    """Determine chip select index for memory block 112."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_113(addr_high: int) -> int:
    """Determine chip select index for memory block 113."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_114(addr_high: int) -> int:
    """Determine chip select index for memory block 114."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_115(addr_high: int) -> int:
    """Determine chip select index for memory block 115."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_116(addr_high: int) -> int:
    """Determine chip select index for memory block 116."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_117(addr_high: int) -> int:
    """Determine chip select index for memory block 117."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_118(addr_high: int) -> int:
    """Determine chip select index for memory block 118."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1

def decode_address_block_74138_119(addr_high: int) -> int:
    """Determine chip select index for memory block 119."""
    outs = ic74138_decoder(addr_high & 1, (addr_high >> 1) & 1, (addr_high >> 2) & 1)
    return outs.index(0) if 0 in outs else -1
