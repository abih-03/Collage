import matplotlib.pyplot as plt
import pandas as pd
import sqlite3



conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)

conn.close()

plt.scatter(df['RollNumber'], df['WEB'], color='purple')
plt.title("WEB Marks Scatter Plot")
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.show()
