'''
Read using DictReader
Print all books priced above 300
Calculate total book value
'''
import csv

try:
    with open('books.csv', 'r') as f:
        total_books = 0
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['Price']) > 300:
                total_books += int(row['Price'])
                print(row['Title'])
except Exception as e:
    print(e)
finally:
    print(total_books)
