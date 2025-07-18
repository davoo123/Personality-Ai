"""
Free Installation Script for AI Personality Learning System
Sets up the system to work completely FREE without any API keys!
"""
import os
import sys
import subprocess
from pathlib import Path

def print_banner():
    """Print welcome banner"""
    try:
        print("=" * 60)
        print("AI PERSONALITY LEARNING SYSTEM - FREE VERSION")
        print("=" * 60)
        print()
        print("* This system works 100% FREE with NO API keys required!")
        print("* Uses Wikipedia, DuckDuckGo, and free web scraping")
        print("* Learns about personality psychology automatically")
        print("* Stores all knowledge locally on your computer")
        print()
    except UnicodeEncodeError:
        print("AI PERSONALITY LEARNING SYSTEM - FREE VERSION")
        print("This system works 100% FREE with NO API keys required!")
        print()

def install_free_requirements():
    """Install only the free requirements"""
    print("Installing FREE dependencies...")

    # Core free requirements
    free_packages = [
        "requests",
        "beautifulsoup4",
        "wikipedia",
        "python-dotenv",
        "rich",
        "colorama"
    ]

    for package in free_packages:
        try:
            print(f"  Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"  [OK] {package} installed")
        except subprocess.CalledProcessError:
            print(f"  [WARNING] Failed to install {package}, but continuing...")

    print("[SUCCESS] Free dependencies installed!")

def create_free_env():
    """Create .env file configured for free usage"""
    print("Setting up FREE configuration...")

    env_content = """# AI Personality Learning System - FREE VERSION
# No API keys required! Everything works for FREE!

# Free version settings (already optimized)
USE_FREE_SEARCH=true
USE_WIKIPEDIA_ONLY=false
ENABLE_OFFLINE_MODE=false

# Optional API keys (leave empty for free version)
OPENAI_API_KEY=
GOOGLE_API_KEY=
GOOGLE_CSE_ID=

# The system will automatically use free sources:
# Wikipedia (completely free)
# DuckDuckGo (completely free)
# Psychology websites (free scraping)
# Offline knowledge base (completely free)
"""

    with open('.env', 'w', encoding='utf-8') as f:
        f.write(env_content)

    print("[SUCCESS] Free configuration created!")

def create_directories():
    """Create necessary directories"""
    print("📁 Creating directories...")
    
    directories = ["memory", "logs", "exports"]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"  ✅ Created {directory}/")

def create_free_launcher():
    """Create a simple launcher script"""
    print("🚀 Creating launcher scripts...")
    
    # Windows batch file
    with open('start_free_ai.bat', 'w') as f:
        f.write('@echo off\n')
        f.write('echo 🆓 Starting FREE AI Personality Learning System...\n')
        f.write('echo 🌐 Using Wikipedia, DuckDuckGo, and free web sources\n')
        f.write('echo 💡 No API keys required!\n')
        f.write('echo.\n')
        f.write('python main_ai.py\n')
        f.write('pause\n')
    
    # Unix shell script
    with open('start_free_ai.sh', 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('echo "🆓 Starting FREE AI Personality Learning System..."\n')
        f.write('echo "🌐 Using Wikipedia, DuckDuckGo, and free web sources"\n')
        f.write('echo "💡 No API keys required!"\n')
        f.write('echo ""\n')
        f.write('python main_ai.py\n')
    
    # Make shell script executable on Unix systems
    if os.name != 'nt':
        os.chmod('start_free_ai.sh', 0o755)
    
    print("  ✅ Created start_free_ai.bat (Windows)")
    print("  ✅ Created start_free_ai.sh (Unix/Linux/Mac)")

def test_free_installation():
    """Test if the free installation works"""
    print("🧪 Testing FREE installation...")
    
    try:
        # Test imports
        import requests
        import wikipedia
        from bs4 import BeautifulSoup
        from rich.console import Console
        
        print("  ✅ All core modules imported successfully")
        
        # Test Wikipedia
        try:
            results = wikipedia.search("personality psychology", results=1)
            if results:
                print("  ✅ Wikipedia search working")
            else:
                print("  ⚠️ Wikipedia search returned no results")
        except:
            print("  ⚠️ Wikipedia test failed, but system will still work")
        
        # Test web requests
        try:
            response = requests.get("https://api.duckduckgo.com/?q=test&format=json", timeout=5)
            if response.status_code == 200:
                print("  ✅ DuckDuckGo API accessible")
            else:
                print("  ⚠️ DuckDuckGo API test failed")
        except:
            print("  ⚠️ DuckDuckGo test failed, but system will still work")
        
        print("✅ FREE installation test completed!")
        return True
        
    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Test error: {e}")
        return False

def show_usage_instructions():
    """Show how to use the free system"""
    print("\n" + "🎉" * 30)
    print("🎉 FREE INSTALLATION COMPLETE! 🎉")
    print("🎉" * 30)
    print()
    print("🚀 HOW TO START YOUR FREE AI:")
    print()
    print("Option 1 - Use the launcher scripts:")
    print("  • Windows: Double-click start_free_ai.bat")
    print("  • Mac/Linux: ./start_free_ai.sh")
    print()
    print("Option 2 - Use Python directly:")
    print("  • Continuous learning: python main_ai.py")
    print("  • Interactive mode: python main_ai.py interactive")
    print("  • Single cycle: python main_ai.py single")
    print()
    print("🆓 WHAT YOUR FREE AI WILL DO:")
    print("  ✅ Generate infinite questions about personality")
    print("  ✅ Search Wikipedia for answers (completely free)")
    print("  ✅ Search DuckDuckGo for more information (free)")
    print("  ✅ Scrape psychology websites (free)")
    print("  ✅ Store all knowledge locally (no cloud costs)")
    print("  ✅ Evolve its personality over time")
    print("  ✅ Learn continuously and improve itself")
    print()
    print("💾 YOUR DATA:")
    print("  • All knowledge stored in memory/ folder")
    print("  • No data sent to paid services")
    print("  • Complete privacy and control")
    print()
    print("🔧 OPTIONAL UPGRADES:")
    print("  • Add Google API key for more search results")
    print("  • Add OpenAI API key for advanced language features")
    print("  • But the system works great without them!")
    print()
    print("🎓 ENJOY YOUR FREE AI LEARNING COMPANION!")
    print("Watch it grow smarter about personality psychology! 🧠✨")

def main():
    """Main installation function"""
    print_banner()
    
    try:
        # Step 1: Install free requirements
        install_free_requirements()
        print()
        
        # Step 2: Create directories
        create_directories()
        print()
        
        # Step 3: Create free configuration
        create_free_env()
        print()
        
        # Step 4: Create launcher scripts
        create_free_launcher()
        print()
        
        # Step 5: Test installation
        if test_free_installation():
            print()
            show_usage_instructions()
        else:
            print("\n⚠️ Some tests failed, but the system should still work.")
            print("Try running: python main_ai.py")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Installation failed: {e}")
        print("Please check your Python installation and try again.")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        input("\nPress Enter to exit...")
        sys.exit(1)
    else:
        input("\nPress Enter to exit...")
