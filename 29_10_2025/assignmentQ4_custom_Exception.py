'''
Create a program that:
Reads ages from a file ages.txt (each line contains one number).
Define a custom exception class NegativeAgeError.
If any age is negative, raise NegativeAgeError with a message "Invalid age found in file".
Catch it and write that invalid value into a file named invalid_ages.txt.
'''

class NegativeAgeError(Exception):
    pass

with open("ages.txt", "r") as f:
    ages = f.readlines()
    for age in ages:
        with open("invalid_ages.txt", 'a') as f2:
            try:
                if int(age) < 0:
                    f2.write(age)
                    raise NegativeAgeError("Invalid age found in file")
            except ValueError:
                print(f"Invalid value for age! {age}")