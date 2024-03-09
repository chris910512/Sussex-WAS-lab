# Generated by Django 5.0.2 on 2024-03-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("name", models.CharField(max_length=100)),
                ("visit_date", models.DateField()),
                ("comment_str", models.CharField(max_length=500)),
            ],
        ),
    ]