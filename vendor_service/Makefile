run:
	python manage.py runserver 0.0.0.0:8003 & \
	celery -A vendor_service worker -n vendor_service@%h --loglevel=info