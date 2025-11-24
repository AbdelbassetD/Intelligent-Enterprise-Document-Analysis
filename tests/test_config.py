"""Tests for configuration module."""

import pytest
from pathlib import Path

from src.iedp.config import Settings, get_settings


class TestSettings:
    """Test configuration settings."""

    def test_settings_initialization(self):
        """Test that settings can be initialized."""
        settings = Settings()
        assert settings.app_name == "intelligent-enterprise-document-analysis"
        assert settings.debug is False
        assert settings.log_level == "INFO"

    def test_settings_custom_values(self):
        """Test settings with custom values."""
        settings = Settings(
            app_env="production",
            debug=True,
            log_level="DEBUG",
            port=9000,
        )
        assert settings.app_env == "production"
        assert settings.debug is True
        assert settings.log_level == "DEBUG"
        assert settings.port == 9000

    def test_settings_paths(self):
        """Test that settings paths are properly configured."""
        settings = Settings()
        assert isinstance(settings.data_dir, Path)
        assert isinstance(settings.models_dir, Path)
        assert isinstance(settings.cache_dir, Path)

    def test_create_directories(self):
        """Test that directories can be created."""
        settings = Settings(
            data_dir=Path("/tmp/test_data"),
            models_dir=Path("/tmp/test_models"),
            cache_dir=Path("/tmp/test_cache"),
        )
        settings.create_directories()
        # Directories should exist after creation
        assert settings.data_dir.exists()
        assert settings.models_dir.exists()
        assert settings.cache_dir.exists()

    def test_get_settings(self):
        """Test getting settings instance."""
        settings = get_settings()
        assert isinstance(settings, Settings)
        assert settings.app_name is not None
