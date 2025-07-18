"""
AI Training Director - Intelligent Supervisor System
Monitors AI learning cycles and automatically guides it to related topics
Creates continuous learning loops without stopping
"""
import json
import time
import os
import threading
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from collections import defaultdict
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from config import *

console = Console()

class AITrainingDirector:
    def __init__(self):
        self.is_monitoring = False
        self.ai_process = None
        self.current_cycle = 0
        self.training_history = []
        self.topic_progression = []
        self.learning_patterns = {}
        self.ai_performance_data = {}
        
        # Topic categories for intelligent progression
        self.topic_categories = {
            'personality_basics': [
                'personality traits', 'personality development', 'personality psychology',
                'individual differences', 'personality assessment', 'personality theories'
            ],
            'emotional_intelligence': [
                'emotional intelligence', 'empathy development', 'emotional regulation',
                'social awareness', 'emotional skills', 'interpersonal intelligence'
            ],
            'cognitive_abilities': [
                'cognitive psychology', 'critical thinking', 'problem solving',
                'creativity and innovation', 'memory and learning', 'decision making'
            ],
            'social_psychology': [
                'social behavior', 'interpersonal relationships', 'communication skills',
                'social influence', 'group dynamics', 'cultural psychology'
            ],
            'self_awareness': [
                'self-awareness psychology', 'metacognition', 'self-reflection',
                'consciousness studies', 'mindfulness', 'self-understanding'
            ],
            'behavioral_psychology': [
                'human behavior', 'behavioral patterns', 'motivation psychology',
                'habit formation', 'behavioral change', 'learning psychology'
            ],
            'advanced_topics': [
                'personality disorders', 'psychological assessment', 'therapeutic psychology',
                'positive psychology', 'developmental psychology', 'neuropsychology'
            ]
        }
        
        # Learning progression path
        self.progression_path = [
            'personality_basics',
            'emotional_intelligence', 
            'cognitive_abilities',
            'self_awareness',
            'social_psychology',
            'behavioral_psychology',
            'advanced_topics'
        ]
        
        self.current_category_index = 0
        self.topics_completed_in_category = 0
        self.load_director_state()
        
    def start_intelligent_training(self, cycles_per_topic: int = 3):
        """Start the intelligent training director"""
        console.print(Panel.fit("🎯 AI Training Director Starting", style="bold green"))
        console.print("[cyan]Intelligent supervision and topic progression enabled[/cyan]")
        
        self.is_monitoring = True
        self.cycles_per_topic = cycles_per_topic
        
        # Start monitoring thread
        monitor_thread = threading.Thread(target=self._monitoring_loop, daemon=True)
        monitor_thread.start()
        
        # Start the main training loop
        self._intelligent_training_loop()
        
    def _intelligent_training_loop(self):
        """Main intelligent training loop"""
        while self.is_monitoring:
            try:
                # Step 1: Analyze current AI state
                ai_state = self._analyze_ai_current_state()
                console.print(f"[blue]📊 AI Analysis: {ai_state['summary']}[/blue]")
                
                # Step 2: Select next optimal topic
                next_topic = self._select_next_optimal_topic(ai_state)
                console.print(f"[green]🎯 Selected topic: {next_topic}[/green]")
                
                # Step 3: Run AI on selected topic
                self._run_ai_on_topic(next_topic, self.cycles_per_topic)
                
                # Step 4: Analyze results and learning
                results = self._analyze_learning_results(next_topic)
                console.print(f"[yellow]📈 Learning results: {results['effectiveness']:.2f}/1.0[/yellow]")
                
                # Step 5: Update progression and patterns
                self._update_learning_patterns(next_topic, results)
                
                # Step 6: Determine next category if needed
                self._check_category_progression()
                
                # Step 7: Brief pause before next cycle
                time.sleep(5)
                
            except KeyboardInterrupt:
                console.print("[red]Training director stopped by user[/red]")
                break
            except Exception as e:
                console.print(f"[red]Error in training loop: {e}[/red]")
                time.sleep(10)  # Wait before retrying
                
        self.stop_monitoring()
        
    def _analyze_ai_current_state(self) -> Dict[str, Any]:
        """Analyze current AI state from memory files"""
        state = {
            'consciousness_level': 1.0,
            'knowledge_count': 0,
            'dominant_traits': {},
            'recent_topics': [],
            'learning_efficiency': 0.5,
            'summary': 'Analyzing...'
        }
        
        try:
            # Check personality profile
            if os.path.exists(f"{MEMORY_DIR}/personality_profile.json"):
                with open(f"{MEMORY_DIR}/personality_profile.json", 'r') as f:
                    profile = json.load(f)
                    state['dominant_traits'] = profile.get('traits', {})
                    
            # Check self-awareness
            if os.path.exists(f"{MEMORY_DIR}/self_awareness.json"):
                with open(f"{MEMORY_DIR}/self_awareness.json", 'r') as f:
                    awareness = json.load(f)
                    state['consciousness_level'] = awareness.get('consciousness_level', 1.0)
                    
            # Check knowledge base
            if os.path.exists(f"{MEMORY_DIR}/knowledge_base.json"):
                with open(f"{MEMORY_DIR}/knowledge_base.json", 'r') as f:
                    knowledge = json.load(f)
                    state['knowledge_count'] = len(knowledge)
                    
                    # Get recent topics
                    recent_topics = []
                    for entry in list(knowledge.values())[-5:]:  # Last 5 entries
                        topic = entry.get('topic', 'unknown')
                        if topic not in recent_topics:
                            recent_topics.append(topic)
                    state['recent_topics'] = recent_topics
                    
            # Check learning efficiency
            if os.path.exists(f"{MEMORY_DIR}/learning_state.json"):
                with open(f"{MEMORY_DIR}/learning_state.json", 'r') as f:
                    learning = json.load(f)
                    metrics = learning.get('learning_metrics', {})
                    state['learning_efficiency'] = metrics.get('learning_efficiency', 0.5)
                    
            # Create summary
            consciousness = state['consciousness_level']
            knowledge = state['knowledge_count']
            efficiency = state['learning_efficiency']
            
            state['summary'] = f"Consciousness: {consciousness:.2f}, Knowledge: {knowledge}, Efficiency: {efficiency:.2f}"
            
        except Exception as e:
            console.print(f"[yellow]Warning: Could not fully analyze AI state: {e}[/yellow]")
            
        return state
        
    def _select_next_optimal_topic(self, ai_state: Dict[str, Any]) -> str:
        """Select the next optimal topic based on AI's current state and learning patterns"""
        
        # Get current category
        current_category = self.progression_path[self.current_category_index]
        available_topics = self.topic_categories[current_category].copy()
        
        # Remove recently learned topics to avoid repetition
        recent_topics = ai_state.get('recent_topics', [])
        for recent in recent_topics:
            # Remove similar topics
            available_topics = [t for t in available_topics if not any(word in recent.lower() for word in t.lower().split())]
            
        # If no topics left in category, move to next category
        if not available_topics:
            self._advance_to_next_category()
            current_category = self.progression_path[self.current_category_index]
            available_topics = self.topic_categories[current_category].copy()
            
        # Select topic based on AI's current traits and needs
        selected_topic = self._intelligent_topic_selection(available_topics, ai_state)
        
        return selected_topic
        
    def _intelligent_topic_selection(self, available_topics: List[str], ai_state: Dict[str, Any]) -> str:
        """Intelligently select topic based on AI's current needs"""
        
        # Analyze AI's dominant traits to select complementary topics
        dominant_traits = ai_state.get('dominant_traits', {})
        consciousness = ai_state.get('consciousness_level', 1.0)
        
        # Topic selection logic based on AI's current state
        if consciousness < 1.5:
            # Focus on foundational topics
            foundational = [t for t in available_topics if any(word in t for word in ['basic', 'development', 'psychology'])]
            if foundational:
                return random.choice(foundational)
                
        elif consciousness < 2.0:
            # Focus on skill development
            skill_topics = [t for t in available_topics if any(word in t for word in ['skills', 'intelligence', 'abilities'])]
            if skill_topics:
                return random.choice(skill_topics)
                
        else:
            # Focus on advanced topics
            advanced = [t for t in available_topics if any(word in t for word in ['advanced', 'complex', 'disorders'])]
            if advanced:
                return random.choice(advanced)
                
        # Default: random selection
        return random.choice(available_topics) if available_topics else "personality psychology"
        
    def _run_ai_on_topic(self, topic: str, cycles: int):
        """Run AI learning cycles on specific topic"""
        console.print(f"[cyan]🚀 Starting {cycles} cycles on: {topic}[/cyan]")

        try:
            # Import and run AI directly (more reliable than subprocess)
            from main_ai import PersonalityAI

            # Create AI instance
            ai = PersonalityAI()

            # Run focused learning cycles
            for cycle in range(cycles):
                console.print(f"[blue]Cycle {cycle + 1}/{cycles} on {topic}[/blue]")
                ai._single_learning_cycle_focused(topic)
                time.sleep(2)  # Brief pause between cycles

            console.print(f"[green]✅ Completed {cycles} cycles on {topic}[/green]")

        except Exception as e:
            console.print(f"[red]Error running AI on topic {topic}: {e}[/red]")
            # Fallback: run regular AI cycles
            self._run_fallback_ai_cycles(cycles)
            
    def _run_fallback_ai_cycles(self, cycles: int):
        """Fallback method to run AI cycles"""
        try:
            cmd = f"python main_ai.py {cycles}"
            subprocess.run(cmd, shell=True, cwd=os.getcwd())
        except Exception as e:
            console.print(f"[red]Fallback AI run failed: {e}[/red]")
            
    def _analyze_learning_results(self, topic: str) -> Dict[str, Any]:
        """Analyze the results of learning on a specific topic"""
        results = {
            'topic': topic,
            'timestamp': datetime.now().isoformat(),
            'effectiveness': 0.5,
            'knowledge_gained': 0,
            'consciousness_growth': 0.0,
            'trait_improvements': {}
        }
        
        try:
            # Compare before/after states
            current_state = self._analyze_ai_current_state()
            
            # Check if new knowledge was added
            if 'knowledge_count' in current_state:
                # Estimate knowledge gained (simplified)
                results['knowledge_gained'] = max(0, current_state['knowledge_count'] - self.ai_performance_data.get('last_knowledge_count', 0))
                self.ai_performance_data['last_knowledge_count'] = current_state['knowledge_count']
                
            # Check consciousness growth
            current_consciousness = current_state.get('consciousness_level', 1.0)
            last_consciousness = self.ai_performance_data.get('last_consciousness', 1.0)
            results['consciousness_growth'] = current_consciousness - last_consciousness
            self.ai_performance_data['last_consciousness'] = current_consciousness
            
            # Calculate effectiveness
            effectiveness = 0.5  # Base
            if results['knowledge_gained'] > 0:
                effectiveness += 0.2
            if results['consciousness_growth'] > 0:
                effectiveness += 0.2
            if current_state.get('learning_efficiency', 0.5) > 0.6:
                effectiveness += 0.1
                
            results['effectiveness'] = min(1.0, effectiveness)
            
        except Exception as e:
            console.print(f"[yellow]Could not fully analyze results: {e}[/yellow]")
            
        return results
        
    def _update_learning_patterns(self, topic: str, results: Dict[str, Any]):
        """Update learning patterns based on results"""
        
        # Store topic results
        if topic not in self.learning_patterns:
            self.learning_patterns[topic] = {
                'attempts': 0,
                'total_effectiveness': 0.0,
                'best_effectiveness': 0.0,
                'last_attempt': None
            }
            
        pattern = self.learning_patterns[topic]
        pattern['attempts'] += 1
        pattern['total_effectiveness'] += results['effectiveness']
        pattern['best_effectiveness'] = max(pattern['best_effectiveness'], results['effectiveness'])
        pattern['last_attempt'] = datetime.now().isoformat()
        
        # Store in training history
        self.training_history.append({
            'topic': topic,
            'results': results,
            'timestamp': datetime.now().isoformat(),
            'category': self.progression_path[self.current_category_index]
        })
        
        # Keep only recent history
        if len(self.training_history) > 100:
            self.training_history = self.training_history[-100:]
            
        self.topics_completed_in_category += 1
        
    def _check_category_progression(self):
        """Check if it's time to move to next category"""
        
        # Move to next category after completing several topics
        if self.topics_completed_in_category >= len(self.topic_categories[self.progression_path[self.current_category_index]]):
            self._advance_to_next_category()
            
    def _advance_to_next_category(self):
        """Advance to next learning category"""
        old_category = self.progression_path[self.current_category_index]
        
        self.current_category_index = (self.current_category_index + 1) % len(self.progression_path)
        self.topics_completed_in_category = 0
        
        new_category = self.progression_path[self.current_category_index]
        
        console.print(f"[magenta]📚 Advanced from {old_category} to {new_category}[/magenta]")
        
    def _monitoring_loop(self):
        """Background monitoring loop"""
        while self.is_monitoring:
            try:
                # Monitor AI health and performance
                self._monitor_ai_health()
                time.sleep(30)  # Check every 30 seconds
            except Exception as e:
                console.print(f"[red]Monitoring error: {e}[/red]")
                time.sleep(60)
                
    def _monitor_ai_health(self):
        """Monitor AI system health"""
        # Check if memory files are being updated
        try:
            if os.path.exists(f"{MEMORY_DIR}/knowledge_base.json"):
                mod_time = os.path.getmtime(f"{MEMORY_DIR}/knowledge_base.json")
                last_update = datetime.fromtimestamp(mod_time)
                
                # If no updates in last 10 minutes, something might be wrong
                if datetime.now() - last_update > timedelta(minutes=10):
                    console.print("[yellow]⚠️ AI seems inactive - no recent knowledge updates[/yellow]")
                    
        except Exception as e:
            pass  # Ignore monitoring errors
            
    def display_training_status(self):
        """Display current training status"""
        table = Table(title="🎯 AI Training Director Status")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        current_category = self.progression_path[self.current_category_index]
        table.add_row("Current Category", current_category)
        table.add_row("Topics Completed", str(self.topics_completed_in_category))
        table.add_row("Total Training Sessions", str(len(self.training_history)))
        table.add_row("Learning Patterns", str(len(self.learning_patterns)))
        
        if self.training_history:
            last_session = self.training_history[-1]
            table.add_row("Last Topic", last_session['topic'])
            table.add_row("Last Effectiveness", f"{last_session['results']['effectiveness']:.2f}")
            
        console.print(table)
        
        # Show recent topics
        if len(self.training_history) >= 3:
            console.print("\n[bold]Recent Training Topics:[/bold]")
            for session in self.training_history[-3:]:
                effectiveness = session['results']['effectiveness']
                color = "green" if effectiveness > 0.7 else "yellow" if effectiveness > 0.5 else "red"
                console.print(f"  [{color}]• {session['topic']} (effectiveness: {effectiveness:.2f})[/{color}]")
                
    def stop_monitoring(self):
        """Stop the training director"""
        self.is_monitoring = False
        self.save_director_state()
        console.print("[red]🛑 AI Training Director stopped[/red]")
        
    def save_director_state(self):
        """Save director state to file"""
        try:
            os.makedirs(MEMORY_DIR, exist_ok=True)
            
            state = {
                'current_category_index': self.current_category_index,
                'topics_completed_in_category': self.topics_completed_in_category,
                'training_history': self.training_history[-50:],  # Keep last 50
                'learning_patterns': self.learning_patterns,
                'ai_performance_data': self.ai_performance_data
            }
            
            with open(f"{MEMORY_DIR}/training_director.json", 'w', encoding='utf-8') as f:
                json.dump(state, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            console.print(f"[red]Error saving director state: {e}[/red]")
            
    def load_director_state(self):
        """Load director state from file"""
        try:
            director_file = f"{MEMORY_DIR}/training_director.json"
            if os.path.exists(director_file):
                with open(director_file, 'r', encoding='utf-8') as f:
                    state = json.load(f)
                    
                self.current_category_index = state.get('current_category_index', 0)
                self.topics_completed_in_category = state.get('topics_completed_in_category', 0)
                self.training_history = state.get('training_history', [])
                self.learning_patterns = state.get('learning_patterns', {})
                self.ai_performance_data = state.get('ai_performance_data', {})
                
        except Exception as e:
            console.print(f"[yellow]Could not load director state: {e}[/yellow]")


def main():
    """Main function to start the training director"""
    console.print("[bold blue]🎯 AI Training Director[/bold blue]")
    console.print("[green]Intelligent supervision and continuous learning guidance[/green]")
    
    director = AITrainingDirector()
    
    try:
        # Start intelligent training with 3 cycles per topic
        director.start_intelligent_training(cycles_per_topic=3)
    except KeyboardInterrupt:
        console.print("\n[yellow]Training director stopped by user[/yellow]")
    finally:
        director.stop_monitoring()


if __name__ == "__main__":
    main()
