'''
Dictionary is a datatype that stores key-value pairs as the element.

Dictionary is ordered, indexed, and mutable.

About Keys:
Dictionary is ordered and indexed.
Dictionary elements are indexed using key. Hence key must be unique and immutable.

Key can be anything that is immutable such as int, string, tuple only if they contain strings, tuple, numbers.

List and tuple containing mutable objects can not be keys.

'''

# Empty dictionary.
dictionary1 = {}
print(type(dictionary1))
print(dictionary1)

# Another way:
dictionary2 = dict()
print(type(dictionary2))
print(dictionary2)

# creating a dictionary to store details:
employee_details = {
    101: {
        'name': 'sameera',
        'empId': 101,
        'designation': 'programmer analyst',
        'skills': {
            'technical skills': ['Python', 'SQL'],
            'soft skills': ('good communication',)
        },
        'hobbies': set(('cricket','chess','reading'))
    },
    102: {
        'name': 'sam',
        'empId': 102,
        'designation': 'programmer analyst',
        'skills': {
            'technical skills': ['Python', 'SQL', 'Java'],
            'soft skills': ('good communication', 'negotiator')
        },
        'hobbies': set(('cricket','chess','reading', 'badminton'))
    },
    103: {
        'name': 'era',
        'empId': 103,
        'designation': 'programmer analyst',
        'skills': {
            'technical skills': ['Python', 'SQL'],
            'soft skills': ('good communication',)
        },
        'hobbies': set(('cricket','chess','reading', 'coding'))
    }
}

print(employee_details)

# ----------------------------- ACCESSING ITEMS IN DICTIONARY ------------
# 1. using key.
# From employee_details dictionary, get the name of employee whose id or key is 102
print(f'Emp id: {list(employee_details.keys())[1]}, Employee Name: {employee_details[102]['name']}')

# 2. get the same thing using .get()
# emp_id = int(input("Enter the employee id: "))
# print(f'Emp id: {emp_id}, Employee Name: {employee_details.get(emp_id).get('name')}')
# I am using .get() because i am taking input from the user and i dont know whether the id user passes. Is it correct or not, so to not get any error I am using .get()

# 3.
print(list(employee_details)) # converts the keys of the dictionary to list.

# 4. in : used to check if the key is present in the dictionary
# emp_id = int(input("Enter the employee id to check if it is present in the employee details or not? : "))
# if emp_id in employee_details:
#     print(f'Yes! {emp_id} is in the employee details table.')
# else:
#     print(f'Invalid employee id')

# 5. Modify the dictionary values: (keys are immutable but values are mutable)
# change the name of empid 102 with eera
employee_details.get(102)['name'] = 'eera'
print(employee_details.get(102).get('name'))

print(employee_details)
# 6. update()
# set back the name of empid 102 to sam
employee_details[102].update({'name':'sam'})
print(employee_details[102]['name'])

# --------------------------- Adding new key:value ---------
# 1. Add new employee 104:
employee_details[104] = {
        'name': 'anusha',
        'empId': 104,
        'designation': 'programmer analyst',
        'skills': {
            'technical skills': ['SQL'],
            'soft skills': ('good communication',)
        },
        'hobbies': set(('cricket','reading', 'coding'))
    }

# print(employee_details[104])

# 2. using update() add new employee 105
employee_details.update({105: {'name': 'anushka', 'empId': 105, 'designation': 'programmer analyst', 'skills': {'technical skills': ['SQL'], 'soft skills': ('good communication',)}, 'hobbies': {'reading', 'cricket', 'coding'}}
})

print(employee_details[105])

print(employee_details)
# ----------------------- Removing elements ---------------
# 1. pop()
temp = employee_details.copy()
print(temp)
temp.pop(105) # deletes the element
print('employee details after removing employee id 105', temp.keys(), sep='\n')
temp.popitem() # removes last inserted element
print('employee details after removing last inserted', temp.keys(), sep='\n')

# 2. del item
print("employee_details keys", temp.keys())
del temp[103]
print('employee details after deleting 103,', temp.keys())

# 3. clear()
print("employee_details keys", temp.keys())
temp.clear()
print('employee details after clear,', temp.keys())

# Assignment Question:
l1 = ['A', 'B','C']
l2 = [1,2,3]
d = {}
# output: {'A':1, 'B':2, 'C':3}
for i in range(len(l1)):
    d[l1[i]] = l2[i]
print(d)





