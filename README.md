# Habit Tracker — Backend
 Проект по разработке бэкенда для SPA-приложения «Трекер привычек».  
Позволяет пользователям создавать, отслеживать и получать напоминания о полезных привычках.

## 🧪 Локальный запуск (без Docker)

## Требования
- Python 3.12
- Poetry
- Redis (для Celery)

# Шаги

## 1. Клонировать репозиторий
```bash
https://github.com/SergeySN84/habit_tracker.git
cd habit-tracker
```
## 2. Создайте и настройте .env
poetry install

## 3. Активировать окружение
poetry shell

## 4. Создать .env (пример ниже)
cp .env.example .env

## 5. Применить миграции
python manage.py migrate

## 6. Запустить сервер
python manage.py runserver

# Деплой на удалённый сервер

## Требования к серверу:
- Ubuntu 22.04+ 
- Публичный IP: 84.252.141.96
- Открытые порты: 22 (SSH), 80 (HTTP)

## Шаги настройки сервера:

## 1. Подключитесь по SSH
```bash
ssh test@84.252.141.96 или ssh -i ~/.ssh/yandex_deploy test@84.252.141.96
```
## 2. Установите Docker и Docker Compose
```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker test
```

## 3. Создайте рабочую директорию
```bash
mkdir -p ~/habit-tracker
cd ~/habit-tracker
```

## 4. Клонируйте проект
```bash
git clone https://github.com/SergeySN84/habit_tracker.git .
```

## 5. Создайте .env.prod
```bash
DEBUG=
SECRET_KEY=
ALLOWED_HOSTS=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=

TELEGRAM_BOT_TOKEN=
CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=
```

## 6. Запустите сервисы
```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

# CI/CD через GitHub Actions

## 1. При пуше в ветку feature/kursovaja_5 запускается workflow.
## 2. Выполняются:
- Линтинг (flake8)
- Тесты (pytest) с покрытием ≥80%
- Сборка Docker-образов

## 3. При успехе — код обновляется на сервере, контейнеры перезапускаются.

# Настройка секретов в GitHub

```bash
HOST - 84.252.141.96
USERNAME - test
SSH_KEY - содержимое приватного ключа
DEPLOY_DIR - /home/test/habit-tracker
SECRET_KEY - сгенерированный ключ для тестов
```

# После деплоя откройте:
```bash
API: http://84.252.141.96/api/
Swagger UI: http://84.252.141.96/schema/swagger-ui/
```
Если видите ошибку 502 Bad Gateway:

Проверьте, что .env.prod содержит ALLOWED_HOSTS=84.252.141.96
Убедитесь, что контейнеры запущены: docker-compose -f docker-compose.prod.yml ps
