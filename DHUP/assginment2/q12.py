import matplotlib.pyplot as plt
import pandas as pd
import sqlite3



conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)

conn.close()


for index, row in df.iterrows():
    plt.plot(['PYTHON', 'OOPS', 'WEB', 'MIL', 'STATE'], 
             [row['PYTHON'], row['OOPS'], row['WEB'], row['MIL'], row['STATE']], label=row['RollNumber'])

plt.title("Student Marks Line Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.show()
