from airflow.models import BaseOperator
# not in airflow 2.7+
from airflow.utils.decorators import apply_defaults
from neo4j import GraphDatabase

class Neo4jIngestOperator(BaseOperator):
    # not in airflow 2.7+
    @apply_defaults
    def __init__(self, query, neo4j_conn_id='neo4j_default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.query = query
        self.conn_id = neo4j_conn_id

    def execute(self, context):
        from airflow.hooks.base import BaseHook
        conn = BaseHook.get_connection(self.conn_id)
        
        driver = GraphDatabase.driver(
            f"bolt://{conn.host}:{conn.port}",
            auth=(conn.login, conn.password)
        )
        
        with driver.session() as session:
            session.run(self.query)