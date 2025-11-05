'''
Create a class Laptop with:
Instance variables: brand, price
Class variable: discount = 10
Instance method: final_price() → applies discount and prints final price
Class method: update_discount(cls, new_discount)
Static method: is_valid_price(price) → returns True if price > 0
✅ Try:
Updating discount using class method
Calling static method before creating any object
'''

class Laptop:
    discount = 10
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def final_price(self):
        return self.price - (self.price * Laptop.discount / 100)

    @classmethod
    def update_discount(cls, new_discount):
        cls.discount = new_discount

    @staticmethod
    def isvalid_price(price):
        if price > 0:
            print("True")
        else:
            print("False")

    def __str__(self):
        return f"Brand: {self.brand}, Price: {self.price}"

laptop1 = Laptop('X', 45000)
laptop1.__str__()
print(f"Discount: {laptop1.discount}")
print(f"Final price after initial discount = {laptop1.final_price()}")
Laptop.update_discount(20)
print(f"Discount: {laptop1.discount}")
print(f"Final price after  discount  update = {laptop1.final_price()}")

Laptop.isvalid_price(100)
