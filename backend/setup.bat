@echo off
echo Installing backend dependencies...
cd /d "%~dp0"
python -m venv .venv
call .venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
echo.
echo Setup complete! Activate virtual environment with: .venv\Scripts\activate.bat
pause
