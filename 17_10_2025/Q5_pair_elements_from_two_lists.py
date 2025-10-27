'''
Q5. Pair Elements from Two Lists
names = ["A", "B", "C"]
scores = [90, 80, 85]
Expected Output: [('A', 90), ('B', 80), ('C', 85)]
'''

names = ["A", "B", "C"]
scores = [90, 80, 85]

outp = []
for i in range(len(names)):
    outp.append((names[i], scores[i]))

print(outp)