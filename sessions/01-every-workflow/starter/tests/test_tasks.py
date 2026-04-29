"""
Comprehensive tests for the /tasks endpoint – due_date and priority filters.
"""

from datetime import date
from typing import List

import pytest
from fastapi.testclient import TestClient

import app.main as main_module
from app.main import Task, app

client = TestClient(app)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_tasks(records: list[dict]) -> List[Task]:
    return [Task(**r) for r in records]


# ---------------------------------------------------------------------------
# Fixtures – patch TASKS in-place so tests are isolated from each other
# ---------------------------------------------------------------------------

@pytest.fixture()
def empty_task_list(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main_module, "TASKS", [])


@pytest.fixture()
def single_task_list(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        main_module,
        "TASKS",
        _make_tasks([
            {"id": 1, "title": "Only task", "priority": "high", "due_date": date(2026, 6, 1)},
        ]),
    )


@pytest.fixture()
def mixed_null_due_dates(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        main_module,
        "TASKS",
        _make_tasks([
            {"id": 1, "title": "Has date",    "priority": "high",   "due_date": date(2026, 6, 1)},
            {"id": 2, "title": "No date",     "priority": "medium", "due_date": None},
            {"id": 3, "title": "Another date","priority": "low",    "due_date": date(2026, 7, 1)},
        ]),
    )


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------

def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# No filters – nominal case
# ---------------------------------------------------------------------------

def test_list_all_tasks_no_filter() -> None:
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 3


# ---------------------------------------------------------------------------
# Priority filter – matching / non-matching
# ---------------------------------------------------------------------------

def test_filter_by_priority_high_returns_match() -> None:
    response = client.get("/tasks", params={"priority": "high"})
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["priority"] == "high"


def test_filter_by_priority_medium_returns_match() -> None:
    response = client.get("/tasks", params={"priority": "medium"})
    items = response.json()
    assert len(items) == 1
    assert items[0]["priority"] == "medium"


def test_filter_by_priority_low_returns_match() -> None:
    response = client.get("/tasks", params={"priority": "low"})
    items = response.json()
    assert len(items) == 1
    assert items[0]["priority"] == "low"


def test_filter_by_priority_nonexistent_returns_422() -> None:
    response = client.get("/tasks", params={"priority": "critical"})
    assert response.status_code == 422


# ---------------------------------------------------------------------------
# due_date filter – matching / non-matching
# ---------------------------------------------------------------------------

def test_filter_by_due_date_returns_match() -> None:
    response = client.get("/tasks", params={"due_date": "2026-04-30"})
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["due_date"] == "2026-04-30"


def test_filter_by_due_date_no_match_returns_empty() -> None:
    response = client.get("/tasks", params={"due_date": "1900-01-01"})
    assert response.status_code == 200
    assert response.json() == []


def test_filter_by_due_date_boundary_first_day_of_year() -> None:
    response = client.get("/tasks", params={"due_date": "2026-01-01"})
    assert response.status_code == 200
    assert response.json() == []


def test_filter_by_due_date_boundary_last_day_of_year() -> None:
    response = client.get("/tasks", params={"due_date": "2026-12-31"})
    assert response.status_code == 200
    assert response.json() == []


# ---------------------------------------------------------------------------
# Combined filter
# ---------------------------------------------------------------------------

def test_filter_by_both_due_date_and_priority_returns_match() -> None:
    response = client.get("/tasks", params={"due_date": "2026-05-01", "priority": "medium"})
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["priority"] == "medium"
    assert items[0]["due_date"] == "2026-05-01"


def test_filter_combined_mismatched_priority_returns_empty() -> None:
    """Date exists but priority doesn't match that task."""
    response = client.get("/tasks", params={"due_date": "2026-04-30", "priority": "low"})
    assert response.status_code == 200
    assert response.json() == []


