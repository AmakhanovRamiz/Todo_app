# Generated by Django 3.0.3 on 2020-03-05 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='added_data',
            new_name='added_date',
        ),
    ]
