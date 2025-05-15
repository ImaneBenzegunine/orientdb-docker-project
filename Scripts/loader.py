import csv
from pyorient import OrientDB
from path import CLEAN_DATA_DIR
import os

csv_file_names=['companies_clean.csv','employment_clean.csv','jobs_clean.csv','users_clean.csv']
path_file = os.path.join(CLEAN_DATA_DIR, csv_file_names[0])
def load_csv_to_orientdb(path_file, class_name, orientdb_host, orientdb_port,
                        database, username, password):
    # Connect to OrientDB
    client = OrientDB(orientdb_host, orientdb_port)
    client.connect(username, password)

    # Open or create database
    if not client.db_exists(database, username+':'+password):
        client.db_create(database, 'graph', 'local')

    client.db_open(database, username, password)

    # Create class if not exists
    if class_name not in [c['name'] for c in client.command("SELECT classes.name FROM metadata:schema")]:
        client.command(f"CREATE CLASS {class_name} EXTENDS V")

    # Load CSV data
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            columns = ', '.join([f"{k}='{v}'" for k, v in row.items()])
            client.command(f"CREATE VERTEX {class_name} SET {columns}")

    print(f"Loaded {csv_path} into {class_name}")
    client.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        for idx, arg in enumerate(sys.argv):
            print("arg #{} is {}".format(idx, arg))
        print(len(sys.argv))
        sys.exit(1)

    load_csv_to_orientdb(
        path_file=sys.argv[1],
        class_name=sys.argv[2],
        database=sys.argv[3],
        orientdb_host="orientdb",
        orientdb_port=2424,
        username="root",
        password="admin"
    )
