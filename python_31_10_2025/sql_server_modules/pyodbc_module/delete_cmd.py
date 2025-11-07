import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL server};'
    'SERVER='';'
    'DATABASE=pyodbc;'
    'UID='';PWD=''@123;'
)

cursor = conn.cursor()

# delete the student whose marks are less than 90.
delete_students_query = '''
DELETE FROM schema1.Students
WHERE marks <= 90;
'''
try:
    cursor.execute(delete_students_query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("Deleted students whose marks are less than 90")

cursor.close()
conn.close()
