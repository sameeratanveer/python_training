# from add_expense import expenses
category_summary = {}
def view_summary_by_category(expenses):
    for expense in expenses:
        if expense['category'] not in category_summary:
            category_summary[expense['category']] = expense['amount']
        else:
            category_summary[expense['category']] += expense['amount']

    print("summary:")
    print(category_summary)
    # print summary report
    print(f"Category\t\t Total Spent")
    print("============================================")
    for key, value in category_summary.items():
        print(f"{key}\t\t {value}")


