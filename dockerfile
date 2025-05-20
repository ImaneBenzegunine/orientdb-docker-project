FROM python:3.8-slim

WORKDIR /app

# Install dependencies
RUN pip install pyorient pandas

# Copy the loader script
COPY Scripts/loader.py .

# Copy data (optional - you're also mounting it via compose)
COPY data/clean_data/ ./data/

CMD ["python", "loader.py"]