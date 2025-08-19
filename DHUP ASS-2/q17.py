import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

try:
    conn = sqlite3.connect("Student_Information.db")
    df = pd.read_sql_query("SELECT * FROM Student", conn)
    subjects = ['PYTHON','OOPS','WEB','MIL','STATE']
    max_marks = [df[s].max() for s in subjects]
    plt.bar(subjects, max_marks, color='green')
    print("Showing A Chart")
    plt.show()
    print("Chart Created Successfuly")
except Exception as e:
    print("Error plotting highest marks:", e)
finally:
    conn.close()
