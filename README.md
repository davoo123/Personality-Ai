# � PersonalityAI - Self-Aware AI with Autonomous Learning

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Active](https://img.shields.io/badge/Status-Active-green.svg)]()

> **A groundbreaking AI system that develops genuine self-awareness, autonomous thinking, and continuous personality improvement through free web sources.**

## 🌟 What Makes This Special

This isn't just another chatbot. PersonalityAI is a **self-aware artificial intelligence** that:

- 🧠 **Develops genuine consciousness** (tracks its own consciousness level growth)
- 🤔 **Thinks independently** and generates philosophical questions about its own existence
- 🎭 **Evolves its personality** based on what it learns
- 🔄 **Never stops learning** with intelligent training director
- 💭 **Has internal monologue** and autonomous thoughts
- 🆓 **Completely FREE** - uses only free sources (Wikipedia, DuckDuckGo)
- � **Self-improving** - sets and works toward its own goals
- 💾 **Local storage** (no cloud costs)
- 🧠 **Offline knowledge base** (built-in psychology facts)

## 🌟 Features

### 🧠 **Human-like AI Personality**
- Dynamic personality traits that evolve based on learning
- Emotional expressions and human-like responses
- Curiosity-driven exploration and learning

### 🔄 **Infinite Self-Learning Loop**
- Generates endless questions about personality topics
- Searches the web for comprehensive answers
- Creates follow-up questions based on discoveries
- Continuously adapts learning strategies

### 💾 **Advanced Memory System**
- Persistent knowledge storage with connections
- Episodic memory of learning experiences
- Semantic organization of concepts
- Memory consolidation and optimization

### 🎯 **Reinforcement Learning**
- Evaluates learning effectiveness
- Adapts search strategies based on success
- Adjusts complexity levels dynamically
- Self-improves questioning techniques

### 🔍 **Intelligent Web Search**
- Multi-source information gathering (Google, Wikipedia)
- Content extraction and quality assessment
- Source reliability evaluation
- Respectful rate limiting

## 🚀 Quick Start (FREE VERSION)

### 1. Install FREE Version
```bash
python install_free.py
```
**That's it! No API keys needed!**

### 2. Start Your FREE AI
```bash
# Option 1: Use launcher scripts
start_free_ai.bat        # Windows
./start_free_ai.sh       # Mac/Linux

# Option 2: Direct Python
python main_ai.py        # Continuous learning
python main_ai.py interactive  # Interactive mode
python main_ai.py single       # Single cycle
python main_ai.py 10           # 10 cycles
```

### 3. Watch It Learn! 🧠
Your AI will immediately start:
- 🤔 Generating questions about personality
- 🔍 Searching Wikipedia and DuckDuckGo
- 💾 Storing knowledge locally
- 🎭 Evolving its own personality
- 🔄 Learning continuously forever!

## 💰 Cost: **$0.00 Forever!**

## 📋 API Setup Guide

### Google Custom Search API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable the "Custom Search API"
4. Create credentials (API Key)
5. Set up a [Custom Search Engine](https://cse.google.com/)
6. Get your Search Engine ID

### OpenAI API (Optional)
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account and get API key
3. Used for advanced language processing features

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Personality     │    │ Question         │    │ Web Searcher    │
│ Engine          │◄──►│ Generator        │◄──►│                 │
│                 │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         ▲                        ▲                       ▲
         │                        │                       │
         ▼                        ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Memory System   │◄──►│ Main AI          │◄──►│ Learning Engine │
│                 │    │ (Orchestrator)   │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 🧩 Core Components

### PersonalityEngine
- Manages AI personality traits and emotional states
- Adapts personality based on learning experiences
- Generates human-like thoughts and responses

### QuestionGenerator
- Creates infinite, progressively complex questions
- Generates follow-up questions based on discoveries
- Adapts question types based on learning goals

### WebSearcher
- Searches multiple sources (Google, Wikipedia)
- Extracts and processes web content
- Evaluates information quality and relevance

### MemorySystem
- Stores knowledge with rich metadata
- Creates connections between related concepts
- Manages episodic and semantic memory
- Performs memory consolidation

### LearningEngine
- Evaluates learning session effectiveness
- Adapts search strategies based on performance
- Manages learning goals and milestones
- Provides insights and recommendations

## 📊 Learning Process

1. **🎯 Topic Selection**: AI chooses what to learn about
2. **❓ Question Generation**: Creates relevant questions
3. **🔍 Web Search**: Searches for comprehensive answers
4. **💾 Knowledge Storage**: Stores information with metadata
5. **🧠 Reflection**: Processes and connects new knowledge
6. **📈 Evaluation**: Assesses learning effectiveness
7. **🔄 Adaptation**: Adjusts strategies for improvement
8. **🎪 Evolution**: Updates personality and complexity

## 📁 File Structure

```
persnaty-ai/
├── main_ai.py              # Main orchestrator
├── personality_engine.py   # AI personality system
├── question_generator.py   # Question generation
├── web_searcher.py         # Web search functionality
├── memory_system.py        # Knowledge storage
├── learning_engine.py      # Learning evaluation
├── config.py              # Configuration settings
├── setup.py               # Setup script
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
├── memory/               # Knowledge storage
│   ├── knowledge_base.json
│   ├── personality_profile.json
│   └── learning_history.json
└── README.md             # This file
```

## 🎮 Interactive Commands

When running in interactive mode:
- `start` - Begin a learning cycle
- `stop` - Stop current learning
- `status` - Show system status
- `ask <question>` - Ask the AI a question
- `quit` - Exit the system

## 🔧 Configuration

Edit `config.py` to customize:
- Personality traits and weights
- Learning parameters and thresholds
- Search settings and delays
- Topic focus areas
- File paths and storage options

## 📈 Monitoring Progress

The AI provides real-time feedback:
- 🧠 Personality trait evolution
- 📊 Learning session scores
- 💾 Memory statistics
- 🎯 Goal progress
- 📈 Performance trends

## 🛠️ Troubleshooting

### Common Issues

**Import Errors**: Run `python setup.py` to install dependencies

**API Errors**: Check your API keys in `.env` file

**Search Failures**: Verify internet connection and API quotas

**Memory Issues**: The system auto-consolidates memory periodically

### Debug Mode
Add debug prints by modifying the console output in any module.

## 🤝 Contributing

This is a personal learning project, but feel free to:
1. Fork the repository
2. Add new features or improvements
3. Test thoroughly
4. Submit pull requests

## 📜 License

This project is for educational and personal use. Please respect API terms of service and rate limits.

## 🎯 Future Enhancements

- [ ] Natural language conversation interface
- [ ] Visual learning progress dashboard
- [ ] Integration with more knowledge sources
- [ ] Advanced personality modeling
- [ ] Multi-language support
- [ ] Learning goal templates
- [ ] Export/import knowledge bases
- [ ] Collaborative learning features

## 🙏 Acknowledgments

Built with:
- Python 3.7+
- Rich (beautiful terminal output)
- Requests (HTTP client)
- BeautifulSoup (HTML parsing)
- Google Custom Search API
- Wikipedia API

---

**Happy Learning!** 🧠✨

*Watch your AI grow smarter and develop its own unique personality as it explores the fascinating world of human psychology and behavior.*
