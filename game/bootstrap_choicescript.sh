#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/dfabulich/choicescript.git"
TARGET_DIR="$(dirname "$0")/choicescript"

if [ -d "$TARGET_DIR" ]; then
  echo "ChoiceScript already present at $TARGET_DIR. Skipping clone."
  exit 0
fi

echo "Cloning ChoiceScript into $TARGET_DIR..."
git clone --depth=1 "$REPO_URL" "$TARGET_DIR"
echo "Done. You can now run ./game/sync_scenes.sh to copy the sample scenes."
