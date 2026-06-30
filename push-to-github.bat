@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo === Pushing to GitHub ===
git push -u origin main --force
echo.
echo === Done! ===
echo Open: https://github.com/Dubaoxu/distillation-skills
pause
