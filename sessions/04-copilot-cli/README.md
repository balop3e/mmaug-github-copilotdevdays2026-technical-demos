# Session 4 - GitHub Copilot CLI: Your AI Terminal Companion

**Speaker:** Benjamin Busari | **Duration:** 20-25 minutes

## Learning Objectives

By completing this session, you will:
- ✅ Convert natural language intent to precise shell commands
- ✅ Understand and validate commands before execution
- ✅ Compose complex pipelines safely with dry-run patterns
- ✅ Generate reusable scripts from command sequences
- ✅ Apply safety guardrails: input validation, error handling, logging
- ✅ Create cross-platform alternatives for portability

---

## What You'll Learn

Experience **Intent-to-Command Workflows** that demonstrate:
- Natural language to CLI translation
- Interactive command explanation and validation
- Safe pipeline composition with preview modes
- Script generation with guardrails
- Cross-platform compatibility patterns

---

## Quick Start

### Prerequisites

- Git bash (macOS/Linux) or Windows Subsystem for Linux (WSL)
- Python 3.10+ (optional, for cross-platform demos)
- A terminal application (Terminal.app, iTerm2, Windows Terminal, etc.)

### Local Setup

```bash
cd sessions/04-copilot-cli/starter
chmod +x *.sh
./setup-demo-data.sh
./analyze-demo-data.sh
```

### GitHub Codespaces

1. Open repo in Codespaces
2. Scripts are ready to run immediately:
   ```bash
   cd sessions/04-copilot-cli/starter
   ./setup-demo-data.sh
   ```

### Workshop VM

Copy this folder to a Linux/macOS VM and run the scripts above.

---

## Demo Flow (Live Demonstration)

Follow this step-by-step flow to showcase Copilot CLI capabilities:

### Step 1: Natural Language to Command
- **Show:** A simple requirement in plain English
- **Do:** Ask Copilot CLI to generate the command
- **Explain:** How Copilot understands intent and translates it
- **Result:** Working command that solves the problem

### Step 2: Command Explanation & Validation
- **Show:** The generated command on screen
- **Do:** Ask Copilot to explain each part
- **Explain:** Why understand before execution is critical
- **Result:** Clear understanding of what the command does

### Step 3: Safe Pipeline Composition
- **Show:** A complex multi-step data process
- **Do:** Ask Copilot to compose the pipeline
- **Explain:** How pipes pass data between commands
- **Result:** Working pipeline with clear output

### Step 4: Dry-Run Patterns
- **Show:** A potentially destructive operation
- **Do:** Ask Copilot for a dry-run variant
- **Explain:** Preview changes without applying them
- **Result:** Confidence before executing

### Step 5: Script Generation
- **Show:** A series of related commands
- **Do:** Ask Copilot to create a reusable script
- **Explain:** Automation and error handling
- **Result:** Production-ready script with guardrails

### Step 6: Cross-Platform Alternatives
- **Show:** A bash-specific command
- **Do:** Ask Copilot for Windows/Python alternative
- **Explain:** Portability and team collaboration
- **Result:** Scripts that work everywhere

---

## Hands-On Challenge

**File:** `challenges/01-challenge.md`

Work through the 7-task challenge to master CLI automation:

1. **File discovery** with natural language
2. **Pipeline composition** and explanation
3. **Archive script** generation with safety
4. **Batch rename** with dry-run preview
5. **Release notes** from git history
6. **Cross-platform** script alternatives
7. **Complex analysis** queries with piping

**Expected time:** 20-25 minutes

---

## Live Command Pack

Ready-to-run examples for your demonstration:

### Safe File Discovery

**Intent:**
```
Find all markdown files in this project and show the 10 largest.
```

**Command:**
```bash
find . -type f -name "*.md" -print0 | xargs -0 du -h | sort -hr | head -n 10
```

**Explanation:**
- `find . -type f -name "*.md"`: Find all markdown files
- `-print0`: Output with null separators (handles spaces in filenames)
- `xargs -0`: Pass output to du, respecting null separators
- `du -h`: Show file sizes in human-readable format
- `sort -hr`: Sort by size in reverse (largest first)
- `head -n 10`: Show only first 10 results

