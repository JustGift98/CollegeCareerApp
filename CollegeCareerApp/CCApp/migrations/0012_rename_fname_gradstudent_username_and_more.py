# Generated by Django 4.1.7 on 2023-04-03 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CCApp', '0011_gradstudent_user_alter_gradstudent_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gradstudent',
            old_name='fname',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='gradstudent',
            name='lname',
        ),
    ]