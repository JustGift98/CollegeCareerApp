# Generated by Django 4.1.7 on 2023-03-25 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CCApp', '0002_gradstudent_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('collegeName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CCApp.college')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CCApp.studyprogram')),
            ],
        ),
    ]
