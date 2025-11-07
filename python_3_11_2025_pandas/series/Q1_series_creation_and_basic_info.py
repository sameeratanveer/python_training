'''
Create a Series temperature with data [32, 35, 30, 28, 40] and
index labels ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'].
'''
import pandas as pd
temperatures = [32,35,30,28,40]
indexes = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperature_series = pd.Series(temperatures, index=indexes)
print(temperature_series)

'''
1. Print the Series
2. Display its .values, .index, .dtype, and .size
3. Print only the temperature on Wednesday using both label and position-based access.
'''

print(f"Series:\n{temperature_series}")
print(f"Values: {temperature_series.values}")
print(f"Index: {temperature_series.index}")
print(f"Type of the data: {temperature_series.dtype}")
print(f"#Elements or size: {temperature_series.size}")
