.PHONY: help install install-dev test test-cov lint format type-check clean run-server run-cli

# Default target
help:
	@echo "IEDP Project - Available commands:"
	@echo ""
	@echo "Installation:"
	@echo "  make install           Install production dependencies"
	@echo "  make install-dev       Install development dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make lint              Run linting checks (ruff, black, isort)"
	@echo "  make format            Format code with black and isort"
	@echo "  make type-check        Run type checking with mypy"
	@echo "  make test              Run tests with pytest"
	@echo "  make test-cov          Run tests with coverage report"
	@echo ""
	@echo "Running:"
	@echo "  make run-server        Start FastAPI development server"
	@echo "  make run-cli           Run CLI help"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean             Clean up temporary files and caches"
	@echo "  make pre-commit        Run pre-commit hooks on all files"
	@echo ""

# Installation targets
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

# Development targets
lint:
	@echo "Running linting checks..."
	ruff check src/ tests/
	black --check src/ tests/
	isort --check-only src/ tests/

format:
	@echo "Formatting code..."
	black src/ tests/
	isort src/ tests/
	ruff check src/ tests/ --fix

type-check:
	@echo "Running type checks..."
	mypy src/

test:
	@echo "Running tests..."
	pytest tests/ -v

test-cov:
	@echo "Running tests with coverage..."
	pytest tests/ -v --cov=src --cov-report=html
	@echo "Coverage report generated in htmlcov/index.html"

# Running targets
run-server:
	@echo "Starting FastAPI server..."
	uvicorn src.iedp.api.main:app --reload --host 0.0.0.0 --port 8000

run-cli:
	@echo "Running CLI..."
	python -m src.iedp.cli --help

# Utility targets
clean:
	@echo "Cleaning up..."
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete
	find . -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache .mypy_cache .coverage htmlcov/ build/ dist/
	@echo "Cleanup complete"

pre-commit:
	@echo "Running pre-commit checks..."
	pre-commit run --all-files

init:
	@echo "Initializing project..."
	mkdir -p data/{documents,processed,embeddings}
	mkdir -p logs
	mkdir -p .cache
	@echo "Project initialized"
