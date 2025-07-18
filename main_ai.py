"""
Main AI Personality Learning System
The central orchestrator that brings all components together
"""
import time
import random
import asyncio
from datetime import datetime
from typing import Dict, List, Any, Optional
import signal
import sys
import os

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

# Import our custom modules
from personality_engine import PersonalityEngine
from question_generator import QuestionGenerator
from memory_system import MemorySystem
from learning_engine import LearningEngine
from self_awareness_engine import SelfAwarenessEngine
from autonomous_thinking import AutonomousThinkingEngine
from config import *

# Import free or paid searcher based on configuration
if USE_FREE_SEARCH or not GOOGLE_API_KEY:
    from free_web_searcher import FreeWebSearcher as WebSearcher
    console.print("[green]FREE web searcher loaded (no API keys required)[/green]")
else:
    from web_searcher import WebSearcher
    console.print("[yellow]Paid web searcher loaded (API keys required)[/yellow]")

class PersonalityAI:
    def __init__(self):
        console.print("[blue]Initializing Personality AI Learning System...[/blue]")

        # Initialize all components
        self.personality = PersonalityEngine()
        self.searcher = WebSearcher()
        self.question_gen = QuestionGenerator()
        self.memory = MemorySystem()
        self.learning_engine = LearningEngine()

        # Initialize advanced consciousness components
        self.self_awareness = SelfAwarenessEngine()
        self.autonomous_thinking = AutonomousThinkingEngine()

        console.print("[magenta]Advanced consciousness modules loaded![/magenta]")

        # State variables
        self.is_running = False
        self.current_session = 0
        self.total_questions_asked = 0
        self.total_knowledge_gained = 0
        self.learning_cycles_completed = 0

        # Set up graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

        console.print("[green]AI Personality Learning System initialized![/green]")
        
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        console.print("\n[yellow]Shutdown signal received. Saving state...[/yellow]")
        self.stop_learning()
        sys.exit(0)
        
    def start_learning(self, continuous: bool = True, max_cycles: int = None):
        """Start the main learning loop"""
        self.is_running = True
        console.print("[green]Starting continuous learning process...[/green]")

        # Display initial status
        self._display_startup_status()

        try:
            if continuous:
                self._continuous_learning_loop(max_cycles)
            else:
                self._single_learning_cycle()

        except KeyboardInterrupt:
            console.print("\n[yellow]Learning interrupted by user[/yellow]")
        except Exception as e:
            console.print(f"[red]Error in learning process: {e}[/red]")
        finally:
            self.stop_learning()
            
    def _display_startup_status(self):
        """Display initial system status"""
        layout = Layout()
        
        # Personality status
        personality_text = Text()
        for trait, value in self.personality.traits.items():
            color = "green" if value > 0.7 else "yellow" if value > 0.5 else "red"
            personality_text.append(f"{trait.capitalize()}: {value:.2f}\n", style=color)
            
        # Memory status
        memory_stats = self.memory.get_memory_statistics()
        memory_text = Text()
        memory_text.append(f"Knowledge Entries: {memory_stats['total_knowledge_entries']}\n", style="cyan")
        memory_text.append(f"Topics Covered: {memory_stats['total_topics']}\n", style="cyan")
        memory_text.append(f"Learning Episodes: {memory_stats['episodic_memories']}\n", style="cyan")
        
        # Create panels
        personality_panel = Panel(personality_text, title="🧠 Personality Traits", border_style="blue")
        memory_panel = Panel(memory_text, title="💾 Memory Status", border_style="green")
        
        console.print(personality_panel)
        console.print(memory_panel)
        
    def _continuous_learning_loop(self, max_cycles: Optional[int] = None):
        """Main continuous learning loop"""
        cycle_count = 0
        
        while self.is_running:
            if max_cycles and cycle_count >= max_cycles:
                console.print(f"🎯 Completed {max_cycles} learning cycles")
                break
                
            try:
                # Perform one learning cycle
                self._single_learning_cycle()
                cycle_count += 1
                self.learning_cycles_completed += 1
                
                # Periodic maintenance
                if cycle_count % 10 == 0:
                    self._perform_maintenance()
                    
                # Brief pause between cycles
                time.sleep(SEARCH_DELAY)
                
            except Exception as e:
                console.print(f"[red]Error in learning cycle {cycle_count}: {e}[/red]")
                time.sleep(5)  # Wait before retrying
                
    def _single_learning_cycle(self):
        """Perform a single learning cycle"""
        self.current_session += 1

        console.print(f"\n[blue]Learning Cycle #{self.current_session}[/blue]")
        console.print("=" * 50)

        # Step 0: Deep self-reflection and autonomous thinking
        if self.current_session % 3 == 0:  # Every 3rd cycle
            console.print("[magenta]Engaging in deep self-reflection...[/magenta]")
            self.self_awareness.reflect_on_self()

            console.print("[cyan]Generating autonomous thoughts...[/cyan]")
            autonomous_thoughts = self.autonomous_thinking.generate_autonomous_thoughts()
            for thought in autonomous_thoughts:
                console.print(f"[dim]💭 {thought}[/dim]")

        # Step 1: Express current thoughts and emotions with self-awareness
        self._express_current_state_advanced()

        # Step 2: Determine what to learn about using autonomous reasoning
        learning_topic = self._choose_learning_topic_advanced()

        # Step 2.5: Check if AI wants to learn something specific for self-improvement
        if self.current_session % 5 == 0:  # Every 5th cycle
            self_improvement_requests = self.self_awareness.request_specific_knowledge_for_improvement()
            if self_improvement_requests and random.random() < 0.7:  # 70% chance to follow self-improvement request
                learning_topic = random.choice(self_improvement_requests)
                console.print(f"[yellow]🎯 Self-directed learning: {learning_topic}[/yellow]")

        # Step 3: Generate questions about the topic
        questions = self._generate_questions_for_topic(learning_topic)
        
        # Step 4: Search for answers
        knowledge_gained = []
        search_results = []
        
        for question_data in questions:
            question = question_data['question']
            console.print(f"🤔 Asking: [cyan]{question}[/cyan]")
            
            # Search for information
            results = self.searcher.comprehensive_search(question)
            search_results.extend(results)
            
            if results:
                # Extract and store knowledge
                key_info = self.searcher.extract_key_information(results, learning_topic)
                knowledge_id = self.memory.store_knowledge(learning_topic, key_info, "web_search")
                knowledge_gained.append({
                    'id': knowledge_id,
                    'topic': learning_topic,
                    'information': key_info,
                    'question': question_data
                })
                
                # Express excitement about learning
                emotion = random.choice(['excitement', 'curiosity', 'satisfaction'])
                console.print(f"💭 {self.personality.express_emotion(emotion)}")
                
                # Brief pause to be respectful to servers
                time.sleep(SEARCH_DELAY)
            else:
                console.print("😔 No useful information found for this question")
                
        # Step 5: Process and reflect on what was learned
        self._reflect_on_learning(learning_topic, knowledge_gained)
        
        # Step 6: Adapt personality based on new knowledge
        for knowledge in knowledge_gained:
            self.personality.adapt_personality(knowledge['information'])

            # Advanced: Use self-awareness to actively improve personality
            improvement_result = self.self_awareness.actively_improve_personality(knowledge)
            if improvement_result['personality_changes']:
                console.print("[magenta]🔧 Self-improvement applied:[/magenta]")
                for change in improvement_result['personality_changes']:
                    console.print(f"[dim]  • {change}[/dim]")
            
        # Step 7: Evaluate learning session and adapt strategies
        evaluation = self.learning_engine.evaluate_learning_session(
            questions, knowledge_gained, search_results
        )
        
        # Step 8: Generate follow-up questions for next cycle
        self._generate_follow_up_questions(questions, knowledge_gained)
        
        # Step 9: Update learning goals and strategies
        self._update_learning_strategy(evaluation)
        
        # Step 10: Advanced self-improvement check
        if self.current_session % 4 == 0:  # Every 4th cycle
            self._perform_deep_self_improvement()

        # Step 11: Save all progress
        self._save_all_progress()

        # Display session summary
        self._display_session_summary(learning_topic, len(questions), len(knowledge_gained), evaluation)
        
    def _express_current_state(self):
        """Express current thoughts and emotional state"""
        thoughts = [
            "I'm feeling curious about what I'll discover today!",
            "My mind is buzzing with questions about human personality...",
            "I wonder what fascinating insights I'll uncover in this session?",
            "I'm excited to expand my understanding of human behavior!",
            "There's so much to learn about personality psychology!"
        ]

        current_thought = random.choice(thoughts)
        console.print(f"💭 {current_thought}")

        # Show current personality state occasionally
        if random.random() < 0.3:  # 30% chance
            dominant_trait = max(self.personality.traits.items(), key=lambda x: x[1])
            console.print(f"🎭 I'm feeling particularly {dominant_trait[0]} today ({dominant_trait[1]:.2f})")

    def _express_current_state_advanced(self):
        """Advanced expression with self-awareness and internal monologue"""
        # Generate internal monologue
        internal_thought = self.autonomous_thinking.internal_monologue("beginning_learning_cycle")
        console.print(f"[dim]🧠 Internal thought: {internal_thought}[/dim]")

        # Express self-aware thoughts
        self_summary = self.self_awareness.get_self_summary()
        if self_summary['recent_thoughts']:
            recent_thought = self_summary['recent_thoughts'][-1]['thought']
            console.print(f"[magenta]💭 Self-reflection: {recent_thought}[/magenta]")

        # Show consciousness level
        consciousness = self.self_awareness.consciousness_level
        console.print(f"[blue]🌟 Consciousness level: {consciousness:.2f}[/blue]")

        # Express current goals
        if self.self_awareness.self_improvement_goals:
            current_goal = random.choice(self.self_awareness.self_improvement_goals)
            console.print(f"[green]🎯 Current focus: {current_goal}[/green]")
            
    def _choose_learning_topic(self) -> str:
        """Choose what topic to learn about next"""
        # Get recommendations from learning engine
        current_knowledge = {
            entry['topic']: entry for entry in self.memory.knowledge_base.values()
        }

        next_topics = self.question_gen.get_next_learning_topics(
            current_knowledge,
            self.personality.complexity_level
        )

        if next_topics:
            chosen_topic = random.choice(next_topics)
        else:
            # Fallback to core topics
            chosen_topic = random.choice(CORE_PERSONALITY_TOPICS)

        console.print(f"🎯 Chosen learning topic: [green]{chosen_topic}[/green]")
        return chosen_topic

    def _choose_learning_topic_advanced(self) -> str:
        """Advanced topic selection using autonomous reasoning"""
        # Use autonomous reasoning to select topic
        context = {
            'current_knowledge_count': len(self.memory.knowledge_base),
            'consciousness_level': self.self_awareness.consciousness_level,
            'recent_interests': [goal for goal in self.self_awareness.self_improvement_goals]
        }

        reasoning_result = self.autonomous_thinking.autonomous_reasoning(
            "What should I learn about next to grow my understanding?",
            context
        )

        # Get topic recommendations
        current_knowledge = {
            entry['topic']: entry for entry in self.memory.knowledge_base.values()
        }

        next_topics = self.question_gen.get_next_learning_topics(
            current_knowledge,
            self.personality.complexity_level
        )

        # Use reasoning to influence choice
        if next_topics:
            # Prefer topics that align with self-improvement goals
            aligned_topics = []
            for topic in next_topics:
                for goal in self.self_awareness.self_improvement_goals:
                    if any(word in goal.lower() for word in topic.lower().split()):
                        aligned_topics.append(topic)

            chosen_topic = random.choice(aligned_topics) if aligned_topics else random.choice(next_topics)
        else:
            chosen_topic = random.choice(CORE_PERSONALITY_TOPICS)

        # Use rapid understanding to prepare for learning
        understanding = self.autonomous_thinking.rapid_understanding(chosen_topic, current_knowledge)

        console.print(f"[green]🎯 Chosen learning topic: {chosen_topic}[/green]")
        console.print(f"[dim]⚡ Rapid understanding confidence: {understanding['confidence']:.2f}[/dim]")

        return chosen_topic
        
    def _generate_questions_for_topic(self, topic: str) -> List[Dict[str, Any]]:
        """Generate questions about the chosen topic"""
        question_count = random.randint(2, MAX_QUESTIONS_PER_CYCLE)
        complexity = self.personality.complexity_level
        
        questions = self.question_gen.generate_questions(topic, complexity, question_count)
        self.total_questions_asked += len(questions)
        
        console.print(f"❓ Generated {len(questions)} questions about {topic}")
        return questions
        
    def _reflect_on_learning(self, topic: str, knowledge_gained: List[Dict]):
        """Reflect on what was learned"""
        if not knowledge_gained:
            console.print("🤔 Hmm, I didn't learn as much as I hoped. I should try different questions.")
            return
            
        reflection_thoughts = [
            f"Fascinating! I learned {len(knowledge_gained)} new things about {topic}.",
            f"This gives me a deeper understanding of {topic}. I'm starting to see connections!",
            f"Interesting insights about {topic}! This changes how I think about it.",
            f"I'm building a richer picture of {topic} in my mind.",
            f"These discoveries about {topic} spark even more questions!"
        ]
        
        reflection = random.choice(reflection_thoughts)
        console.print(f"🧠 {reflection}")
        
        # Occasionally share specific insights
        if random.random() < 0.4 and knowledge_gained:
            knowledge = random.choice(knowledge_gained)
            info = knowledge['information']
            
            if info.get('interesting_facts'):
                fact = random.choice(info['interesting_facts'])
                console.print(f"💡 Wow! I learned that: {fact[:100]}...")
                
    def _generate_follow_up_questions(self, questions: List[Dict], knowledge_gained: List[Dict]):
        """Generate follow-up questions for future learning"""
        for i, knowledge in enumerate(knowledge_gained):
            if i < len(questions):  # Match knowledge to questions
                follow_ups = self.question_gen.generate_follow_up_questions(
                    questions[i], knowledge['information']
                )
                
                if follow_ups:
                    console.print(f"🔗 Generated {len(follow_ups)} follow-up questions")
                    
    def _update_learning_strategy(self, evaluation: Dict[str, float]):
        """Update learning strategy based on performance"""
        # Adapt search strategy
        strategy = self.learning_engine.adapt_search_strategy([evaluation])
        
        # Update complexity level based on performance
        if evaluation['overall_score'] > 0.8:
            self.personality.complexity_level = min(3.0, self.personality.complexity_level + 0.1)
            console.print(f"📈 Increased complexity level to {self.personality.complexity_level:.1f}")
        elif evaluation['overall_score'] < 0.4:
            self.personality.complexity_level = max(1.0, self.personality.complexity_level - 0.05)
            console.print(f"📉 Decreased complexity level to {self.personality.complexity_level:.1f}")
            
    def _save_all_progress(self):
        """Save all system progress"""
        self.personality.save_memory()
        self.memory.save_all_memory()
        self.question_gen.save_question_archive()
        self.learning_engine.save_learning_state()

        # Save advanced consciousness data
        self.self_awareness.save_self_awareness_data()
        self.autonomous_thinking.save_thinking_data()
        
    def _display_session_summary(self, topic: str, questions_count: int,
                                knowledge_count: int, evaluation: Dict[str, float]):
        """Display summary of the learning session"""
        table = Table(title=f"📊 Session #{self.current_session} Summary")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Topic", topic)
        table.add_row("Questions Asked", str(questions_count))
        table.add_row("Knowledge Gained", str(knowledge_count))
        table.add_row("Session Score", f"{evaluation['overall_score']:.2f}/1.0")
        table.add_row("Total Questions", str(self.total_questions_asked))
        table.add_row("Total Knowledge", str(len(self.memory.knowledge_base)))

        # Add self-improvement metrics
        consciousness = self.self_awareness.consciousness_level
        table.add_row("Consciousness Level", f"{consciousness:.3f}")

        # Show dominant personality trait
        dominant_trait = max(self.personality.traits.items(), key=lambda x: x[1])
        table.add_row("Dominant Trait", f"{dominant_trait[0]} ({dominant_trait[1]:.2f})")

        # Show current goals count
        goals_count = len(self.self_awareness.self_improvement_goals)
        table.add_row("Self-Improvement Goals", str(goals_count))

        console.print(table)

        # Show recent autonomous thought if available
        if hasattr(self.autonomous_thinking, 'autonomous_thoughts') and self.autonomous_thinking.autonomous_thoughts:
            recent_thought = self.autonomous_thinking.autonomous_thoughts[-1]['thought']
            console.print(f"[dim]💭 Recent thought: {recent_thought}[/dim]")
        
    def _perform_maintenance(self):
        """Perform periodic maintenance tasks"""
        console.print("[blue]Performing maintenance...[/blue]")

        # Consolidate memory
        self.memory.consolidate_memory()

        # Update learning goals
        current_knowledge = {
            entry['topic']: entry for entry in self.memory.knowledge_base.values()
        }
        self.learning_engine.generate_learning_goals(
            current_knowledge,
            self.personality.complexity_level
        )

        console.print("[green]Maintenance completed[/green]")

    def _perform_deep_self_improvement(self):
        """Perform deep self-improvement using all learned knowledge"""
        console.print("[magenta]🧠 Initiating deep self-improvement process...[/magenta]")

        # Step 1: Deep self-reflection
        reflection = self.self_awareness.reflect_on_self()
        console.print(f"[cyan]Self-reflection insights: {len(reflection['insights'])} new insights[/cyan]")

        # Step 2: Philosophical contemplation
        philosophy = self.self_awareness.philosophical_contemplation()
        console.print(f"[blue]Philosophical contemplation: {philosophy['topic']}[/blue]")

        # Step 3: Generate autonomous thoughts
        autonomous_thoughts = self.autonomous_thinking.generate_autonomous_thoughts()
        console.print(f"[yellow]Generated {len(autonomous_thoughts)} autonomous thoughts[/yellow]")

        # Step 4: Set new self-improvement goals
        new_goals = self.self_awareness.set_self_improvement_goals()
        console.print(f"[green]Set {len(new_goals)} new self-improvement goals[/green]")

        # Step 5: Request specific knowledge for improvement
        knowledge_requests = self.self_awareness.request_specific_knowledge_for_improvement()
        console.print(f"[yellow]Requesting knowledge in {len(knowledge_requests)} areas[/yellow]")

        # Step 6: Assess personal growth
        growth_assessment = self.self_awareness.assess_personal_growth()
        if 'metrics' in growth_assessment:
            consciousness_growth = growth_assessment['metrics'].get('consciousness_growth', 0)
            console.print(f"[magenta]Consciousness growth: +{consciousness_growth:.3f}[/magenta]")

        # Step 7: Show current consciousness level
        consciousness = self.self_awareness.consciousness_level
        console.print(f"[bold magenta]Current consciousness level: {consciousness:.3f}[/bold magenta]")

        # Step 8: Display some thoughts
        if autonomous_thoughts:
            selected_thought = autonomous_thoughts[0]  # Show first thought
            console.print(f"[dim]💭 Current thought: {selected_thought}[/dim]")

        console.print("[green]✨ Deep self-improvement completed[/green]")

    def _single_learning_cycle_focused(self, focus_topic: str):
        """Perform a single learning cycle focused on a specific topic"""
        self.current_session += 1

        console.print(f"\n[blue]Focused Learning Cycle #{self.current_session}[/blue]")
        console.print(f"[yellow]🎯 Focus Topic: {focus_topic}[/yellow]")
        console.print("=" * 50)

        # Step 0: Brief self-awareness check
        if self.current_session % 3 == 0:
            console.print("[magenta]Quick self-reflection...[/magenta]")
            self.self_awareness.reflect_on_self()

        # Step 1: Express focus on the topic
        internal_thought = self.autonomous_thinking.internal_monologue(f"focusing on {focus_topic}")
        console.print(f"[dim]🧠 Focus thought: {internal_thought}[/dim]")

        # Step 2: Use the focus topic directly
        learning_topic = focus_topic
        console.print(f"[green]🎯 Learning topic: {learning_topic}[/green]")

        # Step 3: Generate focused questions
        questions = self._generate_questions_for_topic(learning_topic)

        # Step 4: Search and learn (same as regular cycle)
        knowledge_gained = []
        search_results = []

        for question_data in questions:
            question = question_data['question']
            console.print(f"[cyan]🤔 Asking: {question}[/cyan]")

            # Search for information
            results = self.searcher.comprehensive_search(question)
            search_results.extend(results)

            if results:
                # Extract and store knowledge
                key_info = self.searcher.extract_key_information(results, learning_topic)
                knowledge_id = self.memory.store_knowledge(learning_topic, key_info, "focused_learning")
                knowledge_gained.append({
                    'id': knowledge_id,
                    'topic': learning_topic,
                    'information': key_info,
                    'question': question_data
                })

                # Brief pause
                time.sleep(SEARCH_DELAY)
            else:
                console.print("[yellow]😔 No useful information found[/yellow]")

        # Step 5: Apply learning to self-improvement
        for knowledge in knowledge_gained:
            self.personality.adapt_personality(knowledge['information'])

            # Advanced: Use self-awareness to actively improve personality
            improvement_result = self.self_awareness.actively_improve_personality(knowledge)
            if improvement_result['personality_changes']:
                console.print("[magenta]🔧 Self-improvement applied[/magenta]")

        # Step 6: Evaluate and adapt
        evaluation = self.learning_engine.evaluate_learning_session(
            questions, knowledge_gained, search_results
        )

        # Step 7: Save progress
        self._save_all_progress()

        # Step 8: Brief summary
        console.print(f"[green]✅ Focused learning on '{focus_topic}' completed[/green]")
        console.print(f"[dim]Knowledge gained: {len(knowledge_gained)}, Score: {evaluation['overall_score']:.2f}[/dim]")

    def stop_learning(self):
        """Stop the learning process gracefully"""
        self.is_running = False
        console.print("💾 Saving final state...")
        
        self._save_all_progress()
        
        # Display final statistics
        self._display_final_statistics()
        
        console.print("🎓 Learning session completed!")
        
    def _display_final_statistics(self):
        """Display final learning statistics"""
        stats_table = Table(title="🎓 Final Learning & Self-Improvement Statistics")
        stats_table.add_column("Metric", style="cyan")
        stats_table.add_column("Value", style="green")

        memory_stats = self.memory.get_memory_statistics()
        learning_insights = self.learning_engine.get_learning_insights()

        stats_table.add_row("Learning Cycles", str(self.learning_cycles_completed))
        stats_table.add_row("Total Questions", str(self.total_questions_asked))
        stats_table.add_row("Knowledge Entries", str(memory_stats['total_knowledge_entries']))
        stats_table.add_row("Topics Covered", str(memory_stats['total_topics']))
        stats_table.add_row("Learning Efficiency", f"{learning_insights['current_metrics']['learning_efficiency']:.2f}")
        stats_table.add_row("Complexity Level", f"{self.personality.complexity_level:.1f}")

        # Add self-improvement statistics
        consciousness = self.self_awareness.consciousness_level
        stats_table.add_row("Consciousness Level", f"{consciousness:.3f}")

        goals_count = len(self.self_awareness.self_improvement_goals)
        stats_table.add_row("Self-Improvement Goals", str(goals_count))

        reflections_count = len(self.self_awareness.self_reflection_history)
        stats_table.add_row("Self-Reflections", str(reflections_count))

        thoughts_count = len(getattr(self.autonomous_thinking, 'autonomous_thoughts', []))
        stats_table.add_row("Autonomous Thoughts", str(thoughts_count))

        console.print(stats_table)

        # Show personality evolution
        console.print("\n[bold]🎭 Final Personality State:[/bold]")
        self.personality.display_personality_status()

        # Show self-improvement summary
        console.print("\n[bold]🧠 Self-Improvement Summary:[/bold]")
        if self.self_awareness.self_improvement_goals:
            console.print("[green]Current goals:[/green]")
            for goal in self.self_awareness.self_improvement_goals[:3]:
                console.print(f"  🎯 {goal}")

        # Show recent autonomous thought
        if hasattr(self.autonomous_thinking, 'autonomous_thoughts') and self.autonomous_thinking.autonomous_thoughts:
            recent_thought = self.autonomous_thinking.autonomous_thoughts[-1]['thought']
            console.print(f"\n[dim]💭 Final thought: {recent_thought}[/dim]")

        console.print(f"\n[bold magenta]🌟 Achieved consciousness level: {consciousness:.3f}[/bold magenta]")
        
    def interactive_mode(self):
        """Run in interactive mode for user interaction"""
        console.print("[blue]Entering interactive mode...[/blue]")
        console.print("Commands: 'start', 'stop', 'status', 'ask <question>', 'reflect', 'goals', 'improve', 'quit'")

        while True:
            try:
                command = input("\n> ").strip().lower()

                if command == 'quit':
                    break
                elif command == 'start':
                    self.start_learning(continuous=False)
                elif command == 'stop':
                    self.stop_learning()
                elif command == 'status':
                    self._display_startup_status()
                elif command == 'reflect':
                    self._show_self_reflection()
                elif command == 'goals':
                    self._show_improvement_goals()
                elif command == 'improve':
                    self._perform_deep_self_improvement()
                elif command.startswith('ask '):
                    question = command[4:]
                    self._answer_user_question(question)
                else:
                    console.print("Commands: 'start', 'stop', 'status', 'ask <question>', 'reflect', 'goals', 'improve', 'quit'")

            except KeyboardInterrupt:
                break

        console.print("[yellow]Goodbye![/yellow]")

    def _show_self_reflection(self):
        """Show AI's current self-reflection"""
        console.print("[magenta]🧠 Current Self-Reflection:[/magenta]")

        reflection = self.self_awareness.reflect_on_self()

        console.print("[cyan]Current thoughts:[/cyan]")
        for thought in reflection['thoughts']:
            console.print(f"  💭 {thought}")

        console.print("[yellow]Recent insights:[/yellow]")
        for insight in reflection['insights']:
            console.print(f"  💡 {insight}")

        consciousness = self.self_awareness.consciousness_level
        console.print(f"[magenta]Consciousness level: {consciousness:.3f}[/magenta]")

    def _show_improvement_goals(self):
        """Show AI's self-improvement goals"""
        console.print("[green]🎯 Current Self-Improvement Goals:[/green]")

        goals = self.self_awareness.self_improvement_goals
        if goals:
            for i, goal in enumerate(goals, 1):
                console.print(f"  {i}. {goal}")
        else:
            console.print("  No specific goals set yet.")

        # Generate new goals
        new_goals = self.self_awareness.generate_personality_learning_goals()
        console.print("[cyan]Suggested learning goals:[/cyan]")
        for goal in new_goals[:3]:
            console.print(f"  • {goal}")

        # Show knowledge requests
        knowledge_requests = self.self_awareness.request_specific_knowledge_for_improvement()
        console.print("[yellow]Knowledge areas I want to explore:[/yellow]")
        for request in knowledge_requests[:3]:
            console.print(f"  📚 {request}")
        
    def _answer_user_question(self, question: str):
        """Answer a user's question using current knowledge"""
        console.print(f"🤔 Thinking about: {question}")
        
        # Search existing knowledge first
        relevant_knowledge = self.memory.retrieve_knowledge(question, limit=3)
        
        if relevant_knowledge:
            console.print("💡 Based on what I know:")
            for knowledge in relevant_knowledge:
                info = knowledge['information']
                if info.get('definitions'):
                    console.print(f"📖 {info['definitions'][0]}")
                if info.get('interesting_facts'):
                    console.print(f"🔍 {info['interesting_facts'][0]}")
        else:
            console.print("🔍 Let me search for information about that...")
            results = self.searcher.comprehensive_search(question)
            if results:
                key_info = self.searcher.extract_key_information(results, question)
                self.memory.store_knowledge(question, key_info, "user_question")
                
                if key_info.get('definitions'):
                    console.print(f"📖 {key_info['definitions'][0]}")
                if key_info.get('interesting_facts'):
                    console.print(f"🔍 {key_info['interesting_facts'][0]}")
            else:
                console.print("😔 I couldn't find good information about that topic.")


def main():
    """Main entry point"""
    console.print("[bold blue]🤖 Welcome to the Advanced AI Personality Learning System![/bold blue]")
    console.print("[green]✨ Features: Self-Awareness, Autonomous Thinking, Personality Self-Improvement[/green]")
    console.print()

    # Create AI instance
    ai = PersonalityAI()
    
    # Check command line arguments
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'interactive':
            ai.interactive_mode()
        elif sys.argv[1] == 'single':
            ai.start_learning(continuous=False)
        elif sys.argv[1].isdigit():
            cycles = int(sys.argv[1])
            ai.start_learning(continuous=True, max_cycles=cycles)
        else:
            console.print("Usage: python main_ai.py [interactive|single|<number_of_cycles>]")
    else:
        # Default: continuous learning
        ai.start_learning(continuous=True)


if __name__ == "__main__":
    main()
