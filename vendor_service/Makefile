run:
	python manage.py runserver 0.0.0.0:8005 & \
	celery -A vendor_service worker -n vendor_service@%h --loglevel=info