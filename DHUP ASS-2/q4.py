import sqlite3

try:
    conn = sqlite3.connect("Student_Information.db")
    cur = conn.cursor()
    n = int(input("Enter number of students: "))
    for _ in range(n):
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        python_m = int(input("PYTHON marks: "))
        oops_m = int(input("OOPS marks: "))
        web_m = int(input("WEB marks: "))
        mil_m = int(input("MIL marks: "))
        state_m = int(input("STATE marks: "))
        cur.execute("INSERT INTO Student VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (roll, name, python_m, oops_m, web_m, mil_m, state_m))
    print("Data inserted successfully.")
except Exception as e:
    print("Error inserting data:", e)
finally:
    conn.commit()
    conn.close()
