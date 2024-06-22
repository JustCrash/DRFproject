# Generated by Django 5.0.6 on 2024-06-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_options_remove_user_username_user_avatar_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                (
                    "payment_sum",
                    models.PositiveIntegerField(verbose_name="Cумма платежа"),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("наличными", "наличными"),
                            ("переводом", "переводом"),
                        ],
                        max_length=50,
                        verbose_name="Способ оплаты",
                    ),
                ),
            ],
            options={
                "verbose_name": "платеж",
                "verbose_name_plural": "платежи",
            },
        ),
    ]