---

### Code Search Workflow

**Intent:**
```
Locate references to GitHub Copilot in this repository.
```

**Command:**
```bash
grep -Rin "GitHub Copilot" .
```

**Explanation:**
- `grep`: Global regular expression print (search tool)
- `-R`: Recursive (search all directories)
- `-i`: Ignore case (find "github copilot", "GITHUB COPILOT", etc.)
- `-n`: Show line numbers
- `"GitHub Copilot"`: Search term

**Safer Variant (with progress):**
```bash
find . -type f -not -path '*/\.*' -not -path '*/node_modules/*' | \
  xargs grep -i "GitHub Copilot" 2>/dev/null | head -20
```

---

### Batch Rename with Dry-Run

**Intent:**
```
Show me how to rename files from draft-*.md to final-*.md with dry-run output.
```

**Command (Preview Only):**
```bash
for f in draft-*.md; do
  echo mv "$f" "${f/draft-/final-}"
done
```

**Explanation:**
- `for f in draft-*.md`: Loop through matching files
- `echo mv ...`: Print the command without executing (dry-run)
- `"${f/draft-/final-}"`: Bash string substitution (replace first occurrence)

**Command (Actually Execute):**
```bash
for f in draft-*.md; do
  [ ! -f "${f/draft-/final-}" ] && mv "$f" "${f/draft-/final-}" || echo "Target exists: ${f/draft-/final-}"
done
```

**Safer Version:**
```bash
for f in draft-*.md; do
  target="${f/draft-/final-}"
  if [ -f "$target" ]; then
    echo "SKIP: $target already exists"
  else
    echo "RENAME: $f → $target"
    mv "$f" "$target"
  fi
done
```

---

### Generate Release Notes from Git Log

**Intent:**
```
Create grouped release notes from commit messages from the last 2 weeks.
```

**Command:**
```bash
git log --since="2 weeks ago" --pretty=format:"- %s (%an)"
```

**Explanation:**
- `git log`: Show commit history
- `--since="2 weeks ago"`: Limit to recent commits
- `--pretty=format:`: Custom output format
- `%s`: Subject line (commit message)
- `%an`: Author name

**Enhanced Version (Grouped by Type):**
```bash
echo "# Release Notes (Last 2 Weeks)"
echo ""
echo "## Features"
git log --since="2 weeks ago" --grep="^feat" --pretty=format:"- %s (%an)" || echo "None"
echo ""
echo "## Fixes"
git log --since="2 weeks ago" --grep="^fix" --pretty=format:"- %s (%an)" || echo "None"
echo ""
echo "## Documentation"
git log --since="2 weeks ago" --grep="^docs" --pretty=format:"- %s (%an)" || echo "None"
```

---

### Data Processing Pipeline

**Intent:**
```
Find all Python files, extract imports, count unique ones, show top 20.
```

**Command:**
```bash
grep -rh "^import \|^from " . --include="*.py" | \
  sed 's/ as .*//' | \
  sed 's/ import.*//' | \
  sort | uniq -c | sort -rn | head -20
```

**Explanation:**
- `grep -rh`: Find import statements without filenames
- `sed 's/ as .*//'`: Remove "as" aliases
- `sed 's/ import.*//'`: Remove import details
- `sort`: Initial sort for uniq to work
- `uniq -c`: Count occurrences
- `sort -rn`: Sort by count (reverse numeric)
- `head -20`: Show top 20

---

### Safe File Deletion Preview

**Intent:**
```
Show me how to safely delete files matching a pattern without accidents.
```

**Command (Preview):**
```bash
find . -name "*.log" -type f -print
```

