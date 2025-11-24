"""Command-line interface for IEDP application."""

import click
from pathlib import Path

from src.iedp.config import get_settings
from src.iedp.logging_config import setup_logging, get_logger


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """Intelligent Enterprise Document Analysis CLI."""
    pass


@cli.command()
@click.option("--env", default="development", help="Environment to use")
@click.option("--log-level", default="INFO", help="Logging level")
def init(env: str, log_level: str):
    """Initialize the application."""
    setup_logging(log_level=log_level)
    logger = get_logger(__name__)

    logger.info(f"Initializing application for {env}")

    settings = get_settings()
    settings.create_directories()

    logger.info("Application initialized successfully")


@cli.command()
@click.argument("document_path", type=click.Path(exists=True))
@click.option(
    "--query",
    default="",
    help="Query to analyze the document"
)
def analyze(document_path: str, query: str):
    """Analyze a document."""
    setup_logging(log_level="INFO")
    logger = get_logger(__name__)

    logger.info(f"Analyzing document: {document_path}")
    if query:
        logger.info(f"Query: {query}")

    # TODO: Implement document analysis
    click.echo("Document analysis feature coming soon")


@cli.command()
@click.option("--limit", default=10, help="Number of documents to process")
def process_batch(limit: int):
    """Process a batch of documents."""
    setup_logging(log_level="INFO")
    logger = get_logger(__name__)

    logger.info(f"Processing batch of {limit} documents")

    # TODO: Implement batch processing
    click.echo("Batch processing feature coming soon")


if __name__ == "__main__":
    cli()
