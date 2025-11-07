'''
Take an integer and display its factorial, square root, cube root, and logarithm (base 10).
'''
import math
number = int(input("Enter an integer! :"))
print(f"Factorial of {number} is {math.factorial(number)}")
print(f"Square root of {number} is {math.sqrt(number):.2f}")
print(f"Cube root of {number} is {math.cbrt(number):.2f}")
print(f"Log10 of {number} is {math.log10(number):.2f}")
print(f"log base 10 of {number} is {math.log(number, 10):.2f}")
