import all_functions

while True:
    print("======= Smart Expense Tracker =======")
    print(f'''
    1. Add New Expense
    2. View All Expenses
    3. View Summary by Category
    4. View Monthly Summary
    5. Export Summary to File
    6. Exit''')
    print('===============================')
    user_choice = int(input("Enter your choice: "))
    all_functions.execute_request(user_choice)
