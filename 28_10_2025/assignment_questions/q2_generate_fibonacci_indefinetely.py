'''
Create a generator that yields Fibonacci numbers indefinitely.
'''

def generate_fibonnaci():
    first = 0
    second = 1
    while True:
        yield first
        first, second = second, first + second

for num in generate_fibonnaci():
    print(num)
    if num > 50:
        break
