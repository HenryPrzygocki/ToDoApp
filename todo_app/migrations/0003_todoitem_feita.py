# Generated by Django 4.0.3 on 2022-04-09 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_remove_todoitem_feita'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='feita',
            field=models.BooleanField(default=False),
        ),
    ]
