# Generated by Django 4.2.7 on 2023-11-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
