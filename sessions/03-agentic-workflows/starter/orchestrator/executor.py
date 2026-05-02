"""Step executor: runs each plan step and tracks outcomes."""

from __future__ import annotations

import logging
from typing import List, Set

from .planner import PlanStep

logger = logging.getLogger(__name__)


class ExecutionError(Exception):
    """Raised when a step fails and cannot continue."""


def execute_step(step: PlanStep, completed: Set[str], dry_run: bool = False) -> None:
    """
    Execute a single step.

    In a real agentic system this would invoke Copilot / LLM tooling.
    Here we simulate success/failure and update step.status accordingly.
    """
    if step.is_blocked(completed):
        step.status = "blocked"
        missing = [d for d in step.dependencies if d not in completed]
        raise ExecutionError(
            f"Step '{step.name}' is blocked — unmet dependencies: {missing}"
        )

    prefix = "[DRY RUN] " if dry_run else ""
    logger.info("%sExecuting: %s", prefix, step.name)

    if not dry_run:
        # Simulate work; in a real agent this calls the AI toolchain
        step.status = "done"
        logger.info("  ✓ %s completed", step.name)
    else:
        step.status = "simulated"
        logger.info("  ↩ %s simulated (dry run)", step.name)


def execute_plan(
    steps: List[PlanStep],
    stop_on_high_risk: bool = True,
    dry_run: bool = False,
) -> List[PlanStep]:
    """
    Execute all steps in dependency order.

    If ``stop_on_high_risk`` is True, steps with risk_level=="high" require
    a human approval gate before execution (handled in main.py).
    """
    completed: Set[str] = set()

    for step in steps:
        if step.is_blocked(completed):
            step.status = "blocked"
            logger.warning("Skipping blocked step: %s", step.name)
            continue

        execute_step(step, completed, dry_run=dry_run)

        if step.status in {"done", "simulated"}:
            completed.add(step.name)

    return steps
