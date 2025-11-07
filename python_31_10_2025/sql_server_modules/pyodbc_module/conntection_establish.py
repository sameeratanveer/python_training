import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=;'
    'DATABASE=sameera;'
    'UID=;PWD=;'
)

cursor = conn.cursor()
cursor.execute("SELECT TOP 5 * FROM oct1.Cars;")

for row in cursor:
    print(row)

cursor.close()
conn.close()
