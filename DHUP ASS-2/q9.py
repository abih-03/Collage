import sqlite3
import pandas as pd
import numpy as np

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    arr = df.to_numpy()
    print(arr)
except Exception as e:
    print("Error converting to NumPy:", e)
finally:
    conn.close()
