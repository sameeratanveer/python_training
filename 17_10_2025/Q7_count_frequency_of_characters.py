'''
Q7. Count Frequency of Each Character (Ignore Case)
s = "Success"
Expected Output:{'s': 3, 'u': 1, 'c': 2, 'e': 1}
'''

s = "Success"
s = s.lower()

outp = {}

for char in s:
    if char not in outp:
        outp[char] = 1
    else:
        outp[char] += 1
print(outp)