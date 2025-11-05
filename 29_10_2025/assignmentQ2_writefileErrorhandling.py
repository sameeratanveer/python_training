'''
Write a program that:
Asks the user to enter text input.
Tries to open a file in write mode and save the input.
If any I/O error occurs, catch it using except IOError as e and print the error message.
'''

user_input = input("Enter the text input: ")
try:
    with open("test.txt", "w") as f:
        f.write(user_input)
except Exception as e:
    print(e)
else:
    print("Written successfully!")
finally:
    print("Execution done!")