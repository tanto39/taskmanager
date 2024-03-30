from django import forms
from .models import Status, Priority
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TaskForm(forms.Form):

  title = forms.CharField(
    label='Название',
    widget=forms.TextInput(attrs={"class":"form-control"}))
  
  date_start = forms.DateField(
    label='Дата начала',
    initial='2024-03-24',
    widget=forms.DateInput(attrs={"class":"form-control", "type":"date"}))
  
  date_end = forms.DateField(
    label='Крайний срок',
    initial='2024-05-30',
    widget=forms.DateInput(attrs={"class":"form-control", "type":"date"}))
  
  status = forms.ChoiceField(
    label='Статус',
    choices=list(Status.objects.values_list('id', 'name')),
    widget=forms.Select(attrs={"class":"form-control"}))
  
  priority = forms.ChoiceField(
    label='Приоритет',
    choices=list(Priority.objects.values_list('id', 'name')),
    widget=forms.Select(attrs={"class":"form-control"}))
  
  description = forms.CharField(
    label='Описание', 
    widget=forms.Textarea(attrs={"class":"form-control"}))
  
class RegisterUserForm(UserCreationForm):
  username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
  email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
  password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
  password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

  class Meta:
    model = User
    fields = ('username', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))