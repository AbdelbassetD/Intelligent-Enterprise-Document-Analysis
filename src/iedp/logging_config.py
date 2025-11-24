"""Logging configuration for IEDP application."""

import sys
from pathlib import Path
from typing import Optional

from loguru import logger

# Remove default handler
logger.remove()


def setup_logging(
    log_level: str = "INFO",
    log_file: Optional[Path] = None,
    app_name: str = "iedp",
) -> None:
    """
    Configure logging for the application.

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional file path for log output
        app_name: Application name for log context
    """
    # Add console handler
    logger.add(
        sys.stderr,
        level=log_level,
        format=(
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
    )

    # Add file handler if log file is specified
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        logger.add(
            log_file,
            level=log_level,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
            rotation="500 MB",
            retention="7 days",
        )


def get_logger(name: str) -> logger:
    """
    Get a logger instance with the specified name.

    Args:
        name: Logger name (typically __name__)

    Returns:
        Logger instance
    """
    return logger.bind(name=name)
