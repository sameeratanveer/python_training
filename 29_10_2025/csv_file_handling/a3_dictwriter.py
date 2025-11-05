'''
Create a Python dictionary list:
students = [
    {'Name': 'Sameera', 'Marks': 90, 'City': 'Hyderabad'},
    {'Name': 'Ravi', 'Marks': 82, 'City': 'Chennai'}
]

Write it to students.csv using DictWriter.
Then read back and display all students from "Hyderabad".
'''
import csv
students = [
    {'Name': 'Sameera', 'Marks': 90, 'City': 'Hyderabad'},
    {'Name': 'Ravi', 'Marks': 82, 'City': 'Chennai'}
]

try:
    with open('students2.csv', 'w', newline='') as f:
        filednames = ['Name', 'Marks', 'City']
        writer = csv.DictWriter(f, fieldnames=filednames)

        writer.writeheader()
        writer.writerows(students)
except Exception as e:
    print(e)

with open('students2.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['City'] == 'Hyderabad':
            print(row)



