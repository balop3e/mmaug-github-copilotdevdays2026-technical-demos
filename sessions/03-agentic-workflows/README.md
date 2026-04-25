# Session 3 - GitHub Agentic Workflows

**Speaker:** James Balogun | **Duration:** 20-25 minutes

## Learning Objectives

By completing this session, you will:
- ✅ Understand how Copilot agents break down complex software tasks
- ✅ Leverage agentic workflows for multi-step, autonomous execution
- ✅ Implement human-in-the-loop approval gates for safety
- ✅ Conduct risk-focused code review with Copilot
- ✅ Apply guardrails and best practices for agent-driven development

---

## What You'll Build

A **Multi-Step Workflow Orchestrator** that demonstrates:
- Task decomposition into independently testable steps
- Autonomous planning and execution phases
- Human approval gates before critical operations
- Comprehensive test coverage and risk analysis
- Audit-friendly summary reports

---

## Quick Start

### Local Setup

```bash
cd sessions/03-agentic-workflows/starter
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python orchestrator/main.py
```

### Docker Setup

```bash
cd sessions/03-agentic-workflows/starter
docker build -t mmaug-session3 .
docker run --rm mmaug-session3
```

### GitHub Codespaces

1. Open repo in Codespaces
2. Run the setup commands above
3. Monitor the orchestrator execution

---

## Demo Flow (Live Demonstration)

Follow this step-by-step flow to showcase agentic workflows:

### Step 1: Define the Task
- **Show:** A complex engineering requirement (e.g., add auth to API)
- **Explain:** Breaking tasks into steps is critical for agent success
- **Result:** Clear acceptance criteria and dependencies

### Step 2: Planning Phase
- **Do:** Switch Copilot Chat to "Plan" mode
- **Ask:** "Break this into steps and identify risks"
- **Explain:** Planning ensures safe, step-by-step execution
- **Result:** Proposed task breakdown with risk assessment

### Step 3: Autonomous Implementation
- **Show:** How agents can implement a scoped subset
- **Do:** Ask Copilot to implement step 1 in a dedicated branch
- **Explain:** AI handles coding while humans focus on oversight
- **Result:** Complete, tested implementation of one step

### Step 4: Risk-Focused Review
- **Show:** The generated diff from step 3
- **Do:** Ask Copilot to identify security and correctness risks
- **Explain:** Review focuses on risks, not style
- **Result:** Clear list of issues with recommended fixes

### Step 5: Fix & Test Loop
- **Show:** Any failing tests
- **Do:** Ask Copilot to fix them
- **Explain:** Automated testing catches regressions early
- **Result:** 100% test pass rate

### Step 6: Human Approval Gate
- **Show:** The manual review gate in code
- **Explain:** Humans explicitly approve before production impact
- **Result:** Workflow waits for explicit "yes" before merge

### Step 7: Summary Report
- **Show:** Final execution report with status
- **Explain:** Audit trail for compliance and learning
- **Result:** Complete documentation of what happened and why

---

## Hands-On Challenge

**File:** `challenges/01-challenge.md`

Work through the 8-task challenge to implement a full agentic workflow:

1. **Define high-level task** with acceptance criteria
2. **Create task breakdown** with step-by-step planning
3. **Ask agent to propose plan** (Plan mode)
4. **Let agent implement** first step autonomously
5. **Review diff** with risk-focused analysis
6. **Run tests** and fix failures
7. **Implement manual approval gate** for safety
8. **Generate summary report** with audit trail

**Expected time:** 20-25 minutes

---

## Key Concepts

### Agents vs. Assistants
- **Assistants** respond to individual prompts (like Copilot Chat)
- **Agents** autonomously break down tasks, plan execution, and take action
- Agents can iterate, self-correct, and handle complex workflows

### Planning Mode
- Special Copilot Chat mode for agentic workflows
- Proposes multi-step execution plans before implementation
- Allows human review and modification before execution

### Human-in-the-Loop
- **Critical principle:** Keep humans in control of high-impact decisions
- Manual approval gates for merge, deployment, or data changes
- Clear escalation paths for unexpected situations

### Task Decomposition
- Break large goals into small, independently testable steps
- Each step should be shippable (no hidden dependencies)
- Dependencies should be explicit and documented
- Risk levels should be reassessed after each step

---

## Key Prompts Used in This Session

### Task Definition
```
Define this engineering task with:
- Clear description of the goal
- Specific acceptance criteria
- Known constraints and dependencies
- Non-goals (what we're NOT doing)
- Success metrics
```

