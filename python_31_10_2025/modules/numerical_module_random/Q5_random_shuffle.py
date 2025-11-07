'''
Randomly shuffle a list of numbers from 1–10 and display them.
'''

import random
lst = list(range(1,11))
print(lst)
for i in range(10):
    random.shuffle(lst)
    print(f"Shuffle{i} = {lst}")