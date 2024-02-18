# Generated by Django 4.1 on 2024-02-12 20:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galeria', '0007_alter_fotografia_data_fotografia'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 12, 17, 3, 23, 265690)),
        ),
    ]
