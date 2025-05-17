from path import CLEAN_DATA_DIR
import pandas as pd
users=pd.read_csv(f"{CLEAN_DATA_DIR}/users_clean.csv")
print(users)