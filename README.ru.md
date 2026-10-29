# ⏱️ DevTimeTracker 

> Умный трекер времени для разработчиков. Автоматически отслеживает время, проведённое в ваших любимых IDE.

[![Tests](https://github.com/cynicznykot/DevTimeTracker/actions/workflows/tests.yml/badge.svg)](https://github.com/cynicznykot/DevTimeTracker/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)]()

---

## 📑 Содержание

- [Что это?](#-что-это)
- [Возможности](#-возможности)
- [Установка](#-установка)
- [Использование](#-использование)
- [Пример вывода](#-пример-вывода)
- [Поддерживаемые редакторы](#-поддерживаемые-редакторы)
- [Структура проекта](#-структура-проекта)
- [Дорожная карта](#-дорожная-карта)
- [Тестирование](#-тестирование)
- [Участие](#-участие)
- [Лицензия](#-лицензия)
- [Автор](#-автор)

---

## 🎯 Что это?

**DevTimeTracker** - это лёгкий кроссплатформенный инструмент, который автоматически
отслеживает, сколько времени вы проводите в редактора кода, таких как: **PyCharm**,
**VS Code**, **IntelliJ IDEA**, и многих других.

Просто установите, запустите и забудьте - он работает в фоне и даёт подробную статистику
о вашем времени за кодом.

---

## ✨ Возможности

- 🖥️ **Автоопределение 29+ редакторов** - PyCharm, VS Code, IntelliJ, WebStorm, Vim и другие.
- 🌍 **Кроссплатформенность** - работает на Linux, Windows и macOS.
- 📊 **Детальная статистика** - время по редакторам, дням и языкам.
- 💾 **Локальное хранение** - данные остаются на вашей машине (JSON)
- 🚀 **CLI-интерфейс** - простые команды: `start`, `stats`, `status`, `stop`.
- 🔄 **Автозапуск** - запускается автоматически с системой.
- ⚡ **Лёгкий** - минимальное потребление CPU и памяти.

---

## 🛠️ Установка

### Требования
- Python 3.10+
- Linux: `xdotool` (для определения окон)
- Windows: `pygetwindow` (устанавливается автоматически)

### Быстрый старт

```bash
# Клонирование
git clone https://github.com/cynicznykot/DevTimeTracker.git
cd DevTimeTracker

# Создание виртуального окружения
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows

# Установка зависимостей
pip install -r requirements.txt

# Установка как пакет
pip install -e .
```

## 🚀 Использование
 
```markdown
# Запуск трекера
devtime start

# Статистика
devtime stats

# Статистика за 30 дней
devtime stats -d 30

# Статус
devtime status

# Остановка
devtime stop

# Включить автозапуск
devtime autostart enable

# Выключить автозапуск
devtime autostart disable

# Экспорт статистики
devtime export --format csv
devtime export --format json

# Иконка в трее
devtime tray
```

---

## 📊 Пример вывода

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

## 🖥️ Поддерживаемые редакторы

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

### Кроссплатформенные IDEs
| Editor | Linux | Windows | macOS |
|--------|:-----:|:-------:|:-----:|
| Eclipse | ✅ | ✅ | ✅ |
| NetBeans | ✅ | ✅ | ✅ |
| Sublime Text | ✅ | ✅ | ✅ |
| Atom | ✅ | ✅ | ✅ |
| Geany | ✅ | ✅ | ✅ |

### Терминальные редакторы
| Editor | Linux | Windows | macOS |
|--------|:-----:|:-------:|:-----:|
| Vim | ✅ | ✅ | ✅ |
| Neovim | ✅ | ✅ | ✅ |
| Nano | ✅ | ❌ | ✅ |

### Платформенные редакторы
| Editor | Linux | Windows | macOS |
|--------|:-----:|:-------:|:-----:|
| Xcode | ❌ | ❌ | ✅ |
| Notepad++ | ❌ | ✅ | ❌ |

---

## 📁 Структура проекта

```bash
DevTimeTracker/
├── src/                      # Исходный код
│   ├── cli/                  # Интерфейс командной строки
│   │   ├── __init__.py       # Делает cli Python-пакетом
│   │   └── main.py           # Точка входа CLI
│   │
│   ├── core/                 # Основная логика
│   │   ├── __init__.py       # Делает core Python-пакетом
│   │   ├── detectors.py      # Определение редакторов и языков
│   │   ├── models.py         # Модели данных (Session)
│   │   ├── notifier.py       # Кроссплатформенные уведомления
│   │   ├── tracker.py        # Основной трекер времени
│   │   └── window_manager.py # Кроссплатформенное определение окон
│   │
│   ├── daemon/               # Управление автозапуском
│   │   ├── __init__.py       # Делает daemon Python-пакетом
│   │   └── autostart.py      # Управление автозапуском (Linux/Win/macOS)
│   │
│   ├── gui/                  # GUI-компоненты
│   │   ├── icons/            # Иконки приложения
│   │   ├── __init__.py       # Делает gui Python-пакетом 
│   │   ├── tray.py           # Иконка в системном трее
│   │   └── window.py         # Окно статистики
│   │
│   ├── storage/              # Хранение данных
│   │   ├── __init__.py       # Делает storage Python-пакетом
│   │   ├── exporter.py       # Экспорт в CSV/JSON
│   │   └── json_storage.py   # JSON-база данных
│   │
│   └── __init__.py
│
├── tests/                    # Тесты
│   ├── __init__.py           # Делает tests Python-пакетом
│   ├── conftest.py           # Конфигурация Pytest
│   ├── test_autostart.py     # Тесты для автозапуска
│   ├── test_detectors.py     # Тесты для детекторов
│   ├── test_language.py      # Тесты для языков
│   ├── test_manual.py        # Ручные тесты
│   ├── test_storage.py       # Тесты для JSON-хранилища
│   ├── test_tracker.py       # Тесты для трекера
│   └── test_tray.py          # Тесты для иконки в трее
│
├── .github/
│   └── workflows/
│       └── tests.yml         # CI/CD пайплайн
│
├── .gitignore                # Git ignore rules (venv, кэш, сборки)
├── install_deps.py           # Установщик зависимостей
├── LICENSE                   # MIT License
├── README.md                 # Главная документация (хаб)
├── README.ru.md              # Документация (Русский)
├── README.en.md              # Документация (English)
├── requirements.txt          # Зависимости
└── setup.py                  # Конфигурация пакета
```

## 📝 Дорожная Карта

```bash
### ✅ Сделано
- [x] Определение редакторов (29+ IDEs)
- [x] Определение языков (30+ языков)
- [x] Отслеживание времени с управлением сессиями
- [x] JSON-хранилище
- [x] CLI-интерфейс
- [x] Кроссплатформенность (Linux, Windows, macOS)
- [x] Автозапуск (Linux, Windows, macOS)
- [x] Уведомления
- [x] Экспорт в CSV/JSON

### 🚧 В процессе
- [ ] Иконка в трее (WIP)

### 📋 В планах
- [ ] Веб-дашборд
- [ ] Облачная синхронизация
- [ ] Публикация на PyPI 
```

## 🧪 Тестирование
```bash
# Запуск всех тестов
pytest tests/ -v

# С покрытием
pytest tests/ --cov=src
```

## 🤝 Участие
Приветствуются любые вклады:

- Сообщайте об ошибках
- Предлагайте новые функции
- Отправляйте pull request'ы

## 📄 Лицензия

Проект распространяется под лицензией MIT - см. [LICENSE](LICENSE)

## 🐱 Автор

**cynicznykot**

- GitHub: [@cynicznykot](https://github.com/cynicznykot)
- Проект: [DevTimeTracker](https://github.com/cynicznykot/DevTimeTracker)