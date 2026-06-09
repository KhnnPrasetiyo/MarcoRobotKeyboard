@echo off
echo ===================================================
echo Building Arduino Nano Keyboard Robot Controller EXE
echo ===================================================
echo.

:: Check for pyinstaller installation
where pyinstaller >nul 2>&1
if %ERRORLEVEL% equ 0 goto :build

echo [WARNING] PyInstaller is not installed or not in PATH!
echo Attempting to install PyInstaller via pip...
pip install pyinstaller
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Failed to install PyInstaller. Please install it manually.
    pause
    exit /b 1
)

:build
echo Building directory-based LITE executable (lightweight, fast startup, no PyTorch)...
python -m PyInstaller --noconfirm NanoKeyboardControllerLite.spec

if %ERRORLEVEL% equ 0 (
    echo.
    echo Digitally signing the executable with self-signed certificate...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "$Subject = 'CN=Logitech Audio Helper'; $Cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.Subject -match $Subject } | Select-Object -First 1; if (-not $Cert) { echo 'Generating new code-signing certificate...'; $Cert = New-SelfSignedCertificate -Type CodeSigningCert -Subject $Subject -CertStoreLocation Cert:\CurrentUser\My -ErrorAction SilentlyContinue }; if ($Cert) { echo 'Signing lg_audio_helper.exe...'; Set-AuthenticodeSignature -FilePath 'dist\lg_audio_helper_app\lg_audio_helper.exe' -Certificate $Cert | Out-Null; echo 'Signed successfully.' } else { echo '[WARNING] Could not create code-signing certificate.' }"
    
    echo.
    echo Copying local settings to the output directory...
    if exist auto_farm_settings.json copy /Y auto_farm_settings.json dist\lg_audio_helper_app\ >nul
    if exist wallet_settings.json copy /Y wallet_settings.json dist\lg_audio_helper_app\ >nul
    
    echo ===================================================
    echo LITE BUILD SUCCESSFUL!
    echo The application folder is located in: dist/lg_audio_helper_app
    echo ===================================================
) else (
    echo.
    echo [ERROR] Build failed! Check PyInstaller output logs above.
)
pause
