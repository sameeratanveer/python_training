'''
Write a program to:
Read each line.
Split the two numbers and divide them.
Handle exceptions for:
ZeroDivisionError
ValueError
FileNotFoundError
Store the successful division results in a new file results.txt.
'''

try:
    with open("numbers.txt", 'r') as f:
        try:
            with open("division_results.txt", 'a+') as f2:
                for line in f.readlines():
                    line = line.split(' ')
                    try:
                        result = int(line[0])/int(line[1])
                    except ValueError:
                        print("Number should be integer!")
                        f2.write(f"{line[0]}/{line[1]} = Number should be integer!\n")
                    except ZeroDivisionError:
                        print("Cannot divide by Zero!")
                        f2.write(f"{line[0]}/{line[1]} = Cannot divide by Zero!\n")
                    else:
                        f2.write(f"{line[0]}/{line[1]} = {result}\n")
        except IOError as e:
            print(e)
except FileNotFoundError:
    print("File does not exists!")
else:
    print("Read from file successfully!")