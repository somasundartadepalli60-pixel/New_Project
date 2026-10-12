"""Modified Nodal Analysis (MNA) matrix solver for analog circuit simulation."""
from __future__ import annotations
import math
from dataclasses import dataclass, field

@dataclass
class CircuitNode:
    """Represents an electrical circuit node in MNA formulation."""
    node_id: int
    name: str
    voltage: float = 0.0
    is_ground: bool = False

@dataclass
class Resistor:
    """Linear resistor branch."""
    name: str
    n1: int
    n2: int
    resistance: float

    @property
    def conductance(self) -> float:
        if self.resistance <= 0:
            raise ValueError("Resistance must be positive")
        return 1.0 / self.resistance

@dataclass
class VoltageSource:
    """Independent voltage source."""
    name: str
    n_pos: int
    n_neg: int
    voltage: float
    source_index: int = 0

@dataclass
class CurrentSource:
    """Independent current source."""
    name: str
    n_pos: int
    n_neg: int
    current: float

class MNASolver:
    """Solves linear circuit equations G * v + B * i = J using Gaussian elimination."""

    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.resistors: list[Resistor] = []
        self.voltage_sources: list[VoltageSource] = []
        self.current_sources: list[CurrentSource] = []

    def add_resistor(self, name: str, n1: int, n2: int, resistance: float):
        self.resistors.append(Resistor(name, n1, n2, resistance))

    def add_voltage_source(self, name: str, n_pos: int, n_neg: int, voltage: float):
        idx = len(self.voltage_sources)
        self.voltage_sources.append(VoltageSource(name, n_pos, n_neg, voltage, idx))

    def add_current_source(self, name: str, n_pos: int, n_neg: int, current: float):
        self.current_sources.append(CurrentSource(name, n_pos, n_neg, current))

    def stamp_matrix(self) -> tuple[list[list[float]], list[float]]:
        n = self.num_nodes
        m = len(self.voltage_sources)
        dim = n + m
        a = [[0.0 for _ in range(dim)] for _ in range(dim)]
        z = [0.0 for _ in range(dim)]

        for r in self.resistors:
            g = r.conductance
            if r.n1 > 0:
                a[r.n1 - 1][r.n1 - 1] += g
            if r.n2 > 0:
                a[r.n2 - 1][r.n2 - 1] += g
            if r.n1 > 0 and r.n2 > 0:
                a[r.n1 - 1][r.n2 - 1] -= g
                a[r.n2 - 1][r.n1 - 1] -= g

        for i, vs in enumerate(self.voltage_sources):
            idx = n + i
            if vs.n_pos > 0:
                a[vs.n_pos - 1][idx] += 1.0
                a[idx][vs.n_pos - 1] += 1.0
            if vs.n_neg > 0:
                a[vs.n_neg - 1][idx] -= 1.0
                a[idx][vs.n_neg - 1] -= 1.0
            z[idx] = vs.voltage

        for cs in self.current_sources:
            if cs.n_pos > 0:
                z[cs.n_pos - 1] -= cs.current
            if cs.n_neg > 0:
                z[cs.n_neg - 1] += cs.current

        return a, z

    def solve_dc(self) -> list[float]:
        a, z = self.stamp_matrix()
        dim = len(z)
        for i in range(dim):
            pivot = a[i][i]
            max_row = i
            for k in range(i + 1, dim):
                if abs(a[k][i]) > abs(pivot):
                    pivot = a[k][i]
                    max_row = k
            if abs(pivot) < 1e-12:
                raise ZeroDivisionError(f"Singular matrix encountered at node index {i}")
            if max_row != i:
                a[i], a[max_row] = a[max_row], a[i]
                z[i], z[max_row] = z[max_row], z[i]
            inv_pivot = 1.0 / a[i][i]
            for j in range(i, dim):
                a[i][j] *= inv_pivot
            z[i] *= inv_pivot
            for k in range(dim):
                if k != i and abs(a[k][i]) > 1e-12:
                    factor = a[k][i]
                    for j in range(i, dim):
                        a[k][j] -= factor * a[i][j]
                    z[k] -= factor * z[i]
        return z[:self.num_nodes]

