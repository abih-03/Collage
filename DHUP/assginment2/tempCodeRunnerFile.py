conn=sqlite3.connect('Student_Information.db')
df=pd.read_sql_query("select* from Student",conn)