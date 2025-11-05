def even_numbers(n):
    current = 0
    while current <= n:
        yield current
        current += 2

for num in even_numbers(10):
    print(num)