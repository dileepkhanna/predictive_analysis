#!/bin/bash

# Test Docker build locally before deploying to Railway

echo "Testing Docker build..."

# Build the image
docker build -t django-ml-test .

if [ $? -eq 0 ]; then
    echo "✅ Docker build successful!"
    echo "To test the container:"
    echo "docker run -p 8000:8000 -e PORT=8000 -e DEBUG=True django-ml-test"
else
    echo "❌ Docker build failed!"
    exit 1
fi