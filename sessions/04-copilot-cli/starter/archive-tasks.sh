#!/usr/bin/env bash
# archive-tasks.sh  –  Archive completed tasks from tasks.csv
#
# Usage:
#   ./archive-tasks.sh [--dry-run] [--help] [--input FILE] [--archive FILE]
#
# By default reads  sample-data/tasks.csv
# and writes to     sample-data/archive.csv
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# ── Defaults ────────────────────────────────────────────────────────────────
INPUT_FILE="$SCRIPT_DIR/sample-data/tasks.csv"
ARCHIVE_FILE="$SCRIPT_DIR/sample-data/archive.csv"
LOG_FILE="$SCRIPT_DIR/output/archive.log"
DRY_RUN=false

# ── Logging helper ───────────────────────────────────────────────────────────
mkdir -p "$(dirname "$LOG_FILE")"
log() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"; }

# ── Argument parsing ─────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --help|-h)
      cat << 'HELP'
Usage: archive-tasks.sh [OPTIONS]

Archive rows with status=done from tasks.csv into archive.csv,
then remove them from the original file.

Options:
  --help,    -h          Show this help text and exit
  --dry-run, -n          Preview what would be archived without modifying files
  --input    FILE        Source CSV file (default: sample-data/tasks.csv)
  --archive  FILE        Destination archive CSV (default: sample-data/archive.csv)

Examples:
  ./archive-tasks.sh --dry-run
  ./archive-tasks.sh --input my-tasks.csv --archive my-archive.csv
HELP
      exit 0
      ;;
    --dry-run|-n) DRY_RUN=true; shift ;;
    --input)      INPUT_FILE="$2"; shift 2 ;;
    --archive)    ARCHIVE_FILE="$2"; shift 2 ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

# ── Input validation ─────────────────────────────────────────────────────────
if [[ ! -f "$INPUT_FILE" ]]; then
  echo "ERROR: Input file not found: $INPUT_FILE" >&2
  echo "Run ./setup-demo-data.sh first, or pass --input <path>" >&2
  exit 1
fi

# Validate CSV has at least a header row
header=$(head -1 "$INPUT_FILE")
if [[ -z "$header" ]]; then
  echo "ERROR: Input file is empty: $INPUT_FILE" >&2
  exit 1
fi

# ── Find rows to archive ─────────────────────────────────────────────────────
DONE_COUNT=$(awk -F, 'NR>1 && $4=="done"' "$INPUT_FILE" | wc -l | tr -d ' ')

log "Input file  : $INPUT_FILE"
log "Archive file: $ARCHIVE_FILE"
log "Done rows   : $DONE_COUNT"

if [[ "$DONE_COUNT" -eq 0 ]]; then
  log "Nothing to archive – no rows with status=done."
  exit 0
fi

echo
echo "Tasks to archive ($DONE_COUNT rows):"
awk -F, 'NR>1 && $4=="done" {printf "  [%s] %s (owner: %s)\n", $4, $2, $3}' "$INPUT_FILE"
echo

# ── Dry-run mode ─────────────────────────────────────────────────────────────
if [[ "$DRY_RUN" == "true" ]]; then
  log "[DRY RUN] Would append $DONE_COUNT rows to $ARCHIVE_FILE"
  log "[DRY RUN] Would remove $DONE_COUNT rows from $INPUT_FILE"
  echo "✓  Dry run complete – no files were modified."
  exit 0
fi

# ── Archive: append done rows (with header if new file) ──────────────────────
if [[ ! -f "$ARCHIVE_FILE" ]]; then
  head -1 "$INPUT_FILE" > "$ARCHIVE_FILE"  # write header
fi
awk -F, 'NR>1 && $4=="done"' "$INPUT_FILE" >> "$ARCHIVE_FILE"
log "Appended $DONE_COUNT rows to $ARCHIVE_FILE"

# ── Remove done rows from original (keep header + non-done rows) ─────────────
TMP=$(mktemp)
awk -F, 'NR==1 || $4!="done"' "$INPUT_FILE" > "$TMP"
mv "$TMP" "$INPUT_FILE"
log "Removed $DONE_COUNT rows from $INPUT_FILE"

REMAINING=$(awk 'NR>1' "$INPUT_FILE" | wc -l | tr -d ' ')
echo "✓  Archive complete."
echo "   Archived : $DONE_COUNT rows → $ARCHIVE_FILE"
echo "   Remaining: $REMAINING active tasks in $INPUT_FILE"
