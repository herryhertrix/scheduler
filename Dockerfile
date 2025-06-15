FROM python:3.10-slim

# Install dep OS yang umum (opsional)
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy semua file project
COPY . .

# Install deps Python
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan script utama
CMD ["python", "main.py"]