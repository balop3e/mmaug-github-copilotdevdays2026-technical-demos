#!/usr/bin/env bash
set -euo pipefail

mkdir -p data
cat > data/notes.txt <<'EOF'
copilot cli demo line 1
copilot cli demo line 2
agentic workflow reference
vscode session reference
EOF

cat > data/tasks.csv <<'EOF'
id,title,owner,status
1,Prepare slide deck,imoh,todo
2,Create starter repo,ben,in_progress
3,Publish article,emmanuel,todo
EOF

echo "Demo data created in ./data"
