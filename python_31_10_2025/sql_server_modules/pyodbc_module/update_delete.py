import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL server};'
    'SERVER=;'
    'DATABASE=pyodbc;'
    'UID=;PWD=@123;'
)

cursor = conn.cursor()

# update Rohit marks by 5 in schema1.Students table.
update_rohit_marks_query = '''
UPDATE schema1.Students
SET marks=5
WHERE name = 'Rohit';'''

try:
    cursor.execute(update_rohit_marks_query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("Updated Rohit's marks successfully!")

cursor.close()
conn.close()
