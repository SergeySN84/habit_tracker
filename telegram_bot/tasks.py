import requests
from celery import shared_task
from django.conf import settings


@shared_task
def send_telegram_notification(chat_id, message):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    if not bot_token or not chat_id:
        return
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Ошибка отправки Telegram: {e}")
