'''
iterator example using iter() and next() to iterate over a list!
'''

fruits = ['apple', 'banana', 'cherry']
iterator = iter(fruits)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

'''
Custom iterators by defining a class.. 
'''

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return  self.current - 1
counter = Counter(1,5)
for num in counter:
    print(num)

class EvenNumber:
    def __init__(self, max_number):
        self.number = 0
        self.max = max_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > self.max:
            raise StopIteration
        self.number += 2
        return self.number - 2

even_iterator = EvenNumber(10)
for num in even_iterator:
    print(num)
