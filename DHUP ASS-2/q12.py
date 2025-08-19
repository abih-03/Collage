import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    df.plot(x='Name', y=['PYTHON','OOPS','WEB','MIL','STATE'], kind='line')
    print("Showing a Chart")
    plt.show()
    print("Chart Created Successfuly")
except Exception as e:
    print("Error plotting chart:", e)
finally:
    conn.close()
