# Use official Python slim image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project
COPY . .

# Install linters/formatter globally in container
RUN pip install black ruff isort

# Run formatter/linter once at build (optional)
RUN black --check . || true
RUN ruff check .
RUN isort --check-only .

# Default command (can be overridden)
CMD ["python", "-m", "furniweb"]
