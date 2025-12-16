@echo off
echo Running database migrations...
cd /d "%~dp0"
call .venv\Scripts\activate.bat
alembic upgrade head
echo Migrations complete!
pause
