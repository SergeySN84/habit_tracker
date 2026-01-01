from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import CrontabSchedule, PeriodicTask
import json
from habits.models import Habit


@receiver(post_save, sender=Habit)
def create_or_update_reminder_task(sender, instance, created, **kwargs):
    if not instance.user.telegram_chat_id:
        return

    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=instance.time.minute,
        hour=instance.time.hour,
        day_of_week='*',
        day_of_month='*',
        month_of_year='*',
        timezone='UTC'
    )

    task_name = f"habit-reminder-{instance.id}"

    message = (
        "🔔 Напоминание!\n"
        f"Время: {instance.time}\n"
        f"Место: {instance.place}\n"
        f"Действие: {instance.action}"
    )
    if instance.reward:
        message += f"\nВознаграждение: {instance.reward}"
    elif instance.related_habit:
        message += f"\nПосле — приятная привычка: {instance.related_habit.action}"

    PeriodicTask.objects.update_or_create(
        name=task_name,
        defaults={
            'crontab': schedule,
            'task': 'telegram_bot.tasks.send_telegram_notification',
            'args': json.dumps([instance.user.telegram_chat_id, message]),
            'enabled': True,
        }
    )
