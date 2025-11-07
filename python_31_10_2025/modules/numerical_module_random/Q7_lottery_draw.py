'''
Write a function lottery_draw() that:
Takes N tickets (e.g., numbers 1–100)
Randomly picks 5 unique winners
Ensures repeatable results with a fixed seed
'''
import random
def lottery_draw(tickets):
    random.seed(40)
    winners = random.sample(tickets, k=5)
    return winners

print(lottery_draw([1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]))