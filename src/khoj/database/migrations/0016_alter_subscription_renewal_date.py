# Generated by Django 4.2.5 on 2023-11-11 06:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0015_alter_subscription_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="renewal_date",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
