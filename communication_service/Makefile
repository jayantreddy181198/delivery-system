run:
	python manage.py runserver 0.0.0.0:8004 & \
	celery -A communication_service worker -n worker1@%h --loglevel=info