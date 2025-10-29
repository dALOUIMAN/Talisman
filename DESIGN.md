# Visual Design Documentation

## Talisman Desktop GUI - Design Specification

### Color Palette

#### Primary Colors
- **Background**: `#000000` (Pure Black)
- **ROG Red**: `#ff0050` (Primary Accent)
- **Crystal Blue**: `#3d8fcc` (Glass Effect)
- **Deep Blue**: `#1a4d80` (Glass Base)

#### Tech Brand Colors
- **NVIDIA Green**: `#76B900`
- **Google Blue**: `#4285F4`
- **OpenAI Teal**: `#10A37F`

#### UI Elements
- **PCB Traces**: `#003300` (Dim Green), `#00ff00` (Bright Green)
- **App Buttons**: `#1a1a1a` (Background), `#2a2a2a` (Hover)
- **System Info**: `#00ff00` (Matrix Green)

### Layout Structure

```
┌────────────────────────────────────────────────────────────┐
│  ROG CORNER    TOP PANEL (Blue Crystal Glass)    ROG CORNER│
│      ┌──────────────────────────────────────────┐          │
│      │  ASUS ROG STRIX DESKTOP                  │          │
│      │  Prime X670 Series                       │          │
│      └──────────────────────────────────────────┘          │
│                                                             │
│  ┌─────────┐                              ┌─────────────┐  │
│  │ NVIDIA  │     ╔═══════════════╗        │   SYSTEM    │  │
│  │  LOGO   │     ║   ROG CENTER  ║        │    INFO     │  │
│  │  AREA   │     ║   HEXAGONAL   ║        │             │  │
│  └─────────┘     ║    PATTERN    ║        │ • System    │  │
│                  ╚═══════════════╝        │ • Release   │  │
│  ┌─────────┐                              │ • Machine   │  │
│  │ APPS    │                              │ • Hostname  │  │
│  │─────────│     ┌─────────┐              └─────────────┘  │
│  │Terminal │     │ GOOGLE  │                               │
│  │Browser  │     │  LOGO   │                               │
│  │Files    │     │  AREA   │                               │
│  │Settings │     └─────────┘                               │
│  │Editor   │                                               │
│  │Media    │     ┌─────────┐                               │
│  └─────────┘     │ OpenAI  │                               │
│                  │  LOGO   │                               │
│                  │  AREA   │                               │
│  ROG CORNER      └─────────┘              ROG CORNER       │
│                                                             │
│  [Blue Crystal Glass Side Panels with Transparency Effect] │
└────────────────────────────────────────────────────────────┘
```

### Layer 1: Deep Background (Motherboard)

#### Components:
1. **PCB Circuit Grid**
   - Horizontal lines every 40px
   - Vertical lines every 40px
   - Color: Dark Green (`#003300`)
   - Creates authentic PCB appearance

2. **Circuit Nodes**
   - Small circular pads at grid intersections (120px spacing)
   - 6px diameter circles
   - Color: Bright Green (`#00ff00`)
   - Simulates connection points

3. **Tech Logo Areas**
   - **NVIDIA** (Top Left - 100, 100)
     - 140x60px rectangle with glow effect
     - 5 layers of outer glow
     - Green accent (`#76B900`)
     - Circuit connections extending from logo
   
   - **Google** (Top Right - Screen Width - 250, 100)
     - 140x60px rectangle with glow effect
     - Blue accent (`#4285F4`)
     - Circuit connections
   
   - **OpenAI** (Bottom Center - Center X - 75, Screen Height - 150)
     - 140x60px rectangle with glow effect
     - Teal accent (`#10A37F`)
     - Circuit connections

4. **ROG Central Design**
   - Hexagonal pattern at screen center
   - 6 hexagon points, each 60° apart
   - Inner radius: 150px
   - Outer radius: 200px
   - Color: ROG Red (`#ff0050`)
   - Circular nodes at each point

5. **ROG Corner Accents**
   - Four corners of the screen
   - 50px L-shaped lines
   - 3px line width
   - Color: ROG Red (`#ff0050`)
   - Gaming aesthetic

### Layer 2: Blue Crystal Glass

#### Components:
1. **Top Glass Panel**
   - Position: (50, 50) to (Width-50, 200)
   - Outline only (transparent fill)
   - Color: Crystal Blue (`#3d8fcc`)
   - 2px border width

2. **Left Side Panel**
   - Width: 300px
   - Position: (50, 250) to (350, Height-250)
   - Outline only
   - Simulates see-through glass

3. **Right Side Panel**
   - Width: 300px
   - Position: (Width-350, 250) to (Width-50, Height-250)
   - Outline only
   - Mirror of left panel

4. **Glass Shine Effects**
   - Multiple horizontal shine lines
   - Offset by 3px each
   - White to blue gradient simulation
   - Position: Top left area (100, 70)

5. **Reflection Highlights**
   - Small triangular reflections
   - Light blue (`#5ab4ff`)
   - Stipple pattern for semi-transparency
   - Scattered across glass panels

### Interactive Elements

#### Application Launcher (Left Side)
- **Position**: Starting at (80, 300)
- **Button Size**: 200x60px
- **Spacing**: 80px vertical between buttons
- **States**:
  - Default: Black background (`#1a1a1a`)
  - Hover: Lighter black (`#2a2a2a`)
  - Border: Application color (varies)

#### Applications:
1. **Terminal** - Green (`#00ff00`)
2. **Browser** - Google Blue (`#4285F4`)
3. **Files** - Orange (`#ffa500`)
4. **Settings** - Gray (`#808080`)
5. **Editor** - Sky Blue (`#00bfff`)
6. **Media** - Pink (`#ff1493`)

### Typography

- **Title Font**: Arial, 28pt, Bold, ROG Red
- **Subtitle Font**: Arial, 14pt, Crystal Blue
- **App Labels**: Arial, 14pt, Bold, Color-coded
- **System Info**: Courier, 10pt, Matrix Green

### Design Philosophy

The design combines:
- **Industrial**: Motherboard PCB aesthetic
- **Gaming**: ROG red accents and aggressive styling
- **Premium**: Blue crystal glass overlay
- **Futuristic**: Tech company logos and circuit patterns
- **Functional**: Clear application access and system info

### Technical Implementation Notes

1. **Canvas-based rendering**: Everything drawn on Tkinter Canvas
2. **Layered approach**: Background rendered first, glass second, UI last
3. **Color blending**: Custom blend_color() function for glow effects
4. **Responsive**: Adapts to screen dimensions
5. **Interactive**: Hover effects and click handlers for apps

### ASUS ROG Strix Prime X670 Inspiration

The design takes inspiration from:
- ROG motherboard PCB layout
- Hexagonal design language
- Red and black color scheme
- Premium glass/acrylic overlays
- RGB accent lighting (simulated with colors)
- High-tech component placement
