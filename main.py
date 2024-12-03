import sqlite3 as lite
import sys
import pandas as pd

# denormalize dataset -> 1 dataframe

conn = lite.connect('cycling_big.db')
query = "SELECT * FROM race_results"
df = pd.read_sql_query(query, conn)

for riders in cyclist_df['rider_id']:
    print(rider_id)
