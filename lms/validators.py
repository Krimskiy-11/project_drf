from rest_framework.serializers import ValidationError


def validate_forbidden_link(value):
    if not value.startswith("https://www.youtube.com/"):
        raise ValidationError("Переход на сторонние образовательные платформы или личные сайты запрещена")