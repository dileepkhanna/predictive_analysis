#!/bin/bash

# Manual deployment script for Railway or other platforms

echo "Starting deployment..."

# Build Docker image
echo "Building Docker image..."
docker build -t django-ml-app .

# Test the container locally (optional)
echo "To test locally, run:"
echo "docker run -p 8000:8000 -e PORT=8000 django-ml-app"

echo "For Railway deployment:"
echo "1. Push code to GitHub"
echo "2. Connect GitHub repo to Railway"
echo "3. Railway will automatically detect Dockerfile"
echo "4. Add MySQL database addon"
echo "5. Set environment variables"

echo "Deployment script completed!"