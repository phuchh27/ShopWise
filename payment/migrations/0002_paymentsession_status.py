# Generated by Django 4.2.3 on 2023-09-01 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentsession',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]