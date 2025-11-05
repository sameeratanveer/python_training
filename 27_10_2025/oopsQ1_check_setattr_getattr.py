'''
Q1:
Create a class Car with attributes: brand, model, price.
Now write code that:
Checks if the object has an attribute price.
If it does, prints it.
If not, creates it using setattr() and assigns a value.
Then use getattr() to print it dynamically.
'''

class Car:
    def __init__(self, brand, model, price=0):
        self.brand = brand
        self.model = model
        self.price = price
car1 = Car('XYZ', 'x123')
if hasattr(car1, 'price'):
    print(f"Does car1 have price attribuute? {hasattr(car1, 'price')}: price: {getattr(car1,'price',0)}")
else:
    print(f"No car1 does not have price attribute.. creating one, and the price is: ")
    setattr(car1, 'price', 200)
    print(getattr(car1, 'price'))
'''   
Question 2:
Modify the above to:
Add a new attribute mileage dynamically if not present.
Print all attributes of the object without using obj.__dict__ directly. 
'''
setattr(car1, 'mileage', 10)
print(f"All attributes are: {dir(car1)}")
# this gives all the attributes, but we want only the user defined attributes of the object.
all_attributes_car1 = dir(car1)
only_userdefined_attributes = [attribute for attribute in all_attributes_car1 if not attribute.startswith('__') and not attribute.startswith('_')]
print(only_userdefined_attributes)