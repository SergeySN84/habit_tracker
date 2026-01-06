# Habit Tracker — Backend
 Проект по разработке бэкенда для SPA-приложения «Трекер привычек».  
Позволяет пользователям создавать, отслеживать и получать напоминания о полезных привычках.

## 🧪 Локальный запуск (без Docker)

### Требования
- Python 3.12
- Poetry
- Redis (для Celery)

### Шаги
```bash
# 1. Клонировать репозиторий
https://github.com/SergeySN84/habit_tracker.git
cd habit-tracker

# 2. Установить зависимости
poetry install

# 3. Активировать окружение
poetry shell

# 4. Создать .env (пример ниже)
cp .env.example .env

# 5. Применить миграции
python manage.py migrate

# 6. Запустить сервер
python manage.py runserver