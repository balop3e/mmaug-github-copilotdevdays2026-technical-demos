# Session 1 - GitHub Copilot: Your AI Companion for Every Workflow

**Speaker:** Emmanuel Itoje | **Duration:** 20-25 minutes

## Learning Objectives

By completing this session, you will:
- ✅ Use Copilot Chat for feature implementation from user stories
- ✅ Generate comprehensive unit tests with edge case coverage
- ✅ Leverage Copilot for bug diagnosis and safe refactoring
- ✅ Create professional pull request summaries and documentation
- ✅ Conduct code reviews with Copilot assistance

---

## What You'll Build

A small **FastAPI Task Management API** that supports:
- Create, read, list tasks
- Filter tasks by due date and priority
- Comprehensive test coverage
- Professional documentation and PR workflow

---

## Quick Start

### Local Setup

```bash
cd sessions/01-every-workflow/starter
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit **http://127.0.0.1:8000/docs** to explore the interactive API documentation (Swagger UI).

### Docker Setup

```bash
cd sessions/01-every-workflow/starter
docker build -t mmaug-session1 .
docker run -p 8000:8000 mmaug-session1
```

### GitHub Codespaces (Recommended)

1. Click **Code** → **Codespaces** → **Create codespace on main**
2. Wait for the container to initialize
3. In the terminal:
   ```bash
   cd sessions/01-every-workflow/starter
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
4. Click **Ports** and share port 8000 with your participants

---

## Demo Flow (Live Demonstration)

Follow this step-by-step flow to demonstrate Copilot's value across the development lifecycle:

### Step 1: Feature Implementation
- **Show:** User story on screen
- **Do:** Open Copilot Chat and paste feature implementation prompt
- **Explain:** How Copilot understands context and generates focused code
- **Result:** New /tasks filtering endpoint

### Step 2: Test Generation
- **Show:** The newly implemented feature code
- **Do:** Ask Copilot to generate comprehensive tests (nominal, edge cases, error paths)
- **Explain:** Test coverage reduces bugs and increases confidence
- **Result:** Pytest suite with 8+ test cases

### Step 3: Bug Diagnosis & Fix
- **Do:** Intentionally introduce a bug in the filtering logic
- **Explain:** "Let's see if Copilot can catch and fix it"
- **Ask Copilot:** "Explain the bug and suggest a safe refactor"
- **Result:** Copilot identifies the issue and proposes a minimal fix

### Step 4: PR Summary & Documentation
- **Show:** All the commits and changes made
- **Ask Copilot:** Generate a professional PR summary
- **Then:** Ask Copilot to write README examples for the new feature
- **Result:** Ready-to-publish documentation

### Step 5: Code Review Pass
- **Recap:** All the changes made in this workflow
- **Ask Copilot:** Perform a comprehensive code review
- **Explain:** Security, performance, and test coverage considerations
- **Result:** Quality gates passed, ready for merge

---

## Hands-On Challenge

**File:** `challenges/01-challenge.md`

Work through the 5-task challenge to experience this complete workflow yourself:

1. **Implement a feature** using Copilot Chat
2. **Generate tests** with comprehensive coverage
3. **Debug and fix** an intentional bug
4. **Write PR summary and docs** with Copilot
5. **Conduct a code review** with Copilot

**Expected time:** 20-25 minutes

---

## Key Prompts Used in This Session

### Feature Implementation
```
Implement a feature for filtering tasks by due date and priority in this project. 
Add these capabilities:
- Due date query parameter (optional, format: YYYY-MM-DD)
- Priority filter (optional, values: high, medium, low)
- Both filters should be combinable
- Update the Task model if needed
```

### Test Generation
```
Generate unit tests for edge cases and error handling for this feature.
Include tests for:
- Matching and non-matching values
- Null/missing parameters
- Invalid date formats
- Empty and single-item lists
- Boundary conditions
```

### Bug Diagnosis
```
Explain the bug in this function and suggest a safe refactor.
[Paste function here]
```

### PR Summary
```
Draft a pull request summary with context, changes, tests, and rollout notes.
Focus on: what changed, why, how, test coverage, and rollout risks.
```

### Code Review
```
Perform a review pass and list risks before merge.
Check for: security, performance, test coverage, backward compatibility, and style.
```

---

## Project Structure

```
starter/
├── app/
│   ├── main.py          # FastAPI app with task endpoints
│   └── models.py        # Pydantic models (if separated)
├── tests/
│   └── test_tasks.py    # Pytest test suite
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container configuration
├── .gitignore
└── pytest.ini           # Pytest configuration
```

---

## File Descriptions

| File | Purpose |
|------|---------|
| `app/main.py` | FastAPI application with CRUD endpoints and filtering logic |
| `tests/test_tasks.py` | Comprehensive test suite with edge cases |
| `requirements.txt` | FastAPI, Uvicorn, pytest, httpx, pydantic |
| `Dockerfile` | Production-ready container image |
| `pytest.ini` | Pytest configuration for proper module imports |

---

## Troubleshooting

### "No module named 'app'"
**Solution:** Tests must be run from the starter folder, and pytest.ini configures PYTHONPATH.
```bash
cd sessions/01-every-workflow/starter
pytest -v
```

### Port 8000 already in use
**Solution:** Use a different port:
```bash
uvicorn app.main:app --reload --port 8001
```

### Codespaces port forwarding not working
**Solution:** Ensure port 8000 is explicitly forwarded:
1. Click **Ports** tab
2. Click **Forward a port** and enter 8000
3. Change visibility to **Public** for sharing

---

## What's Next?

After this session, explore:
- **Agent Mode** in Copilot for multi-step changes
- **Copilot CLI** for terminal-driven workflows (Session 4)
- **Agentic Workflows** for autonomous task execution (Session 3)
- **VS Code Pro Tips** for keyboard shortcuts and context attachment (Session 2)

---

## Resources & References

- **GitHub Copilot Docs:** https://github.com/features/copilot
- **FastAPI Documentation:** https://fastapi.tiangolo.com/
- **pytest Guide:** https://docs.pytest.org/
- **Pydantic Models:** https://docs.pydantic.dev/
- **Uvicorn Server:** https://www.uvicorn.org/

---

## Learning Reflection

At the end of the session, consider:
- 💡 What was the most impactful Copilot feature for you?
- 🚀 How could you apply this workflow to your own projects?
- 🤔 What guardrails or practices should teams adopt with Copilot?
