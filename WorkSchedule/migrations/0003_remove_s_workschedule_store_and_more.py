# Generated by Django 4.1.7 on 2023-06-07 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WorkSchedule', '0002_alter_s_workschedule_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s_workschedule',
            name='store',
        ),
        migrations.AddField(
            model_name='s_workschedule',
            name='work_schedule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='WorkSchedule.workschedule'),
            preserve_default=False,
        ),
    ]