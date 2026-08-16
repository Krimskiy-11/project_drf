from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, LessonDestroyAPIView, \
    LessonRetrieveAPIView, PaymentListAPIView, PaymentCreateAPIView, PaymentUpdateAPIView, PaymentDestroyAPIView, \
    PaymentRetrieveAPIView, CourseSubscriptionView
from lms.apps import LmsConfig

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("<int:pk>/subscription/", CourseSubscriptionView.as_view(), name="subscription"),
    # lesson
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path("lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),

    # payment
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path("payment/<int:pk>/update/", PaymentUpdateAPIView.as_view(), name="payment_update"),
    path("payment/<int:pk>/delete/", PaymentDestroyAPIView.as_view(), name="payment_delete"),
    path("payment/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment_retrieve"),
]

urlpatterns += router.urls
