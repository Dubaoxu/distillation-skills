#!/bin/bash
cd "$(dirname "$0")"
echo "=== Pushing to GitHub ==="
git remote add origin https://github.com/Dubaoxu/distillation-skills.git 2>/dev/null
git branch -M main 2>/dev/null
git push -u origin main --force
echo ""
echo "=== Done! ==="
echo "Open: https://github.com/Dubaoxu/distillation-skills"
read -p "Press Enter to close..."
