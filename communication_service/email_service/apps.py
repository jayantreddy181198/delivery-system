from django.apps import AppConfig
from django.conf import settings
from .tasks import start_rabbitmq_consumer

class EmailServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_service'

    def ready(self):
        if settings.CELERY_BROKER_URL:
            start_rabbitmq_consumer.delay()