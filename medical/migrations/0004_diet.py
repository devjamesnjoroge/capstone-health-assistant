# Generated by Django 4.0.5 on 2022-06-23 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medical', '0003_medicalhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carbohydrates', models.TextField(max_length=100)),
                ('proteins', models.TextField(max_length=100)),
                ('vitamins', models.TextField(max_length=100)),
                ('junk', models.TextField(max_length=100)),
                ('water_litres', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
