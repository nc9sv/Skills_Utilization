import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_app_exists():
    assert app is not None


def test_app_is_flask():
    assert app.name == "app"


def test_404_handler():
    client = app.test_client()

    response = client.get("/this-route-does-not-exist")

    assert response.status_code == 404
