'''
Generator Functions
'''

def count_up_to(max_value):
    current  = 1
    while current <= max_value:
        yield current
        current += 1

for num in count_up_to(5):
    print(num)
