import matplotlib.pyplot as plt
import pandas as pd
import sqlite3



conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)

conn.close()

subjects = ['PYTHON', 'OOPS', 'WEB', 'MIL', 'STATE']
max_marks = [df[sub].max() for sub in subjects]

plt.bar(subjects, max_marks, color='lightgreen')
plt.title("Highest Marks in Each Subject")
plt.ylabel("Marks")
plt.show()
