'''
Q1. Get the below expected output from input
	Input: nums = [3, 5, 3, 2, 5, 5, 2, 3]
	Expected Output: {3: 3, 5: 3, 2: 2}
'''

nums = [3, 5, 3, 2, 5, 5, 2, 3]
unique_elements = set(nums)
nums_count_dict = {}
for element in unique_elements:
    nums_count_dict[element] = nums.count(element)
print(nums_count_dict)

'''
Q2. Merge and Sum Common Keys
	Input:
	d1 = {'a': 100, 'b': 200, 'c': 300}
	d2 = {'a': 300, 'b': 200, 'd': 400}
	Expected Output:
	{'a': 400, 'b': 400, 'c': 300, 'd': 400}
'''

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

merged_sum_dict = {}
for key in set(d1).union(set(d2)):
    merged_sum_dict[key] = d1.get(key,0) + d2.get(key,0)
print(merged_sum_dict)

'''
Q3. Remove Keys with None Values
	Input:
	data = {'name': 'Alice', 'age': None, 'city': 'London', 'phone': None}
	Expected Output: {'name': 'Alice', 'city': 'London'}
'''
data = {'name': 'Alice', 'age': None, 'city': 'London', 'phone': None}
temp = data.copy()
for key,value in temp.items():
    if data[key] is None:
        del data[key]
print(data)

'''
Q4. Sum All Numeric Values in Nested Dictionary
	Input:
	data = {
		"a": 5,
		"b": {"x": 10, "y": {"z": 15}},
		"c": "ignore"
	}
	Expected Output: 30
'''
data = {
		"a": 5,
		"b": {"x": 10, "y": {"z": 15}},
		"c": "ignore"
    }
sumed = 0
for key, value in data.items():
    if isinstance(value, (int, float)):
        sumed += value
    elif isinstance(value, dict):
        # nested dictionary:
        for key2, val2 in value.items():
            if isinstance(val2, (int, float)):
                sumed += val2
            elif isinstance(val2, dict):
                for key3, val3 in val2.items():
                    if isinstance(val3, (int,float)):
                        sumed += val3

print(f"Output: {sumed}")

'''
Q5. Group by Value
	Input: data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
	Expected Output: {1: ['a', 'c'], 2: ['b', 'e'], 3: ['d']}
'''

data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
outp = {}

for key, value in data.items():
    if value not in outp:
        outp[value] = [key]
    else:
        outp[value].append(key)

print(outp)
