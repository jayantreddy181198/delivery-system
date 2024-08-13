from django.apps import AppConfig
from django.conf import settings
from .tasks import start_rabbitmq_consumer

class RestrauntAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restraunt_app'

    def ready(self):
        if settings.CELERY_BROKER_URL:
            start_rabbitmq_consumer.delay()