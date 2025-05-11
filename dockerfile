# Dockerfile.data-cleaning
FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/data_cleaner.py /scripts/
COPY scripts/utils.py /scripts/

CMD ["python", "/scripts/data_cleaner.py"]