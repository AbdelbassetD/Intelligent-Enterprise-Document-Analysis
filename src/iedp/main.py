"""Main entry point for the IEDP application."""

import sys
from pathlib import Path

from src.iedp.config import Settings, get_settings
from src.iedp.logging_config import setup_logging, get_logger


def main():
    """Initialize and run the application."""
    settings = get_settings()
    setup_logging(log_level=settings.log_level, app_name=settings.app_name)
    logger = get_logger(__name__)

    logger.info(f"Starting {settings.app_name}")
    logger.info(f"Environment: {settings.app_env}")
    logger.info(f"Debug mode: {settings.debug}")

    # Create necessary directories
    settings.create_directories()
    logger.info("Directories initialized")

    # Application placeholder
    logger.info("Application ready")
    return 0


if __name__ == "__main__":
    sys.exit(main())
