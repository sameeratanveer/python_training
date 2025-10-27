'''
Q9. Remove Duplicate Words in Sentence
s = "this this is is a test test"
Expected Output: "this is a test"
'''

s = "this this is is a test test"
lookup = set()
outp = ''
for i in s.split():
    if i not in lookup:
        outp = outp + i + ' '
        lookup.add(i)
print(outp)