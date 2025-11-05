'''
Create a decorator that logs the arguments and return value of a function.
'''
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is called with arguments {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function returned {result}")
        return result
    return wrapper

@log_decorator
def sum_args(*args):
    return sum(args)

sum_args(1,2)