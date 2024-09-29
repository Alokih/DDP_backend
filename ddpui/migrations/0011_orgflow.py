# Generated by Django 4.1.7 on 2023-04-22 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ddpui", "0010_remove_orgdbt_database_remove_orgdbt_host_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrgDataFlow",
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
                ("deployment_id", models.CharField(max_length=36, unique=True)),
                ("cron", models.CharField(max_length=36, unique=True)),
                (
                    "org",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="ddpui.org"),
                ),
            ],
        ),
    ]
