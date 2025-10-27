'''
1. Create a class Car with attributes brand, model, and price.
Create two objects and print their details.
'''


class Car:
    '''
    3. Add a class variable vehicle_type = "Car".
    Access it through both the class and object.
    Try modifying it via the object and class — what changes where?
    '''
    vehicle_type = 'Car'

    '''
    4. Add a class method that counts how many Car objects were created.
    '''
    cars_count = 0

    @classmethod
    def count_cars(cls):
        cls.cars_count += 1

    @classmethod
    def get_cars_count(cls):
        return cls.cars_count

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.__class__.count_cars()


    '''
    2. Add a method display_info() that prints details nicely.
    Call it using both Car.display_info(car1) and car1.display_info() and observe what happens.
    '''

    def display_info(self):
        print(f"Brand = {self.brand}\nModel = {self.model}\nPrice =  {self.price}")


    '''
    5. Add a static method is_luxury(price) → returns True if price > 50,00,000.
    '''
    @staticmethod
    def is_luxury(price):
        return True if price > 5000000 else False



# car object 1:
car1 = Car("Tata", 'Punch', 555000)
car2 = Car("Hyundai", "Creta", 1000000)

# 1. print the details:
# print(car1.brand, car1.model, car1.price)
# print(car2.brand, car2.model, car2.price)

# 2. Answer:
# Car.display_info(car1)
# car1.display_info()

# 3. Answer:
print(Car.vehicle_type)
print(car1.vehicle_type)
car1.vehicle_type = "Car1"
print(Car.vehicle_type)
print(car1.vehicle_type)
Car.vehicle_type = 'Car'
print(car1.vehicle_type)
print(Car.vehicle_type)

print(Car.get_cars_count())

print(car1.is_luxury(20000))