'''
Q2. Missing Data Handling
Create a Series rainfall with values [5.5, 2.3, None, 0.0, 1.2] and index ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'].
Tasks:
Detect missing values
Replace missing values with the mean rainfall
Print the cleaned Series
Compute the total rainfall for the week.
'''
import pandas as pd
rainfall = pd.Series([5.5, 2.3, None, 0.0, 1.2], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print(rainfall)

# 1. Detect missing values.
print(rainfall[rainfall.isna()])

# 2. replace missing values with the mean rainfall.
rainfall_replaced_missing_rainfall = rainfall.fillna(rainfall.mean())

# 3. print cleaned rainfall series
print(f"Cleaned or filled missing values after: \n{rainfall_replaced_missing_rainfall}")

# 4. Compute the total rainfall for the week.
print(f"Total rainfall for the week is: {rainfall_replaced_missing_rainfall.mean()}")
