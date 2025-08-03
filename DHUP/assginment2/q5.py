import sqlite3

conn = sqlite3.connect('Student_Information.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Student")
data = cursor.fetchall()

print("\nRollNumber | Name | PYTHON | OOPS | WEB | MIL | STATE")
for row in data:
    print(" | ".join(str(x) for x in row))

conn.close()
