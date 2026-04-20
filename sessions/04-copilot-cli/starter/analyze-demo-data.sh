#!/usr/bin/env bash
set -euo pipefail

echo "== Text search =="
grep -in "copilot" data/notes.txt || true

echo

echo "== CSV summary =="
awk -F, 'NR>1 {count[$4]++} END {for (k in count) print k, count[k]}' data/tasks.csv
