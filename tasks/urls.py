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
    TaskDetailView, TeamCreateView, ProjectCreateView, WorkerCreateView, TaskCreateView, UserTaskListView, TagListView,
    TaskTypeListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("mytasks/", UserTaskListView.as_view(), name="mytask-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tasktypes/", TaskTypeListView.as_view(), name="tasktype-list"),

    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("teams/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),

    path("teams/create/", TeamCreateView.as_view(), name="team-create"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "task"
