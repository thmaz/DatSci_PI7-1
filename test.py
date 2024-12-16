import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('cycling_big.db')  # Replace with your actual database file
cur = conn.cursor()

# Query to get columns information
cur.execute("PRAGMA table_info(race_results);")  # Replace 'race_results' with your table name
columns = cur.fetchall()

# Start the SQL to count NULLs
null_count_sql = "SELECT "

# Add each column's NULL count
null_count_sql += ", ".join([f"SUM(CASE WHEN {column[1]} IS NULL THEN 1 ELSE 0 END) AS {column[1]}_null" for column in columns])

null_count_sql += " FROM race_results;"  # Replace 'race_results' with your table name

# Execute the query
cur.execute(null_count_sql)

# Fetch the result
null_counts = cur.fetchone()

# Format and print the results
print("\nMissing Values Count for Each Column:")
print("-" * 50)  # Separator for better readability
print(f"{'Column Name':<30} {'Missing Values'}")  # Header with alignment
print("-" * 50)

# Print each column's null count with aligned formatting
for i, column in enumerate(columns):
    column_name = column[1]  # Column name is the second element in the tuple
    missing_values = null_counts[i]
    print(f"{column_name:<30} {missing_values:>15}")

print("-" * 50)  # Footer to close the table

# Close the connection
conn.close()
