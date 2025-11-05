'''
Each student’s name and marks stored in students.txt as:
Name - Marks
Program menu:
Add Student
View All Students
Find Student by Name
Delete File
'''
import os


while True:
    user_choice = int(input("Press 1 to add student\nPress 2 to View all students and their marks\nPress 3 to find student by name\nPress 4 to delete the file! : "))
    if user_choice == 1:
        name = input("Enter the name: ").lower()
        marks = float(input("Enter the marks: "))
        with open("students.txt", 'a+') as f:
            f.write(f"{name},{marks}\n")
    elif user_choice == 2:
        with open("students.txt", 'r') as f:
            print(f.read())
    elif user_choice == 3:
        name_search = input("Enter the name of the student : ").lower()
        found_student = False
        with open("students.txt", 'r') as f:
            for line in f.readlines():
                if name_search == line.split(',')[0]:
                    found_student = True
                    print(line)
            if not found_student:
                print(f"Student with the name {name_search} does not exists!")
    elif user_choice == 4:
        print("To delete a file, we need to authenticate!")
        admin = input("Enter the admin username: ")
        password = input("Enter the password! :")
        if admin == 'admin' and password == '1234':
            os.remove("students.txt")
            if not os.path.exists("students.txt"):
                print("File deleted successfully!")
    else:
        exit()



