import sqlite3

try:
    conn = sqlite3.connect("Student_Information.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Student (
        RollNumber TEXT PRIMARY KEY,
        Name TEXT NOT NULL,
        PYTHON INTEGER NOT NULL CHECK(PYTHON > 0 AND PYTHON < 100),
        OOPS INTEGER NOT NULL CHECK(OOPS > 0 AND OOPS < 100),
        WEB INTEGER NOT NULL CHECK(WEB > 0 AND WEB < 100),
        MIL INTEGER NOT NULL CHECK(MIL > 0 AND MIL < 100),
        STATE INTEGER NOT NULL CHECK(STATE > 0 AND STATE < 100)
    )
    """)
    print("Table created successfully.")
except Exception as e:
    print("Error creating table:", e)
finally:
    conn.commit()
    conn.close()
