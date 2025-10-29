#!/usr/bin/env python3
"""
Modern GUI Desktop Application for Linux Arch / ASUS ROG Strix
Features a layered background with tech company logos and crystal glass effect
"""

import tkinter as tk
from tkinter import ttk
import os
import sys
import subprocess
from pathlib import Path

class ModernDesktopGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ASUS ROG Strix Desktop")
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Set window to fullscreen
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.configure(bg='#000000')
        
        # Create canvas for layered background
        self.canvas = tk.Canvas(root, width=screen_width, height=screen_height, 
                               highlightthickness=0, bg='#000000')
        self.canvas.pack(fill='both', expand=True)
        
        # Draw the layered background
        self.create_background_layers()
        
        # Create application launcher area
        self.create_app_launcher()
        
        # Add system info
        self.create_system_info()
        
        # Bind ESC key to exit fullscreen
        self.root.bind('<Escape>', lambda e: self.toggle_fullscreen())
        self.root.bind('<F11>', lambda e: self.toggle_fullscreen())
        
        self.is_fullscreen = False
        self.toggle_fullscreen()
        
    def create_background_layers(self):
        """Create the two-layer background system"""
        width = self.canvas.winfo_reqwidth()
        height = self.canvas.winfo_reqheight()
        
        # Layer 1: Deep background with tech logos and motherboard aesthetic
        self.draw_motherboard_layer()
        
        # Layer 2: Blue crystal glass effect
        self.draw_crystal_glass_layer()
        
    def draw_motherboard_layer(self):
        """Draw the deepest layer: futuristic motherboard with tech logos"""
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        
        # Create motherboard circuit pattern
        # Draw PCB traces (horizontal and vertical lines)
        trace_color = '#00ff00'
        trace_dim = '#003300'
        
        # Horizontal traces
        for i in range(0, height, 40):
            self.canvas.create_line(0, i, width, i, fill=trace_dim, width=1)
        
        # Vertical traces
        for i in range(0, width, 40):
            self.canvas.create_line(i, 0, i, height, fill=trace_dim, width=1)
        
        # Draw circuit nodes
        for i in range(0, width, 120):
            for j in range(0, height, 120):
                # Small circuit pads
                self.canvas.create_oval(i-3, j-3, i+3, j+3, fill=trace_color, outline='')
        
        # Draw larger components representing tech logos areas
        # NVIDIA logo area (top left)
        self.draw_tech_logo_area(100, 100, "NVIDIA", '#76B900')
        
        # Google logo area (top right)
        self.draw_tech_logo_area(width - 250, 100, "GOOGLE", '#4285F4')
        
        # OpenAI logo area (bottom center)
        self.draw_tech_logo_area(width // 2 - 75, height - 150, "OpenAI", '#10A37F')
        
        # Draw ROG elements
        self.draw_rog_elements()
        
    def draw_tech_logo_area(self, x, y, name, color):
        """Draw a stylized tech logo area"""
        # Outer glow effect
        for i in range(5, 0, -1):
            alpha = i * 0.1
            glow_color = self.blend_color(color, '#000000', alpha)
            size = 80 + (i * 10)
            self.canvas.create_rectangle(x - size//2, y - size//2, 
                                        x + size//2, y + size//2,
                                        outline=glow_color, width=2)
        
        # Main logo box
        self.canvas.create_rectangle(x - 70, y - 30, x + 70, y + 30,
                                     fill='#111111', outline=color, width=3)
        
        # Logo text
        self.canvas.create_text(x, y, text=name, font=('Arial', 16, 'bold'),
                               fill=color)
        
        # Circuit connections
        self.canvas.create_line(x, y + 30, x, y + 60, fill=color, width=2)
        self.canvas.create_line(x - 40, y, x - 80, y, fill=color, width=2)
        self.canvas.create_line(x + 40, y, x + 80, y, fill=color, width=2)
        
    def draw_rog_elements(self):
        """Draw ASUS ROG Strix style elements"""
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        
        # ROG logo inspired design in center
        center_x = width // 2
        center_y = height // 2
        
        # Hexagonal pattern (ROG style)
        rog_color = '#ff0050'
        
        # Draw hexagonal grid around center
        for angle in range(0, 360, 60):
            import math
            x1 = center_x + 150 * math.cos(math.radians(angle))
            y1 = center_y + 150 * math.sin(math.radians(angle))
            x2 = center_x + 200 * math.cos(math.radians(angle))
            y2 = center_y + 200 * math.sin(math.radians(angle))
            
            self.canvas.create_line(x1, y1, x2, y2, fill=rog_color, width=2)
            self.canvas.create_oval(x2-5, y2-5, x2+5, y2+5, fill=rog_color, outline='')
        
        # Corner accents (ROG style)
        accent_size = 50
        self.draw_corner_accent(20, 20, accent_size, 'bottom-right', rog_color)
        self.draw_corner_accent(width - 20, 20, accent_size, 'bottom-left', rog_color)
        self.draw_corner_accent(20, height - 20, accent_size, 'top-right', rog_color)
        self.draw_corner_accent(width - 20, height - 20, accent_size, 'top-left', rog_color)
        
    def draw_corner_accent(self, x, y, size, direction, color):
        """Draw ROG-style corner accents"""
        if direction == 'bottom-right':
            self.canvas.create_line(x, y, x + size, y, fill=color, width=3)
            self.canvas.create_line(x, y, x, y + size, fill=color, width=3)
        elif direction == 'bottom-left':
            self.canvas.create_line(x, y, x - size, y, fill=color, width=3)
            self.canvas.create_line(x, y, x, y + size, fill=color, width=3)
        elif direction == 'top-right':
            self.canvas.create_line(x, y, x + size, y, fill=color, width=3)
            self.canvas.create_line(x, y, x, y - size, fill=color, width=3)
        elif direction == 'top-left':
            self.canvas.create_line(x, y, x - size, y, fill=color, width=3)
            self.canvas.create_line(x, y, x, y - size, fill=color, width=3)
        
    def draw_crystal_glass_layer(self):
        """Draw the blue crystal glass overlay layer"""
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        
        # Create semi-transparent blue overlay effect
        glass_color = '#1a4d80'
        
        # Draw glass panels with transparency effect (simulated with lighter colors)
        # Top glass panel
        self.canvas.create_rectangle(50, 50, width - 50, 200,
                                     fill='', outline='#3d8fcc', width=2)
        
        # Side panels
        panel_width = 300
        self.canvas.create_rectangle(50, 250, 50 + panel_width, height - 250,
                                     fill='', outline='#3d8fcc', width=2)
        
        self.canvas.create_rectangle(width - 50 - panel_width, 250, 
                                     width - 50, height - 250,
                                     fill='', outline='#3d8fcc', width=2)
        
        # Glass shine effects
        for i in range(5):
            alpha = (5 - i) * 0.05
            shine_color = self.blend_color('#ffffff', glass_color, alpha)
            offset = i * 3
            self.canvas.create_line(100 + offset, 70, 200 + offset, 70,
                                   fill=shine_color, width=2)
            self.canvas.create_line(100 + offset, 100, 200 + offset, 100,
                                   fill=shine_color, width=1)
        
        # Reflection highlights
        self.canvas.create_polygon(150, 100, 180, 100, 165, 130,
                                  fill='#5ab4ff', outline='', stipple='gray50')
        
    def create_app_launcher(self):
        """Create application launcher with icons"""
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        
        # Create a frame for apps (left side)
        app_frame_x = 80
        app_frame_y = 300
        
        apps = [
            ('Terminal', '#00ff00', self.launch_terminal),
            ('Browser', '#4285F4', self.launch_browser),
            ('Files', '#ffa500', self.launch_files),
            ('Settings', '#808080', self.launch_settings),
            ('Editor', '#00bfff', self.launch_editor),
            ('Media', '#ff1493', self.launch_media),
        ]
        
        for i, (app_name, color, command) in enumerate(apps):
            y_pos = app_frame_y + (i * 80)
            
            # Create app button
            app_id = self.canvas.create_rectangle(app_frame_x, y_pos,
                                                  app_frame_x + 200, y_pos + 60,
                                                  fill='#1a1a1a', outline=color, width=2)
            
            text_id = self.canvas.create_text(app_frame_x + 100, y_pos + 30,
                                             text=app_name, font=('Arial', 14, 'bold'),
                                             fill=color)
            
            # Bind click events
            self.canvas.tag_bind(app_id, '<Button-1>', lambda e, cmd=command: cmd())
            self.canvas.tag_bind(text_id, '<Button-1>', lambda e, cmd=command: cmd())
            
            # Hover effects
            self.canvas.tag_bind(app_id, '<Enter>', 
                               lambda e, id=app_id, c=color: self.canvas.itemconfig(id, fill='#2a2a2a'))
            self.canvas.tag_bind(app_id, '<Leave>', 
                               lambda e, id=app_id: self.canvas.itemconfig(id, fill='#1a1a1a'))
        
    def create_system_info(self):
        """Display system information"""
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        
        # System info panel (top right)
        info_x = width - 250
        info_y = 250
        
        # Get system information
        import platform
        import socket
        
        sys_info = [
            f"System: {platform.system()}",
            f"Release: {platform.release()}",
            f"Machine: {platform.machine()}",
            f"Hostname: {socket.gethostname()}",
            "",
            "ASUS ROG Strix",
            "Gaming Desktop",
        ]
        
        for i, info in enumerate(sys_info):
            self.canvas.create_text(info_x, info_y + (i * 25),
                                   text=info, font=('Courier', 10),
                                   fill='#00ff00', anchor='w')
        
        # Add title at top
        self.canvas.create_text(width // 2, 120,
                               text="ASUS ROG STRIX DESKTOP",
                               font=('Arial', 28, 'bold'),
                               fill='#ff0050')
        
        self.canvas.create_text(width // 2, 155,
                               text="Prime X670 Series",
                               font=('Arial', 14),
                               fill='#3d8fcc')
        
    def blend_color(self, color1, color2, alpha):
        """Blend two hex colors with alpha"""
        # Simple color blending
        c1_r = int(color1[1:3], 16)
        c1_g = int(color1[3:5], 16)
        c1_b = int(color1[5:7], 16)
        
        c2_r = int(color2[1:3], 16)
        c2_g = int(color2[3:5], 16)
        c2_b = int(color2[5:7], 16)
        
        r = int(c1_r * alpha + c2_r * (1 - alpha))
        g = int(c1_g * alpha + c2_g * (1 - alpha))
        b = int(c1_b * alpha + c2_b * (1 - alpha))
        
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def toggle_fullscreen(self):
        """Toggle fullscreen mode"""
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes('-fullscreen', self.is_fullscreen)
        
    def launch_terminal(self):
        """Launch terminal application"""
        print("Launching Terminal...")
        if os.path.exists('/usr/bin/xterm'):
            subprocess.Popen(['xterm'])
        else:
            print("Terminal not found")
        
    def launch_browser(self):
        """Launch web browser"""
        print("Launching Browser...")
        if os.path.exists('/usr/bin/firefox'):
            subprocess.Popen(['firefox'])
        elif os.path.exists('/usr/bin/chromium'):
            subprocess.Popen(['chromium'])
        elif os.path.exists('/usr/bin/google-chrome'):
            subprocess.Popen(['google-chrome'])
        else:
            print("No browser found")
        
    def launch_files(self):
        """Launch file manager"""
        print("Launching File Manager...")
        if os.path.exists('/usr/bin/nautilus'):
            subprocess.Popen(['nautilus'])
        elif os.path.exists('/usr/bin/dolphin'):
            subprocess.Popen(['dolphin'])
        elif os.path.exists('/usr/bin/thunar'):
            subprocess.Popen(['thunar'])
        elif os.path.exists('/usr/bin/pcmanfm'):
            subprocess.Popen(['pcmanfm'])
        else:
            print("No file manager found")
        
    def launch_settings(self):
        """Launch system settings"""
        print("Launching Settings...")
        if os.path.exists('/usr/bin/gnome-control-center'):
            subprocess.Popen(['gnome-control-center'])
        elif os.path.exists('/usr/bin/systemsettings5'):
            subprocess.Popen(['systemsettings5'])
        else:
            print("No settings app found")
        
    def launch_editor(self):
        """Launch text editor"""
        print("Launching Editor...")
        if os.path.exists('/usr/bin/gedit'):
            subprocess.Popen(['gedit'])
        elif os.path.exists('/usr/bin/kate'):
            subprocess.Popen(['kate'])
        elif os.path.exists('/usr/bin/vim'):
            subprocess.Popen(['vim'])
        elif os.path.exists('/usr/bin/nano'):
            subprocess.Popen(['nano'])
        else:
            print("No editor found")
        
    def launch_media(self):
        """Launch media player"""
        print("Launching Media Player...")
        if os.path.exists('/usr/bin/vlc'):
            subprocess.Popen(['vlc'])
        elif os.path.exists('/usr/bin/mpv'):
            subprocess.Popen(['mpv'])
        else:
            print("No media player found")

def main():
    """Main entry point"""
    root = tk.Tk()
    app = ModernDesktopGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
