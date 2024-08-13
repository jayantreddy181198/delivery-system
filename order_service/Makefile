run:
	python manage.py runserver 0.0.0.0:8001 & \
	celery -A order_service worker -n worker2@%h --loglevel=info
