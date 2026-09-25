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


class TestAddTime:
    """Tests for add_time() method."""

    def test_add_single_entry(self, temp_storage):
        """Should add time for one editor."""
        temp_storage.add_time("2026-09-24", "PyCharm", 3600)
        stats = temp_storage.get_daily_stats("2026-09-24")
        assert stats == {"PyCharm": 3600}

    def test_add_multiple_entries(self, temp_storage):
        """Should accumulate time for same editor."""
        temp_storage.add_time("2026-09-24", "PyCharm", 3600)
        temp_storage.add_time("2026-09-24", "PyCharm", 1800)
        stats = temp_storage.get_daily_stats("2026-09-24")
        assert stats == {"PyCharm": 5400}

    def test_add_different_editors(self, temp_storage):
        """Should track multiple editors."""
        temp_storage.add_time("2026-09-24", "PyCharm", 3600)
        temp_storage.add_time("2026-09-24", "VS Code", 1800)
        stats = temp_storage.get_daily_stats("2026-09-24")
        assert stats == {"PyCharm": 3600, "VS Code": 1800}

    def test_add_different_days(self, temp_storage):
        """Should track different days separately."""
        temp_storage.add_time("2026-09-24", "PyCharm", 3600)
        temp_storage.add_time("2026-09-23", "PyCharm", 1800)
        assert temp_storage.get_daily_stats("2026-09-24") == {"PyCharm": 3600}
        assert temp_storage.get_daily_stats("2026-09-23") == {"PyCharm": 1800}

        
