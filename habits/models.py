from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Habit(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    place = models.CharField(max_length=255, verbose_name="Место")
    time = models.TimeField(verbose_name="Время выполнения")
    action = models.TextField(verbose_name="Действие")
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(7)],
        verbose_name="Периодичность (дней)",
    )
    reward = models.TextField(blank=True, null=True, verbose_name="Вознаграждение")
    execution_time = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(120)], verbose_name="Время на выполнение (сек)"
    )
    is_public = models.BooleanField(default=False, verbose_name="Публичная")

    def __str__(self):
        return f"{self.user.email}: {self.action} в {self.time} @ {self.place}"
