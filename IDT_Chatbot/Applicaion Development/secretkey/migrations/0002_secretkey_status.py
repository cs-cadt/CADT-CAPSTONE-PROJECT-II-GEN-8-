# Generated by Django 5.0.6 on 2024-06-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("secretkey", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="secretkey",
            name="status",
            field=models.BooleanField(default=True),
        ),
    ]