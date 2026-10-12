# Phase 19 — Security, Accessibility & Reliability

## Implemented safeguards

- Response security headers: `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`, and a configurable-friendly Content Security Policy.
- A random per-request diagnostic ID returned as `X-Request-ID`; unhandled request exceptions are logged server-side with that ID and request method/path. The ID supplied by a client is not trusted as the internal ID.
- Conservative 8 MiB request body limit. Increase only when the deployment genuinely needs larger uploads.
- HTTP-only, SameSite=Lax session/remember cookies. Configure `SESSION_COOKIE_SECURE=True` for HTTPS production deployments; local HTTP development can leave it disabled.
- Existing Flask-WTF CSRF protection remains enabled by default. Keep it enabled outside tests.
- Generic 413/500 responses avoid disclosing internal exception details to visitors.
- Keyboard skip link, visible keyboard focus and reduced-motion preferences.
- SQLite backup script uses SQLite's online backup API and runs `PRAGMA integrity_check` on the backup.

## SQLite backup

From the project root, run:

```bash
python scripts/backup_database.py
python scripts/backup_database.py /secure/backup/location/ldica.sqlite
```

The default output is written to `backups/`. Store backups outside the public web root, restrict access, encrypt them when appropriate, and periodically test restore procedures. The script intentionally refuses non-SQLite database URLs; use the database vendor's native backup procedure for other engines.

## Deployment checklist

1. Set a strong, private `SECRET_KEY` in the deployment environment. Do not commit `.env` or instance keys.
2. Serve behind HTTPS and set `SESSION_COOKIE_SECURE=True`.
3. Review CSP if introducing third-party scripts, embeds, or styles. Avoid relaxing it globally to fix individual features.
4. Keep CSRF enabled and test all state-changing forms.
5. Use least-privilege file permissions for the database, uploaded files and backups.
6. Keep dependencies patched; run tests and dependency audits before releases.
7. Configure log rotation and do not log passwords, session cookies, CSRF tokens or submitted private content.
8. Restore a backup into a test environment periodically; a backup that has never been restored is not a verified recovery plan.

## Scope notes

These changes are defensive defaults, not a penetration-test certification. CSP currently permits inline scripts/styles to accommodate the existing templates; migrating inline code to local files would allow a stricter policy. Validate every feature under the deployed reverse proxy and browser configuration.
