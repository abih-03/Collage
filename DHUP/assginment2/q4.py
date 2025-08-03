import sqlite3

conn = sqlite3.connect('Student_Information.db')
cursor = conn.cursor()

n = int(input("Enter number of students to insert: "))
for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    roll = input("RollNumber (Start with R or r): ")
    name = input("Name: ")
    py = int(input("PYTHON Marks (1-99): "))
    oops = int(input("OOPS Marks (1-99): "))
    web = int(input("WEB Marks (1-99): "))
    mil = int(input("MIL Marks (1-99): "))
    state = int(input("STATE Marks (1-99): "))
    
    try:
        cursor.execute("INSERT INTO Student VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (roll, name, py, oops, web, mil, state))
    except Exception as e:
        print("Error:", e)

conn.commit()
conn.close()
