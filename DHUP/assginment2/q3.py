import sqlite3

conn = sqlite3.connect('Student_Information.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TRIGGER IF NOT EXISTS rollnumbercheck
BEFORE INSERT ON Student
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN NEW.RollNumber NOT LIKE 'R%' AND NEW.RollNumber NOT LIKE 'r%'
        THEN RAISE(ABORT, 'RollNumber must start with R or r')
    END;
END;
''')
conn.commit()
conn.close()
