FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    python3-cffi \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=10000
CMD gunicorn app:app --bind 0.0.0.0:$PORT --timeout 120 --workers 2
