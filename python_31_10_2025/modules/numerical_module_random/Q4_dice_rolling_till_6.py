'''
Simulate a dice rolling game until you roll a 6.
'''
import random
dice_roll = random.randint(1,6)
print(dice_roll)
while dice_roll != 6:
    dice_roll = random.randint(1,6)
    print(dice_roll)
if dice_roll == 6:
    print("Successfully done!")