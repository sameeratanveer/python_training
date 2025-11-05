'''
1️. Hello Caller
Create a class Greeter that takes a name in __init__.
When the object is called (e.g. obj()), it should print:
Hello, <name>!
'''
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"Hello, {self.name}")

g = Greeter('Sam')
g()

'''
Create a class Counter that keeps track of how many times it has been called.
Each call should print "Called n times" where n increases with every call.
'''
class Counter:
    counter = 0
    def __call__(self):
        Counter.counter += 1
        print(Counter.counter)
c = Counter()
c()
c()
c()