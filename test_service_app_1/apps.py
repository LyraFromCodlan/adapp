from django.apps import AppConfig


class TestServiceApp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_service_app_1'
    verbose_name = "user_service"
    labels = "users_service"
