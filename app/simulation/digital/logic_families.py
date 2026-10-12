"""TTL vs CMOS logic family electrical characteristics, noise margins, and fanout."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class LogicFamilySpecs:
    family_name: str
    v_cc: float
    v_ih_min: float
    v_il_max: float
    v_oh_min: float
    v_ol_max: float
    i_ih_ua: float
    i_il_ma: float
    i_oh_ma: float
    i_ol_ma: float
    prop_delay_ns: float
    power_dissipation_mw: float

LOGIC_FAMILIES: dict[str, LogicFamilySpecs] = {
    "74_STANDARD_TTL": LogicFamilySpecs("74_Standard_TTL", 5.0, 2.0, 0.8, 2.4, 0.4, 40.0, 1.6, 0.4, 16.0, 10.0, 10.0),
    "74LS_TTL": LogicFamilySpecs("74LS_TTL", 5.0, 2.0, 0.8, 2.7, 0.5, 20.0, 0.4, 0.4, 8.0, 9.0, 2.0),
    "74ALS_TTL": LogicFamilySpecs("74ALS_TTL", 5.0, 2.0, 0.8, 2.7, 0.5, 20.0, 0.1, 0.4, 8.0, 4.0, 1.0),
    "74HC_CMOS": LogicFamilySpecs("74HC_CMOS", 5.0, 3.5, 1.0, 4.9, 0.1, 1.0, 0.001, 4.0, 4.0, 8.0, 0.05),
    "74HCT_CMOS": LogicFamilySpecs("74HCT_CMOS", 5.0, 2.0, 0.8, 4.9, 0.1, 1.0, 0.001, 4.0, 4.0, 8.0, 0.05),
}

def compute_noise_margins(family_key: str) -> tuple[float, float]:
    spec = LOGIC_FAMILIES[family_key]
    nm_h = spec.v_oh_min - spec.v_ih_min
    nm_l = spec.v_il_max - spec.v_ol_max
    return nm_h, nm_l

def compute_fanout(driving_family: str, load_family: str) -> int:
    drv = LOGIC_FAMILIES[driving_family]
    load = LOGIC_FAMILIES[load_family]
    fanout_high = (abs(drv.i_oh_ma) * 1000.0) / abs(load.i_ih_ua)
    fanout_low = abs(drv.i_ol_ma) / abs(load.i_il_ma)
    return int(min(fanout_high, fanout_low))

def speed_power_product_calc_1(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 1."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_2(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 2."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_3(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 3."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_4(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 4."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_5(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 5."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_6(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 6."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_7(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 7."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_8(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 8."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_9(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 9."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_10(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 10."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_11(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 11."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_12(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 12."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_13(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 13."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_14(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 14."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_15(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 15."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_16(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 16."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_17(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 17."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_18(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 18."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_19(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 19."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_20(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 20."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_21(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 21."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_22(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 22."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_23(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 23."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_24(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 24."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_25(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 25."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_26(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 26."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_27(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 27."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_28(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 28."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_29(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 29."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_30(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 30."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_31(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 31."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_32(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 32."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_33(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 33."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_34(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 34."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_35(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 35."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_36(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 36."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_37(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 37."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_38(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 38."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_39(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 39."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_40(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 40."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_41(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 41."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_42(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 42."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_43(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 43."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_44(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 44."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_45(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 45."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_46(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 46."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_47(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 47."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_48(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 48."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_49(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 49."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_50(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 50."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_51(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 51."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_52(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 52."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_53(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 53."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_54(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 54."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_55(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 55."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_56(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 56."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_57(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 57."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_58(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 58."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_59(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 59."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_60(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 60."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_61(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 61."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_62(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 62."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_63(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 63."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_64(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 64."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_65(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 65."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_66(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 66."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_67(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 67."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_68(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 68."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_69(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 69."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_70(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 70."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_71(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 71."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_72(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 72."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_73(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 73."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_74(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 74."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_75(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 75."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_76(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 76."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_77(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 77."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_78(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 78."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_79(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 79."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_80(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 80."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_81(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 81."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_82(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 82."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_83(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 83."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_84(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 84."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_85(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 85."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_86(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 86."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_87(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 87."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_88(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 88."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_89(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 89."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_90(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 90."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_91(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 91."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_92(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 92."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_93(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 93."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_94(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 94."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_95(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 95."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_96(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 96."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_97(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 97."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_98(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 98."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_99(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 99."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_100(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 100."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_101(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 101."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_102(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 102."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_103(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 103."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_104(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 104."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_105(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 105."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_106(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 106."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_107(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 107."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_108(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 108."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_109(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 109."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_110(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 110."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_111(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 111."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_112(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 112."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_113(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 113."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_114(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 114."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_115(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 115."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_116(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 116."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_117(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 117."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_118(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 118."""
    return prop_delay_ns * power_mw

def speed_power_product_calc_119(prop_delay_ns: float, power_mw: float) -> float:
    """Compute Speed-Power Product (pJ) for family configuration 119."""
    return prop_delay_ns * power_mw
