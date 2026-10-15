"""Regression tests for the application's HTTP security headers."""


def test_security_headers_are_present(client):
    response = client.get("/")

    assert response.status_code < 500
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "SAMEORIGIN"
    assert response.headers["Referrer-Policy"] == "strict-origin-when-cross-origin"
    assert response.headers["Permissions-Policy"] == (
        "camera=(), microphone=(), geolocation=()"
    )
    assert "default-src 'self'" in response.headers["Content-Security-Policy"]
    assert response.headers["X-Request-ID"]


def test_request_id_changes_between_requests(client):
    first = client.get("/")
    second = client.get("/")

    assert first.headers["X-Request-ID"]
    assert second.headers["X-Request-ID"]
    assert first.headers["X-Request-ID"] != second.headers["X-Request-ID"]


def test_hsts_is_only_added_for_secure_requests(client):
    http_response = client.get("/")
    https_response = client.get("/", base_url="https://localhost")

    assert "Strict-Transport-Security" not in http_response.headers
    assert https_response.headers["Strict-Transport-Security"].startswith("max-age=31536000")
