'''
2.Design a class Employee with private attributes for name and salary.
Provide public methods to set and get these details.

Create a subclass Manager that inherits from Employee and adds a department attribute.
Also, create another subclass Developer that adds a programming_language attribute.

Demonstrate how each object (Manager and Developer) can display their full details using a common display_info() method defined in the base class and extended in each subclass.
'''

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
        print(f"Emp Name: {self.__name}, Salary: {self.__salary}")

class Manager(Employee):
    def __init__(self, name, salary, department='General'):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Emp Name: {self.get_name()}, Salary: {self.get_salary()}, Manager of Dept: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language='python'):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        print(f"Emp Name: {self.get_name()}, Salary: {self.get_salary()}, programming Lnaguage uses: {self.programming_language}")

emp1 = Employee('Ram', 20000)
print(f"Salary of {emp1.get_name()} : {emp1.get_salary()}")

emp2 = Manager('Aisha', 120000, 'IT')
emp2.display_info()

emp3 = Developer('Harsh', 80000, 'Python')
emp3.display_info()