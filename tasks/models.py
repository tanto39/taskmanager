from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
  name = models.CharField(verbose_name='Название', max_length=10, help_text='Название статуса')

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Статус'
    verbose_name_plural = 'Статусы'

class Priority(models.Model):
  name = models.CharField(verbose_name='Название', max_length=10, help_text='Название приоритета')
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Приоритет'
    verbose_name_plural = 'Приоритеты'

class Task(models.Model):
  title = models.CharField(verbose_name='Название', max_length=100, help_text='Название задачи')
  date_start = models.DateField(verbose_name='Дата начала', 
                                help_text='Дата начала', 
                                blank=True,
                                null=True)
  date_end = models.DateField(verbose_name='Крайний срок', 
                              help_text='Крайний срок', 
                              blank=True,
                              null=True)
  description = models.TextField(name='description', 
                                 verbose_name='Описание', 
                                 help_text='Описание задачи', 
                                 blank=True,
                                 null=True)
  status = models.ForeignKey('Status', 
                             verbose_name='Статус', 
                             on_delete=models.SET_NULL, 
                             help_text='Статус', 
                             blank=True,
                             null=True)
  priority = models.ForeignKey('Priority', 
                               verbose_name='Приоритет', 
                               on_delete=models.SET_NULL, 
                               help_text='Приоритет', 
                               blank=True,
                               null=True)
  user = models.ForeignKey(User, 
                           verbose_name='Пользователь', 
                           on_delete=models.CASCADE, 
                           help_text='Пользователь',
                           null=True)
  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = 'Задача'
    verbose_name_plural = 'Задачи'
