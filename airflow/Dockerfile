FROM apache/airflow:2.5.0

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR 1

# Install system dependencies
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-11-jre-headless \ 
    && rm -rf /var/lib/apt/lists/* 


# Switch back to airflow user
USER airflow
RUN pip install apache-airflow-providers-apache-spark
# Install Python packages
COPY requirements.txt .
RUN pip install --user -r requirements.txt



# Set Spark environment variables
ENV SPARK_HOME=/usr/local/spark
ENV PATH=$SPARK_HOME/bin:$PATH
ENV PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/scripts"

# Dockerfile fix

