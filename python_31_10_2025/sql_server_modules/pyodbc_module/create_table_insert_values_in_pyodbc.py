import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=;'
    'DATABASE=pyodbc;'
    'UID='';PWD=''@123;',
    autocommit=True
)
cursor = conn.cursor()
# create schema1>
create_schema_query = """
CREATE SCHEMA schema1;
"""
try:
    cursor.execute(create_schema_query)
    print("schema1 created successfully!")
except pyodbc.Error as e:
    print("Error: ", e)
# create table inside pyodbc database.
create_table_query = """
CREATE TABLE schema1.Students(
    roll_no INT PRIMARY KEY,
    name VARCHAR(30),
    marks FLOAT
)"""

try:
    cursor.execute(create_table_query)
    print("Table 'Students' under schema1 is created successfully!")
except pyodbc.Error as e:
    print("error: ", e)

# insert data:
insert_query = """
INSERT INTO schema1.Students (roll_no, name, marks) VALUES (?,?,?)
"""

students_data =[
    (1, 'Sameera', 95),
    (2, 'Rohit', 88),
    (3, 'Kavya', 90)
]

try:
    cursor.executemany(insert_query, students_data)
    print("Records added successfully!")
except pyodbc.Error as e:
    print("Error: ",e)

