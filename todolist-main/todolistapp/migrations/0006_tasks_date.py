# Generated by Django 3.2.4 on 2021-07-02 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0005_auto_20210624_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='date',
            field=models.DateField(default=datetime.date(2021, 7, 2)),
        ),
    ]
