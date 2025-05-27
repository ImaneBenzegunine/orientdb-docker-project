from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from neo4j import GraphDatabase
from airflow.hooks.base import BaseHook
from operators.neo4j_operator import Neo4jIngestOperator

class Neo4jIngestOperator(BaseOperator):
    @apply_defaults
    def __init__(self, query, neo4j_conn_id='neo4j_default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.query = query
        self.neo4j_conn_id = neo4j_conn_id

    def execute(self, context):
        conn = BaseHook.get_connection(self.neo4j_conn_id)
        uri = f"bolt://{conn.host}:{conn.port}"
        driver = GraphDatabase.driver(uri, auth=(conn.login, conn.password))

        with driver.session() as session:
            session.run(self.query)
        self.log.info("Query executed successfully")
