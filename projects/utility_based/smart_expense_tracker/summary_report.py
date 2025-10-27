import datetime
def create_report(expenses, expense_by_category, monthly_summary, total):
    file_name = f'C:/Users/SameeraTanveer/OneDrive - BILVANTIS TECHNOLOGIES PRIVATE LIMITED\Desktop/python/fundamentals_14_10/projects/utility_based/smart_expense_tracker/reports/{datetime.datetime.today().strftime("%Y-%m-%d_%H-%M-%S")}_report.txt'
    with open(file_name, 'w') as file:
        file.write("=========== SMART EXPENSE TRACKER REPORT ===========\n")
        file.write(f"Generated on: {datetime.datetime.today()}\n")
        file.write("========= Category Expense Summary =========\n")
        # print summary report
        file.write(f"Category\t\t Total Spent\n")
        file.write("============================================\n")
        for key, value in expense_by_category.items():
            file.write(f"{key}\t\t {value}\n")

        file.write("\n")
        file.write("========= Monthly Expense Summary =========\n")
        file.write(f"Month         Total Spent\n")
        file.write("-------------------------------------------\n")
        for key, value in monthly_summary.items():
            file.write(f"{key}\t\t{value}\n")
        file.write("-------------------------------------------\n")
        file.write(f"Total Overall: {total:.2f}\n")
        file.write(f"===========================================\n")


