'''
Find your age in days and years using your DOB.
'''
import datetime
birthdate = input("Enter your birthdate: (in yyyy-mm-dd format): ")
birthdate = tuple(birthdate.split('-'))
birthdate = datetime.date(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]))
today = datetime.date.today()
print(birthdate)
if birthdate.month < today.month:
    years = today.year - birthdate.year - 1
