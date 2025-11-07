'''
Convert "2025-01-15 09:30" string into a datetime object and extract month and weekday.
'''
import datetime
string_date = "2025-01-15 09:30"
format = "%Y-%m-%d %H:%M"
date = datetime.datetime.strptime(string_date, format).date()
print(date.strftime("%B"), date.strftime("%a"))
print(type(date))
