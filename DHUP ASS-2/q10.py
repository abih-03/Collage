import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    print(df[df['PYTHON'] > 85])
except Exception as e:
    print("Error filtering data:", e)
finally:
    conn.close()
