"""Tests for the agentic workflow orchestrator."""

import pytest

from orchestrator.executor import execute_plan, ExecutionError, execute_step
from orchestrator.planner import PlanStep, create_auth_plan
from orchestrator.reporter import build_report


# ── Planner ────────────────────────────────────────────────────────────────

class TestPlanner:
    def test_plan_has_four_steps(self):
        steps = create_auth_plan()
        assert len(steps) == 4

    def test_all_steps_start_pending(self):
        for step in create_auth_plan():
            assert step.status == "pending"

    def test_first_step_has_no_dependencies(self):
        steps = create_auth_plan()
        assert steps[0].dependencies == []

    def test_later_steps_have_dependencies(self):
        steps = create_auth_plan()
        for step in steps[1:]:
            assert len(step.dependencies) >= 1

    def test_risk_levels_are_valid(self):
        valid = {"low", "medium", "high"}
        for step in create_auth_plan():
            assert step.risk_level in valid

    def test_step_is_blocked_when_dependency_missing(self):
        step = PlanStep(
            name="s2",
            description="needs s1",
            risk_level="low",
            dependencies=["s1"],
        )
        assert step.is_blocked(completed_names=set()) is True
        assert step.is_blocked(completed_names={"s1"}) is False


# ── Executor ───────────────────────────────────────────────────────────────

class TestExecutor:
    def test_execute_plan_marks_steps_done(self):
        steps = create_auth_plan()
        execute_plan(steps, dry_run=False)
        for step in steps:
            assert step.status == "done"

    def test_execute_plan_dry_run_marks_simulated(self):
        steps = create_auth_plan()
        execute_plan(steps, dry_run=True)
        for step in steps:
            assert step.status == "simulated"

    def test_blocked_step_raises(self):
        step = PlanStep(
            name="child",
            description="blocked by parent",
            risk_level="low",
            dependencies=["parent"],
        )
        with pytest.raises(ExecutionError, match="blocked"):
            execute_step(step, completed=set())

    def test_step_with_met_dependency_executes(self):
        step = PlanStep(
            name="child",
            description="parent done",
            risk_level="low",
            dependencies=["parent"],
        )
        execute_step(step, completed={"parent"})
        assert step.status == "done"


# ── Reporter ───────────────────────────────────────────────────────────────

class TestReporter:
    def _completed_steps(self):
        steps = create_auth_plan()
        for s in steps:
            s.status = "done"
        return steps

    def test_report_has_required_keys(self):
        report = build_report(self._completed_steps())
        for key in ("task", "generated_at", "summary", "steps",
                    "security_notes", "deployment_readiness", "recommended_next_steps"):
            assert key in report

    def test_report_counts_completed(self):
        steps = self._completed_steps()
        report = build_report(steps)
        assert report["summary"]["completed"] == 4
        assert report["summary"]["blocked"] == 0

    def test_report_deployment_ready_when_no_blocked(self):
        report = build_report(self._completed_steps())
        assert report["deployment_readiness"] is True

    def test_report_not_deployment_ready_when_blocked(self):
        steps = create_auth_plan()
        steps[0].status = "done"
        steps[1].status = "blocked"
        report = build_report(steps)
        assert report["deployment_readiness"] is False

    def test_high_risk_steps_appear_in_security_notes(self):
        steps = create_auth_plan()
        for s in steps:
            s.status = "done"
        report = build_report(steps)
        high_risk_names = [s.name for s in steps if s.risk_level == "high"]
        for name in high_risk_names:
            assert any(name in note for note in report["security_notes"])
