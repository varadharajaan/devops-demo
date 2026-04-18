@echo off
echo Cleaning old zip...
if exist "%TEMP%\devops-demo.zip" del "%TEMP%\devops-demo.zip"

echo Creating new zip...
cd /d "%~dp0"
tar -acf "%TEMP%\devops-demo.zip" --exclude=.git --exclude=__pycache__ --exclude=logs --exclude=*.zip --exclude=package.bat --exclude=package.sh *

echo Done! Zip saved to %TEMP%\devops-demo.zip
explorer /select,"%TEMP%\devops-demo.zip"
pause
