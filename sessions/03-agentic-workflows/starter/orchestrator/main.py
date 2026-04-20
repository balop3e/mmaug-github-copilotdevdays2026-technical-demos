from dataclasses import dataclass
from typing import List


@dataclass
class Step:
    name: str
    status: str = "pending"


def build_plan() -> List[Step]:
    return [
        Step(name="Analyze issue and propose plan"),
        Step(name="Implement scoped code changes"),
        Step(name="Generate and run tests"),
        Step(name="Summarize diff and risks"),
    ]


def run_plan(steps: List[Step]) -> None:
    for step in steps:
        step.status = "done"
        print(f"[agent] {step.name} -> {step.status}")


if __name__ == "__main__":
    workflow_steps = build_plan()
    run_plan(workflow_steps)
