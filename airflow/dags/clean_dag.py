from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime
import sys
import os

# Add scripts to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../scripts'))

from clean import clean_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 28),
    'retries': 1,
}

with DAG(
    dag_id='clean_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['data_cleaning']
) as dag:

    start = DummyOperator(task_id='start')

    clean_task = PythonOperator(
        task_id='clean_csv_data',
        python_callable=clean_data,
        op_args=[
            '/opt/airflow/data/raw',  # This is the input_dir inside container
            '/opt/airflow/data/clean'  # Let’s store cleaned data here
        ]
    )

    end = DummyOperator(task_id='end')

    start >> clean_task >> end
    
