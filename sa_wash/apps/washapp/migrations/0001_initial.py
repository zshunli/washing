# Generated by Django 4.1.4 on 2023-01-10 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="order",
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
                ("oUserid", models.CharField(max_length=10, verbose_name="使用者編號")),
                (
                    "oOrdertime",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="成立時間"
                    ),
                ),
                ("oFinish", models.DateTimeField(auto_now=True, verbose_name="完成時間")),
            ],
        ),
        migrations.CreateModel(
            name="price",
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
                ("modename", models.CharField(max_length=20, verbose_name="模式名稱")),
                ("ttime", models.TimeField(verbose_name="所需時間")),
                ("tprice", models.IntegerField(verbose_name="所需價格")),
                ("point", models.IntegerField(verbose_name="獲得點數")),
                ("carbon", models.IntegerField(verbose_name="碳排量")),
            ],
        ),
        migrations.CreateModel(
            name="store",
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
                ("storeID", models.CharField(max_length=10, verbose_name="店鋪編號")),
                ("storeName", models.CharField(max_length=20, verbose_name="店鋪名稱")),
                ("storeAddress", models.CharField(max_length=50, verbose_name="店鋪地址")),
            ],
        ),
    ]
