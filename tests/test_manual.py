"""
Manual tests for detectors.

Verifies that detect_editor, extract_filename and detect_language
work correctly for various window titles.
"""

import pytest
from src.core.detectors import detect_editor, extract_filename, detect_language


class TestManualDetection:
    """Manual tests for detector functions."""

    @pytest.mark.parametrize("title,exp_editor,exp_file,exp_lang", [
        ("main.py - PyCharm", "PyCharm", "main.py", "Python"),
        ("index.js — Visual Studio Code", "VS Code", "index.js", "JavaScript"),
        ("Program.cs - Microsoft Visual Studio", "Visual Studio", "Program.cs", "C#"),
        ("Dockerfile - VS Code", "VS Code", "Dockerfile", "Dockerfile"),
        ("Makefile - VS Code", "VS Code", "Makefile", "Makefile"),
        ("CMakeLists.txt - VS Code", "VS Code", "CMakeLists.txt", "CMake"),
        ("Untitled-1 - PyCharm", "PyCharm", None, None),
        ("Calculator", None, None, None),
    ])

    def test_detection(self, title, exp_editor, exp_file, exp_lang):
        """Should detect editor, filename and language correctly."""
        assert detect_editor(title) == exp_editor
        assert extract_filename(title) == exp_file
        assert detect_language(title) == exp_lang

