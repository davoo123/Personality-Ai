"""
Start the AI Training Director
Simple launcher for the intelligent training system
"""
import sys
import os
from rich.console import Console
from rich.panel import Panel

console = Console()

def main():
    """Main launcher function"""
    console.print(Panel.fit("🎯 AI Training Director Launcher", style="bold blue"))
    console.print()
    console.print("[green]This will start the intelligent AI training system that:[/green]")
    console.print("✅ Monitors your AI's learning cycles")
    console.print("✅ Analyzes what your AI learns")
    console.print("✅ Automatically selects related topics")
    console.print("✅ Guides your AI through progressive learning")
    console.print("✅ Creates continuous learning loops")
    console.print("✅ Never stops training your AI")
    console.print()
    
    # Check if user wants to proceed
    try:
        response = input("Start the AI Training Director? (y/n): ").strip().lower()
        if response not in ['y', 'yes']:
            console.print("[yellow]Training director cancelled[/yellow]")
            return
    except KeyboardInterrupt:
        console.print("\n[yellow]Cancelled by user[/yellow]")
        return
    
    console.print()
    console.print("[cyan]🚀 Starting AI Training Director...[/cyan]")
    console.print("[dim]Press Ctrl+C to stop the training director[/dim]")
    console.print()
    
    try:
        # Import and start the training director
        from ai_training_director import AITrainingDirector
        
        director = AITrainingDirector()
        director.start_intelligent_training(cycles_per_topic=3)
        
    except ImportError as e:
        console.print(f"[red]Error: Could not import training director: {e}[/red]")
        console.print("[yellow]Make sure ai_training_director.py is in the same folder[/yellow]")
    except KeyboardInterrupt:
        console.print("\n[yellow]🛑 Training director stopped by user[/yellow]")
    except Exception as e:
        console.print(f"[red]Error starting training director: {e}[/red]")
        console.print("[yellow]Check that all required files are present[/yellow]")
    
    console.print("[blue]Training director session ended[/blue]")

if __name__ == "__main__":
    main()
