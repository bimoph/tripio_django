# Generated by Django 4.1 on 2023-11-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_rename_email_profileuser_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profileuser",
            name="jumlah_review",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="profileuser",
            name="review_disukai",
            field=models.IntegerField(default=0),
        ),
    ]