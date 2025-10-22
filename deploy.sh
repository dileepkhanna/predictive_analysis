#!/bin/bash

# Deployment script for Django application

echo "Starting deployment..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations
python manage.py migrate

# Create superuser if it doesn't exist (optional)
# python manage.py createsuperuser --noinput

echo "Deployment completed successfully!"

# Start the application with gunicorn
gunicorn main_project.wsgi:application --bind 0.0.0.0:8000