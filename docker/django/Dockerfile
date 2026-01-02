FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Установка Poetry
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-root --only=main

# Копируем код
COPY . .

# Делаем миграции при старте
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]