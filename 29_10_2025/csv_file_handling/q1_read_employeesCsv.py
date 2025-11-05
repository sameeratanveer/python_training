'''
Read the CSV and print only names of employees with salary > 65000.
Handle ValueError if salary is not a number.
'''

import csv

try:
    with open('employees.csv') as f:
        data = csv.reader(f)
        for row in data:
            # print(row)
            try:
                if int(row[2]) > 65000:
                    print(row[0])
            except ValueError:
                print("Salary is not a number")
except Exception as e:
    print(e)

# read :

