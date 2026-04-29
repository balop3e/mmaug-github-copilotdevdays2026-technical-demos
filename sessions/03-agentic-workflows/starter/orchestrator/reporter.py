"""Reporter: generates human-readable and machine-parseable summary reports."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import List

from .planner import PlanStep


def build_report(steps: List[PlanStep], task_name: str = "Workflow") -> dict:
    """Return a structured report dict."""
    now = datetime.now(tz=timezone.utc).isoformat()

    completed  = [s for s in steps if s.status == "done"]
    blocked    = [s for s in steps if s.status == "blocked"]
    pending    = [s for s in steps if s.status == "pending"]
    high_risk  = [s for s in steps if s.risk_level == "high"]

    return {
        "task": task_name,
        "generated_at": now,
        "summary": {
            "total":     len(steps),
            "completed": len(completed),
            "blocked":   len(blocked),
            "pending":   len(pending),
        },
        "steps": [
            {
                "name":        s.name,
                "description": s.description,
                "risk_level":  s.risk_level,
                "status":      s.status,
            }
            for s in steps
        ],
        "security_notes": [
            f"Step '{s.name}' is high-risk — ensure review before merge"
            for s in high_risk
        ],
        "deployment_readiness": len(blocked) == 0 and len(pending) == 0,
        "recommended_next_steps": [
            f"Complete blocked step: {s.name} ({', '.join(s.dependencies)})"
            for s in blocked
        ] or ["All steps completed — ready for review and merge"],
    }


def print_report(report: dict) -> None:
    """Print a human-friendly summary."""
    s = report["summary"]
    print("\n" + "=" * 60)
    print(f"  WORKFLOW REPORT: {report['task']}")
    print(f"  Generated: {report['generated_at']}")
    print("=" * 60)
    print(f"  Total steps : {s['total']}")
    print(f"  Completed   : {s['completed']}")
    print(f"  Blocked     : {s['blocked']}")
    print(f"  Pending     : {s['pending']}")
    print("-" * 60)
    for step in report["steps"]:
        icon = {"done": "✓", "blocked": "✗", "pending": "○", "simulated": "~"}.get(
            step["status"], "?"
        )
        print(f"  [{icon}] {step['name']}  [{step['risk_level']} risk]")
    print("-" * 60)
    if report["security_notes"]:
        print("  ⚠  Security notes:")
        for note in report["security_notes"]:
            print(f"     - {note}")
    print(f"  Deployment ready: {'YES ✓' if report['deployment_readiness'] else 'NO ✗'}")
    print("-" * 60)
    print("  Next steps:")
    for step in report["recommended_next_steps"]:
        print(f"     → {step}")
    print("=" * 60 + "\n")


def save_report(report: dict, path: str = "workflow_report.json") -> None:
    """Persist the report as JSON for audit trail."""
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2)
    print(f"  Report saved to {path}")
