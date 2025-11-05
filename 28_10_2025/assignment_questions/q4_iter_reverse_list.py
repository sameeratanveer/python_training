'''
Implement a class ReverseList that takes a list and iterates through it in reverse order.
'''

class ReverseList:
    def __init__(self, lst):
        self.lst = lst
        self.current = len(lst)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >=0:
            current_element = self.lst[self.current]
            self.current -= 1
            return current_element
        else:
            raise StopIteration

for num in ReverseList([1,2,3,4,5]):
    print(num)