import re
from typing import Optional, Dict, List

# =============================================================================
# EDITORS CONFIGURATION
# =============================================================================
import re

EDITOR_PATTERNS = {
    # =========================================================================
    # JetBrains IDE (cross-platform)
    # =========================================================================
    "PyCharm": ["PyCharm", "pycharm"],
    "IntelliJ IDEA": ["IntelliJ IDEA", "idea"],
    "WebStorm": ["WebStorm", "webstorm"],
    "PhpStorm": ["PhpStorm", "phpstorm"],
    "CLion": ["CLion", "clion"],
    "Rider": ["Rider", "rider"],
    "GoLand": ["GoLand", "goland"],
    "RubyMine": ["RubyMine", "rubymine"],
    "Android Studio": ["Android Studio", "androidstudio"],

    # =========================================================================
    # Microsoft IDE
    # =========================================================================
    "VS Code": [
        "Visual Studio Code",
        "VS Code",
        "VSCode",
        "vscode"
    ],
    "Visual Studio": [
        "Microsoft Visual Studio",
        "Visual Studio",
        "devenv"  # Executable name
    ],

    # =========================================================================
    # Cross-platform IDE
    # =========================================================================
    "Eclipse": ["Eclipse", "eclipse"],
    "NetBeans": ["NetBeans", "netbeans"],
    "Sublime Text": ["Sublime Text", "sublime"],
    "Atom": ["Atom", "atom"],
    "Geany": ["Geany", "geany"],
    "Code::Blocks": ["Code::Blocks", "codeblocks"],
    "Komodo": ["Komodo", "komodo"],

    # =========================================================================
    # macOS IDE
    # =========================================================================
    "Xcode": ["Xcode", "xcode"],

    # =========================================================================
    # Terminal editors (Linux/macOS)
    # =========================================================================
    "Vim": ["VIM", "vim", "gvim"],
    "Neovim": ["NVIM", "neovim", "nvim"],
    "Nano": ["nano"],

    # =========================================================================
    # Windows Editors
    # =========================================================================
    "Notepad++": ["Notepad++", "notepad++"],
}


# =============================================================================
# LANGUAGES CONFIGURATION
# =============================================================================

EXTENSION_TO_LANGUAGE = {
    # Python
    ".py": "Python",
    ".pyw": "Python",
    ".pyi": "Python",

    # JavaScript / TypeScript
    ".js": "JavaScript",
    ".jsx": "React/JavaScript",
    ".mjs": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "React/TypeScript",

    # Java / Kotlin
    ".java": "Java",
    ".kt": "Kotlin",
    ".kts": "Kotlin Script",

    # C / C++
    ".c": "C",
    ".h": "C/C++ Header",
    ".cpp": "C++",
    ".cxx": "C++",
    ".cc": "C++",
    ".hpp": "C++ Header",

    # C#
    ".cs": "C#",

    # Go
    ".go": "Golang",

    # Rust
    ".rs": "Rust",

    # Ruby
    ".rb": "Ruby",

    # PHP
    ".php": "PHP",
    ".php3": "PHP",
    ".php4": "PHP",
    ".php5": "PHP",
    ".php7": "PHP",
    ".php8": "PHP",

    # Swift
    ".swift": "Swift",

    # Dart
    ".dart": "Dart",

    # Scala
    ".scala": "Scala",

    # Web
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".scss": "SASS/SCSS",
    ".sass": "SASS/SCSS",
    ".less": "LESS",
    ".xml": "XML",

    # Data formats
    ".json": "JSON",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".toml": "TOML",

    # Shell scripts
    ".sh": "Shell Script",
    ".bash": "Shell Script",
    ".zsh": "Shell Script",
    ".fish": "Shell Script",
    ".ps1": "PowerShell",
    ".psm1": "PowerShell",

    # Databases
    ".sql": "SQL",
    ".sqlite": "SQLite",

    # Documentation
    ".md": "Markdown",
    ".markdown": "Markdown",
    ".rst": "reStructuredText",
    ".txt": "Text",

    # Configuration
    ".cfg": "Configuration",
    ".conf": "Configuration",
    ".ini": "Configuration",
    ".properties": "Properties",
    ".env": "Environment Variables",

    # Special files (no extension)
    "Dockerfile": "Dockerfile",
    "Makefile": "Makefile",
    "CMakeLists.txt": "CMake",
    ".gitignore": "Git Ignore",
    ".dockerignore": "Docker Ignore",

}

def detect_editor(window_title):
    if not window_title:
        return None

    title_lower = window_title.lower()

    for editor_name, patterns in EDITOR_PATTERNS.items():
        for pattern in patterns:
            if pattern.lower() in title_lower:
                return editor_name

    return None


def extract_filename(window_title):
    if not window_title:
        return None

    editor = detect_editor(window_title)

    if editor:
        for pattern in EDITOR_PATTERNS.get(editor, []):
            if pattern.lower() in window_title.lower():
                pos = window_title.lower().find(pattern.lower())
                clean_title = window_title[:pos].strip()
                clean_title = re.sub(r'[—\-|\[\(].*$', '', clean_title).strip()
                break

        else:
            clean_title = re.split(r'[—\-|]', window_title)[0].strip()
    else:
        clean_title = window_title

    match = re.search(r'([\w\-]+\.\w+)', clean_title)
    if match:
        return match.group(1)

    for special in ["Dockerfile", "Makefile", "CMakeLists.txt"]:
        if special.lower() in clean_title.lower():
            return special

    return None



