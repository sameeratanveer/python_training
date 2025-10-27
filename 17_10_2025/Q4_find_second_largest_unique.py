'''
Q4. Find Second Largest Unique Number
nums = [10, 20, 4, 45, 99, 99, 20]
Expected Output: 45
'''

nums = [10, 20, 4, 45, 99, 99, 20]
nums = list(set(nums))
nums.sort()
print(f'Second largest unique number is: {nums[-2]}')