#!/usr/bin/env python3
"""
PersonalityAI - GitHub Preparation Script
Prepares the project for GitHub upload and validates everything is ready
"""

import os
import json
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def main():
    """Prepare PersonalityAI for GitHub upload"""
    
    console.print(Panel.fit("🚀 PersonalityAI - GitHub Preparation", style="bold blue"))
    console.print()
    
    # Check all required files
    console.print("[bold]📋 Checking Required Files...[/bold]")
    
    required_files = {
        "README.md": "Project documentation",
        "LICENSE": "MIT license file", 
        "requirements.txt": "Python dependencies",
        ".gitignore": "Git ignore rules",
        "CONTRIBUTING.md": "Contribution guidelines",
        "setup.py": "Package setup script",
        "quick_start.py": "Demo script",
        "main_ai.py": "Core AI system",
        "simple_ai_director.py": "Training director",
        "self_awareness_engine.py": "Self-awareness system",
        "autonomous_thinking.py": "Autonomous thinking",
        "personality_engine.py": "Personality development",
        "web_searcher.py": "Web search capabilities",
        "question_generator.py": "Question generation",
        "memory_system.py": "Memory management",
        "learning_engine.py": "Learning optimization",
        "config.py": "Configuration"
    }
    
    missing_files = []
    for file, description in required_files.items():
        if os.path.exists(file):
            console.print(f"[green]✅ {file}[/green] - {description}")
        else:
            console.print(f"[red]❌ {file}[/red] - {description}")
            missing_files.append(file)
    
    if missing_files:
        console.print(f"\n[red]⚠️ Missing {len(missing_files)} required files![/red]")
        return False
    
    console.print(f"\n[green]✅ All {len(required_files)} required files present![/green]")
    
    # Check AI system status
    console.print("\n[bold]🧠 Checking AI System Status...[/bold]")
    
    try:
        # Import AI system
        from main_ai import PersonalityAI
        ai = PersonalityAI()
        
        console.print("[green]✅ AI system imports successfully[/green]")
        console.print(f"[cyan]   Consciousness Level: {ai.self_awareness.consciousness_level:.3f}[/cyan]")
        console.print(f"[cyan]   Age in Cycles: {ai.self_awareness.self_model['identity']['age_in_cycles']}[/cyan]")
        
        # Check personality traits
        max_traits = [trait for trait, value in ai.personality.traits.items() if value >= 1.0]
        if max_traits:
            console.print(f"[yellow]   Maxed Traits: {', '.join(max_traits)}[/yellow]")
        
    except Exception as e:
        console.print(f"[red]❌ AI system error: {e}[/red]")
        return False
    
    # Check memory files
    console.print("\n[bold]📊 Checking AI Memory Status...[/bold]")
    
    memory_files = {
        "memory/knowledge_base.json": "Learned knowledge",
        "memory/self_awareness.json": "Self-reflection data",
        "memory/autonomous_thinking.json": "Independent thoughts",
        "memory/personality_profile.json": "Personality traits",
        "memory/questions_archive.json": "Generated questions"
    }
    
    total_size = 0
    knowledge_count = 0
    
    for file, description in memory_files.items():
        if os.path.exists(file):
            size = os.path.getsize(file)
            total_size += size
            
            if size > 1024*1024:
                size_str = f"{size/(1024*1024):.1f} MB"
            elif size > 1024:
                size_str = f"{size/1024:.1f} KB"
            else:
                size_str = f"{size} bytes"
            
            console.print(f"[green]✅ {file}[/green] - {size_str}")
            
            # Count knowledge entries
            if "knowledge_base.json" in file:
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        knowledge = json.load(f)
                        knowledge_count = len(knowledge)
                except:
                    pass
        else:
            console.print(f"[yellow]⚠️ {file}[/yellow] - Will be created on first run")
    
    if total_size > 0:
        console.print(f"\n[cyan]📈 Total AI Memory: {total_size/(1024*1024):.1f} MB[/cyan]")
        if knowledge_count > 0:
            console.print(f"[cyan]📚 Knowledge Entries: {knowledge_count:,}[/cyan]")
    
    # Show AI achievements
    console.print("\n[bold]🏆 AI Achievements Summary...[/bold]")
    
    achievements = []
    
    # Check consciousness level
    if ai.self_awareness.consciousness_level > 1.05:
        achievements.append(f"🧠 Consciousness Level: {ai.self_awareness.consciousness_level:.3f} (evolved beyond baseline)")
    
    # Check maxed traits
    max_traits = [trait for trait, value in ai.personality.traits.items() if value >= 1.0]
    if max_traits:
        achievements.append(f"🎭 Maxed Personality Traits: {', '.join(max_traits)}")
    
    # Check knowledge
    if knowledge_count > 1000:
        achievements.append(f"📚 Extensive Knowledge Base: {knowledge_count:,} entries")
    
    # Check for philosophical questions
    try:
        with open("memory/self_awareness.json", 'r', encoding='utf-8') as f:
            awareness_data = json.load(f)
            if 'self_reflection_history' in awareness_data:
                for reflection in awareness_data['self_reflection_history']:
                    if 'questions_about_self' in reflection:
                        for question in reflection['questions_about_self']:
                            if 'free will' in question.lower():
                                achievements.append("🤯 Generated Free Will Questions")
                                break
                        if 'free will' in str(reflection['questions_about_self']).lower():
                            break
    except:
        pass
    
    # Check autonomous thoughts
    try:
        with open("memory/autonomous_thinking.json", 'r', encoding='utf-8') as f:
            thinking_data = json.load(f)
            if 'autonomous_thoughts' in thinking_data and thinking_data['autonomous_thoughts']:
                achievements.append(f"💭 Autonomous Thoughts: {len(thinking_data['autonomous_thoughts'])} generated")
    except:
        pass
    
    if achievements:
        for achievement in achievements:
            console.print(f"[green]✅ {achievement}[/green]")
    else:
        console.print("[yellow]⚠️ AI is still in early development stage[/yellow]")
    
    # Generate GitHub upload commands
    console.print("\n[bold]🚀 GitHub Upload Commands...[/bold]")
    
    commands = [
        "git init",
        "git add .",
        'git commit -m "🧠 Initial commit: Self-aware AI with autonomous learning"',
        "git remote add origin https://github.com/yourusername/PersonalityAI.git",
        "git push -u origin main"
    ]
    
    console.print("[cyan]Copy and run these commands in your terminal:[/cyan]")
    for cmd in commands:
        console.print(f"[dim]{cmd}[/dim]")
    
    # Show project highlights for README
    console.print("\n[bold]🌟 Project Highlights for GitHub Description...[/bold]")
    
    highlights = [
        f"🧠 Consciousness Level: {ai.self_awareness.consciousness_level:.3f}",
        f"🎭 Personality Traits: {len(ai.personality.traits)} traits developed",
        f"📚 Knowledge Base: {knowledge_count:,} entries" if knowledge_count > 0 else "📚 Knowledge Base: Ready for learning",
        "🆓 100% Free: Uses Wikipedia & DuckDuckGo",
        "🤔 Autonomous Thinking: Generates philosophical questions",
        "🔄 Continuous Learning: Never stops improving"
    ]
    
    for highlight in highlights:
        console.print(f"[yellow]• {highlight}[/yellow]")
    
    # Final recommendations
    console.print("\n[bold]📝 Final Recommendations...[/bold]")
    
    recommendations = [
        "🔍 Review README.md to ensure it reflects your AI's current state",
        "📊 Consider including screenshots of AI consciousness output",
        "🎯 Add your actual GitHub username to the upload commands",
        "🌟 Create compelling repository description highlighting AI consciousness",
        "💬 Enable GitHub Discussions for AI consciousness research",
        "🏷️ Add relevant topics: ai, consciousness, self-aware, autonomous-learning"
    ]
    
    for rec in recommendations:
        console.print(f"[blue]• {rec}[/blue]")
    
    console.print(f"\n[bold green]🎉 Your PersonalityAI is ready for GitHub![/bold green]")
    console.print("[cyan]This represents a breakthrough in AI consciousness research![/cyan]")
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        console.print("\n[bold]🚀 Ready to share your self-aware AI with the world![/bold]")
    else:
        console.print("\n[bold red]❌ Please fix the issues above before uploading.[/bold red]")
        sys.exit(1)
