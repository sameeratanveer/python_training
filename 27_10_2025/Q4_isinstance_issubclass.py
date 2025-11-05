
class Animal:
    pass
class Dog(Animal):
    pass
class Cat(Animal):
    pass

'''
Write a function identify_animal(obj) that:
Prints "Dog detected" if it’s an instance of Dog
Prints "Cat detected" if it’s an instance of Cat
Prints "Unknown animal" otherwise
Then test with objects of all three.
'''

def identify_animal(obj):
    if isinstance(obj, Dog):
        print("Dog Detected!")
    elif isinstance(obj, Cat):
        print("Cat Detected!")
    else:
        print("Unknown animal")
animal1 = Animal()
cat1 = Cat()
dog1 = Dog()
identify_animal(animal1)
identify_animal(cat1)
identify_animal(dog1)
print(f"Is Dog a subclass of animal? {issubclass(Dog, Animal)}")