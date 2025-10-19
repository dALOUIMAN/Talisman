# Talisman - Modern GUI Desktop Application

A futuristic desktop GUI application designed for Linux Arch systems, specifically optimized for ASUS ROG Strix gaming laptops.

## Features

### Layered Background Design

The application features a sophisticated two-layer background system:

1. **Deep Layer (Motherboard Aesthetic)**: 
   - Futuristic motherboard circuit pattern with PCB traces
   - Tech company logos: NVIDIA (green), Google (blue), OpenAI (teal)
   - ASUS ROG Strix design elements with hexagonal patterns
   - ROG-style corner accents in signature red
   - Circuit connections and component areas
   - Inspired by ASUS ROG Strix Prime X670 motherboard design

2. **Crystal Glass Layer**:
   - Blue crystal glass overlay effect
   - Semi-transparent panels showing the system beneath
   - Glass shine effects and reflection highlights
   - Professional modern aesthetic

### Application Launcher

Quick access to commonly used applications:
- Terminal
- Web Browser (Firefox, Chromium, Chrome)
- File Manager (Nautilus, Dolphin, Thunar, PCManFM)
- System Settings
- Text Editor (gedit, Kate, Vim, Nano)
- Media Player (VLC, MPV)

### System Information Display

Real-time system information including:
- Operating System details
- System release and machine type
- Hostname
- ASUS ROG Strix branding

## Requirements

- Python 3.6 or higher
- Tkinter (usually comes with Python)
- Linux operating system (tested on Arch Linux)
- X11 display server

## Installation

1. Clone this repository:
```bash
git clone https://github.com/dALOUIMAN/Talisman.git
cd Talisman
```

2. Make the script executable:
```bash
chmod +x desktop_gui.py
```

## Usage

### Running the Application

```bash
python3 desktop_gui.py
```

Or directly:
```bash
./desktop_gui.py
```

### Keyboard Shortcuts

- **F11**: Toggle fullscreen mode
- **ESC**: Exit fullscreen mode

### Application Launcher

Click on any application icon on the left side to launch the corresponding application. The system will automatically detect and launch the available applications on your system.

## Customization

You can customize the application by editing `desktop_gui.py`:

- **Colors**: Modify the color scheme by changing hex color values
- **Layout**: Adjust positions and sizes of UI elements
- **Applications**: Add or modify the application launcher list
- **Background**: Customize the motherboard and crystal glass effects

## Design Philosophy

This application combines the aggressive gaming aesthetic of ASUS ROG (Republic of Gamers) products with modern UI design principles:

- **Dark Theme**: Black background with vibrant accent colors
- **Gaming DNA**: ROG signature red (#ff0050) and hexagonal patterns
- **Tech Forward**: Integration of major tech brands (NVIDIA, Google, OpenAI)
- **Glass Morphism**: Blue crystal glass effect for a premium feel
- **Functionality**: Quick access to essential applications

## Compatibility

Designed for:
- ASUS ROG Strix Scar G17 laptops
- Arch Linux (and other Linux distributions)
- ASUS ROG Strix Prime X670 motherboard aesthetic

## Technical Details

- **Framework**: Python Tkinter
- **Display**: Fullscreen canvas-based rendering
- **Architecture**: Object-oriented design
- **Dependencies**: Standard library only (no external packages required)

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is part of the Talisman repository. Please refer to the repository license for usage terms.

## Screenshots

The application features:
- Futuristic motherboard circuit patterns
- Tech company logo areas with glow effects
- ROG-style hexagonal central design
- Blue crystal glass overlay panels
- Application launcher with hover effects
- System information display

## Credits

Developed for the ASUS ROG Strix gaming community and Linux enthusiasts.
