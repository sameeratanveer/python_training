'''
Print today’s date in format: Thursday, 30 October 2025
'''

from datetime import date
today = date.today()
print(today.strftime('%A, %d %B %Y'))