from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson, Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lesson_in_course = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_count_lesson_in_course(self, obj):
        return Lesson.objects.filter(course=obj).count()

    def get_lessons(self,obj):
        lessons = Lesson.objects.filter(course=obj)
        return LessonSerializer(lessons, many=True).data

    class Meta:
        model = Course
        fields = ("total", "description", "count_lesson_in_course", "lessons")
