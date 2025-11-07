'''
You have a DataFrame df:
data = {
    'Name': ['Ali', 'Zoya', 'zoya', 'ALi ', 'John', 'john'],
    'Dept': ['IT', 'Finance', 'Finance', 'IT', 'HR', 'HR'],
    'Salary': [80000, 90000, None, 85000, None, 87000]
}
Tasks:
Clean duplicate names (ignore case and spaces).
Fill missing salaries using the mean salary of that department.
Standardize all names to Title Case.
Create a new column Tax = 10% of Salary if Salary > 85000, else 5%.
Display department-wise average tax.
'''
import pandas as pd
import numpy as np
data = {
    'Name': ['Ali', 'Zoya', 'zoya', 'ALi ', 'John', 'john'],
    'Dept': ['IT', 'Finance', 'Finance', 'IT', 'HR', 'HR'],
    'Salary': [80000, 90000, None, 85000, None, 87000]
}

df = pd.DataFrame(data)
print(df.head())

# 1. Clean duplicate names (ignore case and spaces).
df['Name'] = df['Name'].str.strip(' ').str.lower().str.capitalize()
print(df.head(10))

df.drop_duplicates(subset=['Name', 'Dept'], keep="first", inplace=True)
print(df)

# 2. Fill missing salaries using the mean salary of that department.
df['Salary'] = df.groupby('Dept')['Salary'].transform(lambda x: x.fillna(x.mean()))

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)

# 4. Create a new column Tax = 10% of Salary if Salary > 85000, else 5%.
df['Tax'] = np.where(df['Salary']>85000, df['Salary']*0.1,df['Salary']*0.05)
print(df)

# Department wise average tax.
dat = df.groupby(['Dept'])['Tax'].mean()
print(dat)