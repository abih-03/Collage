import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    print(df.describe())
except Exception as e:
    print("Error describing data:", e)
finally:
    conn.close()
