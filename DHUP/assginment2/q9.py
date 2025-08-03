import numpy as np
import pandas as pd
import sqlite3

conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)

conn.close()

ndarray = df.to_numpy()
print(ndarray)
