from _datetime import datetime
import datetime
monthly_summary = {}
total = 0.0
def view_monthly_summary(expenses):
    global total
    for expense in expenses:
        month_date = str(expense['date'])
        month_date = datetime.datetime.strptime(month_date, "%Y-%m-%d")
        month_date = f'{month_date.year}-{month_date.month}'
        if month_date not in monthly_summary:
            monthly_summary[month_date] = expense['amount']
        else:
            monthly_summary[month_date] += expense['amount']
    # print
    print("========= Monthly Expense Summary =========")
    print(f"Month         Total Spent")
    print("-------------------------------------------")

    for key, value in monthly_summary.items():
        global total
        total += value
        print(f"{key}\t\t{value}")
    print("-------------------------------------------")
    print(f"Total Overall: {total:.2f}")
    print(f"===========================================")

