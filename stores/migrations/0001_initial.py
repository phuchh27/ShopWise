# Generated by Django 4.1.7 on 2023-05-09 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('FOOD', 'FOOD'), ('COFFEE', 'COFFEE'), ('FASHION', 'FASHION'), ('OTHER', 'OTHER')], max_length=255)),
                ('shopname', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]