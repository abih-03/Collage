import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    df['Total'] = df[['PYTHON','OOPS','WEB','MIL','STATE']].sum(axis=1)
    df['Percentage'] = df['Total'] / 5
    df['Minimum'] = df[['PYTHON','OOPS','WEB','MIL','STATE']].min(axis=1)
    df['Maximum'] = df[['PYTHON','OOPS','WEB','MIL','STATE']].max(axis=1)
    print(df)
except Exception as e:
    print("Error adding columns:", e)
finally:
    conn.close()
