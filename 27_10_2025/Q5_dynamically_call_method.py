class Calculator:
    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b

'''
Now write code that:
Takes user input (string): "add" or "sub".
Checks if the class has that method (hasattr()).
Dynamically calls it using getattr().
'''
inp = input("Enter 'add' or 'sub': ")
calc = Calculator()
if hasattr(calc, inp):
    method1 = getattr(calc, inp)
    print(method1(10,20))
