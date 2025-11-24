# Development Guide

This guide provides instructions for setting up your development environment and contributing to the IEDP project.

## Environment Setup

### Prerequisites
- Python 3.10 or higher
- Git
- pip or pipenv

### Initial Setup

1. **Clone the repository**
```bash
git clone <repo_url>
cd intelligent-enterprise-document-analysis
```

2. **Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install development dependencies**
```bash
pip install -r requirements-dev.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your local configuration
```

5. **Install pre-commit hooks**
```bash
pre-commit install
```

6. **Create data directories**
```bash
mkdir -p data/{documents,processed,embeddings}
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test
pytest tests/test_config.py::TestSettings::test_settings_initialization

# Run tests matching pattern
pytest tests/ -k "test_settings"

# Run with verbose output
pytest -v

# Run specific markers
pytest -m "unit"
```

### Code Quality Checks

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint and fix
ruff check src/ tests/ --fix

# Type checking
mypy src/

# Run all pre-commit checks
pre-commit run --all-files
```

### Adding New Features

1. **Create feature branch**
```bash
git checkout -b feature/your-feature-name
```

2. **Implement changes**
- Follow existing code style (see Code Style section below)
- Add appropriate docstrings
- Add type hints where possible

3. **Add tests**
- Write unit tests in `tests/test_*.py`
- Ensure tests pass: `pytest`

4. **Commit changes**
```bash
git add .
git commit -m "feat: description of changes"
```

5. **Push and create PR**
```bash
git push origin feature/your-feature-name
```

## Code Style

### Python Style Guide
We follow PEP 8 with some conventions:
- Line length: 100 characters
- Use type hints
- Use docstrings for all public functions/classes

### Naming Conventions
- Functions and variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private functions: `_leading_underscore`

### Example

```python
"""Module docstring."""

from typing import Optional


class DocumentProcessor:
    """Process enterprise documents."""

    MAX_RETRIES = 3

    def __init__(self, config: dict):
        """Initialize processor."""
        self._config = config
        self._cache = {}

    def process_document(self, doc_id: str) -> Optional[dict]:
        """
        Process a document.

        Args:
            doc_id: Document identifier

        Returns:
            Processed document or None if failed
        """
        pass
```

## Module Structure

### Adding a New Module

1. Create file in `src/iedp/`
2. Add docstring and type hints
3. Update `src/iedp/__init__.py` if needed
4. Create tests in `tests/test_*.py`
5. Add to documentation

### Example Module

```python
# src/iedp/my_module.py
"""My new module."""

from typing import List


class MyClass:
    """Description of my class."""

    def my_method(self, param: str) -> List[str]:
        """
        Description of my method.

        Args:
            param: Parameter description

        Returns:
            List of results
        """
        pass
```

```python
# tests/test_my_module.py
"""Tests for my_module."""

import pytest

from src.iedp.my_module import MyClass


class TestMyClass:
    """Test MyClass."""

    def test_my_method(self):
        """Test my_method."""
        obj = MyClass()
        result = obj.my_method("test")
        assert isinstance(result, list)
```

## Dependency Management

### Adding Dependencies

**For production:**
```bash
pip install package_name
pip freeze > requirements.txt
# Also update pyproject.toml
```

**For development:**
```bash
pip install package_name
# Update requirements-dev.txt or pyproject.toml
```

### Updating Dependencies

```bash
# Update single package
pip install --upgrade package_name

# Update all packages
pip install --upgrade -r requirements.txt
pip install --upgrade -r requirements-dev.txt
```

## Git Workflow

### Commit Message Format

Follow conventional commits:
```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvement
- `test`: Adding tests
- `chore`: Build process, dependencies, tools

Examples:
```
feat(config): add environment-based settings
fix(logging): handle missing log directory
docs(readme): update installation instructions
```

### Branches

- `main` - Production-ready code
- `develop` - Development branch (if used)
- `feature/*` - Feature branches
- `fix/*` - Bug fix branches
- `chore/*` - Maintenance branches

## Testing Best Practices

### Test Structure

```python
class TestFeature:
    """Test feature."""

    def test_success_case(self):
        """Test successful operation."""
        pass

    def test_error_case(self):
        """Test error handling."""
        pass

    def test_edge_case(self):
        """Test edge cases."""
        pass
```

### Using Fixtures

```python
@pytest.fixture
def sample_data():
    """Provide sample data."""
    return {"key": "value"}


def test_with_fixture(sample_data):
    """Test using fixture."""
    assert sample_data["key"] == "value"
```

## Debugging

### Using Print Debugging
```python
from src.iedp.logging_config import get_logger

logger = get_logger(__name__)
logger.debug(f"Debug info: {variable}")
```

### Using Python Debugger
```python
import pdb; pdb.set_trace()
```

### Running Tests with Debug Output
```bash
pytest -v -s  # Show print statements
pytest --pdb  # Drop into debugger on failure
```

## Common Tasks

### Run a single test
```bash
pytest tests/test_config.py::TestSettings::test_settings_initialization -v
```

### Check test coverage
```bash
pytest --cov=src --cov-report=html tests/
# Open htmlcov/index.html in browser
```

### Format all code
```bash
black src/ tests/
isort src/ tests/
```

### Check types
```bash
mypy src/
```

## Troubleshooting

### Import Errors
- Ensure virtual environment is activated
- Check PYTHONPATH includes project root
- Verify `src` package structure

### Pre-commit Hook Failures
```bash
# Run pre-commit on all files to identify issues
pre-commit run --all-files

# Fix common issues
black src/ tests/
isort src/ tests/
ruff check src/ tests/ --fix
```

### Test Failures
```bash
# Run with verbose output
pytest -v

# Show print statements
pytest -v -s

# Stop on first failure
pytest -x

# Enter debugger on failure
pytest --pdb
```

## Resources

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Black Documentation](https://black.readthedocs.io/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
