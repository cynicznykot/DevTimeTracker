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


class TestDetectLanguage:
    """Tests for language detection."""

    def test_python(self):
        """Should detect Python."""
        assert detect_language_from_filename("main.py") == "Python"

    def test_javascript(self):
        """Should detect JavaScript."""
        assert detect_language_from_filename("app.js") == "JavaScript"

    def test_typescript(self):
        """Should detect TypeScript."""
        assert detect_language_from_filename("app.ts") == "TypeScript"

    def test_dockerfile(self):
        """Should detect Dockerfile."""
        assert detect_language_from_filename("Dockerfile") == "Dockerfile"

    def test_unknown_extension(self):
        """Should return None for unknown extension."""
        assert detect_language_from_filename("file.xyz") is None

    def test_full_title(self):
        """Should detect language from full window title."""
        assert detect_language("main.py - PyCharm") == "Python"
        assert detect_language("app.js - VS Code") == "JavaScript"

        