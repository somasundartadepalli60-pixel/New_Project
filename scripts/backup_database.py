#!/usr/bin/env python3
"""Create a consistent backup of the app's SQLite database.

Usage: python scripts/backup_database.py [destination.sqlite]
Defaults to backups/ldica-YYYYMMDD-HHMMSS.sqlite relative to the project root.
This utility intentionally refuses non-SQLite database URLs.
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    database_url = os.environ.get("DATABASE_URL", f"sqlite:///{ROOT / 'instance' / 'ldica.db'}")
    if not database_url.startswith("sqlite:///"):
        print("Backup helper supports SQLite only. Use the database vendor's native backup tool.", file=sys.stderr)
        return 2
    raw_path = database_url[len("sqlite:///"):]
    source = Path(unquote(raw_path))
    if not source.is_absolute():
        # Flask-SQLAlchemy resolves relative SQLite URLs against Flask's
        # instance directory, not the repository root.
        source = (ROOT / "instance" / source).resolve()
    if not source.is_file():
        print(f"Database file not found: {source}", file=sys.stderr)
        return 2
    if len(sys.argv) > 2:
        print("Usage: python scripts/backup_database.py [destination.sqlite]", file=sys.stderr)
        return 2
    if len(sys.argv) == 2:
        destination = Path(sys.argv[1]).expanduser().resolve()
    else:
        folder = ROOT / "backups"
        folder.mkdir(parents=True, exist_ok=True)
        destination = folder / f"ldica-{datetime.now().strftime('%Y%m%d-%H%M%S')}.sqlite"
    if destination == source:
        print("Destination must differ from the live database.", file=sys.stderr)
        return 2
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        with sqlite3.connect(f"file:{source}?mode=ro", uri=True) as src, sqlite3.connect(destination) as dst:
            src.backup(dst)
            result = dst.execute("PRAGMA integrity_check").fetchone()[0]
            if result != "ok":
                raise RuntimeError(f"SQLite integrity check failed: {result}")
        print(f"Backup created and verified: {destination}")
        return 0
    except Exception as exc:
        try:
            destination.unlink(missing_ok=True)
        except OSError:
            pass
        print(f"Backup failed: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
