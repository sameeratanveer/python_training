'''
1. Create a class Student:
    Class variable: school_name = "ABC High School"
    Instance variables: name, marks
    Local variable: inside a method calculate_grade()
Print all 3 types and note differences.
'''

class Student:
    school_name = 'ABC High School'
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def calculate_grade(self, marks):
        self.grade = None
        if self.marks > 75:
            self.grade = 'Distinction'
        elif self.marks > 50:
            self.grade = 'Second class'
        else:
            self.grade = 'Fail'
        print(self.grade)
student1 = Student('Mahi', 66)
print(student1.school_name)
print(student1.name)
print(student1.marks)
print(student1.calculate_grade(student1.marks))
print(student1.grade)