def solve_mesh_subnetwork_branch_1(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 1."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 1, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_2(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 2."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 2, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_3(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 3."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 3, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_4(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 4."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 4, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_5(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 5."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 5, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_6(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 6."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 6, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_7(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 7."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 7, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_8(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 8."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 8, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_9(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 9."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 9, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_10(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 10."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 10, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_11(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 11."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 11, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_12(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 12."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 12, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_13(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 13."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 13, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_14(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 14."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 14, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_15(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 15."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 15, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_16(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 16."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 16, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_17(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 17."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 17, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_18(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 18."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 18, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_19(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 19."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 19, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_20(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 20."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 20, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_21(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 21."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 21, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_22(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 22."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 22, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_23(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 23."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 23, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_24(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 24."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 24, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_25(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 25."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 25, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_26(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 26."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 26, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_27(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 27."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 27, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_28(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 28."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 28, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_29(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 29."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 29, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_30(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 30."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 30, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_31(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 31."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 31, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_32(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 32."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 32, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_33(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 33."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 33, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_34(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 34."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 34, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_35(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 35."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 35, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_36(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 36."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 36, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_37(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 37."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 37, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_38(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 38."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 38, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_39(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 39."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 39, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_40(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 40."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 40, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_41(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 41."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 41, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_42(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 42."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 42, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_43(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 43."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 43, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_44(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 44."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 44, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_45(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 45."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 45, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_46(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 46."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 46, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_47(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 47."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 47, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_48(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 48."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 48, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_49(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 49."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 49, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_50(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 50."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 50, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_51(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 51."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 51, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_52(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 52."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 52, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_53(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 53."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 53, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_54(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 54."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 54, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_55(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 55."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 55, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_56(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 56."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 56, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_57(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 57."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 57, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_58(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 58."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 58, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_59(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 59."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 59, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_60(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 60."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 60, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_61(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 61."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 61, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_62(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 62."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 62, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_63(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 63."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 63, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_64(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 64."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 64, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_65(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 65."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 65, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_66(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 66."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 66, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_67(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 67."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 67, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_68(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 68."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 68, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_69(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 69."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 69, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_70(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 70."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 70, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_71(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 71."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 71, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_72(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 72."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 72, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_73(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 73."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 73, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_74(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 74."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 74, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_75(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 75."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 75, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_76(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 76."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 76, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_77(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 77."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 77, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_78(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 78."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 78, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_79(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 79."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 79, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_80(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 80."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 80, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_81(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 81."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 81, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_82(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 82."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 82, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_83(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 83."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 83, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_84(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 84."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 84, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_85(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 85."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 85, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_86(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 86."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 86, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_87(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 87."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 87, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_88(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 88."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 88, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_89(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 89."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 89, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_90(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 90."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 90, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_91(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 91."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 91, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_92(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 92."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 92, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_93(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 93."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 93, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_94(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 94."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 94, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_95(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 95."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 95, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_96(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 96."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 96, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_97(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 97."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 97, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_98(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 98."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 98, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_99(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 99."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 99, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_100(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 100."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 100, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_101(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 101."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 101, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_102(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 102."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 102, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_103(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 103."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 103, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_104(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 104."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 104, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_105(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 105."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 105, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_106(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 106."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 106, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_107(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 107."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 107, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_108(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 108."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 108, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_109(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 109."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 109, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_110(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 110."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 110, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_111(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 111."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 111, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_112(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 112."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 112, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_113(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 113."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 113, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_114(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 114."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 114, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_115(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 115."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 115, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_116(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 116."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 116, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_117(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 117."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 117, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_118(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 118."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 118, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_119(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 119."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 119, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_120(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 120."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 120, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_121(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 121."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 121, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_122(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 122."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 122, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_123(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 123."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 123, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_124(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 124."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 124, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_125(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 125."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 125, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_126(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 126."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 126, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_127(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 127."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 127, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_128(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 128."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 128, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_129(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 129."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 129, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_130(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 130."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 130, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_131(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 131."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 131, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_132(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 132."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 132, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_133(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 133."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 133, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_134(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 134."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 134, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_135(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 135."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 135, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_136(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 136."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 136, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_137(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 137."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 137, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_138(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 138."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 138, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_139(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 139."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 139, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_140(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 140."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 140, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_141(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 141."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 141, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_142(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 142."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 142, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_143(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 143."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 143, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_144(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 144."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 144, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_145(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 145."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 145, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_146(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 146."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 146, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_147(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 147."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 147, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_148(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 148."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 148, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}

def solve_mesh_subnetwork_branch_149(v_bias: float, r_series: float, r_parallel: float) -> dict[str, float]:
    """Compute Norton/Thevenin equivalent for subnetwork stage 149."""
    r_thev = (r_series * r_parallel) / (r_series + r_parallel) if (r_series + r_parallel) > 0 else 0.0
    v_thev = v_bias * (r_parallel / (r_series + r_parallel)) if (r_series + r_parallel) > 0 else 0.0
    i_norton = v_thev / r_thev if r_thev > 0 else 0.0
    power_dissipation = (v_thev ** 2) / (r_thev + 1e-9)
    return {'stage': 149, 'v_thev': v_thev, 'r_thev': r_thev, 'i_norton': i_norton, 'power': power_dissipation}
