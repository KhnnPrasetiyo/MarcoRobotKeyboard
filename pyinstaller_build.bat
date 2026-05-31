@echo off
echo ===================================================
echo Building Arduino Nano Keyboard Robot Controller EXE
echo ===================================================
echo.

:: Check for pyinstaller installation
where pyinstaller >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [WARNING] PyInstaller is not installed or not in PATH!
    echo Attempting to install PyInstaller via pip...
    pip install pyinstaller
    if %ERRORLEVEL% neq 0 (
        echo [ERROR] Failed to install PyInstaller. Please install it manually.
        pause
        exit /b 1
    )
)

echo Building single-file executable...
pyinstaller --onefile --windowed --name="NanoKeyboardController" --noconfirm app/main.py

if %ERRORLEVEL% equ 0 (
    echo.
    echo ===================================================
    echo BUILD SUCCESSFUL!
    echo The executable is located in: dist/NanoKeyboardController.exe
    echo ===================================================
) else (
    echo.
    echo [ERROR] Build failed! Check PyInstaller output logs above.
)
pause
