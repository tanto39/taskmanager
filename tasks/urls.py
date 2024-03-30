
from django.urls import path
from .views import tasks, create, edit, delete, logout_user, RegisterUser, LoginUser

urlpatterns = [
    path('', tasks, name='tasks'),
    path('create', create, name='create'),
    path('edit/<int:task_id>', edit, name='edit'),
    path('delete/<int:task_id>', delete, name='delete'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]