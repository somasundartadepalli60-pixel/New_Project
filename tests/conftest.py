import pytest
from app import create_app
from app.extensions import db

@pytest.fixture()
def app(tmp_path):
    test_db = tmp_path / "test.sqlite"
    app = create_app({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{test_db}",
        "SECRET_KEY": "test-secret",
    })
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()
