from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from habits.models import Habit

User = get_user_model()


class HabitViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="user@test.com", password="pass123")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place="Парк",
            time="07:00",
            action="Пробежка",
            execution_time=100,
        )

    def test_list_own_habits(self):
        response = self.client.get(reverse("habit-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)

    def test_create_habit(self):
        data = {
            "place": "Офис",
            "time": "09:00",
            "action": "Сделать зарядку",
            "execution_time": 90,
        }
        response = self.client.post(reverse("habit-list"), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Habit.objects.count(), 2)
