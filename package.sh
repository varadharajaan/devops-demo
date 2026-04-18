#!/bin/bash
echo "Cleaning old zip..."
rm -f devops-demo.zip

echo "Creating new zip..."
zip -r devops-demo.zip . -x ".git/*" "__pycache__/*" "logs/*" "*.zip" "package.bat" "package.sh"

echo "Done! Zip saved to $(pwd)/devops-demo.zip"
