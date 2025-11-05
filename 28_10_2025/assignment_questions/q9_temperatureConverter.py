'''
Create a class TemperatureConverter with static methods for Celsius ↔ Fahrenheit conversions.
'''

class TemperatureConverter:
    @staticmethod
    def celsius_fahrenheit(temp):
        return f' {temp * 1.8 + 32} F'

    @staticmethod
    def fahrenheit_celsius(temp):
        return f'{(temp - 32)*5/9} C'

inp = int(input("Press 1 to convert temperature from Celsius to Fahrenheit, else 2 otherwise: "))
if inp == 1:
    celsius = float(input("Enter celsius to convert to Fahrenheit : "))
    print(TemperatureConverter.celsius_fahrenheit(celsius))
elif inp == 2:
    fahrenheit = float(input("Enter fahrenheit to convert to celsius : "))
    print(TemperatureConverter.fahrenheit_celsius(fahrenheit))
else:
    print("Invalid input!")