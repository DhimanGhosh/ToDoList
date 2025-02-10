# Generated by Django 5.1.5 on 2025-02-10 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SiteConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("auto_delete_days", models.PositiveIntegerField(default=7)),
            ],
        ),
    ]
