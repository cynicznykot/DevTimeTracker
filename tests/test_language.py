"""
Tests for language detection.

Verifies that all languages are correctly mapped.
"""

from src.core.detectors import EXTENSION_TO_LANGUAGE, detect_language_from_filename


class TestLanguageMapping:
    """Tests for EXTENSION_TO_LANGUAGE mapping."""

    def test_python(self):
        """Should map .py to Python."""
        assert EXTENSION_TO_LANGUAGE[".py"] == "Python"
        assert EXTENSION_TO_LANGUAGE[".pyw"] == "Python"
        assert EXTENSION_TO_LANGUAGE[".pyi"] == "Python"

    def test_javascript(self):
        """Should map .js to JavaScript."""
        assert EXTENSION_TO_LANGUAGE[".js"] == "JavaScript"
        assert EXTENSION_TO_LANGUAGE[".jsx"] == "React/JavaScript"

    def test_typescript(self):
        """Should map .ts to TypeScript."""
        assert EXTENSION_TO_LANGUAGE[".ts"] == "TypeScript"
        assert EXTENSION_TO_LANGUAGE[".tsx"] == "React/TypeScript"

    def test_java(self):
        """Should map .java to Java."""
        assert EXTENSION_TO_LANGUAGE[".java"] == "Java"

    def test_cpp(self):
        """Should map .cpp to C++"""
        assert EXTENSION_TO_LANGUAGE[".cpp"] == "C++"
        assert EXTENSION_TO_LANGUAGE[".hpp"] == "C++ Header"

    def test_dockerfile(self):
        """Should map Dockerfile to Dockerfile."""
        assert EXTENSION_TO_LANGUAGE["Dockerfile"] == "Dockerfile"

    