from datetime import date
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MMAUG Session 1 Task API")

Priority = Literal["high", "medium", "low"]


class Task(BaseModel):
    id: int
    title: str
    priority: str
    completed: bool = False
    due_date: date | None = None


TASKS: list[Task] = [
    Task(id=1, title="Create session plan", priority="high", due_date=date(2026, 4, 30)),
    Task(id=2, title="Prepare demo repo", priority="medium", due_date=date(2026, 5, 1)),
    Task(id=3, title="Write challenge prompts", priority="low", due_date=date(2026, 5, 2)),
]


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks(due_date: date | None = None, priority: Priority | None = None) -> list[Task]:
    results = TASKS
    if priority is not None:
        results = [task for task in results if task.priority == priority]
    if due_date is not None:
        results = [task for task in results if task.due_date == due_date]
    return results
