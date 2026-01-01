from rest_framework.serializers import ValidationError


def validate_habit(data):
    """Валидация привычки."""
    reward = data.get('reward')
    related_habit = data.get('related_habit')
    is_pleasant = data.get('is_pleasant', False)

    if reward and related_habit:
        raise ValidationError("Нельзя указывать и вознаграждение,"
                              " и связанную привычку.")

    if is_pleasant:
        if reward or related_habit:
            raise ValidationError("У приятной привычки не может"
                                  " быть вознаграждения или связанной привычки.")

    if related_habit and not getattr(related_habit, 'is_pleasant', False):
        raise ValidationError("Связанная привычка должна быть приятной.")

    periodicity = data.get('periodicity', 1)
    if periodicity > 7:
        raise ValidationError("Периодичность не может превышать 7 дней.")

    execution_time = data.get('execution_time')
    if execution_time and execution_time > 120:
        raise ValidationError("Время выполнения не может превышать 120 секунд.")
