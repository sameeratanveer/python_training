def squares(n):
    current = 1
    while current <= n:
        yield current * current
        current += 1

for square in squares(10):
    print(square)