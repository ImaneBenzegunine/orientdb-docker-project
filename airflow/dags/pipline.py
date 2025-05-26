from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def load_to_neo4j():
    from neo4j import GraphDatabase
    import pandas as pd

    driver = GraphDatabase.driver("bolt://neo4j:7687", auth=("neo4j", "StrongPass123"))

    df = pd.read_csv("/scripts/generate_data.csv")

    with driver.session() as session:
        session.run("""
        UNWIND $rows AS row
        MERGE (u:User {id: row.user_id})
        SET u.name = row.name
        """, parameters={'rows': df.to_dict('records')})

with DAG('simple_neo4j', start_date=datetime(2025,5,25), schedule_interval='@daily') as dag:
    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_to_neo4j
    )
