"""
Tests for editor and language detection.
"""

import pytest
from src.core.detectors import (
    detect_editor,
    extract_filename,
    detect_language,
    detect_language_from_filename,
)


class TestDetectEditor:
    """Tests for detect_editor() function."""

    def test_pycharm(self):
        """Should detect PyCharm."""
        assert detect_editor("main.py - PyCharm") == "PyCharm"
        assert detect_editor("jetbrains-pycharm-ce") == "PyCharm"

    def test_vscode(self):
        """Should detect VS Code."""
        assert detect_editor("main.py - Visual Studio Code") == "VS Code"
        assert detect_editor("index.js - VS Code") == "VS Code"

    def test_visual_studio(self):
        """Should detect Intellij IDEA."""
        assert detect_editor("Main.java - Intellij IDEA") == "Intellij IDEA"

    def test_empty_title(self):
        """Should return None for empty title."""
        assert detect_editor("") is None
        assert detect_editor(None) is None

    def test_not_an_editor(self):
        """Should return None for non-editor windows."""
        assert detect_editor("Calculator") is None
        assert detect_editor("Google Chrome") is None


class TestExtractFilename:
    """Tests for extract_filename() function."""

    def test_pycharm_format(self):
        """Should extract filename from PyCharm title."""
        assert extract_filename("main.py - PyCharm") == "main.py"

    def test_vscode_format(self):
        """Should extract filename from VS Code title."""
        assert extract_filename("index.js - Visual Studio Code") == "index.js"

    def test_with_brackets(self):
        """Should handle titles with brackets."""
        assert extract_filename("README.md [GitHub] - VS Code") == "README.md"

    def test_untitled(self):
        """Should return None for untitled files."""
        assert extract_filename("Untitled-1 - PyCharm") is None

    def test_empty(self):
        """Should return None for empty title."""
        return extract_filename("") is None

    