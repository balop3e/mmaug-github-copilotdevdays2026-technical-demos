import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# ── Health ──────────────────────────────────────────────────────────────────

def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


# ── Nominal priority filter ──────────────────────────────────────────────────

def test_filter_by_priority_high() -> None:
    response = client.get("/tasks", params={"priority": "high"})
    assert response.status_code == 200
    items = response.json()
    assert len(items) >= 1
    assert all(t["priority"] == "high" for t in items)


def test_filter_by_priority_medium() -> None:
    response = client.get("/tasks", params={"priority": "medium"})
    assert response.status_code == 200
    assert all(t["priority"] == "medium" for t in response.json())


def test_filter_by_priority_low() -> None:
    response = client.get("/tasks", params={"priority": "low"})
    assert response.status_code == 200
    assert all(t["priority"] == "low" for t in response.json())


def test_no_filters_returns_all_tasks() -> None:
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 5  # matches TASKS fixture


# ── Nominal due_date filter ──────────────────────────────────────────────────

def test_filter_by_due_date_match() -> None:
    response = client.get("/tasks", params={"due_date": "2026-04-30"})
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["due_date"] == "2026-04-30"


def test_filter_by_due_date_no_match() -> None:
    response = client.get("/tasks", params={"due_date": "2000-01-01"})
    assert response.status_code == 200
    assert response.json() == []


# ── Combined filters ─────────────────────────────────────────────────────────

def test_filter_by_priority_and_due_date_match() -> None:
    response = client.get("/tasks", params={"priority": "high", "due_date": "2026-04-30"})
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["priority"] == "high"
    assert items[0]["due_date"] == "2026-04-30"


def test_filter_by_priority_and_due_date_no_match() -> None:
    """High-priority task exists for 2026-05-10, but none with priority=medium on 2026-04-30."""
    response = client.get("/tasks", params={"priority": "medium", "due_date": "2026-04-30"})
    assert response.status_code == 200
    assert response.json() == []


# ── Edge cases ───────────────────────────────────────────────────────────────

def test_filter_tasks_with_no_due_date_field() -> None:
    """Tasks without due_date should not match when due_date filter is applied."""
    response = client.get("/tasks", params={"due_date": "2026-05-05"})
    assert response.status_code == 200
    items = response.json()
    # All returned items must have the matching due_date
    assert all(t["due_date"] == "2026-05-05" for t in items)


def test_task_model_has_due_date_field() -> None:
    """All tasks in the list endpoint expose the due_date field (nullable)."""
    response = client.get("/tasks")
    assert response.status_code == 200
    for task in response.json():
        assert "due_date" in task


# ── Error handling ───────────────────────────────────────────────────────────

def test_invalid_due_date_format_returns_422() -> None:
    response = client.get("/tasks", params={"due_date": "not-a-date"})
    assert response.status_code == 422


def test_invalid_priority_returns_422() -> None:
    response = client.get("/tasks", params={"priority": "urgent"})
    assert response.status_code == 422


def test_invalid_date_format_dd_mm_yyyy() -> None:
    """European date format should be rejected."""
    response = client.get("/tasks", params={"due_date": "30-04-2026"})
    assert response.status_code == 422


# ── Individual task endpoint ─────────────────────────────────────────────────

def test_get_task_by_id() -> None:
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_task_not_found() -> None:
    response = client.get("/tasks/9999")
    assert response.status_code == 404
