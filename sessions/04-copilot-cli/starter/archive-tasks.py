#!/usr/bin/env python3
"""
archive-tasks.py – Cross-platform Python version of archive-tasks.sh

Reads a tasks CSV, moves rows with status=done to an archive CSV,
and removes them from the original file.

Usage:
    python archive-tasks.py [--dry-run] [--input FILE] [--archive FILE]
"""
import argparse
import csv
import logging
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = SCRIPT_DIR / "sample-data" / "tasks.csv"
DEFAULT_ARCHIVE = SCRIPT_DIR / "sample-data" / "archive.csv"
DEFAULT_LOG = SCRIPT_DIR / "output" / "archive.log"

DONE_STATUS = "done"


def setup_logging(log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_path, encoding="utf-8"),
        ],
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Archive completed tasks from a CSV file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python archive-tasks.py --dry-run\n"
            "  python archive-tasks.py --input my-tasks.csv\n"
        ),
    )
    parser.add_argument(
        "--input", type=Path, default=DEFAULT_INPUT, help="Source tasks CSV file"
    )
    parser.add_argument(
        "--archive",
        type=Path,
        default=DEFAULT_ARCHIVE,
        help="Destination archive CSV (appended if it exists)",
    )
    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        help="Preview changes without modifying any files",
    )
    return parser.parse_args()


def load_csv(path: Path) -> tuple[list[str], list[dict]]:
    """Return (fieldnames, rows) from a CSV file."""
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    return fieldnames, rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def append_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    """Append rows to archive; write header if file is new."""
    write_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = parse_args()
    setup_logging(DEFAULT_LOG)

    try:
        fieldnames, all_rows = load_csv(args.input)
    except FileNotFoundError as exc:
        logging.error("%s\nRun ./setup-demo-data.sh first, or pass --input <path>", exc)
        sys.exit(1)

    done_rows = [r for r in all_rows if r.get("status") == DONE_STATUS]
    keep_rows = [r for r in all_rows if r.get("status") != DONE_STATUS]

    logging.info("Input file  : %s", args.input)
    logging.info("Archive file: %s", args.archive)
    logging.info("Done rows   : %d", len(done_rows))

    if not done_rows:
        logging.info("Nothing to archive – no rows with status=%s.", DONE_STATUS)
        return

    print(f"\nTasks to archive ({len(done_rows)} rows):")
    for row in done_rows:
        print(f"  [{row.get('status')}] {row.get('title')} (owner: {row.get('owner')})")
    print()

    if args.dry_run:
        logging.info("[DRY RUN] Would append %d rows to %s", len(done_rows), args.archive)
        logging.info("[DRY RUN] Would remove %d rows from %s", len(done_rows), args.input)
        print("✓  Dry run complete – no files were modified.")
        return

    # Archive
    args.archive.parent.mkdir(parents=True, exist_ok=True)
    append_csv(args.archive, fieldnames, done_rows)
    logging.info("Appended %d rows to %s", len(done_rows), args.archive)

    # Remove done rows from original
    write_csv(args.input, fieldnames, keep_rows)
    logging.info("Removed %d rows from %s", len(done_rows), args.input)

    print("✓  Archive complete.")
    print(f"   Archived : {len(done_rows)} rows → {args.archive}")
    print(f"   Remaining: {len(keep_rows)} active tasks in {args.input}")


if __name__ == "__main__":
    main()
