"""Executable entry point for generating the LDICA Enterprise Suite (500k+ LOC, 85 PRs, 100+ commits)."""
from __future__ import annotations

import sys
from pathlib import Path

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.generator.runner import run_pipeline

if __name__ == "__main__":
    run_pipeline()
