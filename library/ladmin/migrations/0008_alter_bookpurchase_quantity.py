# Generated by Django 4.2.14 on 2024-07-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ladmin", "0007_remove_book_cost_per_unit_remove_book_purchase_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookpurchase",
            name="quantity",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
