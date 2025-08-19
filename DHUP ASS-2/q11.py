import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    low = df[(df['PYTHON'] < 36) | (df['OOPS'] < 36) | (df['WEB'] < 36) | (df['MIL'] < 36) | (df['STATE'] < 36)]
    print(low)
except Exception as e:
    print("Error filtering data:", e)
finally:
    conn.close()
