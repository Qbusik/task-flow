from django.contrib.auth import get_user_model
from django.test import TestCase

from hub.forms import WorkerCreationForm, TaskForm
from hub.models import Position, Task


class FormsTests(TestCase):

    def test_worker_creation_form(self):
        position = Position.objects.create(name="Test")
        form_data = {
            "username": "test_tester1",
            "password1": "user336test",
            "password2": "user336test",
            "email": "test@test.com",
            "first_name": "test",
            "last_name": "user",
            "position": position.id,
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(
            form.cleaned_data["first_name"],
            form_data["first_name"]
        )
        self.assertEqual(
            form.cleaned_data["last_name"],
            form_data["last_name"]
        )
        self.assertEqual(
            form.cleaned_data["email"],
            form_data["email"]
        )

        form_data = {
            "username": "test_tester1",
            "password1": "user336test",
            "password2": "user336test",
            "email": "test@test.com",
            "first_name": "",
            "last_name": "user",
            "position": position.id,
        }
        form = WorkerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

        form_data = {
            "username": "test_tester1",
            "password1": "user336test",
            "password2": "user336test",
            "email": "test@test.com",
            "first_name": "test",
            "last_name": "",
            "position": position.id,
        }
        form = WorkerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


    def test_task_form(self):
        user = get_user_model().objects.create_user(
            username="test",
            password="user336test"
        )

        form_data = {
            "name": "Test Task",
            "description": "test description",
            "deadline": "2026-01-20T12:00",
            "priority": Task.Priority.HIGH,
            "assignees": [user.id],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
        task = form.save()
        self.assertIn(user, task.assignees.all())
