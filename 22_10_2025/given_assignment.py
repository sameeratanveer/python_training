'''
1. Write a function `register_user(name, age, city)` that accepts both positional and keyword arguments.
Call the function in 3 different ways:
  1. All positional
  2. Mix of positional and keyword
  3. All keyword
  Explain what happens if you pass an extra or missing argument.
'''
def register_user(name, age, city):
    print(f'Name: {name}\nAge: {age}\nCity: {city}')
# calling a function:
register_user('Sameera', 21, 'Hyderabad')
register_user(21, 'sameera', 'Hyderabad')
register_user(name='sameera', city='Hyderabad', age=21)
# register_user(city='Hyderabad', 'sameera', 21) # Error because SyntaxError: positional argument follows keyword argument that means once keyword argument is in the sequence, then we cant send positional argument at all!
# register_user(city='Hyderabad', 21, 'Sameera') # same error as above

'''
2. Define a function:
def calculate_area(length, /, width, * , unit="sq.m"):
Explain what `/` and * mean in the signature.
Write valid and invalid function calls.
What error do you get if you try `calculate_area(length=5, width=3)`?
'''

def calculate_area(length, /, width, *, unit='sq.m'):
    print(f'Area = {length * width} {unit}')
# / means before this the arguments are positional only, whereas * after this the arguments are keywords only.
# That means length should be only positional argument, and unit parameter should be keyword only. And width is our wish,
calculate_area(10, 20, unit='m')
# calculate_area(length=10, 20) # invalid because positional after keyword.
# calculate_area(10, width=20, 'sq.m2') # invalid because unit must be keyword argument
# calculate_area(10, 20, 'sq.m3') # invalid because unit must be keyword. [error: calculate_area() takes 2 positional arguments but 3 were given]
# calculate_area(length=10, width=20) # invalid because length must be positional. [error: calculate_area() got some positional-only arguments passed as keyword arguments: 'length']
calculate_area(10, width=20, unit='sq.m2')

'''
3. Write a function:
def append_item(item, item_list=[]):
    item_list.append(item)
    return item_list

Call it multiple times and observe the output.
Explain why the list keeps growing.
Fix it by making the default parameter immutable.
'''

# def append_item(item, item_list=[]):
def append_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list
print(append_item(1))
print(append_item(2))
print(append_item([1,3]))
print(append_item(2, [1,3]))


'''
4.Create a function `student_profile(*courses, **details)` that:
Prints all courses from `*args`.
Prints all key-value pairs from `**kwargs`.
  Write a function call mixing both — e.g: student_profile("Math", "Science", name="John", grade="A")
'''

def student_profile(*courses, **details):
    print('Taken courses: ', end = '')
    for course in courses:
        print(f'{course}', end=',')
    print()
    print('Details: ')
    for key, value in details.items():
        print(f'{key}:{value}')

student_profile("Math", "Science", name="John", grade="A")
student_profile("Physics", 'Maths', 'English', name='Sam', grade='A', age=21)

'''
5. Write a function `compare_numbers(a, b)` that:
Returns `"Equal"` if both are same
Returns the larger number if not
Demonstrate that a function stops executing after the first `return`.
'''

def compare_numbers(a,b):
    if a == b:
        return 'Equal'
    if a > b:
        return a
    else:
        return b
    print('Never gets printed!')
print(compare_numbers(10,10)) # stops the execution after the return stmt 'Equal' doesnt go after that at all..
print(compare_numbers(10,5)) # stops execution after the return stmt return a doesnt go to else also.
print(compare_numbers(5, 10)) # goes till the last return b but doesnt print the next stmt, if wont go next.

'''
6. Write a function `analyze_numbers(lst)` that returns:
Minimum, maximum, and average of a list.Then show how to unpack it like:
    min_val, max_val, avg = analyze_numbers([1,2,3,4])
What happens if you unpack incorrectly?
'''

def analyze_numbers(lst):
    return max(lst), min(lst), sum(lst)/len(lst)
min_val, max_val, avg = analyze_numbers([1,2,3,4])
print(f'Min value: {min_val}\nMax value: {max_val}\nAvg : {avg}')

'''
7. Return Types and Implicit `None`
Write a function `display_message(msg)` that prints the message but does not use a return statement.
Show what happens when you assign its result to a variable.
Explain why the variable becomes `None`.
'''

def display_message(msg):
    print(msg)
print(display_message('Hi'))
msged = display_message('Hello')
print(msged)

'''
8. Nested Functions and Scope (`global`, `nonlocal`)
Write a function:
count = 0
def outer():
    total = 10
    def inner():
        nonlocal total
        global count
        total += 5
        count += 1
        return total, count
    return inner()
Predict the output.
Explain what happens if you remove `global` or `nonlocal`.
'''

count = 0
def outer():
    total = 10
    def inner():
        nonlocal total
        global count
        total += 5
        count += 1
        return total, count
    return inner()
print(outer())
