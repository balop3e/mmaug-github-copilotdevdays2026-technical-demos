# Session 1 - GitHub Copilot: Your AI Companion for Every Workflow

## Goal

Build and improve a small task API using Copilot for implementation, tests, review, and documentation.

## Folder contents

- starter/ - runnable FastAPI starter project
- challenges/ - guided tasks for participants

## Local run

```bash
cd sessions/01-every-workflow/starter
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs.

## Deploy options

Option A - Docker:

```bash
cd sessions/01-every-workflow/starter
docker build -t mmaug-session1 .
docker run -p 8000:8000 mmaug-session1
```

Option B - Codespaces:

1. Open repo in GitHub Codespaces.
2. Install dependencies and run uvicorn command above.
3. Share forwarded port 8000 with participants.
