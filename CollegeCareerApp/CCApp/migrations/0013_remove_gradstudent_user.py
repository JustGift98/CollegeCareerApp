# Generated by Django 4.1.7 on 2023-04-03 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CCApp', '0012_rename_fname_gradstudent_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradstudent',
            name='user',
        ),
    ]