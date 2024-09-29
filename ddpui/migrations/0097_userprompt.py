# Generated by Django 4.2 on 2024-09-04 05:50

import ddpui.models.llm
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ddpui", "0096_llmsession_request_meta_llmsession_session_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserPrompt",
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
                ("prompt", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("log_summarization", "LOG_SUMMARIZATION"),
                            ("long_text_summarization", "LONG_TEXT_SUMMARIZATION"),
                        ],
                        default=ddpui.models.llm.LlmAssistantType["LONG_TEXT_SUMMARIZATION"],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]
