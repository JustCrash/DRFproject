# Generated by Django 5.0.6 on 2024-06-19 15:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                    "title",
                    models.CharField(
                        help_text="Напишите название курса",
                        max_length=50,
                        verbose_name="Название курса",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Вставьте картинку",
                        null=True,
                        upload_to="materials/preview_course",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Напишите описание курса",
                        null=True,
                        verbose_name="Описание курса",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите владельца",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                    "title",
                    models.CharField(
                        help_text="Напишите название урока",
                        max_length=50,
                        verbose_name="Название урока",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Напишите описание урока",
                        null=True,
                        verbose_name="Описание урока",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Вставьте картинку",
                        null=True,
                        upload_to="materials/preview_lesson",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "video",
                    models.FileField(
                        blank=True,
                        help_text="Вставьте видео",
                        null=True,
                        upload_to="materials/video_lesson",
                        verbose_name="Видео",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        help_text="Выберите курс",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                        verbose_name="Курс",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите владельца",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]
