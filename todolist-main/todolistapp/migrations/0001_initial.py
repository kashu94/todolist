# Generated by Django 3.2.4 on 2021-06-24 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]