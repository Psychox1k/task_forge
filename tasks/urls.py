# tasks/urls.py
from django.urls import path

from .views import (
    index,
    WorkerListView,
    ProjectListView,
    TeamListView,
    TaskListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("tasks/", TaskListView.as_view(), name="task-list")
]

app_name = "task"
