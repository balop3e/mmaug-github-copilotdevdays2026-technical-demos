from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MMAUG Session 1 Task API")


class Task(BaseModel):
    id: int
    title: str
    priority: str
    completed: bool = False


TASKS: List[Task] = [
    Task(id=1, title="Create session plan", priority="high"),
    Task(id=2, title="Prepare demo repo", priority="medium"),
    Task(id=3, title="Write challenge prompts", priority="low"),
]


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/tasks", response_model=List[Task])
def list_tasks(priority: str | None = None) -> List[Task]:
    if priority is None:
        return TASKS
    return [task for task in TASKS if task.priority == priority]
