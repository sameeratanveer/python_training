'''
3.Create a class Vehicle that has the following attributes:

brand, model, __rental_price_per_day (private attribute)
Include methods:
display_info() → prints vehicle details
set_price(price) → sets the daily rental price
get_price() → returns the daily rental price
'''

class Vehicle:
    def __init__(self, brand, model, rent_price):
        self.brand = brand
        self.model = model
        self.__rental_price_per_day = rent_price

    def get_price(self):
        return self.__rental_price_per_day
    def set_price(self, new_price):
        self.__rental_price_per_day = new_price

    def display_info(self):
        print(f"Brand = {self.brand}, Model = {self.model}, Daily price = ₹{self.__rental_price_per_day}")

'''
Then create two subclasses:

Car → with extra attributes: seating_capacity, fuel_type

Bike → with extra attributes: engine_capacity, bike_type
Both subclasses should override the display_info() method to include their additional attributes.
'''

class Car(Vehicle):
    def __init__(self, brand, model, rent_price, seating_capacity=4, fuel_type='petrol'):
        super().__init__(brand, model, rent_price)
        self.seating_capacity = seating_capacity
        self.fuel_type = fuel_type
    def display_info(self):
        print(f"Brand = {self.brand}\nModel = {self.model}")
        print(f"seating capacity = {self.seating_capacity}\nfuel-type = {self.fuel_type}\nDaily price = ₹{self.get_price()}")

class Bike(Vehicle):
    def __init__(self, brand, model, rent_price, engine_capacity='', bike_type=''):
        super().__init__(brand, model, rent_price)
        self.engine_capacity = engine_capacity
        self.bike_type = bike_type
    def display_info(self):
        print(f"Brand = {self.brand}, \nModel = {self.model}")
        print(f"engine_capacity = {self.engine_capacity}, \nbike_type = {self.bike_type}\nDaily price = ₹{self.get_price()}")

car1 = Car("Toyota", "Corolla", 0, seating_capacity=5, fuel_type="Petrol")
car1.set_price(2500)

bike1 = Bike("Yamaha", "R15", 0, engine_capacity="155cc", bike_type="Sports")
bike1.set_price(1200)

print("\n--- Car Details ---")
car1.display_info()

print("\n--- Bike Details ---")
bike1.display_info()
