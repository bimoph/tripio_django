# Generated by Django 4.1 on 2023-11-06 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("review", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="reply",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
