import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    df['Total'] = df[['PYTHON','OOPS','WEB','MIL','STATE']].sum(axis=1)
    plt.pie(df['Total'], labels=df['Name'], autopct='%1.1f%%')
    plt.savefig("result.png")
    print("Pie chart saved as result.png In Your Folder")
except Exception as e:
    print("Error saving pie chart:", e)
finally:
    conn.close()
