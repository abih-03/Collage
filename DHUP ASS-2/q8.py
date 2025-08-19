import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    df.to_csv("studentinfo.csv", index=False)
    print("Saved to studentinfo.csv")
except Exception as e:
    print("Error saving CSV:", e)
finally:
    conn.close()
