from django.test import TestCase
from rest_framework.serializers import ValidationError
from habits.validators import validate_habit


class HabitValidatorTest(TestCase):
    def test_valid_pleasant_habit(self):
        data = {"is_pleasant": True, "reward": None, "related_habit": None}
        validate_habit(data)  # не должно быть ошибки

    def test_pleasant_habit_with_reward(self):
        data = {"is_pleasant": True, "reward": "Чай", "related_habit": None}
        with self.assertRaises(ValidationError):
            validate_habit(data)

    def test_both_reward_and_related(self):
        related = type("Habit", (), {"is_pleasant": True})()
        data = {"reward": "Чай", "related_habit": related}
        with self.assertRaises(ValidationError):
            validate_habit(data)

    def test_related_not_pleasant(self):
        related = type("Habit", (), {"is_pleasant": False})()
        data = {"related_habit": related}
        with self.assertRaises(ValidationError):
            validate_habit(data)
