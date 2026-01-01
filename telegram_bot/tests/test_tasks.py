from unittest.mock import patch
from django.test import TestCase
from telegram_bot.tasks import send_telegram_notification


class TelegramTaskTest(TestCase):
    @patch("telegram_bot.tasks.requests.post")
    def test_send_telegram_notification(self, mock_post):
        send_telegram_notification("123456", "Test message")
        mock_post.assert_called_once()
