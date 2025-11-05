'''
Given names = ['Sameera', 'Tanveer', 'Ali'], create a dictionary mapping each name to its length.
'''
names = ['Sameera', 'Tanveer', 'Ali']
name_len_map = {name:len(name) for name in names}
print(name_len_map)