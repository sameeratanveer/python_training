'''
Simulate 1000 coin tosses (Heads/Tails) and show the probability of heads.
'''

import random
random.seed(10)
choices = ['H', 'T']
head_count = 0
for i in range(1000):
    if random.choice(choices) == 'H':
        head_count += 1
print(head_count)
print(f"Probability = {head_count/1000}")

# or
head_counts = random.choices(choices, k=1000)
h_counts = sum(1 for x in head_counts if x == 'H')
print(f"Probability: {h_counts/len(head_counts)}")

# or
print(f"probability : {head_counts.count('H')/1000}")