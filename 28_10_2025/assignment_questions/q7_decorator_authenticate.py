'''
Implement a decorator that checks if a user is authenticated before executing a function.
'''
def authenticate_execute(func):
    def wrapper(*args, **kwargs):
        user_name = input("Enter name: ")
        user_password = input("Enter password: ")
        if user_name == "sameera" and user_password == "1234":
            print("Authenticated successfully! Executing the function!")
            func(*args, **kwargs)
        else:
            print("Authentication failed!")
    return wrapper


class AuthenticateUser:
    @authenticate_execute
    def execute_func(self):
        print("Executed after authentication!")


au = AuthenticateUser()
au.execute_func()
