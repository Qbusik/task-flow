from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from hub.models import Task, Position, TaskType

TASK_URL = reverse("hub:task-list")
TASK_TYPE_URL = reverse("hub:task_type-list")
WORKER_URL = reverse("hub:worker-list")
POSITION_URL = reverse("hub:position-list")


class PublicTaskTest(TestCase):

    def test_login_required(self):
        response = self.client.get(TASK_URL)
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(TASK_TYPE_URL)
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(WORKER_URL)
        self.assertNotEqual(response.status_code, 200)
        response = self.client.get(POSITION_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivatePagesAndSearchTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="123vc123a",
            first_name="test",
            last_name="user",
        )
        self.client.force_login(self.user)

    def test_retrieve_and_search(self):
        Task.objects.create(name="TestTask11", deadline=datetime(2025, 1, 2, 15, 1))
        Task.objects.create(name="TestTask22", deadline=datetime(2025, 1, 2, 15, 1))
        TaskType.objects.create(name="TestTaskType11")
        TaskType.objects.create(name="TestTaskType22")
        Position.objects.create(name="Position11")
        Position.objects.create(name="Position22")


        # Task Test

        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks),
        )
        self.assertTemplateUsed(response, "hub/task_list.html")

        response = self.client.get(TASK_URL, {"name": "TestTask11"})
        self.assertEqual(response.status_code, 200)
        result = list(response.context["task_list"])
        self.assertEqual(len(result), 1)

        response = self.client.get(TASK_URL, {"name": ""})
        self.assertEqual(response.status_code, 200)
        result = list(response.context["task_list"])
        self.assertEqual(len(result), 2)

        # Task Type Test

        response = self.client.get(TASK_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        task_types = TaskType.objects.all()
        self.assertEqual(
            list(response.context["task_type_list"]),
            list(task_types),
        )
        self.assertTemplateUsed(response, "hub/tasktype_list.html")

        response = self.client.get(TASK_TYPE_URL, {"name": "TestTaskType11"})
        self.assertEqual(response.status_code, 200)
        result = list(response.context["task_type_list"])
        self.assertEqual(len(result), 1)

        response = self.client.get(TASK_TYPE_URL, {"model": ""})
        self.assertEqual(response.status_code, 200)
        result = list(response.context["task_type_list"])
        self.assertEqual(len(result), 2)

        # Position Test

        response = self.client.get(POSITION_URL)
        self.assertEqual(response.status_code, 200)
        positions = Position.objects.all()
        self.assertEqual(
            list(response.context["position_list"]),
            list(positions),
        )
        self.assertTemplateUsed(response, "hub/position_list.html")

        response = self.client.get(POSITION_URL, {"name": "Position11"})
        self.assertEqual(response.status_code, 200)
        result = list(response.context["position_list"])
        self.assertEqual(len(result), 1)

        response = self.client.get(POSITION_URL, {"name": ""})
        self.assertEqual(response.status_code, 200)
        result = list(response.context["position_list"])
        self.assertEqual(len(result), 2)

        # Worker Test

        response = self.client.get(WORKER_URL)
        self.assertEqual(response.status_code, 200)
        workers = get_user_model().objects.all()
        self.assertEqual(
            list(response.context["worker_list"]),
            list(workers),
        )
        self.assertTemplateUsed(response, "hub/worker_list.html")

        response = self.client.get(WORKER_URL, {"username": "test"})
        self.assertEqual(response.status_code, 200)
        result = list(response.context["worker_list"])
        self.assertEqual(len(result), 1)

        response = self.client.get(WORKER_URL, {"username": "aaaa"})
        self.assertEqual(response.status_code, 200)
        result = list(response.context["worker_list"])
        self.assertEqual(len(result), 0)
