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

