# Generated by Django 4.1.4 on 2023-01-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("washapp", "0004_alter_price_ttime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="ttime",
            field=models.IntegerField(verbose_name="所需時間"),
        ),
    ]
