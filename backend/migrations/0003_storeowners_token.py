# Generated by Django 4.2 on 2023-04-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_storeowners_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeowners',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
