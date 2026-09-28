"""
Tests for the time tracker module.

Uses mocks to avoid real window detection and file I/O.
"""

import pytest
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock

from src.core.tracker import TimeTracker
from src.storage.json_storage import JsonStorage


@pytest.fixture
def mock_storage():
    """Create a mock storage."""
    storage = MagicMock(spec=JsonStorage)
    storage.get_all_stats.return_value = {}
    return storage


@pytest.fixture
def tracker(mock_storage):
    """Create a tracker with mock storage."""
    return TimeTracker(check_interval=1, storage=mock_storage)


class TestTrackerInit:
    """Tests for TimeTracker initialization."""

    def test_initial_state(self, tracker):
        """Should start with no active session."""
        assert tracker.current_editor is None
        assert tracker.session_start is None
        assert tracker.is_running is False

    def test_uses_provided_storage(self, mock_storage):
        """Should use the provided storage."""
        tracker = TimeTracker(storage=mock_storage)
        assert tracker.storage is mock_storage

        

