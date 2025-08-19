import sqlite3

try:
    conn = sqlite3.connect("Student_Information.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TRIGGER IF NOT EXISTS rollnumbercheck
    BEFORE INSERT ON Student
    FOR EACH ROW
    BEGIN
        SELECT CASE
            WHEN NEW.RollNumber NOT LIKE 'R%' AND NEW.RollNumber NOT LIKE 'r%'
            THEN RAISE(ABORT, 'RollNumber must start with R or r')
        END;
    END;
    """)
    print("Trigger created successfully.")
except Exception as e:
    print("Error creating trigger:", e)
finally:
    conn.commit()
    conn.close()
