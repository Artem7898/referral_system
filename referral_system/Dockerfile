# Stage 1: Build the Application
FROM python:3.9 AS builder

WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# ... (previous stages and setup)

# Stage 2: Create the Final Image
FROM python:3.9-slim

# ... (copying installed packages and application code)

# Install Gunicorn
RUN pip install gunicorn

# Expose the necessary port (adjust as needed)
EXPOSE 8000

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE referral_system.settings

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the Django application using gunicorn
CMD ["gunicorn", "referral_system.wsgi:application", "--bind", "0.0.0.0:8000"]

