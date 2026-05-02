# Task Management API

A simple FastAPI-based task manager with priority and due-date filtering.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

## API Endpoints

### `GET /health`
Returns `{"status": "ok"}`.

### `GET /tasks`

List all tasks. Optionally filter by `priority` and/or `due_date`.

| Parameter  | Type   | Values                   | Description                 |
|------------|--------|--------------------------|-----------------------------|
| `priority` | string | `high`, `medium`, `low`  | Filter by priority level    |
| `due_date` | string | `YYYY-MM-DD`             | Filter by exact due date    |

Both filters can be combined.

#### Examples

**All tasks:**
```bash
curl http://localhost:8000/tasks
```

**Filter by priority:**
```bash
curl "http://localhost:8000/tasks?priority=high"
```

**Filter by due date:**
```bash
curl "http://localhost:8000/tasks?due_date=2026-04-30"
```

**Combine both filters:**
```bash
curl "http://localhost:8000/tasks?priority=high&due_date=2026-05-01"
```

**Python requests:**
```python
import requests

# Filter high-priority tasks due on 2026-05-01
tasks = requests.get(
    "http://localhost:8000/tasks",
    params={"priority": "high", "due_date": "2026-05-01"}
).json()
```

### `GET /tasks/{task_id}`

Retrieve a single task by ID.

```bash
curl http://localhost:8000/tasks/1
```

## Running Tests

```bash
pytest -v
```

## PR Summary

### What
Added `due_date` filtering to the `/tasks` endpoint alongside the existing `priority` filter. Both parameters are optional and combinable.

### Why
Users need to surface urgent items by combining priority and deadline—previously only priority filtering existed.

### How
- Extended the `Task` Pydantic model with an optional `due_date: Optional[str]` field (ISO 8601)
- Updated `list_tasks()` to accept and apply the new query parameter
- Input validation rejects non-ISO date strings and unknown priority values with HTTP 422
- Added a `GET /tasks/{task_id}` convenience endpoint

### Tests
15 test cases added covering:
- All three priority values
- Due-date match, no-match, and tasks without a due date
- Combined filter scenarios
- Invalid date format (non-ISO, garbage strings)
- Invalid priority value
- 404 for unknown task ID

### Rollout
No breaking changes. Existing callers that don't pass `due_date` receive the same response as before.
