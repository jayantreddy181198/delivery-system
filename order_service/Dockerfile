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
EXPOSE 8001

# Set the entrypoint script
CMD ["sh", "-c", "python manage.py migrate --database=mysql_db && python manage.py migrate --database=postgres_db && python manage.py runserver 0.0.0.0:80
01"]