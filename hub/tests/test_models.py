from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from hub.models import Position, TaskType, Task, Comment


class ModelsTests(TestCase):

    def test_position_str(self):
        position = Position.objects.create(name="Test")
        self.assertEqual(str(position), position.name)

    def test_worker_str(self):
        worker = get_user_model().objects.create(
            username="test_t",
            password="1234",
            first_name="Test",
            last_name="Tester",
        )
        self.assertEqual(
            str(worker),
            f"{worker.username} ({worker.first_name} {worker.last_name})"
        )

    def test_task_type_str(self):
        task_type = TaskType.objects.create(name="Test22")
        self.assertEqual(str(task_type), task_type.name)

    def test_task_str(self):
        task = Task.objects.create(
            name="Test22",
            deadline=datetime(2025, 1, 2, 15, 1)
        )
        self.assertEqual(str(task), f"{task.name} [{task.deadline}]")

    def test_comment_str(self):
        task = Task.objects.create(
            name="Test1234",
            deadline=datetime(2025, 1, 2, 15, 1)
        )
        worker = get_user_model().objects.create(
            username="test_t",
            password="1234",
            first_name="Test",
            last_name="Tester",
        )
        comment = Comment.objects.create(
            task=task,
            author=worker,
        )
        self.assertEqual(str(comment), f"Comment on task: {comment.task.name}")
