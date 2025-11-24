"""Pytest configuration and fixtures."""

import pytest
from pathlib import Path
from unittest.mock import MagicMock

from src.iedp.config import Settings
from src.iedp.logging_config import setup_logging


@pytest.fixture
def settings():
    """Provide application settings for testing."""
    return Settings(
        app_env="testing",
        debug=True,
        log_level="DEBUG",
    )


@pytest.fixture
def mock_retriever():
    """Provide a mock retriever for testing."""
    return MagicMock()


@pytest.fixture
def mock_orchestrator():
    """Provide a mock orchestrator for testing."""
    return MagicMock()


@pytest.fixture
def mock_reasoner():
    """Provide a mock reasoner for testing."""
    return MagicMock()


@pytest.fixture(autouse=True)
def setup_test_logging():
    """Set up logging for tests."""
    setup_logging(log_level="DEBUG")
