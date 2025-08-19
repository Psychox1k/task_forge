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
    TaskTypeListView, TagCreateView, TaskTypeCreateView, TagUpdateView, TaskTypeUpdateView, TagDeleteView,
    TaskTypeDeleteView, TeamUpdateView, TeamDeleteView, WorkerDeleteView, WorkerUpdateView, ProjectDeleteView,
    ProjectUpdateView,
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
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tasktypes/create/", TaskTypeCreateView.as_view(), name="tasktype-create"),

    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("teams/<int:pk>/update/", TeamUpdateView.as_view(), name="team-update"),
    path("tasktypes/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="tasktype-update"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("projects/<int:pk>/update/", ProjectUpdateView.as_view(), name="project-update"),

    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tasktypes/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="tasktype-delete"),
    path("teams/<int:pk>/delete/", TeamDeleteView.as_view(), name="team-delete"),
    path("workers/<int:pk>delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project-delete"),

]

app_name = "task"

