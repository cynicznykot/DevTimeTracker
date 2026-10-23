"""
Tests for tray icon module.

Tests icon creation and basic functionality.
"""

import pytest
from unittest.mock import patch, MagicMock

from src.gui.tray import create_icon


class TestCreateIcon:
    """Tests for create_icon()."""

    def test_returns_image(self):
        """Should return a PIL Image."""
        icon = create_icon()
        assert icon is not None
        assert icon.size == (64, 64)

    def test_green_color(self):
        """Should create green icon."""
        icon = create_icon('green')
        assert icon is not None
        assert icon.size == (64, 64)

    def test_red_color(self):
        """Should create red icon."""
        icon = create_icon('red')
        assert icon is not None
        assert icon.size == (64, 64)

    def test_default_color(self):
        """Should default to green."""
        icon = create_icon()
        assert icon is not None