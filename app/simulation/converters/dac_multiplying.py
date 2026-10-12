"""Multiplying DAC (DAC0808, AD7524) four-quadrant attenuation models."""
from __future__ import annotations

def multiplying_dac_output(digital_code: int, max_code: int, vin_analog: float) -> float:
    scale = digital_code / max_code
    return vin_analog * scale

def evaluate_programmable_attenuator_step_1(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 1."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_2(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 2."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_3(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 3."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_4(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 4."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_5(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 5."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_6(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 6."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_7(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 7."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_8(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 8."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_9(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 9."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_10(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 10."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_11(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 11."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_12(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 12."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_13(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 13."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_14(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 14."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_15(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 15."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_16(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 16."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_17(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 17."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_18(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 18."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_19(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 19."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_20(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 20."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_21(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 21."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_22(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 22."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_23(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 23."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_24(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 24."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_25(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 25."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_26(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 26."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_27(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 27."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_28(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 28."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_29(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 29."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_30(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 30."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_31(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 31."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_32(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 32."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_33(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 33."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_34(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 34."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_35(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 35."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_36(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 36."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_37(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 37."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_38(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 38."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_39(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 39."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_40(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 40."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_41(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 41."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_42(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 42."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_43(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 43."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_44(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 44."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_45(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 45."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_46(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 46."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_47(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 47."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_48(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 48."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_49(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 49."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_50(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 50."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_51(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 51."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_52(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 52."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_53(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 53."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_54(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 54."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_55(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 55."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_56(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 56."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_57(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 57."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_58(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 58."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_59(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 59."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_60(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 60."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_61(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 61."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_62(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 62."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_63(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 63."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_64(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 64."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_65(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 65."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_66(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 66."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_67(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 67."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_68(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 68."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_69(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 69."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_70(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 70."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_71(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 71."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_72(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 72."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_73(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 73."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_74(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 74."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_75(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 75."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_76(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 76."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_77(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 77."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_78(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 78."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_79(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 79."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_80(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 80."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_81(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 81."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_82(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 82."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_83(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 83."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_84(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 84."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_85(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 85."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_86(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 86."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_87(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 87."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_88(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 88."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_89(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 89."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_90(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 90."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_91(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 91."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_92(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 92."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_93(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 93."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_94(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 94."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_95(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 95."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_96(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 96."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_97(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 97."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_98(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 98."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_99(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 99."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_100(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 100."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_101(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 101."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_102(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 102."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_103(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 103."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_104(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 104."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_105(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 105."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_106(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 106."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_107(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 107."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_108(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 108."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_109(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 109."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_110(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 110."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_111(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 111."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_112(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 112."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_113(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 113."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_114(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 114."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_115(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 115."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_116(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 116."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_117(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 117."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_118(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 118."""
    return vin_v * (digital_in / 256.0)

def evaluate_programmable_attenuator_step_119(digital_in: int, vin_v: float) -> float:
    """Compute output voltage of digitally controlled gain amplifier 119."""
    return vin_v * (digital_in / 256.0)
