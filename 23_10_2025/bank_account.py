'''1. Create a class Account that stores a customer’s name and balance.

Make the balance a private variable.

Provide methods to deposit and withdraw money (withdraw should check for insufficient funds).
Then create a subclass SavingsAccount that inherits from Account and adds an attribute for interest_rate, and a method add_interest() to increase the balance based on the interest rate.
'''

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance # balance is a private variable

    def get_balance(self):
        return self.__balance

    def deposit(self, money):
        if money < 0:
            print("Cannot deposit negative money!")
            return
        self.__balance += money # desposit moneyy
        print(f"{money} Money deposited")

    def withdraw(self, money):
        if self.__balance - money < 0:
            print("Insufficient balance!")
        else:
            self.__balance -= money
            print(f"{money} withdrawn from account")


class SavingsAccount(Account):
    def __init__(self, name, balance=0, interest_rate = 0):
        super().__init__(name, balance)
        self.interest_rate = interest_rate / 100 # interest rate is in percentages..

    def add_interest(self):
        # interest gets deposited..
        interest_balance =  (self.get_balance() * self.interest_rate)
        self.deposit(interest_balance)
        print(f"{interest_balance} interest is added successfully!")

acc1 = Account('Sam', 1000)
print(f"Balance for the Account Holder {acc1.name} is {acc1.get_balance()} ")
acc1.deposit(200)
print(f"Balance for the Account Holder {acc1.name} is {acc1.get_balance()} ")
acc1.withdraw(10)
print(f"Balance for the Account Holder {acc1.name} is {acc1.get_balance()} ")
acc1.withdraw(4000)
acc1.deposit(-10)

savingacc1 = SavingsAccount('Sameera', 10000, 5)
print(f"Balance for the Account Holder {savingacc1.name} is {savingacc1.get_balance()} ")
savingacc1.deposit(20000)
print(f"Balance for the Account Holder {savingacc1.name} is {savingacc1.get_balance()} ")
savingacc1.withdraw(1000)
print(f"Balance for the Account Holder {savingacc1.name} is {savingacc1.get_balance()} ")
savingacc1.withdraw(4000)
print(f"Balance for the Account Holder {savingacc1.name} is {savingacc1.get_balance()} ")
savingacc1.deposit(-10)
savingacc1.add_interest()
print(f"Balance for the Account Holder {savingacc1.name} is {savingacc1.get_balance()} ")
