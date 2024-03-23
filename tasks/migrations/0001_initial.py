# Generated by Django 5.0.3 on 2024-03-23 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название приоритета', max_length=10, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название статуса', max_length=10, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название задачи', max_length=100, verbose_name='Название')),
                ('date_start', models.DateField(blank=True, help_text='Дата начала', null=True, verbose_name='Дата начала')),
                ('date_end', models.DateField(blank=True, help_text='Крайний срок', null=True, verbose_name='Крайний срок')),
                ('Description', models.TextField(blank=True, help_text='Описание задачи', null=True, verbose_name='Описание')),
                ('priority', models.ForeignKey(blank=True, help_text='Приоритет', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.priority', verbose_name='Приоритет')),
                ('status', models.ForeignKey(blank=True, help_text='Статус', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.status', verbose_name='Статус')),
            ],
        ),
    ]