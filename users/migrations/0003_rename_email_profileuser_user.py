# Generated by Django 4.1 on 2023-09-02 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_profileuser"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profileuser",
            old_name="email",
            new_name="user",
        ),
    ]
