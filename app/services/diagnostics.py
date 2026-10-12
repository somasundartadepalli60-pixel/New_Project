"""Read-only diagnostics helpers shared by CLI checks and tests."""
from pathlib import Path
from sqlalchemy import text


def database_check(engine):
    """Return a minimal database status without exposing connection credentials."""
    try:
        with engine.connect() as connection:
            dialect = engine.dialect.name
            if dialect == "sqlite":
                result = connection.execute(text("PRAGMA integrity_check")).scalar()
                if result != "ok":
                    return {"name": "database", "status": "fail", "detail": "integrity check failed"}
            else:
                connection.execute(text("SELECT 1")).scalar()
        return {"name": "database", "status": "ok", "detail": f"{dialect} connection and basic check succeeded"}
    except Exception:
        # Never return connection strings or exception text; these can contain secrets.
        return {"name": "database", "status": "fail", "detail": "connection or integrity check failed"}


def writable_directory_check(path):
    target = Path(path)
    try:
        target.mkdir(parents=True, exist_ok=True)
        probe = target / ".ldica-write-check"
        probe.write_text("ok", encoding="utf-8")
        probe.unlink()
        return {"name": "instance_directory", "status": "ok", "detail": "directory is writable"}
    except OSError:
        return {"name": "instance_directory", "status": "fail", "detail": "directory is not writable"}
