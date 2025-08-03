import sqlite3

conn = sqlite3.connect('Student_Information.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Student (
    RollNumber TEXT PRIMARY KEY CHECK (RollNumber LIKE 'R%' OR RollNumber LIKE 'r%'),
    Name TEXT NOT NULL,
    PYTHON INTEGER NOT NULL CHECK (PYTHON > 0 AND PYTHON < 100),
    OOPS INTEGER NOT NULL CHECK (OOPS > 0 AND OOPS < 100),
    WEB INTEGER NOT NULL CHECK (WEB > 0 AND WEB < 100),
    MIL INTEGER NOT NULL CHECK (MIL > 0 AND MIL < 100),
    STATE INTEGER NOT NULL CHECK (STATE > 0 AND STATE < 100)
);
''')
conn.commit()
conn.close()
