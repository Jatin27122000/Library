# Generated by Django 4.2.14 on 2024-07-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cust", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
