import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER='';'
    'UID='';PWD=''@123;',
    autocommit=True
)

cursor = conn.cursor()

# create a new database pyodbc
query = "CREATE DATABASE pyodbc;"
try:
    cursor.execute(query)
    print("Database pyodbc created successfully!")
except pyodbc.Error as e:
    print("Error:",e)

cursor.execute("SELECT name FROM sys.databases")
for db in cursor:
    print(db.name)

