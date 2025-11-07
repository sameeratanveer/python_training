import pandas as pd

df = pd.DataFrame({
    'timestamp': pd.date_range('2025-02-01', periods=10, freq='h'),
    'level': ['INFO', 'ERROR', 'DEBUG', 'INFO', 'ERROR', 'WARNING', 'INFO', 'ERROR', 'INFO', 'INFO'],
    'message': ['User login', 'DB fail', 'Cache cleared', 'User logout', 'Server down',
                'Low memory', 'API hit', 'DB fail', 'User login', 'Server up']
})

df['date'] = df['timestamp'].dt.date

# 1️⃣ Count number of error logs per day
errors_log = df[df['level'] == 'ERROR'].groupby('date').size()
print("Error logs per day:\n", errors_log, "\n")

# 2️⃣ Most frequent error message
most_common_error = (
    df[df['level'] == 'ERROR']
    .groupby('message')
    .size()
    .sort_values(ascending=False)
    .head(1)
)
print("Most frequent error message:\n", most_common_error, "\n")

# 3️⃣ Summary DataFrame → level, count, percentage
counts = df['level'].value_counts().reset_index()
counts.columns = ['level', 'count']
counts['percentage'] = (counts['count'] / counts['count'].sum()) * 100
summary_df = counts
print("Summary:\n", summary_df, "\n")

# 4️⃣ Save only ERROR or WARNING logs to new file
critical_logs = df[df['level'].isin(['ERROR', 'WARNING'])]
critical_logs.to_csv("critical_logs.csv", index=False)
print("Saved critical logs to 'critical_logs.csv'.")
