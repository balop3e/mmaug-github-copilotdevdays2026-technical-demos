# Challenge 01 - Human-in-the-Loop Workflow

## Task

Extend the orchestrator to stop before merge and request manual approval.

## Acceptance criteria

- Add a gate step named manual_review
- If review is not approved, workflow exits with clear status
- Add a final summary report with completed and blocked steps

## Suggested prompts

- Add a manual review gate to this orchestrator with safe default behavior.
- Generate a text report summarizing workflow execution.
