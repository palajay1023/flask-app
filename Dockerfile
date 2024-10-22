# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory inside container to /backend
WORKDIR /backend

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose port 8080 (Cloud Run default)
EXPOSE 8080

# Command to run the application
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:create_app()