#!/bin/bash
# Build script for Render.com deployment

echo "Starting build process..."

# Install dependencies
pip install -r requirements.txt

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --settings=server.settings_render

# Run migrations
echo "Running migrations..."
python manage.py migrate --settings=server.settings_render

echo "Build completed successfully!"
