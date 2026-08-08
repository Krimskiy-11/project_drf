from django.contrib import admin
from .models import Course, Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "total", "course")
    search_fields = ("total",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "total")
    list_filter = ("total",)
    search_fields = (
        "total",
        "description",
    )

