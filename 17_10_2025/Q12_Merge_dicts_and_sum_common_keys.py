'''
Q12. Merge Dicts and Sum Common Keys
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'a': 5, 'b': 15, 'd': 25}
Expected Output: {'a': 15, 'b': 35, 'c': 30, 'd': 25}
'''

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'a': 5, 'b': 15, 'd': 25}

outp = d1.copy()
for key, value in d2.items():
    if key not in outp:
        outp[key] = value
    else:
        outp[key] += value
print(outp)

