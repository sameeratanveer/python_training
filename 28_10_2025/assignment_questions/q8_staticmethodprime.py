'''
Write a class MathUtils with a static method to check if a number is prime.
'''
class MathUtils:
    @staticmethod
    def prime(number):
        prime_bool = True
        for i in range(2,number//2):
            if number % i:
                prime_bool = False
                return prime_bool
        return prime_bool

print(MathUtils.prime(5))
