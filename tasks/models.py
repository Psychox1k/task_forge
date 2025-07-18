from django.db import models
from django.contrib.auth.models import AbstractUser


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name

class Task(models.Model):

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("critical", "Critical"),
    ]

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default="medium")

    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tasks")

    assignees = models.ManyToManyField(
        Worker,
        related_name="assigned_tasks"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="tasks"
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks"
    )

    class Meta:
        ordering = ["-deadline"]

    def __str__(self):
        return f"{self.name} (priority: {self.priority})"

class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):

    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workers"
    )



    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    @property
    def completed_tasks(self):
        return self.assigned_tasks.filter(is_completed=True)

    @property
    def pending_tasks(self):
        return self.assigned_tasks.filter(is_completed=False)

    def __str__(self):
        return f"{self.username} ({self.get_full_name()})"