**Explanation:**
- Uses `find` to show matching files
- Only uses `-print` (doesn't delete)
- Shows exact paths before any action

**Command (Actually Delete, But Safely):**
```bash
find . -name "*.log" -type f -newer /tmp/cutoff -delete
```

**Explanation:**
- `-newer /tmp/cutoff`: Only delete files newer than cutoff date
- `-delete`: Actually remove them
- Still safer with time-based filter

---

### Cross-Platform: List Environment Variables

**Bash:**
```bash
env | grep -E "^(PATH|PYTHONPATH|USER)" | sort
```

**PowerShell (Windows):**
```powershell
Get-ChildItem env: | Where-Object { $_.Name -match '^(PATH|PYTHONPATH|USER)' } | Sort-Object Name
```

**Python (Universal):**
```bash
python -c "import os; print('\n'.join([f'{k}={v}' for k,v in sorted(os.environ.items()) if any(x in k for x in ['PATH', 'PYTHON'])]))"
```

---

## Safety Practices

### Before Executing Any Command

- [ ] Read the full command carefully
- [ ] Ask Copilot to explain what it does
- [ ] Use `echo` to preview output without side effects
- [ ] Use `--dry-run` flag if available
- [ ] Test on sample data first
- [ ] Verify you're in the right directory

### For Destructive Operations

- [ ] Always preview with `echo` or similar
- [ ] Create a backup first
- [ ] Use time-based filters when possible
- [ ] Implement confirmation prompts in scripts
- [ ] Log all operations
- [ ] Have a rollback procedure

### Script Best Practices

```bash
#!/bin/bash
# Add error handling
set -euo pipefail

# Document the script
# Usage: script.sh [options]

# Validate inputs
if [ $# -lt 1 ]; then
  echo "Error: Missing required argument"
  exit 1
fi

# Support --help and --dry-run
case "$1" in
  --help)
    echo "Usage: script.sh [--help|--dry-run]"
    exit 0
    ;;
  --dry-run)
    DRY_RUN=true
    ;;
esac

# Log operations
log_file="script.log"
log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$log_file"
}

# Use log in operations
log "Starting operation..."
```

---

## Troubleshooting

### "command not found"
**Solution:** Ensure the command is installed:
```bash
which grep
which find
which git
```

### "Permission denied" on scripts
**Solution:** Make script executable:
```bash
chmod +x script.sh
```

### Command takes too long
**Solution:** Limit scope:
```bash
# Instead of:
grep -r "pattern" /

# Use:
grep -r "pattern" . --include="*.py"
```

### "No such file or directory"
**Solution:** Check your working directory:
```bash
pwd
ls -la
```

---

## Project Structure

```
starter/
├── setup-demo-data.sh        # Initialize sample data
├── analyze-demo-data.sh      # Run analysis examples
├── archive-tasks.sh          # Archive script template
├── archive-tasks.py          # Python cross-platform version
├── sample-data/              # Sample CSV, text files
│   ├── tasks.csv
│   └── projects.csv
└── output/                   # Results from analysis
    └── results.txt
```

---

## File Descriptions

| File | Purpose |
|------|---------|
| `setup-demo-data.sh` | Create sample data for demos |
| `analyze-demo-data.sh` | Run live command examples |
| `archive-tasks.sh` | Bash archive script with dry-run |
| `archive-tasks.py` | Python version for cross-platform |
| `sample-data/` | CSV files for processing examples |

---

## What's Next?

After this session, explore:
- **Agentic Workflows** for complex automation (Session 3)
- **GitHub Actions** for CI/CD automation
- **Custom Copilot Agents** for domain-specific tasks
- **Integration** with your development workflow

---

## Important Resources

- **GitHub Copilot CLI Docs:** https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents
- **Bash Manual:** https://www.gnu.org/software/bash/manual/
- **GNU Coreutils:** https://www.gnu.org/software/coreutils/
- **Git Documentation:** https://git-scm.com/doc
- **grep Examples:** https://www.gnu.org/software/grep/manual/
- **find Manual:** https://www.gnu.org/software/findutils/manual/find.html
- **sed Tutorial:** https://www.gnu.org/software/sed/manual/sed.html

---

## Learning Reflection

At the end of the session, consider:
- 🔍 Which type of command was most useful?
- 🛡️ What safety practices will you adopt?
- 🚀 How can you automate repetitive tasks?
- 💡 What workflows in your team could benefit from CLI automation?
