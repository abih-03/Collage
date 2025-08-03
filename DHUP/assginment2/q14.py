import matplotlib.pyplot as plt
import pandas as pd
import sqlite3



conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)

conn.close()

plt.pie(df['PYTHON'], labels=df['RollNumber'], autopct='%1.1f%%')
plt.title("PYTHON Marks Distribution")
plt.show()
