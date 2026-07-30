# ⏱️ DevTimeTracker 

Умный трекер времени для разработчиков

## 🎯 Что это?

DevTimeTracker - это полезный инструмент для разработчиков для отслеживания времени, проведенного в редакторах кода.
Он автоматически определяет:

- **В каком редакторе** вы работаете (PyCharm, VS Code, Visual Studio и др.)
- **На каком языке** программирования вы работаете (Python, JavaScript, C# и др.)
- **Сколько времени** вы потратили на каждый язык и редактор.

## ✨ Возможности

- 🖥️ Определение редакторов по заголовку окна
- 📊 Статистика по редакторам и языкам
- 💾 Хранение данных в JSON
- 🔧 Гибкая настройка

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
