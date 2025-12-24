FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN pip install black ruff isort
RUN black --check . 
RUN ruff check . 
RUN isort --check-only . 


# Default command: Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
