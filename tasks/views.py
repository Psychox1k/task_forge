from django.shortcuts import render
from .models import Team, Project, Task, Worker
from django.views import generic

# Create your views here.
def index(request):
    num_projects = Project.objects.count()
    num_teams = Team.objects.count()
    num_workers = Worker.objects.count()

    context = {
        "num_projects": num_projects,
        "num_teams": num_teams,
        "num_workers": num_workers,
    }

    return render(request, "tasks/index.html")


class WorkerListView(generic.ListView):
    model = Worker


class TeamListView(generic.ListView):
    model = Team


class ProjectListView(generic.ListView):
    model = Project

class TaskListView(generic.ListView):
    model = Task