class Account:
    def __init__(self):
        self.balance = 1000

    def __del__(self):
        print(f"Instead of deleting, resetting the balance:")
        self.balance = 0
        print(f"Balance = {self.balance}")
acc = Account()
del acc.balance