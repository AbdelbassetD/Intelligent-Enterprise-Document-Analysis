"""Configuration module for IEDP application settings."""

from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings managed by pydantic."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Application Settings
    app_name: str = Field(
        default="intelligent-enterprise-document-analysis",
        description="Application name"
    )
    app_env: str = Field(
        default="development",
        description="Application environment (development, staging, production)"
    )
    debug: bool = Field(default=False, description="Enable debug mode")
    log_level: str = Field(default="INFO", description="Logging level")

    # LLM/VLM Configuration
    openai_api_key: Optional[str] = Field(
        default=None,
        description="OpenAI API key"
    )
    google_api_key: Optional[str] = Field(
        default=None,
        description="Google API key for Gemini"
    )
    anthropic_api_key: Optional[str] = Field(
        default=None,
        description="Anthropic API key for Claude"
    )

    # Vector Database Configuration
    qdrant_url: str = Field(
        default="http://localhost:6333",
        description="Qdrant vector database URL"
    )
    qdrant_api_key: Optional[str] = Field(
        default=None,
        description="Qdrant API key"
    )

    # Redis Configuration
    redis_url: Optional[str] = Field(
        default="redis://localhost:6379",
        description="Redis connection URL"
    )

    # Database Configuration
    database_url: Optional[str] = Field(
        default=None,
        description="Database connection URL"
    )

    # Server Configuration
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, description="Server port")
    workers: int = Field(default=4, description="Number of worker processes")

    # Data Paths
    data_dir: Path = Field(
        default_factory=lambda: Path("./data"),
        description="Data directory path"
    )
    models_dir: Path = Field(
        default_factory=lambda: Path("./models"),
        description="Models directory path"
    )
    cache_dir: Path = Field(
        default_factory=lambda: Path("./.cache"),
        description="Cache directory path"
    )

    # RAG Configuration
    chunk_size: int = Field(
        default=1000,
        description="Document chunk size for embedding"
    )
    chunk_overlap: int = Field(
        default=200,
        description="Overlap between chunks"
    )
    embedding_model: str = Field(
        default="openai",
        description="Embedding model to use"
    )
    retrieval_k: int = Field(
        default=5,
        description="Number of documents to retrieve"
    )

    # Agent Configuration
    agent_max_iterations: int = Field(
        default=10,
        description="Maximum iterations for agent loops"
    )
    agent_timeout: int = Field(
        default=300,
        description="Agent timeout in seconds"
    )

    def create_directories(self) -> None:
        """Create necessary directories if they don't exist."""
        for directory in [self.data_dir, self.models_dir, self.cache_dir]:
            directory.mkdir(parents=True, exist_ok=True)


def get_settings() -> Settings:
    """Get application settings instance."""
    return Settings()
