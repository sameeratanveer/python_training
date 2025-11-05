class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id, salary):
        super().__init__(name)
        self.emp_id = emp_id
        self.salary = salary
'''
Now write a function print_employee_info(obj) that:
First checks if the object has emp_id and salary using hasattr()
If yes → prints their values using getattr()
If not → adds them dynamically using setattr() and default values
'''
def print_employee_info(obj):
    if hasattr(obj, 'emp_id'):
        print(f"Emp id ={getattr(obj, 'emp_id')}")
    else:
        print("Emp id attriute not found! Dynamically created the attribute")
        setattr(obj, 'emp_id', None)
        print(f"Emp id = {getattr(obj, 'emp_id')}")
    if hasattr(obj, 'salary'):
            print(f"Salary = {getattr(obj, 'salary')}")
    else:
            print("Salary attriute not found! Dynamically created the attribute")
            setattr(obj, 'salary',0)
            print(f"Salary = {getattr(obj, 'salary')}")


person1 = Person('sam')
emp1 = Employee('Same', 3, 10)
print("For person sam: the details are: ")
print_employee_info(person1)
print("For employee same: the details are: ")
print_employee_info(emp1)