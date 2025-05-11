FROM python:3.9-slim

WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only what's needed
COPY Scripts/ ./Scripts/
# Data volume
VOLUME /data

# Run as non-root user (security best practice)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

CMD ["python", "Scripts/clean_data.py"]