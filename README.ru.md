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

```bash
> # Клонирование
> git clone https://github.com/cynicznykot/DevTimeTracker.git
> cd DevTimeTracker
> 
> # Создание виртуального окружэения
> python -m venv .venv
> source .venv/bin/activate  # for Linux System
> 
> venv\Scripts\activate      # for Windows System
> 
> # Установка зависимостей
> 
>pip install -r requirements.txt
```

## 🚀 Использование
 
```bash
> python -m src.cli.main
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
