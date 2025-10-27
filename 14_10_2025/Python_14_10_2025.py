import keyword
print("Hello")

# Variables: 
myName = 'Sameera Tanveer'
MyAge = 21
friend1 = 'Navya'
my_marks = 20.5

# Input: 
# your_name = input("Please Enter your name: ")
# print("Hello", your_name)

# input age and print the result
# yourAge = int(input("Enter your age: "))
# print("Next year your age will be ", yourAge + 1)

# Taking multiple inputs:
# Taking multiple string inputs separated by space
# name, age = input("Enter your name and age (separated by space): ").split()
# print("Name ", name, "and age ", age)

# # Taking multiple integer inputs separated by comma
# num1, num2, num3 = map(int, input("Enter three numbers (separated by comma): ").split(','))
# print("num1 = ", num1, "\n", "num2 =", num2, "\n", "num3 = ", num3)

# Keywords:
# print(len(keyword.kwlist))
# print(keyword.kwlist)
# print(keyword.iskeyword('hello'))
# print(keyword.iskeyword('if'))

# Operators:
# 1. Arithmetic operators:
num1 = 20
num2 = 13
print(f'Addition: {num1} + {num2} = {num1 + num2}')
print(f'Subtraction: {num1} - {num2} = {num1 - num2}')
print(f'Multiplication: {num1} * {num2} = {num1 * num2}')
print(f'Division: {num1} / {num2} = {num1 / num2}')
print(f'Modulo: {num1} % {num2} = {num1 % num2}')
print(f'Floor Division: {num1} // {num2} = {num1 // num2}')
print(f'Exponential: {num1} ** {num2} = {num1 ** num2}')

# 2. Assignment Operators:
print(f"Assigning a value using = like name = 'sameera' or age = 21")
print(f"Compound Assignment operators : +=, -=, *=, /=, %=, //= **=")
num1 += 1
print(f'Addition Assignment: {num1}')
num1 -= 1
print(f'Subtraction Assignment: {num1}')
num1 *= 2
print(f'Multiplication Assignment: {num1}')
num1 /= 5
print(f'Division Assignment: {num1} ')
num1 %= 4
print(f'Modulo Assignment: {num1}')
num1 //= 4
print(f'Floor Division Assignment: {num1}')
num1 **= 2
print(f'Exponential Assignment: {num1}')





