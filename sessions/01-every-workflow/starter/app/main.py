from datetime import date
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="MMAUG Session 1 Task API")


class Task(BaseModel):
    id: int
    title: str
    priority: str  # high | medium | low
    due_date: Optional[str] = None  # YYYY-MM-DD
    completed: bool = False


TASKS: List[Task] = [
    Task(id=1, title="Create session plan", priority="high", due_date="2026-04-30"),
    Task(id=2, title="Prepare demo repo", priority="medium", due_date="2026-05-05"),
    Task(id=3, title="Write challenge prompts", priority="low", due_date="2026-05-10"),
    Task(id=4, title="Record intro video", priority="high", due_date="2026-05-01"),
    Task(id=5, title="Review pull requests", priority="medium"),
]

VALID_PRIORITIES = {"high", "medium", "low"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/tasks", response_model=List[Task])
def list_tasks(
    priority: Optional[str] = None,
    due_date: Optional[str] = None,
) -> List[Task]:
    """Return tasks, optionally filtered by priority and/or due_date."""
    if priority is not None and priority not in VALID_PRIORITIES:
        raise HTTPException(status_code=422, detail=f"Invalid priority '{priority}'. Use: high, medium, low")

    if due_date is not None:
        try:
            date.fromisoformat(due_date)
        except ValueError:
            raise HTTPException(status_code=422, detail=f"Invalid due_date '{due_date}'. Use YYYY-MM-DD format")

    results = TASKS
    if priority is not None:
        results = [t for t in results if t.priority == priority]
    if due_date is not None:
        results = [t for t in results if t.due_date == due_date]
    return results


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    for task in TASKS:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
