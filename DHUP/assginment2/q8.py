import pandas as pd
import sqlite3

conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)

conn.close()

df.to_csv('studentinfo.csv', index=False)

print("CSV file 'studentinfo.csv' created successfully.")