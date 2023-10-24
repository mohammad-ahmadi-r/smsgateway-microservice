# Use an official Django image as the base
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose ports
EXPOSE 8000

# Run the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Add the Celery worker
RUN celery -A app.sms_gateway.celery worker --detach

# Add the Redis cache
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379
ENV DJANGO_REDIS_HOST=redis
ENV DJANGO_REDIS_PORT=6379