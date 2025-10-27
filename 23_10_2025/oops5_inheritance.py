'''
15. Create a base class Person with name, age.
Derive class Employee with additional emp_id, salary.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Person Name: {self.name}, Age:{self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.__salary = salary

    def show_details(self):
        print(f"Employee name: {self.name}, Age: {self.age}\nEmployee id:{self.emp_id}, Employee salary:{self.__salary}")

# person1 = Person("Sam", 21)
# person1.show_details()
# emp1 = Employee('sam', 21, 322, 220000)
# emp1.show_details()

class A:
    def func(self):
        print("I am from A class")
class B:
    def func(self):
        print("I am from B class")
class C(B, A):
    def check(self):
        print("I am C")
c = C()
c.func()

class A:
    def feature_a(self):
        print("Feature A")

class B(A):
    def feature_b(self):
        print("Feature B")

class C(A):
    def feature_c(self):
        print("Feature C")

class D(B, C):  # hybrid inheritance
    def feature_d(self):
        print("Feature D")

d = D()
d.feature_a()
d.feature_b()
d.feature_c()
d.feature_d()

class Vehicle:
    def move(self):
        print("Vehicles help in transportation")

class Car(Vehicle):
    def car_info(self):
        print("Car runs on 4 wheels")

class Bike(Vehicle):
    def bike_info(self):
        print("Bike runs on 2 wheels")

c = Car()
b = Bike()
c.move(); c.car_info()
b.move(); b.bike_info()

class Grandparent:
    def legacy(self):
        print("Legacy from Grandparent")

class Parent(Grandparent):
    def assets(self):
        print("Assets from Parent")

class Child(Parent):
    def future(self):
        print("Future belongs to Child")

c = Child()
c.legacy()
c.assets()
c.future()


