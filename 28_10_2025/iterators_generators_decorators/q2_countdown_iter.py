'''
Create a class Countdown that:
Takes a number n in __init__.
Iterates from n down to 1.
Prints "Liftoff 🚀" when iteration ends.
'''

class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 1:
            print("Liftoff!")
            raise StopIteration
        else:
            current = self.n
            self.n = self.n - 1
            return current
countdown10 = Countdown(10)
for count in countdown10:
    print(count)