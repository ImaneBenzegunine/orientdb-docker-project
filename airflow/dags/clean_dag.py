from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

import sys
sys.path.append('/opt/airflow/scripts')
from clean import clean_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='clean_dag',
    default_args=default_args,
    schedule_interval=None,  # manual trigger
    catchup=False,
    tags=['data_cleaning']
) as dag:


    clean_task = PythonOperator(
    task_id='clean_csv_data',
    python_callable=clean_data,
    op_args=['/opt/airflow/data/raw', '/opt/airflow/data/output']
    )

    clean_task
