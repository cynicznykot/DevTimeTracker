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

## 📁 Project Structure

```bash
DevTimeTracker/
├── src/
│   ├── core/
│   │   ├── detectors.py     # Editor and language detection
│   │   └── tracker.py       # Main tracking logic
│   ├── storage/
│   │   └── json_storage.py  # JSON operations
│   └── cli/
│       └── main.py          # Entry point
├── tests/                   # Tests
├── config/                  # Configuration
└── README.md
```

## 📝 Roadmap

```bash
- [ ] ⏳ Editor detection by window title
- [ ] ⏳ Language detection by extension
- [ ] ⏳ Tracking loop
- [ ] ⏳ Statistics storage
- [ ] ⏳ Reports and visualization
- [ ] ⏳ Auto-pause on inactivity
- [ ] ⏳ GUI
- [ ] ⏳ CSV/Excel export
```

## 📄 License

Distributed under the MIT. See the LICENSE file for details.

## 🐱 Author

**cynicznykot**

- GitHub: [@cynicznykot](https://github.com/cynicznykot)
- Проект: [DevTimeTracker](https://github.com/cynicznykot/DevTimeTracker)
