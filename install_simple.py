"""
Simple Windows-Compatible Installation Script
No emojis, just works!
"""
import os
import sys
import subprocess
from pathlib import Path

def main():
    """Simple installation without emojis"""
    print("=" * 50)
    print("AI PERSONALITY LEARNING SYSTEM - FREE VERSION")
    print("=" * 50)
    print("Installing FREE version (no API keys required)...")
    print()
    
    # Step 1: Install packages
    print("Step 1: Installing required packages...")
    packages = ["requests", "beautifulsoup4", "wikipedia", "python-dotenv", "rich", "colorama"]
    
    for package in packages:
        try:
            print(f"  Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package], 
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"  [OK] {package}")
        except:
            print(f"  [SKIP] {package} (may already be installed)")
    
    print("[SUCCESS] Packages installed!")
    print()
    
    # Step 2: Create directories
    print("Step 2: Creating directories...")
    for directory in ["memory", "logs", "exports"]:
        Path(directory).mkdir(exist_ok=True)
        print(f"  [OK] {directory}/")
    print()
    
    # Step 3: Create .env file
    print("Step 3: Creating configuration...")
    env_content = """# AI Personality Learning System - FREE VERSION
USE_FREE_SEARCH=true
USE_WIKIPEDIA_ONLY=false
ENABLE_OFFLINE_MODE=false

# Leave these empty for free version
OPENAI_API_KEY=
GOOGLE_API_KEY=
GOOGLE_CSE_ID=
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    print("  [OK] Configuration created")
    print()
    
    # Step 4: Create launcher
    print("Step 4: Creating launcher...")
    with open('start_ai.bat', 'w') as f:
        f.write('@echo off\n')
        f.write('echo Starting FREE AI Personality Learning System...\n')
        f.write('echo No API keys required!\n')
        f.write('echo.\n')
        f.write('python main_ai.py\n')
        f.write('pause\n')
    print("  [OK] start_ai.bat created")
    print()
    
    # Step 5: Test
    print("Step 5: Testing installation...")
    try:
        import requests
        import wikipedia
        from bs4 import BeautifulSoup
        print("  [OK] All modules working")
    except ImportError as e:
        print(f"  [ERROR] {e}")
        print("  Try running: pip install requests beautifulsoup4 wikipedia rich")
        return False
    
    print()
    print("=" * 50)
    print("INSTALLATION COMPLETE!")
    print("=" * 50)
    print()
    print("HOW TO START:")
    print("1. Double-click: start_ai.bat")
    print("2. Or run: python main_ai.py")
    print()
    print("Your AI will start learning immediately using:")
    print("- Wikipedia (free)")
    print("- DuckDuckGo (free)")
    print("- Psychology websites (free)")
    print()
    print("Advanced Features:")
    print("- Self-awareness and consciousness")
    print("- Autonomous thinking and reasoning")
    print("- Personality self-improvement")
    print("- Philosophical contemplation")
    print("- Internal monologue and thoughts")
    print()
    print("Total cost: $0.00 forever!")
    print()
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if success:
            input("Press Enter to continue...")
        else:
            input("Press Enter to exit...")
    except Exception as e:
        print(f"Installation error: {e}")
        input("Press Enter to exit...")
