'''
Write a program that:
Takes a filename from the user.
Tries to open and read the file.
If the file doesn’t exist, catch the exception and print "File not found. Please check the name."
If successful, print the file content.
'''
import os

file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Please check the name.")
except Exception as e:
    print("Caught error: ", e)
else:
    print("Successfully read from the file!")
finally:
    print("Program executed!")