@echo off
title Sleeping Giants Scanner - Installation

cd /d "%~dp0"

echo.
echo ============================================
echo   SLEEPING GIANTS SCANNER - SETUP
echo ============================================
echo.

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python from https://python.org
    echo.
    pause
    exit
)

echo Creating virtual environment...
python -m venv .venv

echo.
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ============================================
echo Installation Complete!
echo You can now run: Run Scanner.bat
echo ============================================
echo.

pause
