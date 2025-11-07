'''
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL server};'
    'SERVER='
    'DATABASE=pyodbc;'
    'UID=;PWD=;'
)
'''
import pymssql
conn = pymssql.connect(
    server='',
    port='',
    user='',
    password=''
)

cursor = conn.cursor()

# create DB.. pymssql
create_DB_query = '''
CREATE DATABASE pymssql;
GO
'''

try:
    cursor.execute(create_DB_query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("Database created successfully!")

cursor.close()
conn.close()

# use the pymssql database.
conn = pymssql.connect(
    server='',
    port='',
    user='',
    password='',
    database='pymssql'
)

cursor= conn.cursor()

# create schema  schema1
schema_query = '''
CREATE SCHEMA schema1;
'''

try:
    cursor.execute(schema_query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("Schema 1 created successfully!")

# create a table.
table_creation_query = '''
CREATE TABLE schema1.LibraryBooks(
    book_id INT PRIMARY KEY,
    book_name VARCHAR(40),
    author_name VARCHAR(30),
    rack_no VARCHAR(10),
    available_copies INT);
'''

try:
    cursor.execute(table_creation_query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("Table created successfully!")

# insert values:
insert_values_query = '''
INSERT INTO schema1.LibraryBooks(?,?,?,?,?) VALUES
(1,	'Data Structures',	'Mark Allen',	'R1',	3),
(2,	'Database Management',	'James Martin',	'R2',	0)
(3,	'Python Programming',	'Eric Matthews',	'R3',	5)
(4,	'Machine Learning Basics',	'Tom White',	'R4',	2)
(5,	'Cloud Computing',	'Andrew Miller',	'R5',	0)
(6,	'Artificial Intelligence',	'Stuart Russell',	'R6',	4);
'''

try:
    cursor.execute(insert_values_query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("Insered all the values successfully!")


# read the data:
try:
    cursor.execute("SELECT * FROM schema1.LibraryBooks")
except Exception as e:
    print(e)
else:
    for row in cursor.fetchall():
        print(row)

cursor.close()
conn.close()
