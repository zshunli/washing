# Generated by Django 4.1.4 on 2023-01-10 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("washapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="order_detail",
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
                ("orderId", models.CharField(max_length=20, verbose_name="訂單編號")),
                ("washmode", models.CharField(max_length=20, verbose_name="洗衣模式")),
                ("spinmode", models.CharField(max_length=20, verbose_name="脫水模式")),
                ("drymode", models.CharField(max_length=20, verbose_name="烘衣模式")),
                ("foldmode", models.CharField(max_length=20, verbose_name="摺衣模式")),
                ("card", models.IntegerField(default=0, verbose_name="信用卡")),
                ("oTotal", models.IntegerField(verbose_name="總金額")),
                ("oPoint", models.IntegerField(verbose_name="總點數")),
                ("C_amount", models.IntegerField(verbose_name="花費碳排總量")),
                ("oTransport", models.CharField(max_length=10, verbose_name="運送方式")),
                ("oSendcode", models.CharField(max_length=30, verbose_name="寄件條碼")),
                ("oReceivecode", models.CharField(max_length=30, verbose_name="取件條碼")),
                ("sId", models.CharField(max_length=10, verbose_name="店鋪標號")),
                ("mState", models.CharField(max_length=10, verbose_name="洗衣狀態")),
                (
                    "oDelivery",
                    models.CharField(blank=True, max_length=10, verbose_name="外送員編號"),
                ),
            ],
        ),
    ]