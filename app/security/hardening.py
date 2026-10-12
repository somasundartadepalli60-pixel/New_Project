"""Security headers and request diagnostics for the LDICA application."""
from __future__ import annotations

import logging
import secrets
from flask import current_app, g, request


def install_security_hardening(app):
    """Install low-risk defaults; deployment-specific policy stays configurable."""
    app.config.setdefault("MAX_CONTENT_LENGTH", 8 * 1024 * 1024)
    app.config.setdefault("SESSION_COOKIE_HTTPONLY", True)
    app.config.setdefault("SESSION_COOKIE_SAMESITE", "Lax")
    app.config.setdefault("REMEMBER_COOKIE_HTTPONLY", True)
    app.config.setdefault("REMEMBER_COOKIE_SAMESITE", "Lax")

    @app.before_request
    def assign_request_id():
        # Do not trust a client-supplied request ID as the canonical internal ID.
        g.request_id = secrets.token_hex(8)

    @app.after_request
    def add_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        response.headers.setdefault(
            "Content-Security-Policy",
            "default-src 'self'; base-uri 'self'; form-action 'self'; frame-ancestors 'self'; "
            "object-src 'none'; img-src 'self' data:; font-src 'self' data: https://fonts.gstatic.com; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
            "script-src 'self' 'unsafe-inline'; connect-src 'self'"
        )
        response.headers["X-Request-ID"] = getattr(g, "request_id", "unavailable")
        if request.is_secure:
            response.headers.setdefault("Strict-Transport-Security", "max-age=31536000; includeSubDomains")
        return response

    @app.teardown_request
    def log_failed_request(error):
        if error is not None:
            current_app.logger.error(
                "Unhandled request error request_id=%s method=%s path=%s",
                getattr(g, "request_id", "unavailable"), request.method, request.path,
                exc_info=(type(error), error, error.__traceback__),
            )
