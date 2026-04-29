#!/usr/bin/env bash
# analyze-demo-data.sh  –  Live CLI analysis examples for the Copilot CLI lab
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DATA_DIR="$SCRIPT_DIR/sample-data"
OUTPUT_DIR="$SCRIPT_DIR/output"
mkdir -p "$OUTPUT_DIR"

if [[ ! -f "$DATA_DIR/tasks.csv" ]]; then
  echo "⚠  Sample data not found. Run ./setup-demo-data.sh first." >&2
  exit 1
fi

separator() { echo; echo "── $1 ──────────────────────────────────────────────"; echo; }

# ── 1. Text search ──────────────────────────────────────────────────────────
separator "Text search (grep)"
grep -in "copilot" "$DATA_DIR/notes.txt" || echo "(no matches)"

# ── 2. Task status summary (awk) ────────────────────────────────────────────
separator "Task status breakdown"
awk -F, 'NR>1 {count[$3]++} END {
  for (k in count) printf "  %-15s %d\n", k, count[k]
}' "$DATA_DIR/tasks.csv" | sort

# ── 3. Owners with most tasks ───────────────────────────────────────────────
separator "Tasks per owner"
awk -F, 'NR>1 {print $3}' "$DATA_DIR/tasks.csv" \
  | sort | uniq -c | sort -rn \
  | awk '{printf "  %-10s %d tasks\n", $2, $1}'

# ── 4. High-priority incomplete tasks ───────────────────────────────────────
separator "High-priority tasks not done"
awk -F, 'NR>1 && $4!="done" && $6=="high" {printf "  [%s] %s (owner: %s)\n", $4, $2, $3}' \
  "$DATA_DIR/tasks.csv"

# ── 5. Pipeline demo: import counts ─────────────────────────────────────────
separator "Pipeline demo – count CSV columns"
awk -F, 'NR==1 {for(i=1;i<=NF;i++) printf "  col %d: %s\n",i,$i}' \
  "$DATA_DIR/tasks.csv"

# ── 6. Save summary report ───────────────────────────────────────────────────
separator "Saving summary report"
{
  echo "=== Task Analysis Report ==="
  echo "Generated: $(date)"
  echo ""
  echo "-- Status breakdown --"
  awk -F, 'NR>1 {count[$4]++} END {for (k in count) printf "%-15s %d\n", k, count[k]}' \
    "$DATA_DIR/tasks.csv" | sort
  echo ""
  echo "-- High-priority open tasks --"
  awk -F, 'NR>1 && $4!="done" && $6=="high" {print $2}' "$DATA_DIR/tasks.csv"
} | tee "$OUTPUT_DIR/results.txt"

echo
echo "✓  Analysis complete. Report saved to $OUTPUT_DIR/results.txt"
