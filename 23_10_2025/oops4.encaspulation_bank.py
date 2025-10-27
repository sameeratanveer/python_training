'''
1. Create a class BankAccount:
    Private variable: __balance
    Methods: deposit(amount), withdraw(amount), get_balance()
Try to access __balance directly — what happens?
'''

class BankAccount:
    def __init__(self, name, balance=0, password = '1234'):
        self.name = name
        self.__balance = balance # private variable.
        self._password = password

    def get_balance(self):
        return self.__balance

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, amount):
        balance = self.get_balance()
        if balance - amount < 0:
            print("Insufficient fund!")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn!")

account1 = BankAccount('Sam')
print(account1.get_balance())
print(account1.deposit(2000))
print(account1.get_balance())
print(account1.withdraw(30000))
account1.__BankAccount__balance = 100
account1._password = 'ABC'
print(account1._password)
