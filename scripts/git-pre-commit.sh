#!/bin/bash
# Pre-commit hook to sync theme and export styles in archviz
echo "Syncing theme and export templates..."
python3 scripts/sync_theme.py
python3 scripts/sync_export.py
git add templates/html/*.html
