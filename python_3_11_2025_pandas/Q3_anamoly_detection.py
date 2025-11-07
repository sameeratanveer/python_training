import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'timestamp': pd.date_range('2025-01-01', periods=100, freq='h'),
    'temperature': np.random.normal(30, 3, 100)
})
df.loc[[10, 40, 75], 'temperature'] = [50, 2, 55]  # anomalies

print("Original DataFrame:")
print(df.head(15)) # Showing more rows to see anomalies

# 1. Detect anomalies: values 3 standard deviations away from the mean.
mean_temp = df['temperature'].mean()
std_temp = df['temperature'].std()
lower_bound = mean_temp - (3 * std_temp)
upper_bound = mean_temp + (3 * std_temp)

# Corrected use of .where() with parentheses around conditions
anomalies_df = df.where((df['temperature'] < lower_bound) | (df['temperature'] > upper_bound))
print("\nAnomalies detected (non-anomalies are NaN):")
print(anomalies_df.dropna()) # Dropping NaNs to only show anomaly rows

# 2. Add a new column is_anomaly (True/False).
# Corrected use of np.where() with parentheses around conditions
df['is_anomaly'] = np.where(
    (df['temperature'] < lower_bound) | (df['temperature'] > upper_bound),
    True,
    False
)
print("\nDataFrame with is_anomaly column:")
print(df[df['is_anomaly'] == True]) # Displaying only anomaly rows

# 3. Count how many anomalies occurred per day.
df['date'] = df['timestamp'].dt.date
anomalies_per_day = df[df['is_anomaly'] == True].groupby('date').size()
print("\nAnomalies per day:")
print(anomalies_per_day)

# 4. Replace anomalies with median temperature.
median_temp = df['temperature'].median()
# Use the boolean mask we created to select only the anomaly rows and set their temperature
df.loc[df['is_anomaly'] == True, 'temperature'] = median_temp

print("\nDataFrame after replacing anomalies with median:")
print(df.loc[[10, 40, 75]]) # Check the anomaly indices to verify replacement
print(df)
