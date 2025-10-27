import add_expense
import view_expenses
import view_expense_by_category
import view_monthly_summary
import summary_report

def execute_request(user_request):
    if user_request == 1:
        add_expense.add_expense_in_dict() # take input.
    elif user_request == 2:
        view_expenses.view_expenses(add_expense.expenses)
    elif user_request == 3:
        view_expense_by_category.view_summary_by_category(add_expense.expenses)
    elif user_request == 4:
        view_monthly_summary.view_monthly_summary(add_expense.expenses)
    elif user_request == 5:
        view_expense_by_category.view_summary_by_category(add_expense.expenses)
        view_monthly_summary.view_monthly_summary(add_expense.expenses)
        summary_report.create_report(add_expense.expenses, view_expense_by_category.category_summary, view_monthly_summary.monthly_summary, view_monthly_summary.total)
    elif user_request == 6:
        print("Exit")
        exit()
    else:
        print("Invalid instruction")

