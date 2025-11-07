import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL server};'
    'SERVER=;'
    'DATABASE=pyodbc;'
    'UID=;PWD=@123;'
)

cursor = conn.cursor()
try:
    conn.rollback()
except Exception as e:
    print(e)
else:
    print("Rollbacked successfully!")

cursor.close()
conn.close()
