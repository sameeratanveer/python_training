'''
Q10. Most Frequent Word
s = "apple banana apple mango banana apple"
Expected Output:"apple"
'''

s = "apple banana apple mango banana apple"
s = s.split()
counts = {}
for element in s:
    if element not in counts:
        counts[element] = 1
    else:
        counts[element] += 1
print(counts)

print(sorted(counts, key=lambda item: item[1], reverse=True)[0]) # the element with the highest count!
