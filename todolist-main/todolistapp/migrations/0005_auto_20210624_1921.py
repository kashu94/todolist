# Generated by Django 3.2.4 on 2021-06-24 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0004_auto_20210624_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='taskCategory',
            field=models.ForeignKey(default=-78, on_delete=django.db.models.deletion.CASCADE, to='todolistapp.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='taskDetails',
            field=models.ForeignKey(default=-78, on_delete=django.db.models.deletion.CASCADE, to='todolistapp.details'),
            preserve_default=False,
        ),
    ]
