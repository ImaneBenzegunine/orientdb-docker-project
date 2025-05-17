FROM python:3.8-slim

# Set WORKDIR to the root of the container (/) 
# and copy files directly there
WORKDIR /

# Install dependencies
RUN pip install pyorient pandas

# Copy loader script (adjust path if needed)
COPY Scripts/loader.py ./Scripts/loader.py
COPY Scripts/path.py ./Scripts/path.py

# Run the script
CMD ["python", "Scripts/loader.py"]