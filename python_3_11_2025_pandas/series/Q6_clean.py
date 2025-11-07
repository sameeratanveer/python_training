'''
Your Series has messy text data from a CSV column:

cities = pd.Series(['hyderabad ', ' MUMBAI', 'delhi', 'HYDERABAD', '  pune '])
Tasks:
Strip extra spaces
Convert all to lowercase
Remove duplicates
Sort alphabetically
Expected Output:
['delhi', 'hyderabad', 'mumbai', 'pune']
'''
import pandas as pd
cities = pd.Series(['hyderabad ', ' MUMBAI', 'delhi', 'HYDERABAD', '  pune '])
cities.str.strip().str.lower().drop_duplicates().sort_values()
