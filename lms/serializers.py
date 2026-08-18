from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, CharField

from lms.models import Course, Lesson, Payment, CourseSubscription, CoursePayment
from lms.validators import validate_forbidden_link


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    link = CharField(validators=[validate_forbidden_link])
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
    is_subscribed = SerializerMethodField()

    def get_count_lesson_in_course(self, obj):
        return Lesson.objects.filter(course=obj).count()

    def get_lessons(self,obj):
        lessons = Lesson.objects.filter(course=obj)
        return LessonSerializer(lessons, many=True).data

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        if not user.is_authenticated:
            return False
        return CourseSubscription.objects.filter(user=user, course=obj).exists()

    class Meta:
        model = Course
        fields = ("id", "total", "description", "count_lesson_in_course", "lessons", "is_subscribed")

class CoursePaymentSerializer(ModelSerializer):
    class Meta:
        model = CoursePayment
        fields = "__all__"
