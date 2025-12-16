@echo off
echo Starting FastAPI server...
cd /d "%~dp0"
if not exist .venv\Scripts\activate.bat (
    echo Virtual environment not found. Please run setup.bat first.
    pause
    exit /b 1
)
call .venv\Scripts\activate.bat
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
pause
