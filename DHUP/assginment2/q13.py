import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)

df['Total']= df['PYTHON'] + df['OOPS'] + df['WEB'] + df['MIL'] + df['STATE']

conn.close()

plt.bar(df['RollNumber'], df['Total'], color='lightblue')
plt.title("Total Marks of Students")
plt.xlabel("Roll Number")
plt.ylabel("Total Marks")
plt.show()
