'''
11.Scenario: Design an abstract base class PaymentGateway with abstract methods like authenticate() and pay(), and
implement subclasses for CreditCardPayment and UPIPayment.
'''

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(PaymentGateway):
    def __init__(self, cardnumber, expiry_date, cvv, amount):
        self.cardnumber = cardnumber
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.amount = amount
    def authenticate(self):
        print("Card Authenticated!")


    def pay(self):
        print(f"Paid ₹{self.amount} using Credit Card successfully")

class UPIPayment(PaymentGateway):
    def __init__(self, upi_id, pin, amount):
        self.upi_id =upi_id
        self.pin = pin
        self.amount = amount
    def authenticate(self):
        if len(self.pin) < 4:
            print("Authenticated successfully")

    def pay(self):
        print(f"Paid ₹{self.amount} using UPI successfully")

choice = int(input("Choose payment method Enter 1 for card, enter 2 for upi : "))
if choice == 1:
    card = CreditCardPayment("1234567890123456", "12/26", "123", 5000)
    card.authenticate()
    card.pay()
elif choice== 2:
    upi = UPIPayment("sameera@upi", "1234", 2000)
    upi.authenticate()
    upi.pay()
else:
    print("Invalid choice")
