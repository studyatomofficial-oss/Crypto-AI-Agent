@echo off
title Sleeping Giants Scanner v1.1

cd /d "%~dp0"

echo ======================================================
echo        SLEEPING GIANTS SCANNER v1.1
echo ======================================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Virtual Environment not found.
    echo Please run Install.bat first.
    pause
    exit /b
)

call .venv\Scripts\activate.bat

echo Starting scan...
echo.

python main.py

echo.
echo ======================================================
echo Scan completed successfully!
echo.
echo Check:
echo   - Telegram for the report
echo   - output\latest.csv
echo   - output\history\
echo ======================================================
echo.

pause
