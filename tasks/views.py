from django.shortcuts import render
from .models import Task


def tasks(request):
  request.user.id
  tasks = Task.objects.filter(user=request.user.id)
  return render(request, 'tasks/tasks.html', context={"tasks":tasks})
