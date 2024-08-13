import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vendor_service.settings')

app = Celery('vendor_service')
app.conf.task_routes = {
    'restraunt_app.tasks.*': {'queue': 'order.process'},
}

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
