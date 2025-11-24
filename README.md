# Intelligent Enterprise Document Analysis
<!-- Agentic multimodal RAG platform for enterprise document analysis powered by GenAI (LLMS/VLMs). -->

#### A platform utilizing **agentic RAG workflows** and **multimodal LLM/VLM reasoning** for enterprise document intelligence.

## 🧠 Vision
The goal of this project is to build an **autonomous, multimodal RAG platform** capable of analyzing unstructured enterprise data (text, tables, images, documents) and coordinating AI agents to perform reasoning-intensive tasks such as:
- regulatory document auditing
- visual quality inspection
- contextual summarization and reporting

## 🧩 Architecture
- **Hybrid RAG layer:** Dense-sparse retrieval (LangChain + Qdrant)
- **Agentic layer:** Multi-agent collaboration (CrewAI/LangGraph)
- **Multimodal layer:** Integration of large multimodal models (GPT-5, Gemini 2.5 Pro, Qwen3-VL)
- **Deployment target:** CLI + REST microservice for enterprise analytics

## 🎬 Video Demo
https://github.com/user-attachments/assets/f87dfb58-cda5-47b7-95b2-2ff01a563acb





<!-- ## 🚧 Current Status
- [x] Initial architecture draft  
- [x] RAG evaluation notebook prototype  
- [x] Agent orchestration layer  
- [x] Multimodal extension  
- [ ] API endpoints & CLI tooling   -->

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip or uv package manager
- Git

### Installation

1. **Clone the repository**
```bash
git clone <repository_url>
cd intelligent-enterprise-document-analysis
```

2. **Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

Option A: Install from requirements.txt
```bash
pip install -r requirements.txt
```

Option B: Install with development tools
```bash
pip install -r requirements-dev.txt
```

Option C: Install using pyproject.toml
```bash
pip install -e ".[dev]"
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

5. **Install pre-commit hooks**
```bash
pre-commit install
```

### Running the Application

#### Development Server
```bash
# Initialize logging and configuration
python -c "from src.iedp import setup_logging; setup_logging()"

# Run application (when main entry point is ready)
# python -m src.iedp.main
```

#### Command Line Interface
The CLI will be available through Click once the main module is implemented.

#### REST API
```bash
# Start the FastAPI server
uvicorn src.iedp.api.main:app --reload --host 0.0.0.0 --port 8000
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_config.py

# Run tests matching a pattern
pytest tests/ -k "test_settings"

# Run with verbose output
pytest -v
```

### Code Quality

```bash
# Format code with black
black src/ tests/

# Sort imports
isort src/ tests/

# Lint with ruff
ruff check src/ tests/ --fix

# Type checking
mypy src/

# Run all checks
pre-commit run --all-files
```

### Project Structure

```
.
├── src/
│   └── iedp/                          # Main package
│       ├── __init__.py
│       ├── config.py                  # Configuration management
│       ├── logging_config.py           # Logging utilities
│       ├── retrieval.py               # Hybrid RAG retrieval layer
│       ├── agents.py                  # Multi-agent orchestration
│       └── multimodal.py              # Multimodal reasoning layer
├── tests/                             # Test suite
│   ├── conftest.py                    # Pytest configuration
│   ├── test_config.py
│   └── test_logging.py
├── config/                            # Configuration files
│   └── settings.yaml                  # Default configuration
├── data/                              # Data directory (gitignored)
│   ├── documents/                     # Source documents
│   ├── processed/                     # Processed documents
│   └── embeddings/                    # Cached embeddings
├── pyproject.toml                     # Project metadata and dependencies
├── requirements.txt                   # Production dependencies
├── requirements-dev.txt               # Development dependencies
├── .env.example                       # Environment template
├── .gitignore                         # Git ignore rules
├── .pre-commit-config.yaml            # Pre-commit hooks configuration
└── README.md                          # This file
```

## 📚 Documentation

- [Architecture Overview](docs/architecture.md) - Coming soon
- [API Reference](docs/api.md) - Coming soon
- [Configuration Guide](docs/configuration.md) - Coming soon
- [Development Guide](docs/development.md) - Coming soon

## 🛠️ Development

### Adding Dependencies

```bash
# Add a new dependency
pip install <package_name>
pip freeze > requirements.txt

# Or update pyproject.toml directly and reinstall
pip install -e ".[dev]"
```

### Creating New Modules

1. Create a new Python file in `src/iedp/`
2. Add appropriate imports and docstrings
3. Update `src/iedp/__init__.py` if needed
4. Add corresponding tests in `tests/`

### Git Workflow

```bash
# Create a feature branch
git checkout -b feature/your-feature

# Make changes and commit
git add .
git commit -m "feat: description of changes"

# Pre-commit hooks will run automatically
# Push changes
git push origin feature/your-feature
```

## 📅 Roadmap

- [ ] Implement hybrid RAG layer with LangChain + Qdrant
- [ ] Integrate CrewAI/LangGraph for multi-agent orchestration
- [ ] Connect multimodal LLM/VLM models (GPT-5, Gemini 2.5 Pro, Qwen3-VL)
- [ ] Develop CLI tooling with Click
- [ ] Build REST API with FastAPI
- [ ] Add Docker containerization
- [ ] Implement CI/CD pipelines
- [ ] Add comprehensive documentation
- [ ] Deploy microservices

## 📝 License

MIT License

