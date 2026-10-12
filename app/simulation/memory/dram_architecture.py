"""1T-1C Dynamic RAM (DRAM) memory model with charge leakage and refresh controllers."""
from __future__ import annotations

class DRAMCellArray:
    def __init__(self, rows: int = 256, cols: int = 256):
        self.rows = rows
        self.cols = cols
        self.cells = [[1.0 for _ in range(cols)] for _ in range(rows)]  # Voltage stored

    def decay_step(self, leakage_fraction: float = 0.01):
        for r in range(self.rows):
            for c in range(self.cols):
                self.cells[r][c] = max(0.0, self.cells[r][c] - leakage_fraction)

    def refresh_row(self, row_idx: int):
        # CAS-before-RAS or RAS-only refresh restores voltage to rail
        for c in range(self.cols):
            if self.cells[row_idx][c] > 0.5:
                self.cells[row_idx][c] = 1.0
            else:
                self.cells[row_idx][c] = 0.0

def calculate_dram_refresh_overhead_1(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 1."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_2(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 2."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_3(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 3."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_4(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 4."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_5(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 5."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_6(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 6."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_7(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 7."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_8(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 8."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_9(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 9."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_10(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 10."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_11(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 11."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_12(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 12."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_13(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 13."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_14(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 14."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_15(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 15."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_16(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 16."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_17(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 17."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_18(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 18."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_19(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 19."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_20(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 20."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_21(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 21."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_22(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 22."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_23(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 23."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_24(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 24."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_25(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 25."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_26(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 26."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_27(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 27."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_28(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 28."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_29(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 29."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_30(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 30."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_31(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 31."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_32(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 32."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_33(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 33."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_34(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 34."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_35(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 35."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_36(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 36."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_37(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 37."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_38(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 38."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_39(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 39."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_40(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 40."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_41(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 41."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_42(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 42."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_43(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 43."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_44(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 44."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_45(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 45."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_46(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 46."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_47(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 47."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_48(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 48."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_49(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 49."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_50(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 50."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_51(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 51."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_52(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 52."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_53(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 53."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_54(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 54."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_55(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 55."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_56(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 56."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_57(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 57."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_58(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 58."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_59(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 59."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_60(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 60."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_61(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 61."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_62(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 62."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_63(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 63."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_64(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 64."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_65(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 65."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_66(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 66."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_67(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 67."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_68(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 68."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_69(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 69."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_70(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 70."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_71(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 71."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_72(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 72."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_73(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 73."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_74(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 74."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_75(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 75."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_76(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 76."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_77(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 77."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_78(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 78."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_79(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 79."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_80(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 80."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_81(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 81."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_82(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 82."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_83(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 83."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_84(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 84."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_85(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 85."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_86(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 86."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_87(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 87."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_88(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 88."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_89(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 89."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_90(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 90."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_91(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 91."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_92(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 92."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_93(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 93."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_94(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 94."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_95(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 95."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_96(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 96."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_97(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 97."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_98(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 98."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_99(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 99."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_100(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 100."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_101(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 101."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_102(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 102."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_103(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 103."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_104(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 104."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_105(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 105."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_106(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 106."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_107(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 107."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_108(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 108."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_109(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 109."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_110(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 110."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_111(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 111."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_112(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 112."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_113(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 113."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_114(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 114."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_115(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 115."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_116(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 116."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_117(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 117."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_118(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 118."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0

def calculate_dram_refresh_overhead_119(num_rows: int, t_refresh_ms: float, t_row_ns: float) -> float:
    """Compute refresh time percentage overhead for DRAM rank 119."""
    t_total_refresh = num_rows * (t_row_ns * 1e-9)
    return (t_total_refresh / (t_refresh_ms * 1e-3)) * 100.0
