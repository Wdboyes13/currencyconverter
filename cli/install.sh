#!/bin/bash

# Define the download URL for your CLI tool (using raw.githubusercontent.com)
CLI_URL="https://github.com/Wdboyes13/currencyconverter/raw/refs/heads/main/cli/currconv"  # Replace with the correct URL

# Define the destination path for installation
DEST="/usr/local/bin/currconv"

# Download the CLI tool
echo "Downloading the CLI tool..."
curl -sSL "$CLI_URL" -o "$DEST"

# Make it executable
echo "Making the tool executable..."
chmod +x "$DEST"

# Verify installation
if command -v currconver &>/dev/null; then
    echo "Installation complete! You can now run 'currconv' from anywhere."
else
    echo "Installation failed. Please check the script for errors."
    exit 1
fi