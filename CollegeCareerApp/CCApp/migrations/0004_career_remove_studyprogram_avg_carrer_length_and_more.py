# Generated by Django 4.1.7 on 2023-03-25 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CCApp', '0003_offering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carName', models.CharField(max_length=50)),
                ('opportunities', models.CharField(choices=[('H', 'HIGH'), ('M', 'MODERATE'), ('F', 'FEW')], max_length=50)),
                ('employability', models.FloatField()),
                ('avg_carrer_length', models.IntegerField()),
                ('travel_opps', models.FloatField()),
                ('starting_pay', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='studyprogram',
            name='avg_carrer_length',
        ),
        migrations.RemoveField(
            model_name='studyprogram',
            name='employability',
        ),
        migrations.RemoveField(
            model_name='studyprogram',
            name='price',
        ),
        migrations.RemoveField(
            model_name='studyprogram',
            name='travel_opps',
        ),
        migrations.AddField(
            model_name='studyprogram',
            name='entry_grade',
            field=models.CharField(choices=[('A', 'Excellent'), ('B', 'Above average'), ('C', 'Credit'), ('D', 'Pass')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='studyprogram',
            name='skills',
            field=models.CharField(default='null', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gradstudent',
            name='gender',
            field=models.CharField(default='M', max_length=50),
        ),
        migrations.AlterField(
            model_name='studyprogram',
            name='career',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CCApp.career'),
        ),
    ]
