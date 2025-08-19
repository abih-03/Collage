import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    plt.scatter(df['Name'], df['WEB'], color='red')
    print("Showing A Chart")
    plt.show()
    print("Chart Created Successfuly")
except Exception as e:
    print("Error plotting scatter:", e)
finally:
    conn.close()
