'''
Sets: set is a datatype in python that stores multiple values or elements in a single variable or container

Set is unorders, unchangeable, and unindexed datatype that means the elements inside the set cant be accessed using indexes
Set is mutable but the elements inside it can not be changed because we cant use index to specify the element and then change that element. either we add the new value and delete the old value but we cant access the old value and mutate it with the other value.
'''

set1 = set()
print(type(set1))

set2 = {}
print(type(set2))

fruits = {'apple', 'banana', 'cherry'}
print(type(fruits))
print(fruits)

fruits1 =set(('apple', 'banana', 'cherry'))
print(type(fruits1))
print(fruits1)

data = {'fruit', 'vegetable', 28, True, 1, 10.14}
print(type(data))
print(data)

# Sets doesnt allow duplicates
dupset = {'fruit', 'vegetable', 28, True, 28, 1, 10.14}
print(dupset)


print(len(dupset))

# 1. add() : to add element in set
data.add(10)
print(data)

# 2. update() : add iterable in set
data.update(['hello', 3, (20, 30, 40)])
print(data)

# 3. remove() : remove an item
data.remove(True)
print(data)

# 4. discard() : removes items
data.discard('vegetable')

# 5. pop() : removes any random item from the set
data.pop()
print(data)

# 6. clear(): empties the set
data.clear()
print(data)

# 7. del : deltes the whole set from the memory
del data

# ======================== Join sets : union, intersect, ... ===============
# 1. union
dupset.union(fruits)
print(dupset)

# 2. intersect
fruits.intersection(fruits1)
print(fruits)

# -- frozenset() is an immutable version of set means we cant add or delete elemets from the set
dupset = frozenset(dupset)
print(type(dupset))
print(dupset)
print(dupset.add(10))

# isupperset() -- returns true if all elements of other set is present in
# issubset() -- returns true if all elements of this main set is present in subset

