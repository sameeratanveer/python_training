'''
Conditional Filtering (Real Use Case)
You have daily customer counts in a store:
customers = pd.Series(
    [120, 80, 95, 150, 200, 170, 65],
    index=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
)
Tasks:
Print days with more than 100 customers.
Print days with fewer than the weekly average.
Sort the Series by customer count descending.
'''
import pandas as pd
customers = pd.Series(
    [120, 80, 95, 150, 200, 170, 65],
    index=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
)
print("Customer count daily:\n",customers)
# 1. print days with more than 100 customers
print(f"print days with more than 100 customers\n{customers[customers>100].index}")
# 2. print days with fewer than the weekly average:
print(f"print days with fewer than the weekly average:\n{customers[customers<customers.mean()].index}")
# 3. sort the series by customer count descending.
print(f"sort the series by customer count descending.:\n{customers.sort_values(ascending=False)}")
