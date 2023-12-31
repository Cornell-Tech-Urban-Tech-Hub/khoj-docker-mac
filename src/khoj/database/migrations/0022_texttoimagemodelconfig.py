# Generated by Django 4.2.7 on 2023-12-04 22:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0021_speechtotextmodeloptions_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TextToImageModelConfig",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("model_name", models.CharField(default="dall-e-3", max_length=200)),
                ("model_type", models.CharField(choices=[("openai", "Openai")], default="openai", max_length=200)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
