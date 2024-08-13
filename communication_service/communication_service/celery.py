import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'communication_service.settings')

app = Celery('communication_service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_routes = {
    'email_service.tasks.*': {'queue': 'orders.confirmations'},
}
app.autodiscover_tasks()

