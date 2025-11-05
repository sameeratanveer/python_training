'''
Given {'a':1, 'b':2, 'c':3}, create a new dict with values squared.
'''
squares_dict = {key:value*value for key, value in {'a':1, 'b':2, 'c':3}.items()}
print(squares_dict)