# Session 3 - GitHub Agentic Workflows

## Goal

Simulate a simple multi-step agent workflow to plan, execute, and summarize engineering tasks.

## Folder contents

- starter/orchestrator/ - Python orchestrator starter
- challenges/ - workflow and review exercises

## Local run

```bash
cd sessions/03-agentic-workflows/starter
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python orchestrator/main.py
```

## Deploy options

Option A - Docker:

```bash
cd sessions/03-agentic-workflows/starter
docker build -t mmaug-session3 .
docker run --rm mmaug-session3
```

Option B - GitHub Actions:

Create a workflow that runs orchestrator/main.py on push and stores logs as artifacts.
