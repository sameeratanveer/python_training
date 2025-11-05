import csv
rows = [
    ['Aisha', 88, 'Mumbai'],
    ['Rahul', 76, 'Delhi']
]
try:
    with open('students.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
except Exception as e:
    print(e)

try:
    with open('students.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except Exception as e:
    print(e)
