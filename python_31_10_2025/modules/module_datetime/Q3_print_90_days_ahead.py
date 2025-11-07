'''
Print date 90 days from today
'''
import datetime
today_date = datetime.datetime.today()
print(f"90 days today: {today_date + datetime.timedelta(days=90)}")