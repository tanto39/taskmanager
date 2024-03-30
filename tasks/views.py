from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, RegisterUserForm, LoginUserForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .utils import DataMixin, check_access_task
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def tasks(request):
  request.user.id
  tasks = Task.objects.filter(user=request.user.id)
  return render(request, 'tasks/tasks.html', context={"tasks":tasks})

@login_required(login_url='login')
def create(request):
  message = ''
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      task = Task.objects.create(
        title=request.POST.get('title'),
        date_start=request.POST.get('date_start'),
        date_end=request.POST.get('date_end'),
        description=request.POST.get("description"),
        priority_id=request.POST.get("priority"),
        status_id=request.POST.get("status"),
        user_id=request.user.id)
      task.save()
      return redirect('tasks')
    else:
      message = 'Форма заполнена неверно'

  taskform = TaskForm()
  return render(request, 'tasks/task.html', context={"title":"Создать задачу", "form":taskform, "message":message})

@login_required(login_url='login')
def edit(request, task_id):
  message = ''
  task = Task.objects.filter(id=task_id)
  if not check_access_task(request=request, task=task[0]):
    return redirect('tasks')
  
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      task.update(
        title=request.POST.get('title'),
        date_start=request.POST.get('date_start'),
        date_end=request.POST.get('date_end'),
        description=request.POST.get("description"),
        priority_id=request.POST.get("priority"),
        status_id=request.POST.get("status"),
        user_id=request.user.id)
      #task.save()
      message = 'Задача сохранена'
    else:
      message = 'Форма заполнена неверно'
  else:
    initial_task = {
      "title": task[0].title,
      "date_start": str(task[0].date_start),
      "date_end": str(task[0].date_end),
      "description": task[0].description,
      "priority": task[0].priority.id,
      "status": task[0].status.id,
    }
    form = TaskForm(initial = initial_task)
  
  return render(request, 'tasks/task.html', 
                context={"title":"Изменить задачу", "task_id":task[0].id, "form":form, "message":message})

@login_required(login_url='login')
def delete(request, task_id):
  task = Task.objects.filter(id=task_id)
  
  if not check_access_task(request=request, task=task[0]):
    return redirect('tasks')

  task.delete()
  return redirect('tasks')

def logout_user(request):
    logout(request)
    return redirect('login')
  
class RegisterUser(DataMixin, CreateView):
  form_class = RegisterUserForm
  template_name = 'tasks/register.html'
  success_url = reverse_lazy('login')

  def get_context_data(self, *, object_list=None, **kwargs):
    context = super().get_context_data(**kwargs)
    c_def = self.get_user_context(title="Регистрация")
    return dict(list(context.items()) + list(c_def.items()))

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'tasks/login.html'
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))