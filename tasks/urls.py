# tasks/urls.py
from django.urls import path

from .views import (
    index,
    WorkerListView,
    ProjectListView,
    TeamListView,
    TaskListView,
    WorkerDetailView,
    ProjectDetailView,
    TeamDetailView,
    TaskDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),

    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("teams/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),

]

app_name = "task"
