'''
Generate 5 random integers between 10 and 50.
'''
import random
random_5_ints = []
for i in range(5):
    random_5_ints.append(random.randint(10,50))
print(random_5_ints)