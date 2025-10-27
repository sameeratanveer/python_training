"""
What is String?
Strings are surrounded by either ' ' or  " "
'hello' is same as "hello"
"""

# Example of strings are:
my_name = 'sameera'
company = "Bilvantis"

# strings within "" or  ''
daily_quote = "Today he wrote the quote: \"Practice makes man perfect!\""
print(daily_quote)

weather_today = "It's raining today"
print(weather_today)

weather_again = 'It\'s raining today'
print(weather_again)

# Multiline String: ''' ''' or """ """
poem = """Twinkle twinkle little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky!"""
print(poem)


# Methods and work arounds of string:

# 1. Len() : length of the string:
name = 'sam  eera '
print(len(name))

# 2. IN operator for strings
# in operator is used to check if the substring of the string is present inside it
# Question: Check if twinkle is present inside the poem?
print('twinkle' in poem) # it returns True or False.

# 3. NOT IN operator for strings:
# not in checks if the substring not there in the string (opposite of in)
print('twinkle' not in poem) # true if it is not there else false

# ----------------------------- STRING INDEXING ---------------
sentence = 'Hello world! Welcome.'
print("Index of first character is: ", sentence[0])
print("Index of last character is : ", sentence[len(sentence)-1])
print("Index of e in the sentence is: ", sentence.index('e'))
print("Index of first letter of the substring 'Hello' in the sentence is", sentence.index('Hello'))

# ------------------------------ STRING SLICING --------------------------
daily_quote = "Today he wrote the quote: \"Practice makes man perfect!\""
# Q: Only get the word Practice from the daily_quote
print(daily_quote[27:36])

# Q: first 5 characters from the string:
print(daily_quote[:5])

# Q: Last 4 characters:
print(daily_quote[-4:])

# Q: Get the characters placed on even positions:
print(daily_quote[::2])

# Q. Reverse a string using negative slicing.
print("Reverse: ", daily_quote[::-1])

# Q. Index out of range:
print(daily_quote[len(daily_quote)-2: len(daily_quote) +5])

# ------------------------- MODIFYING STRINGS ----------------------
# 1. UPPER() : converts the string to an uppercase letters.
print(daily_quote.upper())

# 2. lower() : converts each character of the string to its equivalent lower case character.
print(daily_quote.lower())

# 3. strip() : removes whitespaces
print('   hello  '.strip())
print('//hello//'.strip('/'))

# 4. lstrip() : removes left whitespaces
print('   hello  '.lstrip())
print('%hello%%'.lstrip('%'))

# 5. rstrip() : removes right side whitespaces in string
print('   hello  '.rstrip())
print('__hello__'.rstrip('_'))

# 6. replace() : replaces character or substring of the string with other character or substring
print('   hello   '.replace(' ', '_'))
print('hello'.replace('hel', 'bel'))

# 7. split() : split method splits the string into substring when it find the given separator.
print('hello,world'.split(','))
print('welcome/home'.split('/'))
print('hii..hello'.split('..'))

# 7.1: splitlines() : splits the string on line breaks
print(poem.splitlines())

# 8. count() : returns the count of the value inside a string
print('hello'.count('l'))
print(daily_quote.count(' '))
print(poem.count('\n'))

# 9. index() : finds the index of the character or starting position of the substring
print('hello'.index('l')) # returns first instance index.
print('hello'.index('llo'))

# 9.1: rindex() : returns the last instance index.
print('hello'.rindex('l'))
print('hello'.rindex('el'))

# 10. find() : finds the index of the character or starting position of the substring
print('hello'.find('l'))
print('hello'.find('llo'))

# 10.1: rfind() : right most index
print('hello'.rfind('l'))
print('hello'.rfind('llo'))

# 11. startswith() : checks if the string starts with the specified character or substring
print('hello'.startswith('h'))
print('hello'.startswith('hell'))
print('hello'.startswith(('he', 'hel', 'wal')))
print('hello'.startswith('h',2,len('hello')))

# 12. endswith() : checks if the string ends with the specified character or the substring
print('hello'.endswith('o'))
print('hello'.endswith('ello'))
print('hello'.endswith(('he', 'hel', 'ello')))
print('hello'.endswith('o',2,len('hello')))

# ------------ checks methods : is... --------------
# 1. isalpha() : checks if the string contains all alphabets onlu
print('hello'.isalpha())
print('h@lla'.isalpha()) # special character
print('héllo'.isalpha()) # é is a latin character

# 2. isalnum() : checks combination of numbers + characters
print('hello123'.isalnum())
print('__la34'.isalnum()) # _  special character
print('héllo123'.isalnum()) # é is a latin character

# 3. isascii() : checks if the string all characters are ascii
print('hellp'.isascii())
print('65_'.isascii())
print('héllo123'.isascii())
print('£euro'.isascii())
print('🎉congrats'.isascii())

# 4. isnumeric(), isdigit(), isdecimal() : returns true if all characters inside the string is specific.

# 5. islower(), isupper() : checks if all characters in the strings are lower or upper respectively

# 6. isspace(), istitle()

# 7. join() : joins the string with the iterable.
print(','.join(['Hi', '123']))

# 8. swapcase() : lower case becomes uppercase, uppercase becomes lowercase
print('Hello'.swapcase())

# 9. zfill() :
print('hello'.zfill(10)) # fills the hello with leading zeroes until the length becomes 10.

# ------------------- CONCATENATE string: -------------
# using +
print('hello' + ' ' +  'world' + '\n' + 'welcome!')

# --------------- FORMAT STRINGS ----------------
# using f'' string
name = 'sameera'
age = 21
marks = 8.19
details = f'My name is {name} and I am {age} years old\nI got {marks:.6f} points'
print(details)

details = f'My name is {name} and I am {age} years old\nI got {marks*10} percentage'
print(details)

details = 'My name is {} and I am {} years old'.format(name, age)
print(details)




