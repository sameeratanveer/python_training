'''
Use dictionary comprehension to:
Include only employees earning >50,000
Give them a 10% bonus in the new dictionary
'''
employees = {'Alice': 50000, 'Bob': 72000, 'Charlie': 48000, 'Diana': 85000}
soln = {emp_name:round(salary*1.1,2) if salary>50000 else salary for emp_name, salary in employees.items()}
print(soln)

colors = ["Red", "Green", "Blue"]
objects = ["Ball", "Pen"]
print([color+' '+object for color in colors for object in objects])