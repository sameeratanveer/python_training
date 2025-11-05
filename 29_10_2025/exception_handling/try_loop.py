'''
Create a loop that reads inputs until user enters quit. Use try to catch KeyboardInterrupt and print a friendly message, but allow SystemExit to propagate.
'''
while True:
    try:
        inp = input("Enter the number: ")
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("Program interrupted by keyboard interruption!")
    else:
        if inp.lower() == 'quit':
            exit()
    finally:
        print("Finally!")

