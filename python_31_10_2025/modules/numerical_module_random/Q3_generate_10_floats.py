'''
Generate a list of 10 random floats between 0 and 1.
'''
import random
random_10_floats =[]
for i in range(10):
    random_10_floats.append(random.random())
print(random_10_floats)