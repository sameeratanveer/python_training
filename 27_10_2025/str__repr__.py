class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student {self.name} scored {self.marks}"

    def __repr__(self):
        return f"Student(name='{self.name}', marks={self.marks})"

s = Student("Sameera", 95)
print(s)        # Uses __str__
print(str(s))   # Also uses __str__
print(repr(s))  # Uses __repr__
