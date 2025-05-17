FROM python:3.8-slim

WORKDIR /

# Install with specific pyorient version
RUN pip install pyorient==1.7.10 pandas

# Copy all necessary files
COPY Scripts/loader.py .
COPY data/clean_data/ /app/data/

CMD ["python", "Scripts/loader.py"]