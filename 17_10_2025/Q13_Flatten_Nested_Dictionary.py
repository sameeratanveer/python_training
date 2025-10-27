'''
Q13. Flatten Nested Dictionary
data = {'a': {'b': {'c': 1}}, 'd': 2}
Expected Output: {'a.b.c': 1, 'd': 2}
'''

data = {'a': {'b': {'c': 1}}, 'd': 2}
outp = {}
for key, value in data.items():
    if isinstance(value, dict):
        for key2, value2 in value.items():
            if isinstance(value2, dict):
                for key3, value3 in value2.items():
                    keyc = f'{key}.{key2}.{key3}'
                    outp[keyc] = value3
            else:
                keyc = f'{key}.{key2}'
                outp[keyc] = value2
    else:
        outp[key] = value
print(outp)