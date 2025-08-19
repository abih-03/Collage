import sqlite3

try:
    conn = sqlite3.connect("Student_Information.db")
    print("Database created and connected successfully.")
except Exception as e:
    print("Error creating database:", e)
finally:
    conn.close()
