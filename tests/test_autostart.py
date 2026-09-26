"""
Tests for autostart module.

Uses mocks to avoid touching real filesystem.
"""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from src.daemon import autostart


class TestGetAutostartPath:
    """Tests for get_autostart_path()."""

    @patch("src.daemon.autostart.platform.system")
    def test_linux_path(self, mock_system):
        """Should return Linux path."""
        mock_system.return_value = 'Linux'
        path = autostart.get_autostart_path()
        assert path == Path.home() / ".config" / "autostart" / "devtime.desktop"

    @patch("src.daemon.autostart.platform.system")
    @patch.dict("os.environ", {"APPDATA": "/fake/appdata"})
    def test_windows_path(self, mock_system):
        """Should return Windows path."""
        mock_system.return_value = 'Windows'
        path = autostart.get_autostart_path()
        assert "DevTimeTracker.lnk" in str(path)
        assert "Startup" in str(path)

    @patch("src.daemon.autostart.platform.system")
    def test_macos_path(self, mock_system):
        """Should return macOS path."""
        mock_system.return_value = 'Darwin'
        path = autostart.get_autostart_path()
        assert "com.devtime.tracker.plist" in str(path)

    @patch("scr.daemon.autostart.platform.system")
    def test_unsupported_os(self, mock_system):
        """Should raise OSError on unsupported OS."""
        mock_system.return_value = 'FreeBDS'
        with pytest.raises(OSError):
            autostart.get_autostart_path()

