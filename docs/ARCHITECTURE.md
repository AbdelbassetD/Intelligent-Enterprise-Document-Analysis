# Architecture Overview

## System Architecture

The Intelligent Enterprise Document Analysis (IEDP) platform is designed as a layered architecture with three main components:

```
┌─────────────────────────────────────────────────┐
│         API Layer (FastAPI/CLI)                 │
├─────────────────────────────────────────────────┤
│         Agentic Layer (CrewAI/LangGraph)        │
├─────────────────────────────────────────────────┤
│      Multimodal Reasoning (LLM/VLM Models)      │
├─────────────────────────────────────────────────┤
│    Retrieval Layer (LangChain + Qdrant)         │
├─────────────────────────────────────────────────┤
│      Data Layer (Documents, Embeddings)         │
└─────────────────────────────────────────────────┘
```

## Layer Descriptions

### 1. Data Layer (`src/iedp/retrieval.py`)
- **Purpose**: Store and manage enterprise documents and their embeddings
- **Components**:
  - Document storage (text, images, tables)
  - Vector database (Qdrant) for embeddings
  - Hybrid indexing (dense + sparse retrieval)
- **Technology**: Qdrant, LangChain Document loaders
- **Key Classes**: `HybridRetriever`

### 2. Retrieval Layer
- **Purpose**: Implement efficient document retrieval using RAG principles
- **Components**:
  - Hybrid dense-sparse retrieval
  - Document chunking and processing
  - Embedding generation
  - Relevance scoring
- **Technology**: LangChain, Qdrant
- **Key Features**:
  - Configurable chunk sizes
  - Multi-model embeddings support
  - Semantic search

### 3. Multimodal Reasoning Layer (`src/iedp/multimodal.py`)
- **Purpose**: Process and analyze multimodal content
- **Components**:
  - LLM integration (GPT-5, Claude)
  - VLM integration (Gemini 2.5 Pro, Qwen3-VL)
  - Document analysis engine
  - Information extraction
- **Technology**: LangChain LLM integrations
- **Key Classes**: `MultimodalReasoner`
- **Capabilities**:
  - Text understanding
  - Image analysis
  - Table extraction
  - Cross-modal reasoning

### 4. Agentic Layer (`src/iedp/agents.py`)
- **Purpose**: Coordinate multi-agent workflows for complex tasks
- **Components**:
  - Agent orchestration
  - Task dispatching
  - Workflow management
  - Memory management
- **Technology**: CrewAI or LangGraph
- **Key Classes**: `AgentOrchestrator`
- **Use Cases**:
  - Regulatory auditing workflows
  - Quality inspection pipelines
  - Document analysis orchestration

### 5. API Layer
- **REST API** (`src/iedp/api/main.py`):
  - FastAPI framework
  - RESTful endpoints
  - Health checks
  - Document analysis endpoints
  
- **CLI** (`src/iedp/cli.py`):
  - Click-based command interface
  - Local analysis capabilities
  - Batch processing

## Key Components

### Configuration Management (`src/iedp/config.py`)
- Pydantic-based settings
- Environment variable support
- Type-safe configuration
- Directory management

### Logging (`src/iedp/logging_config.py`)
- Loguru-based logging
- Configurable log levels
- File and console output
- Structured logging

## Data Flow

### Document Analysis Flow
```
User Input
    ↓
API/CLI
    ↓
Agentic Layer (Task Planning)
    ↓
Retrieval Layer (Document Search)
    ↓
Multimodal Reasoning (Analysis)
    ↓
Agent Synthesis (Result Assembly)
    ↓
Response/Output
```

### Hybrid Retrieval Flow
```
Query
    ↓
Query Embedding (Dense)
    ↓
Qdrant Semantic Search
    ↓
Sparse Retrieval (BM25)
    ↓
Score Fusion
    ↓
Top-K Results
    ↓
Context to LLM
```

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Framework | FastAPI | REST API |
| CLI | Click | Command interface |
| LLM Integration | LangChain | Model abstractions |
| Vector DB | Qdrant | Embeddings storage |
| Multi-Agent | CrewAI/LangGraph | Orchestration |
| Config | Pydantic | Settings management |
| Logging | Loguru | Structured logging |
| Testing | Pytest | Unit testing |
| Code Quality | Black, Ruff, MyPy | Formatting & linting |

## Module Dependencies

```
src/iedp/
├── __init__.py
│   └── exports: Settings, setup_logging
├── config.py
│   └── depends on: pydantic
├── logging_config.py
│   └── depends on: loguru
├── main.py
│   └── depends on: config, logging_config
├── retrieval.py
│   └── depends on: langchain, qdrant
├── agents.py
│   └── depends on: crewai/langgraph
├── multimodal.py
│   └── depends on: langchain (LLM/VLM)
├── cli.py
│   └── depends on: click, config, logging_config
└── api/
    └── main.py
        └── depends on: fastapi, config, logging_config
```

## Configuration

### Environment-Based Configuration
All settings are configurable via environment variables (.env file):

```env
# LLM Keys
OPENAI_API_KEY=...
GOOGLE_API_KEY=...

# Vector DB
QDRANT_URL=http://localhost:6333

# RAG Settings
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
RETRIEVAL_K=5

# Server
HOST=0.0.0.0
PORT=8000
```

## Scalability Considerations

### Horizontal Scaling
- API endpoints can be load balanced
- Vector database supports clustering
- Agents can run on separate workers

### Vertical Optimization
- Efficient embedding caching
- Batch processing capabilities
- Async/await for I/O operations

## Security Considerations

- API key management via environment variables
- Input validation with Pydantic
- CORS configuration in FastAPI
- Rate limiting (to be implemented)
- Authentication (to be implemented)

## Future Enhancements

- [ ] Authentication & authorization
- [ ] Advanced caching strategies
- [ ] Rate limiting
- [ ] Monitoring & observability
- [ ] Containerization (Docker)
- [ ] Kubernetes orchestration
- [ ] Advanced workflow templates
- [ ] Custom model fine-tuning
- [ ] Performance optimization
