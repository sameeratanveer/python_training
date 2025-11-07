'''
Q1: You have a CSV file transactions.csv with the following columns:
customer_id, transaction_date, amount, city
Tasks:
Read the file and parse transaction_date as a DateTime column.
Add a new column month extracted from transaction_date.
Compute total amount spent per city per month.
For each city, find the top 2 customers based on spending.
Save the result into a new CSV file city_monthly_top_customers.csv.
'''
import pandas as pd

# 1. Read the file and parse transaction_date as a DateTime column.
df = pd.read_csv("transactions.csv", parse_dates=["transaction_date"])

print("Data preview:")
print(df.head(), "\n")
print("Info:\n")
print(df.info(), "\n")

# 2 Add a new column month extracted from transaction_date.
df["month"] = df["transaction_date"].dt.strftime("%B")

# 3 Compute total amount spent per city per month.
city_monthly_total = (
    df.groupby(["city", "month"], as_index=False)["amount"]
    .sum()
    .rename(columns={"amount": "total_spent"})
)
print("Total amount spent per city per month:")
print(city_monthly_total.head(), "\n")

# 4. For each city, find the top 2 customers based on spending.
top_customers = (
    df.groupby(["city", "customer_id"], as_index=False)["amount"]
    .sum()
    .sort_values(["city", "amount"], ascending=[True, False])
    .groupby("city")
    .head(2)
)
print("Top 2 customers per city based on spending:")
print(top_customers, "\n")

final_result = top_customers.merge(city_monthly_total, on="city", how="left")

# Save final result to a CSV
final_result.to_csv("city_monthly_top_customers.csv", index=False)
print("Result saved to 'city_monthly_top_customers.csv'")
