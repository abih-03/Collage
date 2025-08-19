import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    df.plot(x='Name', y='OOPS', kind='line', marker='o')
    print("Showing A Chaert")
    plt.show()
    print("Chart Created Successfuly")
except Exception as e:
    print("Error plotting OOPS chart:", e)
finally:
    conn.close()
