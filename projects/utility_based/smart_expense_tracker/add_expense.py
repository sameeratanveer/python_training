'''
Expense format:
{
  "date": "2025-10-23",
  "category": "Food",
  "description": "Lunch at café",
  "amount": 120.50
}
'''
import datetime
from datetime import datetime
from datetime import date

expenses = []

def take_expense_input():
    print("welcome to Smart Expense tracker.")
    print("To add a new expense, Please give following information")

    # take inputs:
    date_input = input( "Please Enter the Date in YYYY-MM-DD format. If not leave it empty, it will take current date.: ")
    category_input = input("Enter the expense Category, Example: Food, Travel, Education. Please make sure spelling is correct!: ")
    description_input = input("Enter the description of the expense.: ")
    amount_input = float(input("Enter the amount. Amount must be  > 0:"))

    # validates input checks (amount >0, add date if null or empty string.., category lowercase.)
    if date_input is None or date_input == '' or date_input == ' ':
        date_input = date.today() # todat's date.
    else:
        format_string = "%Y-%m-%d"
        date_input = datetime.strptime(date_input, format_string).date()
    category_input = category_input.strip().lower()
    description_input = description_input.strip()
    while amount_input < 0.0:
        amount_input = float(input(f"Invalid Amount as input. Please enter amount > 0:"))

    return date_input, category_input, description_input, amount_input

def add_expense_in_dict():
    date_input, category_input, description_input, amount_input = take_expense_input()
    expenses.append({
        "date": date_input,
        "category": category_input,
        "description": description_input,
        "amount": amount_input
    })
    print("Expense added successfully!")




