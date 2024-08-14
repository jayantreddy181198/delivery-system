FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . /app/

# Expose the port that your Django application runs on
EXPOSE 8004

# Run both the Django development server and the Celery worker
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8004 & celery -A communication_service worker -n communication_service@%h --loglevel=info"]
