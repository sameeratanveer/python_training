'''
Generate a random password of length 12 using random.choices().
'''
import random
import string
available_chars = string.ascii_letters + string.digits + '!@#_$%'
password = ''.join(random.choices(available_chars, k=12))
print(password)