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
print(riders_df.describe)
print("done")
