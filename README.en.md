# ⏱️ DevTimeTracker 

Smart time tracker for developers

## 🎯 What is it?

DevTimeTracker is a useful tool for tracking time spent in code editors.
It automatically detects:

- **Witch editors** you're working in (PyCharm, VS Code, Visual Studio и др.)
- **Witch language** programming you're coding in (Python, JavaScript, C# и др.)
- **How much time** you've spent on each language and editor.

## ✨ Features

- 🖥️ Editor detection by windows title
- 📊 Statistics by editor and language
- 💾 JSON storage
- 🔧 Flexible configuration

## 🛠️ Installation

```bash
> # Clone
> git clone https://github.com/cynicznykot/DevTimeTracker.git
> cd DevTimeTracker
> 
> # Create virtual environment
> python -m venv .venv
> source .venv/bin/activate  # for Linux System
> 
> venv\Scripts\activate      # for Windows System
> 
> # Install dependencies
> 
>pip install -r requirements.txt
```

## 🚀 Usage
 
```bash
> python -m src.cli.main
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
