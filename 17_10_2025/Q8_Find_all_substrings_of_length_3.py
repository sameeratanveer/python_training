'''

Q8. Find All Substrings of Length 3
s = "ABCDE"
Expected Output: ['ABC', 'BCD', 'CDE']
'''

s = "ABCDE"
outp = []
for i in range(len(s)-2):
    outp.append(s[i:i+3])
print(outp)