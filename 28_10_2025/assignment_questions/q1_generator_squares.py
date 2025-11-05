'''
Write a generator function to yield squares of numbers up to n.
'''

def generate_squares(n):
    current = 1
    while current <= n:
        yield current * current
        current += 1

for square in generate_squares(10):
    print(square)