'''
Q15. Invert a Nested Dictionary
data = {'a': {'id': 1}, 'b': {'id': 2}, 'c': {'id': 1}}
Expected Output: {1: ['a', 'c'], 2: ['b']}
'''

data = {'a': {'id': 1}, 'b': {'id': 2}, 'c': {'id': 1}}
outp = {}

for key,value in data.items():
    if data[key]['id'] not in outp:
        outp[value['id']] = [key]
    else:
        outp[value['id']].append(key)
print(outp)
