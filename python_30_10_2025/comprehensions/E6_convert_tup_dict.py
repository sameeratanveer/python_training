'''
Convert a list of tuples [('a',1), ('b',2)] to a dictionary using comprehension.
'''
tup_dict = {element[0]:element[1] for element in [('a',1), ('b',2)]}
print(tup_dict)