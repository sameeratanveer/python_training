import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL server};'
    'SERVER='';'
    'DATABASE=pyodbc;'
    'UID='';PWD=''@123;'
)

cursor = conn.cursor()
# create table query
table_courses_creation_query = '''
    CREATE TABLE schema1.Courses(
        CourseID INT PRIMARY KEY,
        CourseName VARCHAR(50),
        Credits INT
)'''
try:
    cursor.execute(table_courses_creation_query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("Table created successfully!")

# Add new column to the Students table.
alter_Student_add_city = '''
ALTER TABLE schema1.Students
ADD city VARCHAR(20)
'''

try:
    cursor.execute(alter_Student_add_city)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("Added city column to Students table!")

# Drop column City from Students table.
drop_city_Students_table = '''
ALTER TABLE schema1.Students DROP COLUMN city
'''
try:
    cursor.execute(drop_city_Students_table)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("Dropped Column city from the table Students")

# read the data from students.
try:
    table_students = cursor.execute("SELECT * FROM schema1.Students")
except Exception as e:
    print(e)
else:
    for row in table_students:
        print(row)



