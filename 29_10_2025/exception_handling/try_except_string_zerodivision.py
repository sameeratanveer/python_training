'''
Write a program that asks for two integers and prints their division. Use try/except to handle non-integer input and division by zero separately.
'''
try:
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    res = num1 / num2
except ValueError:
    print("Value is not integer!")
except ZeroDivisionError:
    print("Can not divide by zero!")
except Exception as e:
    print(e)
else:
    print(f"{num1}/{num2} = {num1 / num2}")
finally:
    print("Execution successful!")
print("Program finished!")
