# Generated by Django 3.2.4 on 2021-06-24 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0003_tasks_taskuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='taskCategory',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='taskUser',
        ),
    ]
