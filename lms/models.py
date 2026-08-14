from django.db import models

from users.models import User


class Course(models.Model):
    total = models.CharField(
        max_length=150,
        verbose_name="Название"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="lms/image",
        blank=True,
        null=True,
        verbose_name="Превью"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец"
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    total = models.CharField(
        max_length=150,
        verbose_name="Название"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="lms/image",
        blank=True,
        null=True,
        verbose_name="Превью"
    )
    link = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Ссылка на видео"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Payment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Пользователь"
    )
    date_payment = models.CharField(
        max_length=15,
        verbose_name="Дата оплаты",
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Оплаченный курс"
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Оплаченный урок"
    )
    amount = models.PositiveIntegerField(
        verbose_name="Сумма оплаты"
    )
    card_method = models.BooleanField(
        default=False,
        verbose_name="Оплата картой"
    )
    cash_method = models.BooleanField(
        default=False,
        verbose_name="Оплата наличными"
    )

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
