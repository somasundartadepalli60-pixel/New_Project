"""Expanded, structured LDICA engineering curriculum catalogs."""
from pathlib import Path

def catalog_files():
    """List catalog module paths for discovery and curriculum tooling."""
    return tuple(sorted(Path(__file__).parent.glob('*_catalog_*.py')))
