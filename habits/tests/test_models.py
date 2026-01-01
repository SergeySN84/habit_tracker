from django.test import TestCase
from django.contrib.auth import get_user_model
from habits.models import Habit

User = get_user_model()


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="pass123")

    def test_habit_str(self):
        habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time="08:00",
            action="Выпить воды",
            execution_time=60,
        )
        self.assertIn("Выпить воды", str(habit))
