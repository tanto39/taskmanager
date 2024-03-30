from .models import Task

def check_access_task(request, task:Task) -> bool:
  if request.user.id == task.user_id:
    return True

class DataMixin:
  def get_user_context(self, **kwargs):
    context = kwargs
    return context