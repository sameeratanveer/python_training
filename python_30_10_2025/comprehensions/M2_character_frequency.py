'''
Task: Use a dictionary comprehension to count frequency of each character in the string.
💡 Expected output example: {'c':1, 'o':1, 'm':1, ...}
text = "comprehension"
'''
text = "comprehension"
# outp = {char : outp[char] += 1 if char in outp else char :outp[char] = 1 for char in text}
outp = {char:text.count(char) for char in text.lower()}
print(outp)