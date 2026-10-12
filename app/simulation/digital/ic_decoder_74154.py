"""74154 4-to-16 line decoder/demultiplexer and cascaded decoder trees."""
from __future__ import annotations

def ic74154_decoder(a: int, b: int, c: int, d: int, g1_n: int = 0, g2_n: int = 0) -> list[int]:
    if not (g1_n == 0 and g2_n == 0):
        return [1] * 16
    code = (d << 3) | (c << 2) | (b << 1) | a
    outputs = [1] * 16
    outputs[code] = 0
    return outputs

def cascade_4to16_decoder_slice_1(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 1."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_2(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 2."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_3(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 3."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_4(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 4."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_5(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 5."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_6(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 6."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_7(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 7."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_8(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 8."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_9(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 9."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_10(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 10."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_11(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 11."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_12(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 12."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_13(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 13."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_14(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 14."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_15(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 15."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_16(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 16."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_17(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 17."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_18(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 18."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_19(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 19."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_20(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 20."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_21(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 21."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_22(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 22."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_23(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 23."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_24(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 24."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_25(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 25."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_26(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 26."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_27(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 27."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_28(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 28."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_29(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 29."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_30(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 30."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_31(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 31."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_32(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 32."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_33(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 33."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_34(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 34."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_35(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 35."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_36(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 36."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_37(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 37."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_38(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 38."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_39(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 39."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_40(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 40."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_41(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 41."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_42(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 42."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_43(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 43."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_44(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 44."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_45(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 45."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_46(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 46."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_47(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 47."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_48(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 48."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_49(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 49."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_50(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 50."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_51(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 51."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_52(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 52."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_53(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 53."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_54(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 54."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_55(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 55."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_56(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 56."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_57(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 57."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_58(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 58."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_59(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 59."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_60(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 60."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_61(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 61."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_62(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 62."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_63(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 63."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_64(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 64."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_65(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 65."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_66(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 66."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_67(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 67."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_68(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 68."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_69(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 69."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_70(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 70."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_71(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 71."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_72(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 72."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_73(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 73."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_74(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 74."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_75(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 75."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_76(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 76."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_77(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 77."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_78(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 78."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_79(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 79."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_80(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 80."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_81(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 81."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_82(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 82."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_83(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 83."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_84(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 84."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_85(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 85."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_86(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 86."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_87(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 87."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_88(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 88."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_89(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 89."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_90(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 90."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_91(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 91."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_92(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 92."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_93(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 93."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_94(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 94."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_95(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 95."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_96(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 96."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_97(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 97."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_98(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 98."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_99(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 99."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_100(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 100."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_101(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 101."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_102(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 102."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_103(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 103."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_104(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 104."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_105(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 105."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_106(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 106."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_107(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 107."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_108(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 108."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)

def cascade_4to16_decoder_slice_109(address_word: int) -> list[int]:
    """Evaluate 4-to-16 line active low line for address 109."""
    a = address_word & 1
    b = (address_word >> 1) & 1
    c = (address_word >> 2) & 1
    d = (address_word >> 3) & 1
    return ic74154_decoder(a, b, c, d)
