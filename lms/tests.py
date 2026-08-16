from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import force_authenticate, APIClient

from lms.models import Course, Lesson
from users.models import User


class CourseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(total="Python-разработчик",
                                            description="Научим программировать на языке Python",
                                            owner= self.user)
        self.lesson = Lesson.objects.create(total="Основы Python",
                                            course=self.course,
                                            link="https://www.youtube.com/python_basics",
                                            description="Научим программировать на языке Python",
                                            owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("total"), self.course.total
        )

    def test_course_create(self):
        url = reverse("lms:course-list",)
        data = {
            "total": "Test",
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        data = {
            "total": "Test",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("total"), "Test"
        )

    def test_course_delete(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):
        url = reverse("lms:course-list",)
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("total"), self.lesson.total
        )

    def test_lesson_create(self):
        url = reverse("lms:lesson_create",)
        data = {
            "total": "Test",
            "course": self.course.pk,
            "link": "https://www.youtube.com/test"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse("lms:lesson_update", args=(self.lesson.pk,))
        data = {
            "total": "Test",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("total"), "Test"
        )

    def test_lesson_delete(self):
        url = reverse("lms:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("lms:lesson_list", )
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_course_subscription(self):
        url = reverse("lms:subscription",  args=(self.course.pk,))
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(), {'message': 'Подписка добавлена'} or {'message': 'Подписка удалена'}
        )
