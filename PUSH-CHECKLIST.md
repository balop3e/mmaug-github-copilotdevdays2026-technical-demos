# Push Checklist

## 1. Initialize repository

```bash
cd /Users/imohetuk/Library/CloudStorage/OneDrive-Imoh-Etuk/GitHub\ Copilot\ Dev\ Days\ \ 2026-\ Malta/mmaug-github-copilotdevdays2026-technical-demos
git init
git add .
git commit -m "Scaffold MMAUG Copilot Dev Days 2026 technical demos"
```

## 2. Create remote repository

```bash
gh repo create MMAUG-ORG/mmaug-github-copilotdevdays2026-technical-demos --public --source=. --remote=origin --push
```

If you do not use GitHub CLI, create the repo in browser and then run:

```bash
git branch -M main
git remote add origin git@github.com:MMAUG-ORG/mmaug-github-copilotdevdays2026-technical-demos.git
git push -u origin main
```

## 3. Verify after push

- Confirm all 5 session folders are present.
- Confirm scripts in sessions 04 and 05 are executable.
- Enable Issues and Discussions for participant self-paced questions.
