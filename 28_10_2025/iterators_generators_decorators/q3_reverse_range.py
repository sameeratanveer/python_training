'''
Create a class ReverseRange that works like Python’s built-in range() but iterates backward.
'''
class ReverseRange:
    def __init__(self, end, start):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.end > self.start:
            raise StopIteration
        else:
            current = self.start
            self.start -= 1
            return current

for num in ReverseRange(1,5):
    print(num)