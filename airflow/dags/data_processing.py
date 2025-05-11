from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1
}

def validate_file_exists(filepath):
    import os
    if not os.path.exists(filepath):
        raise ValueError(f"Missing file: {filepath}")

with DAG(
    'professional_network_etl',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2025, 5, 9),
    catchup=False
) as dag:

    validate_inputs = PythonOperator(
        task_id='validate_input_files',
        python_callable=lambda: [validate_file_exists(f"/data/output/{f}") 
                                for f in ['companies.csv', 'users.csv', 
                                         'employment.csv', 'jobs.csv']]
    )

    clean_data = DockerOperator(
        task_id='clean_and_transform_data',
        image='data-cleaning:latest',
        api_version='auto',
        auto_remove=True,
        command="python /scripts/data_cleaner.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        volumes=['/data:/data', '/scripts:/scripts'],
        environment={
            'INPUT_DIR': '/data/output',
            'OUTPUT_DIR': '/data/processed'
        }
    )

    build_graph = DockerOperator(
        task_id='build_networkx_graph',
        image='networkx:latest',
        api_version='auto',
        auto_remove=True,
        command="python /scripts/graph_builder.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        volumes=['/data:/data', '/scripts:/scripts'],
        environment={
            'GRAPH_FILE': '/data/processed/professional_network.graphml'
        }
    )

    validate_inputs >> clean_data >> build_graph