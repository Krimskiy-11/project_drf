from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, LessonDestroyAPIView, \
    LessonRetrieveAPIView, PaymentListAPIView, PaymentCreateAPIView, PaymentUpdateAPIView, PaymentDestroyAPIView, \
    PaymentRetrieveAPIView, CourseSubscriptionView, CoursePaymentCreateAPIView
from lms.apps import LmsConfig
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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

    # pay course
    path("pay_course/", CoursePaymentCreateAPIView.as_view(), name="pay_course"),

    # payment
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path("payment/<int:pk>/update/", PaymentUpdateAPIView.as_view(), name="payment_update"),
    path("payment/<int:pk>/delete/", PaymentDestroyAPIView.as_view(), name="payment_delete"),
    path("payment/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment_retrieve"),

    # docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += router.urls
