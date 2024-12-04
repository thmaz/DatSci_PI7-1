import sqlite3 as lite
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

con = lite.connect('cycling_big.db')

#query = "SELECT * FROM race_results"
#df = pd.read_sql_query(query, con)

if con:
    print("Succesfully loaded at: ", con)

# Ranking the average bmi of riders per country
# In metric units: BMI = mass_kg / height_m^2
# To calculate this, one needs the height in meters and weight in kilos
# To visualise this, one will need to make a bar chart for numerical values

bmiavg_query = """
SELECT height, weight, country, rider_id 
FROM riders 
WHERE height IS NOT NULL AND weight IS NOT NULL AND country IS NOT NULL
"""

bmiavg_df = pd.read_sql_query(bmiavg_query, con)

bmiavg_df['BMI'] = bmiavg_df['weight'] / (bmiavg_df['height'] ** 2) # Using the formula for BMI as stated above

bmi_country = bmiavg_df.groupby('country')['BMI'].mean().sort_values(ascending=False) # We use the groupby() function to calculate the BMI mean per country 

plt.figure(figsize=(12, 8))
bmi_country.plot(kind='bar', color='skyblue')

plt.title('Average BMI of Riders by Country', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Average BMI', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()