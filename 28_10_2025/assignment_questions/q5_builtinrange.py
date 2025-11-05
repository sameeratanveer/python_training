'''
Scenario: Build a RangeIterator that mimics Python’s built-in range() function.
'''

class RangeIterator:
    def __init__(self, start, end, skip=1):
        self.start = start
        self.end = end
        self.skip = skip

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            current = self.start
            self.start += self.skip
            return current
        else:
            raise StopIteration

for num in RangeIterator(1,10, 2):
    print(num)