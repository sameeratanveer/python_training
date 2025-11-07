'''
Q3. Data Cleaning and Transformation
You have a Series representing product ratings:
ratings = pd.Series(['5', '4', '3', '5', 'not rated', '2', '5'])
Tasks:
Replace 'not rated' with np.nan
Convert all data to numeric (astype(float))
Compute the average rating (ignoring NaN).
'''
import numpy as np
import pandas as pd
ratings = pd.Series(['5', '4', '3', '5', 'not rated', '2', '5'])

print(f"Ratings: \n{ratings}")

# Replace not rated witn np.nan
ratings.replace({'not rated':np.nan}, inplace=True)
print(f"Ratings: \n{ratings}")

# convert all data to numeric.
print(f"Dtype of ratings before conversions is: {ratings.dtypes}")
ratings = pd.to_numeric(ratings, errors="coerce")
print(f"Dtype of ratings after conversions is: {ratings.dtypes}")

# compute average rating
print(f"Average rating = {ratings[ratings!=np.nan].mean()}")
