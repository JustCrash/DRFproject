from django.db import models
from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название курса",
        help_text="Напишите название курса",
    )
    preview = models.ImageField(
        upload_to="materials/preview_course",
        verbose_name="Превью",
        help_text="Вставьте картинку",
        **NULLABLE,
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Напишите описание курса",
        **NULLABLE,
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name='Владелец',
        help_text="Укажите владельца",
        **NULLABLE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название урока",
        help_text="Напишите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока",
        help_text="Напишите описание урока",
        **NULLABLE,
    )
    preview = models.ImageField(
        upload_to="materials/preview_lesson",
        verbose_name="Превью",
        help_text="Вставьте картинку",
        **NULLABLE,
    )
    video = models.FileField(
        upload_to="materials/video_lesson",
        verbose_name="Видео",
        help_text="Вставьте видео",
        **NULLABLE,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Выберите курс",
        **NULLABLE,
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name='Владелец',
        help_text="Укажите владельца",
        **NULLABLE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
