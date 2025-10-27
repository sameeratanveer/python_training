from datetime import datetime

# Original datetime object
original_date = datetime(2023, 10, 27, 14, 35, 12, 123456)

# Truncate to month and year
truncated_date = datetime(original_date.year, original_date.month, 1)

print(f"Original date: {original_date}")
print(f"Truncated date (month and year): {truncated_date}")