import pandas as pd
import sqlite3

conn = sqlite3.connect('Student_Information.db')
df = pd.read_sql_query("SELECT * FROM Student", conn)
print(df.describe())
conn.close()
