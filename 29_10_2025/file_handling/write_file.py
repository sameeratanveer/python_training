'''
Create a program that takes user input (name and age) and writes them into users.txt.
Run the program again and append more users.
Verify by reading and printing all data.
'''

def write_to_file(name, age):
    with open('users.txt', 'a') as f:
        f.write(f"{name}, {age}\n")
        return True
name = input("Enter the name: ")
age = int(input("Enter the age: "))
if write_to_file(name, age):
    print("Successfully noted!")

with open('users.txt', 'r') as f:
    print(f.read())

