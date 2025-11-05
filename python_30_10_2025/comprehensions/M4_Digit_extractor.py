'''
Digit Extractor:
Given a string like "Data123Science456", extract all the digits and convert them into a list of integers using comprehension
'''
s = "Data123Science456"
int_list = [int(char) for char in s if char.isdigit()]
print(int_list)