from django.db import models
from django.contrib.auth.models import AbstractUser


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name

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

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    members = models.ManyToManyField(Worker, related_name="teams")
    description = models.TextField(blank=True)
    lead = models.ForeignKey(
        Worker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leading_teams"
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "team"
        verbose_name_plural = "teams"

    def __str__(self):
        return self.name

    def members_count(self):
        return self.members.count()


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )
    deadline = models.DateField()

    teams = models.ManyToManyField(
        Team,
        related_name="projects"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
        ordering = ["-deadline"]

    @property
    def completion_percentage(self):
        total = self.tasks.count()
        if total == 0:
            return 0
        completed = self.tasks.filter(is_completed=True).count()
        return round((completed / total) * 100)

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


