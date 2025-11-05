class Account:
    def __init__(self):
        self.__balance = 1000
        self._branchcode = 'ABC'
acc = Account()
print(f"Branchcode = {getattr(acc, '_branchcode')}")
# print(f"Balance = {getattr(acc, '__balance')}")
setattr(acc, '_branchcode', 'XYZ')
print(f"Branchcode after chanfing = {getattr(acc, '_branchcode')}")
setattr(acc, '__balance', 100)
print(f"balance after changing: {getattr(acc, '__balance')}")
