'''
Create all pairs (fruit, color) only if the first letter of the fruit matches the first letter of the color.
'''
fruits = ["apple", "anana", "cherry"]
colors = ["aed", "cellow", "bink"]
soln = [(fruit,color) for fruit in fruits for color in colors if fruit[0]==color[0]]
print(soln)
