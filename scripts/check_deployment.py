"""Run safe, read-only LDICA deployment diagnostics.

Usage: python scripts/check_deployment.py
The command reports configuration categories, never secret values.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import create_app
from app.extensions import db
from app.services.diagnostics import database_check, writable_directory_check


def run_checks(app):
    results = [
        database_check(db.engine),
        writable_directory_check(app.instance_path),
    ]
    secret = app.config.get("SECRET_KEY")
    results.append({
        "name": "session_secret",
        "status": "ok" if isinstance(secret, str) and len(secret) >= 32 else "fail",
        "detail": "configured" if isinstance(secret, str) and len(secret) >= 32 else "missing or too short",
    })
    results.append({
        "name": "https_cookie",
        "status": "ok" if app.config.get("SESSION_COOKIE_SECURE") else "warning",
        "detail": "secure cookie enabled" if app.config.get("SESSION_COOKIE_SECURE") else "enable SESSION_COOKIE_SECURE behind HTTPS in production",
    })
    return results


if __name__ == "__main__":
    application = create_app()
    checks = run_checks(application)
    for check in checks:
        print(f"[{check['status'].upper()}] {check['name']}: {check['detail']}")
    raise SystemExit(1 if any(item["status"] == "fail" for item in checks) else 0)
