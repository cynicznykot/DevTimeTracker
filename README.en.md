# ⏱️ DevTimeTracker 

> Smart time tracker for developers. Automatically tracks time spent in your favorite IDEs.

[![Tests](https://github.com/cynicznykot/DevTimeTracker/actions/workflows/tests.yml/badge.svg)](https://github.com/cynicznykot/DevTimeTracker/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)]()

---

## 🎯 What is it?

**DevTimeTracker** is a lightweight, cross-platform tool that automatically tracks 
how much time you spend in code editors like **PyCharm**, **VS Code**, **IntelliJ IDEA**,
and many more.

Just install it, run it, and forget about it - it works in the background and gives 
you detailed statistics about your coding time.

---


## ✨ Features

- 🖥️ **Auto-detects 29+ editors** - PyCharm, VS Code, IntelliJ, WebStorm, Sublime, Vim and more
- 🌍 **Cross-platform** - works on Linux, Windows, and macOS
- 📊 **Detailed statistics** - time per editor, per day, per language
- 💾 **Local storage** - your data stays on your machine (JSON)
- 🚀 **CLI interface** - simple commands: `start`, `stats`, `status`, `stop`
- 🔄 **Autostart** - starts automatically with your system
- ⚡ **Lightweight** - minimal CPU and memory usage

---

## 🛠️ Installation

### Requirements
- Python 3.10+
- Linux: `xdotool` (for window detection)
- Windows: `pygetwindow` (installed automatically)

### Quick Start

```bash
> # Clone
> git clone https://github.com/cynicznykot/DevTimeTracker.git
> cd DevTimeTracker
> 
> # Create virtual environment
> python -m venv .venv
> source .venv/bin/activate  # Linux/macOS
> venv\Scripts\activate      # Windows
> 
> # Install dependencies
>pip install -r requirements.txt

# Install as a package
pip install -e .
```

## 🚀 Usage
 
```bash
# Start tracking
devtime start

# Check statistics
devtime stats

# Show last 30 days
devtime stats -d 30

# Check status
devtime status

# Stop tracking
devtime stop

# Enable autostart
devtime autostart enable

# Disable autostart
devtime autostart disable

# Export statistics
devtime export --format csv
devtime export --format json

# Run system tray icon
devtime tray
```

---

## 📊 Example Output

```text
📊 STATISTICS FOR ALL TIME
========================================
Total time:       42h 15m
Days tracked:     15
Average/day:      2h 49m
🔥 Streak:         5 days in a row!

🖥️ BY EDITOR:
  PyCharm  : ███████████████ 28h 30m (67%)
  VS Code  : █████ 10h 45m (25%)
  IntelliJ : █ 3h 0m (8%)

📝 BY LANGUAGE:
  Python   : ███████████████ 28h 30m (67%)
  JavaScript: █████ 10h 45m (25%)
  HTML/CSS : █ 3h 0m (8%)

📅 LAST 7 DAYS
========================================
2026-10-13: ████████████████████ 5h 00m
2026-10-12: █████████████ 3h 15m
2026-10-11: ██████████████████ 4h 30m
```

---

## 🖥️ Supported Editors

### JetBrains IDEs
| Editor | Linux | Windows | macOS |
|--------|:-----:|:-------:|:-----:|
| PyCharm | ✅ | ✅ | ✅ |
| IntelliJ IDEA | ✅ | ✅ | ✅ |
| WebStorm | ✅ | ✅ | ✅ |
| PhpStorm | ✅ | ✅ | ✅ |
| CLion | ✅ | ✅ | ✅ |
| GoLand | ✅ | ✅ | ✅ |
| RubyMine | ✅ | ✅ | ✅ |
| Rider | ✅ | ✅ | ✅ |
| Android Studio | ✅ | ✅ | ✅ |

### Microsoft IDEs
| Editor | Linux | Windows | macOS |
|--------|:-----:|:-------:|:-----:|
| VS Code | ✅ | ✅ | ✅ |
| Visual Studio | ❌ | ✅ | ❌ |

### Cross-platform IDEs
| Editor | Linux | Windows | macOS |
|--------|:-----:|:-------:|:-----:|
| Eclipse | ✅ | ✅ | ✅ |
| NetBeans | ✅ | ✅ | ✅ |
| Sublime Text | ✅ | ✅ | ✅ |
| Atom | ✅ | ✅ | ✅ |
| Geany | ✅ | ✅ | ✅ |

### Terminal Editors
| Editor | Linux | Windows | macOS |
|--------|:-----:|:-------:|:-----:|
| Vim | ✅ | ✅ | ✅ |
| Neovim | ✅ | ✅ | ✅ |
| Nano | ✅ | ❌ | ✅ |

### Platform-specific
| Editor | Linux | Windows | macOS |
|--------|:-----:|:-------:|:-----:|
| Xcode | ❌ | ❌ | ✅ |
| Notepad++ | ❌ | ✅ | ❌ |

## 📁 Project Structure

```bash
DevTimeTracker/
├── src/
│   ├── cli/              # Command-line interface
│   ├── core/             # Core logic (tracker, detectors)
│   ├── storage/          # Data persistence (JSON)
│   ├── daemon/           # Autostart management
│   └── gui/              # System tray icon
├── tests/                # Tests
├── setup.py              # Package configuration
├── requirements.txt
└── README.ru.md
└── README.en.md
```

## 📝 Roadmap

### ✅ Done
- [x] Editor detection (29+ IDEs)
- [x] Language detection (30+ languages)
- [x] Time tracking with session management
- [x] JSON storage
- [x] CLI interface
- [x] Cross-platform support (Linux, Windows, macOS)
- [x] Autostart (Linux, Windows, macOS)
- [x] Notifications
- [x] Export to CSV/JSON

### 🚧 In Progress
- [ ] System tray icon (WIP)

### 📋 Planned
- [ ] Web dashboard
- [ ] Cloud sync
- [ ] PyPI publication


## 🧪 Testing
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src
```

## 🤝 Contributing
Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License — see the LICENSE file for details.

## 🐱 Author

**cynicznykot**

- GitHub: [@cynicznykot](https://github.com/cynicznykot)
- Project: [DevTimeTracker](https://github.com/cynicznykot/DevTimeTracker)
