@echo off
title Sleeping Giants Scanner

cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo.
    echo ERROR: Virtual Environment not found.
    echo Please run Install.bat first.
    echo.
    pause
    exit
)

echo.
echo ============================================
echo      SLEEPING GIANTS SCANNER v1.0.0
echo ============================================
echo.

call .venv\Scripts\activate.bat

python main.py

echo.
echo ============================================
echo Scan Completed Successfully!
echo Telegram report has been sent.
echo CSV saved in output folder.
echo ============================================
echo.

pause
