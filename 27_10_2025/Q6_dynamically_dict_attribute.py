'''
Create a class Student with name, roll_no.
Now take a dictionary:
data = {"age": 21, "department": "CSE", "grade": "A"}
Loop through this dictionary and dynamically attach each key-value pair as attributes of the object using setattr().
'''
class Student:
    pass
data = {"age": 21, "department": "CSE", "grade": "A"}
student1 = Student()
for key, value in data.items():
    setattr(student1, key, value)
print(student1.age, student1.department, student1.grade)