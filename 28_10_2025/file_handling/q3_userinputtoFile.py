'''
Write a program that takes user input and writes it to a file.
Append user’s name and timestamp to the same file each time it runs.
Write multiple lines using a list with writelines().
'''
from datetime import  datetime
user_input = []
while True:
    current_inp = input("Enter input: ")
    user_input.append(current_inp+f' Sameera - {datetime.now()}\n')
    contin = input("Would you like to continue? 'y/Y' to continue else 'n/N': ")
    if contin.lower() != 'y':
        break
with open('userfile.txt', 'w') as f:
    f.writelines(user_input)

with open('userfile.txt', 'r') as f:
    print(f.read())