'''
Q14. Group by Value
data = {'x': 1, 'y': 2, 'z': 1}
Expected Output: {1: ['x', 'z'], 2: ['y']}
'''

data = {'x': 1, 'y': 2, 'z': 1}
outp = {}

for key, value in data.items():
    if value not in outp:
        outp[value] = [key]
    else:
        outp[value].append(key)
print(outp)
