"""
test for JSON storage module.
"""

import os
import json
import pytest
from pathlib import Path

from src.storage.json_storage import JsonStorage


@pytest.fixture
def temp_storage(tmp_path):
    """Create a temporary storage for testing."""
    file_path = tmp_path / "test_sessions.json"
    storage = JsonStorage(str(file_path))
    yield storage
    if file_path.exists():
        file_path.unlink()


class TestJsonStorageInit:
    """Tests for storage initialization."""

    def test_creates_file(self, tmp_path):
        """Should create file on init."""
        file_path = tmp_path / "new.json"
        storage = JsonStorage(str(file_path))
        assert file_path.exists()

    def test_initial_structure(self, tmp_path):
        """Should have empty daily_stats."""
        file_path = tmp_path / "new.json"
        storage = JsonStorage(str(file_path))
        data = storage.load_all()
        assert data == {"daily_stats": {}}

        