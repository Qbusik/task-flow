from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):

    class Priority(models.IntegerChoices):
        LOW = 1, "Low"
        MEDIUM = 2, "Medium"
        HIGH = 3, "High"
        URGENT = 4, "Urgent"

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    priority = models.IntegerField(
        choices=Priority.choices,
        default=Priority.LOW,
    )
    task_type = models.ForeignKey(
        TaskType, on_delete=models.SET_NULL, null=True, blank=True
    )
    assignees = models.ManyToManyField(Worker, blank=True, related_name="tasks")

    class Meta:
        ordering = ["-priority", "deadline"]

    def __str__(self):
        return f"{self.name} [{self.deadline}]"


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    def __str__(self):
        return f"Comment on task: {self.task.name}"
