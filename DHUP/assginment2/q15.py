import matplotlib.pyplot as plt
import pandas as pd
import sqlite3



conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)

conn.close()

plt.plot(df['RollNumber'], df['OOPS'], marker='o', linestyle='-', color='blue')
plt.title("OOPS Marks")
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
