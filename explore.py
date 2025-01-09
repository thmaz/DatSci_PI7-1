import sqlite3 as lite
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
import numpy as np
import ast

# from sklearn.impute import KNNImputer

conn = lite.connect('cycling_big.db')

riders_df = pd.read_sql_query('SELECT * FROM riders;', conn)
races_df = pd.read_sql_query('SELECT * FROM race_results', conn)

# df = races_df.set_index('rider_id').join(riders_df.set_index('rider_id'))

conn.close()

print("Null values riders_df:\n", riders_df.isna().sum(), "\n")
print("Null values races_df:\n", races_df.isna().sum(), "\n")

races_dfnew = races_df.dropna(subset=['rider_id'])

print("Null values before dropping:\n", races_df['rider_id'].isna().sum(), "\n")
print("Null values after dropping:\n", races_dfnew['rider_id'].isna().sum(), "\n")

df = races_df.set_index('rider_id').join(riders_df.set_index('rider_id'))

df = df.reset_index()

print("Total after dropping: \n", df.isna().sum())