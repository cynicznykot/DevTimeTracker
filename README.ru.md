# ⏱️ DevTimeTracker 

> Умный трекер времени для разработчиков. Автоматически отслеживает время, проведённое в ваших любимых IDEю

[![Tests](https://github.com/cynicznykot/DevTimeTracker/actions/workflows/tests.yml/badge.svg)](https://github.com/cynicznykot/DevTimeTracker/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)]()

---

## 📑 Содержание

- [Что это?](#-что-это)
- [Возможности](#-возможности)- [Установка](#️-установка)
- [Использование](#-использование)
- [Пример вывода](#-пример-вывода)
- [Поддерживаемые редакторы](#-поддерживаемые-редакторы)
- [Структура проекта](#-структура-проекта)
- [Планы](#-планы)
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

# Создание виртуального окружэения
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows

# Установка зависимостей
pip install -r requirements.txt

# Установка как пакет
pip install -e.
```

## 🚀 Использование
 
```bash
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
## 📁 Структура проекта

```bash
DevTimeTracker/
├── src/
│   ├── core/
│   │   ├── detectors.py     # Определение редакторов и языков
│   │   └── tracker.py       # Основная логика трекера
│   ├── storage/
│   │   └── json_storage.py  # Работа с JSON
│   └── cli/
│       └── main.py          # Точка входа
├── tests/                   # Тесты
├── config/                  # Конфигурация
└── README.md
```

## 📝 Дорожная Карта

```bash
- [ ] ⏳ Определение редакторов по заголовку окна
- [ ] ⏳ Определение языка по расширению
- [ ] ⏳ Цикл отслеживания времени
- [ ] ⏳ Сохранение статистики
- [ ] ⏳ Отчеты и визуализация
- [ ] ⏳ Автопаузы при бездействии
- [ ] ⏳ Графический интерфейс
- [ ] ⏳ Экспорт в CSV/Excel
```

## 📄 Лицензия

Распространяется под лицензией **MIT**. См. файл [LICENSE](LICENSE) для подробностей.

## 🐱 Автор

**cynicznykot**

- GitHub: [@cynicznykot](https://github.com/cynicznykot)
- Проект: [DevTimeTracker](https://github.com/cynicznykot/DevTimeTracker)
