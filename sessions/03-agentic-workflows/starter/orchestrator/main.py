"""Workflow orchestrator with human-in-the-loop approval gate."""

from __future__ import annotations

import logging
import sys

from orchestrator.executor import execute_plan
from orchestrator.planner import PlanStep, create_auth_plan
from orchestrator.reporter import build_report, print_report, save_report

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


# ── Human approval gate ────────────────────────────────────────────────────

def manual_review_gate(steps: list[PlanStep]) -> bool:
    """
    Stop the workflow and require explicit human approval before merge.

    Returns True only if the operator types "yes".
    Safe default: any other input blocks the merge.
    """
    high_risk = [s for s in steps if s.risk_level == "high"]
    completed = [s for s in steps if s.status == "done"]

    print("\n" + "=" * 60)
    print("  ⛔  MANUAL REVIEW REQUIRED")
    print("=" * 60)
    print(f"  Completed steps : {len(completed)}/{len(steps)}")
    print()
    print("  Review checklist:")
    print("    [ ] Code logic is correct and matches acceptance criteria")
    print("    [ ] Tests cover all scenarios (>80% coverage)")
    print("    [ ] No security risks identified")
    print("    [ ] Backward compatibility maintained")
    print("    [ ] Documentation is updated")

    if high_risk:
        print()
        print("  ⚠  HIGH-RISK steps requiring extra scrutiny:")
        for s in high_risk:
            print(f"     - {s.name}: {s.description}")

    print("=" * 60)

    try:
        answer = input("  Approve merge? (yes / no): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\n  Approval cancelled — workflow aborted.")
        return False

    approved = answer == "yes"
    if approved:
        print("  ✓ Merge approved by operator.\n")
    else:
        print("  ✗ Merge rejected — workflow will not proceed.\n")
    return approved


# ── Main entry point ───────────────────────────────────────────────────────

def run_workflow(interactive: bool = True, dry_run: bool = False) -> bool:
    """
    Execute the full agentic workflow.

    Returns True if the workflow completed and was approved.
    """
    logger.info("─" * 60)
    logger.info("  AGENTIC WORKFLOW: Add JWT Authentication")
    logger.info("─" * 60)

    # 1. Planning phase
    steps = create_auth_plan()
    logger.info("\n[planner] Task breakdown:")
    for s in steps:
        print(f"  • {s.name}  [{s.risk_level} risk]")

    # 2. Execution phase
    logger.info("\n[executor] Running steps…")
    execute_plan(steps, stop_on_high_risk=False, dry_run=dry_run)

    # 3. Human approval gate (skip in non-interactive / test mode)
    if interactive:
        approved = manual_review_gate(steps)
        if not approved:
            report = build_report(steps, task_name="JWT Auth – REJECTED")
            print_report(report)
            save_report(report, path="workflow_report.json")
            return False
    else:
        approved = True  # tests bypass interactive gate

    # 4. Summary report
    report = build_report(steps, task_name="JWT Auth")
    print_report(report)
    save_report(report, path="workflow_report.json")
    return approved


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    success = run_workflow(interactive=True, dry_run=dry_run)
    sys.exit(0 if success else 1)
