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


def test_filter_by_due_date() -> None:
    response = client.get("/tasks", params={"due_date": "2026-04-30"})
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["due_date"] == "2026-04-30"


def test_filter_by_both_due_date_and_priority() -> None:
    response = client.get("/tasks", params={"due_date": "2026-05-01", "priority": "medium"})
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["priority"] == "medium"
    assert items[0]["due_date"] == "2026-05-01"


def test_no_match_returns_empty_list() -> None:
    response = client.get("/tasks", params={"due_date": "1900-01-01"})
    assert response.status_code == 200
    items = response.json()
    assert items == []


def test_invalid_date_format_returns_422() -> None:
    response = client.get("/tasks", params={"due_date": "not-a-date"})
    assert response.status_code == 422
