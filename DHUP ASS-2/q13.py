import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    df['Total'] = df[['PYTHON','OOPS','WEB','MIL','STATE']].sum(axis=1)
    df.plot(x='Name', y='Total', kind='bar', color='orange')
    print("Showing A Chart")
    plt.show()
    print("Chart Created Successfuly")
except Exception as e:
    print("Error plotting bar chart:", e)
finally:
    conn.close()
