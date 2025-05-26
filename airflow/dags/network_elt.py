from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False
}

with DAG(
    'network_processing',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2025, 5, 25),
    end_date=datetime(2025, 6, 25),
    catchup=False
) as dag:
    
    spark_job = SparkSubmitOperator(
        task_id='process_network_data',
        application='/jobs/graph_processor.py',
        conn_id='spark_default',
        application_args=[],
        jars='/opt/bitnami/spark/jars/graphframes-0.8.2-spark3.1-s_2.12.jar'
    )