### Task Breakdown
```
Break this feature into independently shippable steps with risk notes.
For each step provide: description, acceptance criteria, effort estimate,
risk level, dependencies, and testing approach.
```

### Planning (Plan Mode)
```
Plan how you will implement Step 1 in detail.
Propose:
- File modifications needed
- Code structure changes
- Test cases to add
- Any breaking changes or migration needed
- Safety recommendations
```

### Implementation
```
Implement this step according to the plan:
Create a branch, make code changes, add tests, 
update documentation, and commit with clear messages.
```

### Risk Analysis
```
Analyze this diff and identify:
- Potential bugs or logic errors
- Security risks (SQL injection, auth bypass, etc.)
- Missing test coverage
- Performance implications
- Backward compatibility concerns
- Deviations from best practices
```

### Approval Gate
```
Add a manual review gate that:
- Stops the workflow before merge
- Shows a summary of changes
- Lists approval criteria
- Requires explicit confirmation
- Has a safe default (requires "yes")
```

---

## Project Structure

```
starter/
├── orchestrator/
│   ├── main.py          # Workflow orchestrator
│   ├── planner.py       # Task planning logic
│   ├── executor.py      # Step execution
│   └── reporter.py      # Summary reporting
├── tests/
│   └── test_orchestrator.py
├── requirements.txt
├── Dockerfile
└── pytest.ini
```

---

## Architecture Patterns

### Orchestration Pattern
```
Task Definition
    ↓
Task Breakdown (Planning)
    ↓
Step 1 Execution
    ↓
Risk Review
    ↓
Human Approval Gate
    ↓
Step 2 Execution
    ↓
... (repeat)
    ↓
Summary Report
```

### Safe Defaults Pattern
```
Before Merge (HIGH RISK):
  ├─ Human MUST explicitly approve
  └─ Default is BLOCKED (safe default)

Before Deploy (MEDIUM RISK):
  ├─ Approval gate required
  └─ Rollback procedure documented

Before Review (LOW RISK):
  ├─ Automatic, with logging
  └─ Human review after-the-fact ok
```

---

## Safety & Guardrails

**Critical Principles:**
- 🚦 **Keep humans in the loop** for all critical decisions
- 🔍 **Review all diffs** before merge, especially for security
- 📋 **Maintain audit trails** of all agent decisions
- 🛑 **Set explicit approval gates** and require confirmation
- 📊 **Log and monitor** all agent activity
- 🚨 **Escalate** unclear or high-risk situations to humans
- 🔐 **Never trust** agent-generated code blindly—verify and test

**Recommended Guardrails:**
1. Manual approval required for production changes
2. Automated security scanning before deployment
3. Comprehensive test coverage (>80%)
4. Rollback procedure documented before deploy
5. Audit logs for compliance and learning
6. Limited scope for initial agent tasks
7. Clear error handling and escalation paths

---

## Troubleshooting

### "Plan mode not available"
**Solution:** 
- Update GitHub Copilot to the latest version
- Ensure you have access to agentic workflows (beta/preview feature)
- Refresh VS Code

### Agent proposes unsafe changes
**Solution:**
- Don't approve the plan
- Ask Copilot to revise with specific constraints
- Add additional guardrails before implementation

### Tests fail after agent implementation
**Solution:**
- Ask Copilot to explain and fix the failures
- Ensure agent has context about existing tests
- Review diff to find discrepancies with expected behavior

---

## What's Next?

After this session, explore:
- **Copilot CLI** for terminal-driven workflows (Session 4)
- **Custom Agents** for domain-specific tasks
- **GitHub Actions Integration** for automated approval workflows
- **Multi-Agent Coordination** for complex projects

---

## Important Resources

- **GitHub Agentic Workflows Blog:** https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/
- **GitHub Copilot Agent Announcement:** https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/
- **Agentics Framework:** https://github.com/githubnext/agentics/
- **Quick Start Guide:** https://github.github.com/gh-aw/setup/quick-start/
- **Architecture Overview:** https://github.github.com/gh-aw/introduction/architecture/
- **ChatOps Patterns:** https://github.github.com/gh-aw/patterns/chat-ops/

---

## Learning Reflection

At the end of the session, consider:
- 🤖 What tasks would benefit from agentic workflows in your team?
- 🛡️ What guardrails would you implement for your use case?
- 📈 How could you measure the effectiveness of agentic workflows?
- 🚀 What are the long-term implications for software development?
