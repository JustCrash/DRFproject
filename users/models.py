from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Ввведите номер телефона",
        **NULLABLE
    )
    city = models.CharField(
        max_length=50, verbose_name="Город", help_text="Кажите город", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватарка",
        help_text="Загрузите аватарку",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Пользователь'),
    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты'),
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", **NULLABLE),
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", **NULLABLE),
    payment_sum = models.PositiveIntegerField(verbose_name='Cумма платежа')
    method_choices = {"наличными": "наличными", "переводом": "переводом"}
    payment_method = models.CharField(max_length=50, choices=method_choices, verbose_name='Способ оплаты')

    def __str__(self):
        return (f'{self.user}: {self.date_of_payment}, {self.payment_sum}, {self.payment_method}, '
                f'за {self.paid_course if self.paid_course else self.paid_lesson}')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
