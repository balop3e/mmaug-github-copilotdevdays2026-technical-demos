#!/usr/bin/env bash
# setup-demo-data.sh  –  Initialise sample data for the Copilot CLI lab
set -euo pipefail

DATA_DIR="$(cd "$(dirname "$0")" && pwd)/sample-data"
mkdir -p "$DATA_DIR"

# tasks.csv -------------------------------------------------------------------
cat > "$DATA_DIR/tasks.csv" << 'EOF'
id,title,owner,status,due_date,priority
1,Prepare slide deck,imoh,done,2026-04-20,high
2,Create starter repo,ben,done,2026-04-22,high
3,Publish article,emmanuel,todo,2026-05-10,medium
4,Review pull requests,ben,done,2026-04-25,medium
5,Set up CI pipeline,imoh,in_progress,2026-05-01,high
6,Write unit tests,emmanuel,todo,2026-05-08,medium
7,Update documentation,ben,done,2026-04-28,low
8,Fix auth bug,imoh,done,2026-04-27,high
9,Deploy to staging,emmanuel,in_progress,2026-05-03,high
10,Code review session 3,ben,todo,2026-05-12,low
11,Design system audit,imoh,done,2026-04-29,medium
12,Migrate database schema,emmanuel,todo,2026-05-15,high
13,Add dark mode,ben,done,2026-04-26,low
14,Performance profiling,imoh,todo,2026-05-20,medium
15,Release notes draft,emmanuel,done,2026-04-30,low
EOF

# projects.csv ----------------------------------------------------------------
cat > "$DATA_DIR/projects.csv" << 'EOF'
id,name,lead,status,deadline,team_size
1,Dev Days 2026,imoh,active,2026-05-01,8
2,Platform Rewrite,ben,active,2026-06-30,5
3,Mobile App,emmanuel,planning,2026-07-15,4
4,Security Audit,imoh,completed,2026-04-15,3
5,Analytics Dashboard,ben,active,2026-05-20,6
EOF

# notes.txt -------------------------------------------------------------------
cat > "$DATA_DIR/notes.txt" << 'EOF'
GitHub Copilot CLI demo – session 4 notes
===========================================
- copilot cli transforms natural language to shell commands
- always review before executing
- dry-run first for destructive operations
- agentic workflows build on CLI primitives
- context engineering improves suggestion quality
vscode copilot inline completions save keystrokes
EOF

echo "✓  Sample data created in $DATA_DIR"
