'''
6. Create a class Employee where __init__ takes name, role, salary.
Add a method describe() that prints all details.
'''

class Employee:
    '''
    8. Add a default parameter in __init__ like department='General'.
    Create an employee without specifying department — see the output.
    '''
    def __init__(self, name, role, salary, department='General'):
        self.name = name
        self.role = role
        self.salary = salary
        self.department = department

    def describe(self):
        print(f"Details of the employee:{self}")
        print(f"Name = {self.name}, Role = {self.role}, Salary = {self.salary}, Department = {self.department}")

'''
7. Create 3 employees and store them in a list.
Loop through and print their names and roles.
'''
employees = []
emp1 = Employee('Sam', 'SE1', 200000)
emp2 = Employee('era', 'SE2', 500000)
emp3 = Employee('Sameera', 'DS1', 700000, 'IT')
employees.extend([emp1, emp2, emp3])

for employee in employees:
    employee.describe()
    # or just for names: employee.name
