from django.db import models


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

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
