run:
	python manage.py runserver 0.0.0.0:8004 & \
	celery -A communication_service worker -n communication_service@%h --loglevel=info