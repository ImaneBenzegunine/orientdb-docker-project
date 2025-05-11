import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "output")
CLEAN_DATA_DIR = os.path.join(BASE_DIR, "data", "clean_data")

PATH_GENE_DATA = os.path.join(BASE_DIR, "data", "output")


#PATH_PROCESSED_CSV = os.path.join(BASE_DIR, "data", "outputTransfomed", "processed.csv")