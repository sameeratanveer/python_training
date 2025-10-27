'''
Q2. Flatten a Nested List
data = [1, [2, 3, [4, 5]], 6]
Expected Output: [1, 2, 3, 4, 5, 6]
'''

data = [1, [2, 3, [4, 5]], 6]
outp = []
for element in data:
    if isinstance(element, list):
        for element2 in element:
            if isinstance(element2, list):
                outp.extend(element2)
            else:
                outp.append(element2)
    else:
        outp.append(element)
print(outp)