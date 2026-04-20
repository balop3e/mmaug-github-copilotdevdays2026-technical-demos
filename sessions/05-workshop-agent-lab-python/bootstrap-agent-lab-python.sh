#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/copilot-dev-days/agent-lab-python"
TARGET_DIR="${1:-agent-lab-python}"

if [[ -d "$TARGET_DIR" ]]; then
  echo "Directory already exists: $TARGET_DIR"
  exit 1
fi

git clone "$REPO_URL" "$TARGET_DIR"
cd "$TARGET_DIR"

if command -v uv >/dev/null 2>&1; then
  uv sync || true
fi

echo "Workshop repo ready: $PWD"
