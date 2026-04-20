from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_filter_by_priority() -> None:
    response = client.get("/tasks", params={"priority": "high"})
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["priority"] == "high"
