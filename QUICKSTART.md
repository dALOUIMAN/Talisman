# Quick Start Guide

## Talisman Desktop GUI - Get Started in 5 Minutes

### For Arch Linux Users (ASUS ROG Strix)

#### Step 1: Install Prerequisites

```bash
# Install Tkinter (if not already installed)
sudo pacman -S tk

# Optional: Install common applications
sudo pacman -S firefox nautilus gnome-terminal gedit vlc
```

#### Step 2: Clone and Setup

```bash
# Clone the repository
git clone https://github.com/dALOUIMAN/Talisman.git
cd Talisman

# Run the installer (recommended)
./install.sh
```

#### Step 3: Launch

```bash
# Method 1: Direct launch
python3 desktop_gui.py

# Method 2: If you created desktop entry
# Find "Talisman Desktop" in your application menu
```

---

### For Other Linux Distributions

#### Ubuntu/Debian
```bash
# Install Tkinter
sudo apt-get update
sudo apt-get install python3-tk

# Install optional applications
sudo apt-get install firefox nautilus gnome-terminal gedit vlc

# Clone and run
git clone https://github.com/dALOUIMAN/Talisman.git
cd Talisman
chmod +x desktop_gui.py install.sh
./install.sh
```

#### Fedora
```bash
# Install Tkinter
sudo dnf install python3-tkinter

# Install optional applications
sudo dnf install firefox nautilus gnome-terminal gedit vlc

# Clone and run
git clone https://github.com/dALOUIMAN/Talisman.git
cd Talisman
chmod +x desktop_gui.py install.sh
./install.sh
```

---

## First Time Usage

### 1. Launch in Windowed Mode (Recommended for First Time)

```bash
python3 desktop_gui.py
```

The application will start. Press **F11** to enter fullscreen mode.

### 2. Navigate the Interface

- **Top**: ASUS ROG Strix branding and title
- **Left Side**: Application launcher buttons
- **Right Side**: System information
- **Center**: Futuristic motherboard design with tech logos
- **Overlay**: Blue crystal glass effect

### 3. Launch Applications

Click on any application button:
- **Terminal**: Opens system terminal
- **Browser**: Opens Firefox/Chromium/Chrome
- **Files**: Opens file manager
- **Settings**: Opens system settings
- **Editor**: Opens text editor
- **Media**: Opens media player

### 4. Exit

Press **ESC** or **F11** to exit fullscreen, then close the window.

---

## Customization

### Change Colors

Edit `desktop_gui.py` and modify the color constants:

```python
# ROG Red (primary accent)
rog_color = '#ff0050'

# Crystal Blue (glass effect)
glass_color = '#3d8fcc'

# NVIDIA Green
nvidia_color = '#76B900'

# Google Blue
google_color = '#4285F4'

# OpenAI Teal
openai_color = '#10A37F'
```

### Add New Applications

Add to the `apps` list in `create_app_launcher()`:

```python
apps = [
    ('Terminal', '#00ff00', self.launch_terminal),
    ('Browser', '#4285F4', self.launch_browser),
    # Add your app here:
    ('My App', '#ff00ff', self.launch_my_app),
]
```

Then create the launcher function:

```python
def launch_my_app(self):
    """Launch my custom application"""
    print("Launching My App...")
    os.system('my-app-command &')
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'tkinter'"

**Solution**: Install Tkinter using your package manager

```bash
# Arch Linux
sudo pacman -S tk

# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

### "Application doesn't launch in fullscreen"

**Solution**: Press F11 to toggle fullscreen mode

### "Applications don't launch"

**Cause**: Application not installed on your system

**Solution**: Install the missing application or edit `desktop_gui.py` to remove/modify launcher

### "Graphics look different"

**Cause**: Screen resolution differences

**Solution**: The GUI adapts to screen size automatically. For best results, use 1920x1080 or higher resolution.

---

## Advanced Usage

### Run on System Startup

The installer can add Talisman to your startup applications:

```bash
./install.sh
# Answer 'y' when asked about startup applications
```

Or manually create autostart entry:

```bash
mkdir -p ~/.config/autostart
cat > ~/.config/autostart/talisman-desktop.desktop << EOF
[Desktop Entry]
Type=Application
Name=Talisman Desktop
Exec=python3 /path/to/Talisman/desktop_gui.py
X-GNOME-Autostart-enabled=true
EOF
```

### Run on Specific Display

```bash
DISPLAY=:0 python3 desktop_gui.py
```

### Run on Secondary Monitor

```bash
# Move window to secondary display after launch
# Or edit desktop_gui.py to specify monitor
```

---

## System Requirements

- **OS**: Linux (any distribution)
- **Python**: 3.6 or higher
- **Display**: X11 (Wayland may work with XWayland)
- **RAM**: Minimal (< 50MB)
- **Disk**: < 1MB
- **GPU**: Any (no 3D acceleration needed)

---

## Performance Tips

1. **Faster Startup**: The application starts instantly (< 1 second)
2. **Low Resource**: Uses minimal CPU and RAM
3. **Battery Friendly**: No continuous animations (power efficient)
4. **Responsive**: All interactions are immediate

---

## Getting Help

### Check Documentation
- `README.md` - Full documentation
- `DESIGN.md` - Design specifications
- `VISUAL_PREVIEW.md` - Visual guide

### Run Tests
```bash
python3 test_gui.py
```

### Common Issues
1. Tkinter not installed → Install via package manager
2. Applications not launching → Check if apps are installed
3. Display issues → Check X11 configuration

---

## What's Next?

After you're comfortable with the basics:

1. **Customize Colors**: Make it your own
2. **Add Applications**: Add your favorite apps
3. **Modify Layout**: Adjust positions and sizes
4. **Share**: Show off your setup!

---

## Support

For issues, suggestions, or contributions:
- GitHub: https://github.com/dALOUIMAN/Talisman
- Open an issue or pull request

---

**Enjoy your futuristic ASUS ROG Strix desktop experience!**
