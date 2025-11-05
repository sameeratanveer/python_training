import csv

try:
    with open('students.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Marks', 'City'])
        writer.writerow(['Sameera', 92, 'Hyderabad'])
        writer.writerow(['Ravi', 85, 'Chennai'])
except Exception as e:
    print(e)

try:
    with open('students.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except Exception as e:
    print(e)

