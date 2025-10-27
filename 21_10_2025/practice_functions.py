'''
Q1:
Write a function that takes two numbers as positional arguments and prints their sum and difference.
Then call it using both positional and keyword arguments.
'''

def do_sum_difference(num1, num2):
    print(f'Sum of {num1} + {num2} = {num1+num2}')
    print(f'Difference of {num1} - {num2} = {num1-num2}')

do_sum_difference(2,1)
do_sum_difference(num2=1, num1=2)
# do_sum_difference(num2=10, 2) this gives error because the sequence should be position then keyword!
do_sum_difference(2, num2=1)

'''
Q2:
Create a function that takes a name and a greeting message (default “Hello”) and prints a personalized message.
Call it once using the default message and once with a custom message.
'''
def greetings(name, msg='Hello'):
    print(f'{name}:{msg}')
greetings('sam')
greetings('sam','Welcome')


''' 3.
Write a function display_student_info(name, age, /, course) 
where name and age must be positional-only and course can be passed as keyword-only.
'''
def display_student_info(name, age, /, course):
    print(f'Name:{name}\nAge:{age}\ncourse taken:{course}')
display_student_info('sam',21, course=['SQL','Python'])

# ,/ shows that the arguments before / are positional only, while *, arguments after * are keywords but still accepts positional.

'''
4.
Define a function that accepts any number of integers (*args) and returns both their sum and average.
'''
def sum_average_numbers(*nums):
    sum = 0
    avg = 0
    for element in nums:
        sum += element
    avg = sum/len(nums)
    return (sum,avg)

sum, avg = sum_average_numbers(1,2,3,4,5)
print(f'Sum = {sum}\nAvg: {avg}')

'''
5.
Create a function describe_person(**kwargs) that 
accepts variable-length keyword arguments (like name, age, hobby) 
and prints each key-value pair nicely formatted.
'''

def describe_person(**details):
    for key, value in details.items():
        print(f'{key}:{value}')
describe_person(name ="sameera", age=20, hobby='playing Games')

'''
6.
Write a function that mixes all argument types — positional, default, *args, and **kwargs — 
and demonstrate at least two valid calls.
'''

def valids(ids, name, age, role, office='Bilvantis', *worked_projects, **role_in_worked_projects):
    print(f'id={ids}\nName={name}\nAge: {age}\nRole:{role}\nOffice:{office}\nWorked_projects:{worked_projects}\nrole_in worked projects:{role_in_worked_projects}')
valids(322, 'Sameera', 21, 'Programmer Analyst', 'Bilvantis', 'p1', 'p2', 'p3', 'p4', p1='Analyst', p2='DE', p3='SE', p4='CDE')
valids('sameera', 322, p1='Hello', age=25, role='Programmer')

'''
8.
Write a function concat_strings(*args, sep=" ") that joins multiple strings together with a given separator.
'''
def concat_strings(*args, sep=''):
    s = ''
    for element in args:
        s += element + sep
    return s
print(concat_strings('Hello', 'World', 'Python', 'Programming', sep=','))

'''
11.
Write a function power(base, exp=2) to calculate power, then call it using positional, keyword, and mixed argument passing.
'''
def power(base, exp=2):
    return base**exp
print(power(base=10))
print(power(10, 3))

'''
12,
Create a function that takes a list of numbers and a keyword argument reverse=False.
If reverse=True, print the list in reverse order, else in normal order.
'''
def reverse(*nums, reversed=False):
    soln = []
    if reversed:
        for i in range(len(nums)-1, 0, -1):
            soln.append(nums[i])
        return soln
    return nums
print(reverse(10,20,30,40,50))
print(reverse(10,20,30,40,50, reversed=True))

# After *args, the remaining arguments passed must be keyword arguments!!

# - ---------------------- checks of the datatype for function parameters.. --------------
# 1. usinf isinstance:
def add_numbers(a,b):
    if isinstance(a,(int, float)) and isinstance(b, (int, float)):
        return a + b
    return 'Error: Only numbers are allowed!'
print(add_numbers(10, 15))
print(add_numbers(10, 'sam'))
print(add_numbers('sam', 10))


# -------------------------------- scope -----------------------------
# 1. Local variable:
def func1():
    x = 10
    print(x)
func1()
# print(x) # local varibale x is not accessible because the scope is to that fucntion only.

# 2. Global varibale..
x = 12
def func1():
    x = 10
    print(x) # local variable
    x = 21
    print(x) # local variable change
func1()
print(x) # global variable
x = x + 2
print(x) # global variable change

# 3. nonlocal : allows modification of outer function variable inside inner fucntion variable.
def func1():
    x = 'Jane'
    def func2():
        nonlocal  x
        x = 'sam'
    func2()
    return x
print(func1())

# global:
x = 100

def test():
    global x
    x += 50

test()
print(x)  # 150

x = 100  # global

# cant update the global when local exists.. becuase local gets priority.
# def test():
#     x = 10  # local
#     print("Before:", x)
#
#     global x  # trying to modify global
#     x += 50
#
#
# test()
# print("Global x:", x)
