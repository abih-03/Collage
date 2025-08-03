import pandas as pd
import sqlite3

conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)

conn.close()

print(df[(df[['PYTHON', 'OOPS', 'WEB', 'MIL', 'STATE']] < 36).any(axis=1)])