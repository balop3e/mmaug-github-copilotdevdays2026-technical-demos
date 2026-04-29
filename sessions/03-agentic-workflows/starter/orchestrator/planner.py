"""Task planner: breaks a high-level goal into independently testable steps."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class PlanStep:
    name: str
    description: str
    risk_level: str  # low | medium | high
    dependencies: List[str] = field(default_factory=list)
    acceptance_criteria: List[str] = field(default_factory=list)
    status: str = "pending"

    def is_blocked(self, completed_names: set[str]) -> bool:
        return any(dep not in completed_names for dep in self.dependencies)


def create_auth_plan() -> List[PlanStep]:
    """Return a pre-defined step breakdown for adding JWT auth to the task API."""
    return [
        PlanStep(
            name="add-user-model",
            description="Create User model with id, email, hashed_password fields",
            risk_level="low",
            dependencies=[],
            acceptance_criteria=[
                "User dataclass/model is defined",
                "Passwords are stored hashed (bcrypt), never plaintext",
                "Model has email uniqueness constraint",
            ],
        ),
        PlanStep(
            name="implement-register",
            description="POST /register endpoint: validate email, hash password, persist user",
            risk_level="medium",
            dependencies=["add-user-model"],
            acceptance_criteria=[
                "Returns 201 on success with user id",
                "Returns 409 if email already registered",
                "Password is hashed before storage",
            ],
        ),
        PlanStep(
            name="implement-login",
            description="POST /login endpoint: verify credentials, issue JWT",
            risk_level="high",
            dependencies=["implement-register"],
            acceptance_criteria=[
                "Returns JWT token on valid credentials",
                "Returns 401 on invalid credentials",
                "Token expires after a configurable period",
            ],
        ),
        PlanStep(
            name="protect-endpoints",
            description="Add JWT auth dependency to /tasks endpoints",
            risk_level="high",
            dependencies=["implement-login"],
            acceptance_criteria=[
                "Unauthenticated requests return 401",
                "Valid token grants access",
                "Existing tests are updated",
            ],
        ),
    ]
