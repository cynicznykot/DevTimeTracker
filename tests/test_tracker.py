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


class TestGetActiveEditor:
    """Tests for _get_active_editor."""

    @patch("src.core.tracker.get_all_windows")
    @patch("src.core.tracker.detect_editor")
    def test_returns_editor(self, mock_detect, mock_windows, tracker):
        """Should return editor name when found."""
        mock_window = MagicMock()
        mock_window.title = "main.py - PyCharm"
        mock_window.return_value = [mock_window]
        mock_detect.return_value = "PyCharm"

        assert tracker._get_active_editor() == "PyCharm"

    @patch("src.core.tracker.get_all_windows")
    def test_returns_none_when_no_windows(self, mock_windows, tracker):
        """Should return None when no windows."""
        mock_windows.return_value = []

        assert tracker._get_active_editor() is None

    @patch("src.core.tracker.get_all_windows")
    def test_handles_exception(self, mock_windows, tracker):
        """Should return None on exception."""
        mock_windows.side_effect = Exception("Test error")

        assert tracker._get_active_editor() is None


class TestStartSession:
    """Tests for _start_session()."""

    @patch("src.core.tracker.send_notification")
    def test_starts_sessions(self, mock_notify, tracker):
        """Should set current_editor and session_start."""
        tracker._start_session("PyCharm")

        assert tracker.current_editor == "PyCharm"
        assert tracker.session_start is not None

    @patch("src.core.tracker.send_notification")
    def test_sends_notification(self, mock_notify, tracker):
        """Should send a notification."""
        tracker._start_session("PyCharm")

        mock_notify.assert_called_once()
        args = mock_notify.call_args[0]
        assert "DevTimeTracker" in args[0]
        assert "PyCharm" in args[1]




