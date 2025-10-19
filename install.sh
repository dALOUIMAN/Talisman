#!/bin/bash

# Installation script for Talisman Modern GUI Desktop Application
# For Arch Linux / ASUS ROG Strix systems

echo "=========================================="
echo "Talisman Desktop GUI Installation Script"
echo "=========================================="
echo ""

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "Warning: This script is designed for Linux systems"
    echo "Current OS: $OSTYPE"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check Python version
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.6 or higher"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Found Python $PYTHON_VERSION"

# Check Tkinter
echo "Checking Tkinter availability..."
if ! python3 -c "import tkinter" &> /dev/null; then
    echo "Warning: Tkinter is not available"
    echo ""
    echo "To install Tkinter on Arch Linux:"
    echo "  sudo pacman -S tk"
    echo ""
    echo "To install Tkinter on Ubuntu/Debian:"
    echo "  sudo apt-get install python3-tk"
    echo ""
    echo "To install Tkinter on Fedora:"
    echo "  sudo dnf install python3-tkinter"
    echo ""
    read -p "Would you like to try installing Tkinter? (requires sudo) (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        # Try to detect package manager and install
        if command -v pacman &> /dev/null; then
            sudo pacman -S tk
        elif command -v apt-get &> /dev/null; then
            sudo apt-get install python3-tk
        elif command -v dnf &> /dev/null; then
            sudo dnf install python3-tkinter
        else
            echo "Could not detect package manager. Please install Tkinter manually."
            exit 1
        fi
    else
        echo "Tkinter is required. Please install it manually."
        exit 1
    fi
fi

# Make the main script executable
echo "Making desktop_gui.py executable..."
chmod +x desktop_gui.py

# Optional: Create desktop entry
echo ""
read -p "Would you like to create a desktop entry? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    DESKTOP_FILE="$HOME/.local/share/applications/talisman-desktop.desktop"
    CURRENT_DIR=$(pwd)
    
    mkdir -p "$HOME/.local/share/applications"
    
    cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Talisman Desktop
Comment=Modern GUI Desktop for ASUS ROG Strix
Exec=python3 $CURRENT_DIR/desktop_gui.py
Icon=computer
Terminal=false
Categories=Utility;System;
Keywords=desktop;gui;rog;asus;
EOF
    
    chmod +x "$DESKTOP_FILE"
    echo "Desktop entry created at: $DESKTOP_FILE"
fi

# Optional: Create startup script
echo ""
read -p "Would you like to add Talisman to startup applications? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    AUTOSTART_FILE="$HOME/.config/autostart/talisman-desktop.desktop"
    CURRENT_DIR=$(pwd)
    
    mkdir -p "$HOME/.config/autostart"
    
    cat > "$AUTOSTART_FILE" << EOF
[Desktop Entry]
Type=Application
Name=Talisman Desktop
Comment=Modern GUI Desktop for ASUS ROG Strix
Exec=python3 $CURRENT_DIR/desktop_gui.py
Icon=computer
X-GNOME-Autostart-enabled=true
EOF
    
    chmod +x "$AUTOSTART_FILE"
    echo "Autostart entry created at: $AUTOSTART_FILE"
fi

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "To run the application:"
echo "  python3 desktop_gui.py"
echo "  or"
echo "  ./desktop_gui.py"
echo ""
echo "Keyboard shortcuts:"
echo "  F11 - Toggle fullscreen"
echo "  ESC - Exit fullscreen"
echo ""
echo "Enjoy your ASUS ROG Strix Desktop experience!"
