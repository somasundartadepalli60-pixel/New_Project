"""Tests for generated local Flask session signing keys."""

from app import load_local_secret


def test_local_secret_is_generated_and_persisted(tmp_path):
    key = load_local_secret(str(tmp_path))

    assert len(key) >= 32
    assert (tmp_path / ".local_session_key").read_text(encoding="utf-8") == key


def test_existing_valid_local_secret_is_reused(tmp_path):
    expected = "x" * 48
    key_path = tmp_path / ".local_session_key"
    key_path.write_text(expected, encoding="utf-8")

    assert load_local_secret(str(tmp_path)) == expected


def test_short_local_secret_is_replaced(tmp_path):
    key_path = tmp_path / ".local_session_key"
    key_path.write_text("too-short", encoding="utf-8")

    key = load_local_secret(str(tmp_path))

    assert len(key) >= 32
    assert key != "too-short"
    assert key_path.read_text(encoding="utf-8") == key


def test_missing_instance_directory_is_created(tmp_path):
    instance_path = tmp_path / "nested" / "instance"

    key = load_local_secret(str(instance_path))

    assert len(key) >= 32
    assert (instance_path / ".local_session_key").is_file()
