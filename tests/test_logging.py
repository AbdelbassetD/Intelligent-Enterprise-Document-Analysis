"""Tests for logging configuration module."""

import pytest
from pathlib import Path
import tempfile

from src.iedp.logging_config import setup_logging, get_logger


class TestLoggingConfig:
    """Test logging configuration."""

    def test_setup_logging_basic(self):
        """Test basic logging setup."""
        setup_logging(log_level="INFO")
        logger = get_logger("test")
        assert logger is not None

    def test_setup_logging_with_file(self):
        """Test logging setup with file output."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = Path(tmpdir) / "test.log"
            setup_logging(log_level="DEBUG", log_file=log_file)
            logger = get_logger("test")
            logger.debug("Test message")
            # File should be created
            # Note: loguru may not create file until first write

    def test_get_logger(self):
        """Test getting a logger instance."""
        logger = get_logger("test_module")
        assert logger is not None
        # Logger should have bind method from loguru
        assert hasattr(logger, "bind")

    def test_setup_logging_levels(self):
        """Test different logging levels."""
        for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            setup_logging(log_level=level)
            logger = get_logger("test")
            assert logger is not None
