@echo off
title Rolling Summary Charts v1.1

cd /d "%~dp0"

echo ======================================================
echo         ROLLING SUMMARY CHARTS v1.1
echo ======================================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Virtual Environment not found.
    echo Please run Install.bat first.
    pause
    exit /b
)

if not exist "output\rolling_summary.csv" (
    echo ERROR: output\rolling_summary.csv not found.
    echo Run the scanner at least once to generate rolling summary data.
    pause
    exit /b
)

call .venv\Scripts\activate.bat

echo Generating charts...
echo.

python plot_rolling_summary.py

if errorlevel 1 (
    echo.
    echo ======================================================
    echo Chart generation failed.
    echo ======================================================
    echo.
    pause
    exit /b 1
)

echo.
echo ======================================================
echo Charts generated successfully!
echo.
echo Check:
echo   - output\rolling_overlap_trend.png
echo   - output\rolling_contribution_trends.png
echo ======================================================
echo.

pause
