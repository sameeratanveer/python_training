'''
1. You are developing a mini library system.
Write a Python program that manages a list of books where each book is represented as a dictionary containing:
title, author, year, and available (Boolean).

Requirements:

Create an initial list of at least 5 books.

Display all available books (use a for loop and conditional).

Allow a user to borrow a book:

Ask for the book title (case insensitive).

If the book is available, mark it as borrowed (available = False) and confirm.

If not available or not found, print an appropriate message.

Allow the user to return a book — change its status back to available = True.

At the end, display how many books are still available in the library.
'''
from zoneinfo import available_timezones

# books = {
#     'python programming': {
#         'author': 'Guido Von Rossum',
#         'year': 1991,
#         'available': True
#     },
#     'Pride and Prejudice':{
#        'author':'Jane Austen' ,
#         'year':1813,
#         'available': True
#     },
#     'The Great Gatsby':{
#         'author':'F. Scott Fitzgerald' ,
#         'year':1925,
#         'available': True
#     },
#     'To Kill a Mockingbird':{
#         'author':'Harper Lee' ,
#         'year':1960,
#         'available': True
#     },
#     'Anna Karenina':{
#         'author':'Leo Tolstoy' ,
#         'year':1877,
#         'available': True
#     }
# }
#
# # Q. Print the all books using for loop
# # for key,value in books.items():
# #     print(f'{key}: {value}')
#
# # 2. Display all available books:
# # print("Avaialbe books are:")
# # for key,value in books.items():
# #     if books.get(key).get('available'):
# #         print(key)
#
# # 3. Allow user to borrow a book.
# # book = input(f"Enter the book title from these {books.keys()} to borrow: ")
# # book_exist = False
# # available_flag = False
# # for key, value in books.items():
# #     if key.lower() == book.lower():
# #         book_exist = True
# #         if books[key]['available']:
# #             available_flag = False
# #             print("Available to borrow")
# #             books[key]['available'] = False
# #             print("Borrowed!")
# #             break
# # else:
# #     if not book_exist:
# #         print("Book not found")
# #     elif not available_flag:
# #         print("Not available for borrowing")
#
#
# # 4. Allow the user to return a book and changet the available status
# return_book = input(f"Return book name: {books.keys()} :")
# available_to_return = False
# for key, value in books.items():
#     if return_book.lower() == key.lower() and not books[key]['available']:
#         available_to_return = True
#         print("Book found and available to return")
#         books[key]['available'] = True
#         print("Return completed!")
# else:
#     if not available_to_return:
#         print('book not found or not available to return')


'''
2. 
Write a program that tracks employee performance for a quarter.

Each employee has:

name (string)

projects_completed (list of project names)

rating (float between 1.0 and 5.0)

Tasks:

Store data for at least 5 employees in a list of dictionaries.

For each employee:

Print total projects completed (len() of list).

If rating >= 4.5 → print "Excellent Performer"

If rating >= 3.5 → print "Good Performer"

If rating >= 2.5 → print "Average Performer"

Otherwise → print "Needs Improvement".

Find and print:

The employee with the highest rating

The average rating across all employees

Display the names of employees who worked on a project named "Data Migration" (use membership operator in).

'''

employees = {
    101:{
        'name':'emp1',
        'projects_completed':['p1','p2','p3'],
        'rating':3.0
    },
    102:{
        'name':'emp2',
        'projects_completed':['p2','p3'],
        'rating':4.5
    },
    103:{
        'name':'emp3',
        'projects_completed':['p3'],
        'rating':2.47
    },
    104:{
        'name':'emp4',
        'projects_completed':['p1','p2','p3', 'p4'],
        'rating':4.8
    },
    105:{
        'name':'emp5',
        'projects_completed':['p1','p2','p3'],
        'rating':3.91
    },
}

# 1. For each employee Print total projects completed (len() of list).
for key, value in employees.items():
    print(f'Employee id:{key}, Employee Name: {employees[key]['name']}, Total Projects: {len(employees[key]['projects_completed'])}')

# 2. If rating >= 4.5 → print "Excellent Performer"
#
# If rating >= 3.5 → print "Good Performer"
#
# If rating >= 2.5 → print "Average Performer"
#
# Otherwise → print "Needs Improvement".
for key, value in employees.items():
    print(f'Employee id:{key}, Employee Name: {employees[key]['name']}, Total Projects: {len(employees[key]['projects_completed'])}', end =' Performance: ')
    print("Excellent Performer") if employees[key]['rating'] >= 4.5 else print("Good performer") if employees[key]['rating'] >= 3.5 else print("Average performer") if employees[key]['rating'] >= 2.5 else print("Needs Improvement")

# 3. Find and printt The employee with the highest rating
ratings = []
for key, value in employees.items():
    ratings.append(employees[key]['rating'])
print(ratings)
print(f"Highest rating = {sorted(ratings, reverse=True)[0]}")

# 4. The average rating across all employees
total = 0
for key, value in employees.items():
    total += employees[key]['rating']
print(f'Average rating = {total/len(list(employees.keys()))}')

# 5. Display the names of employees who worked on a project named "Data Migration" (use membership operator in).
for key, value in employees.items():
    if 'p1' in employees[key]['projects_completed']:
        print(employees[key]['name'])