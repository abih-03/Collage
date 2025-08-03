import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)

conn.close()

df['Total']= df['PYTHON'] + df['OOPS'] + df['WEB'] + df['MIL'] + df['STATE']

plt.pie(df['Total'], labels=df['RollNumber'], autopct='%1.1f%%')
plt.title("Total Marks Distribution")
plt.savefig("result.png")
plt.show()
