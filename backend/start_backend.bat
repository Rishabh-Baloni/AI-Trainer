@echo off
cd /d "d:\Projects\AI-Fitness Trainer\backend"
call venv\Scripts\activate.bat
set PYTHONIOENCODING=utf-8
python -m uvicorn app:app --host 127.0.0.1 --port 8001
pause
