import pandas as pd
import sqlite3

conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)

df['Total'] = df[['PYTHON', 'OOPS', 'WEB', 'MIL', 'STATE']].sum(axis=1)
df['Percentage'] = df['Total'] / 5
df['Minimum'] = df[['PYTHON', 'OOPS', 'WEB', 'MIL', 'STATE']].min(axis=1)
df['Maximum'] = df[['PYTHON', 'OOPS', 'WEB', 'MIL', 'STATE']].max(axis=1)
print(df)
