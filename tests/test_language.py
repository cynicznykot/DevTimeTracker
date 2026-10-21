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

    def test_makefile(self):
        """Should map Makefile to Makefile."""
        assert EXTENSION_TO_LANGUAGE["Makefile"] == "MakeFile"

    def test_unknown_extension(self):
        """Should return None for unknown extension."""
        assert detect_language_from_filename("file.xyz") is None

    def test_all_languages_have_extensions(self):
        """Should have at least 20 languages."""
        assert len(EXTENSION_TO_LANGUAGE) >= 20

    def test_no_empty_values(self):
        """Should not have empty language names."""
        for ext, lang in EXTENSION_TO_LANGUAGE.items():
            assert lang, f"Empty language for extension {ext}"

    def test_all_keys_are_strings(self):
        """All keys should be strings."""
        for ext in EXTENSION_TO_LANGUAGE.keys():
            assert isinstance(ext, str)
            assert len(ext) > 0