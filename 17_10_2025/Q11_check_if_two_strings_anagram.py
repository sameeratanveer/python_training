'''
Q11. Check if Two Strings Are Anagrams
s1 = "listen"
s2 = "silent"
Expected Output: True
'''

s1 = "listen"
s2 = "silent"

count_s1 = {}
count_s2 = {}
for element in s1:
    if element not in count_s1:
        count_s1[element] = 1
    else:
        count_s1[element] += 1

for element in s2:
    if element not in count_s2:
        count_s2[element] = 1
    else:
        count_s2[element] += 1

print(count_s1)
print(count_s2)
print(count_s2 == count_s1)