def test_filter_combined_mismatched_date_returns_empty() -> None:
    """Priority exists but date doesn't match that task."""
    response = client.get("/tasks", params={"due_date": "2099-12-31", "priority": "high"})
    assert response.status_code == 200
    assert response.json() == []


# ---------------------------------------------------------------------------
# Null / missing parameters
# ---------------------------------------------------------------------------

def test_omitting_due_date_returns_all_tasks() -> None:
    response = client.get("/tasks", params={"priority": "high"})
    items = response.json()
    assert all(item["priority"] == "high" for item in items)


def test_omitting_priority_returns_all_tasks_for_date() -> None:
    response = client.get("/tasks", params={"due_date": "2026-04-30"})
    items = response.json()
    assert all(item["due_date"] == "2026-04-30" for item in items)


def test_omitting_both_params_returns_all_tasks() -> None:
    response = client.get("/tasks")
    assert len(response.json()) == 3


def test_tasks_with_null_due_date_are_excluded_when_filtering(
    mixed_null_due_dates: None,
) -> None:
    """Tasks with due_date=None should never appear in a date-filtered result."""
    response = client.get("/tasks", params={"due_date": "2026-06-01"})
    items = response.json()
    assert len(items) == 1
    assert items[0]["due_date"] == "2026-06-01"


# ---------------------------------------------------------------------------
# Edge cases – empty list, single task
# ---------------------------------------------------------------------------

def test_empty_task_list_returns_empty(empty_task_list: None) -> None:
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_empty_task_list_with_filters_returns_empty(empty_task_list: None) -> None:
    response = client.get("/tasks", params={"priority": "high", "due_date": "2026-04-30"})
    assert response.status_code == 200
    assert response.json() == []


def test_single_task_list_matching_priority(single_task_list: None) -> None:
    response = client.get("/tasks", params={"priority": "high"})
    items = response.json()
    assert len(items) == 1
    assert items[0]["priority"] == "high"


def test_single_task_list_non_matching_priority(single_task_list: None) -> None:
    response = client.get("/tasks", params={"priority": "low"})
    assert response.json() == []


def test_single_task_list_matching_due_date(single_task_list: None) -> None:
    response = client.get("/tasks", params={"due_date": "2026-06-01"})
    items = response.json()
    assert len(items) == 1
    assert items[0]["due_date"] == "2026-06-01"


def test_single_task_list_non_matching_due_date(single_task_list: None) -> None:
    response = client.get("/tasks", params={"due_date": "2026-01-01"})
    assert response.json() == []


# ---------------------------------------------------------------------------
# Error handling – invalid date formats
# ---------------------------------------------------------------------------

def test_invalid_date_format_returns_422() -> None:
    response = client.get("/tasks", params={"due_date": "not-a-date"})
    assert response.status_code == 422


def test_invalid_date_format_dd_mm_yyyy_returns_422() -> None:
    response = client.get("/tasks", params={"due_date": "30-04-2026"})
    assert response.status_code == 422


def test_invalid_date_format_slash_separated_returns_422() -> None:
    response = client.get("/tasks", params={"due_date": "2026/04/30"})
    assert response.status_code == 422


def test_invalid_date_partial_returns_422() -> None:
    response = client.get("/tasks", params={"due_date": "2026-04"})
    assert response.status_code == 422


def test_invalid_date_empty_string_returns_422() -> None:
    response = client.get("/tasks", params={"due_date": ""})
    assert response.status_code == 422

# ---------------------------------------------------------------------------
# Priority enum validation (post code-review fix)
# ---------------------------------------------------------------------------

def test_invalid_priority_value_returns_422() -> None:
    response = client.get("/tasks", params={"priority": "critical"})
    assert response.status_code == 422


def test_priority_is_case_sensitive_uppercase_returns_422() -> None:
    response = client.get("/tasks", params={"priority": "High"})
    assert response.status_code == 422


def test_priority_empty_string_returns_422() -> None:
    response = client.get("/tasks", params={"priority": ""})
    assert response.status_code == 422