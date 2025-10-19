#!/usr/bin/env python3
"""
Test script for desktop_gui.py that doesn't require a display
Tests the logic and structure of the GUI application
"""

import sys
import os

def test_imports():
    """Test that all required standard library modules are available"""
    print("Testing imports...")
    try:
        import platform
        import socket
        from pathlib import Path
        print("✓ All standard library imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_file_structure():
    """Test that all necessary files exist"""
    print("\nTesting file structure...")
    required_files = [
        'desktop_gui.py',
        'README.md',
        'requirements.txt',
        'install.sh'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            all_exist = False
    
    return all_exist

def test_executable_permissions():
    """Test that scripts have executable permissions"""
    print("\nTesting executable permissions...")
    scripts = ['desktop_gui.py', 'install.sh']
    
    all_executable = True
    for script in scripts:
        if os.path.exists(script):
            is_executable = os.access(script, os.X_OK)
            if is_executable:
                print(f"✓ {script} is executable")
            else:
                print(f"✗ {script} is not executable")
                all_executable = False
        else:
            print(f"✗ {script} not found")
            all_executable = False
    
    return all_executable

def test_syntax():
    """Test Python syntax of main script"""
    print("\nTesting Python syntax...")
    try:
        import py_compile
        py_compile.compile('desktop_gui.py', doraise=True)
        print("✓ desktop_gui.py has valid Python syntax")
        return True
    except py_compile.PyCompileError as e:
        print(f"✗ Syntax error: {e}")
        return False

def test_code_structure():
    """Test that the main script has required components"""
    print("\nTesting code structure...")
    
    with open('desktop_gui.py', 'r') as f:
        content = f.read()
    
    required_components = [
        ('ModernDesktopGUI class', 'class ModernDesktopGUI'),
        ('Main function', 'def main()'),
        ('Background layers', 'create_background_layers'),
        ('Motherboard layer', 'draw_motherboard_layer'),
        ('Crystal glass layer', 'draw_crystal_glass_layer'),
        ('App launcher', 'create_app_launcher'),
        ('System info', 'create_system_info'),
        ('Tech logos', 'draw_tech_logo_area'),
        ('ROG elements', 'draw_rog_elements'),
    ]
    
    all_present = True
    for name, component in required_components:
        if component in content:
            print(f"✓ {name} present")
        else:
            print(f"✗ {name} missing")
            all_present = False
    
    return all_present

def test_readme_content():
    """Test that README has required sections"""
    print("\nTesting README content...")
    
    with open('README.md', 'r') as f:
        content = f.read()
    
    required_sections = [
        'Features',
        'Installation',
        'Usage',
        'Requirements',
        'Layered Background Design',
        'Application Launcher',
        'ASUS ROG Strix',
    ]
    
    all_present = True
    for section in required_sections:
        if section in content:
            print(f"✓ {section} section present")
        else:
            print(f"✗ {section} section missing")
            all_present = False
    
    return all_present

def main():
    """Run all tests"""
    print("=" * 60)
    print("Talisman Desktop GUI Test Suite")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_file_structure,
        test_executable_permissions,
        test_syntax,
        test_code_structure,
        test_readme_content,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print(f"Test Results: {sum(results)}/{len(results)} passed")
    print("=" * 60)
    
    if all(results):
        print("✓ All tests passed!")
        print("\nNote: GUI functionality cannot be tested in headless environment.")
        print("To test the GUI, run the application on a system with X11 display:")
        print("  python3 desktop_gui.py")
        return 0
    else:
        print("✗ Some tests failed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
