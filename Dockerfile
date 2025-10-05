# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy app code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Copy Nginx config
COPY nginx.conf /etc/nginx/sites-available/default

# Start Gunicorn + Nginx
CMD service nginx start && gunicorn --config gunicorn.conf.py your_project_name.wsgi:application
