'''
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_nums = [number for l_element in numbers for number in l_element if number%2==0]
print(even_nums)