# Use Python 3.11 slim
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Optional: linters/formatters
RUN pip install black ruff isort
RUN black --check . || true
RUN ruff check . || true
RUN isort --check-only . || true


# Default command: Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
