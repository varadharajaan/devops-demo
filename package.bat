@echo off
echo Cleaning old zip...
if exist "%TEMP%\devops-demo.zip" del "%TEMP%\devops-demo.zip"

echo Creating new zip...
powershell -Command "Get-ChildItem -Path '%~dp0' -Exclude .git, __pycache__, logs, *.zip, package.bat | Compress-Archive -DestinationPath '%TEMP%\devops-demo.zip' -Force"

echo Done! Zip saved to %TEMP%\devops-demo.zip
explorer /select,"%TEMP%\devops-demo.zip"
pause
