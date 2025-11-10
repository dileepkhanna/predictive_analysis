# Use Python 3.10 slim image (better ML library compatibility)
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    gfortran \
    libffi-dev \
    libssl-dev \
    libhdf5-dev \
    libopenblas-dev \
    liblapack-dev \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN python -m pip install --no-cache-dir --upgrade pip setuptools wheel
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create directories
RUN mkdir -p /app/data /app/staticfiles

# Collect static files (ignore errors if static dir is empty)
RUN python manage.py collectstatic --noinput --clear || echo "Static files collection skipped"

# Expose port (Railway automatically sets PORT at runtime)
EXPOSE 8000

# Run the application with better error handling and PORT fallback
CMD PORT=${PORT:-8000} && \
    echo "Starting application on port $PORT" && \
    python manage.py migrate --noinput && \
    python manage.py collectstatic --noinput --clear || true && \
    gunicorn main_project.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --threads 4 \
    --timeout 0 \
    --keep-alive 5 \
    --access-logfile - \
    --error-logfile - \
    --log-level debug \
    --capture-output \
    --enable-stdio-inheritance