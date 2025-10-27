'''
Q3. Group Consecutive Elements
nums = [1, 1, 2, 3, 3, 3, 4, 1, 1]
Expected Output: [[1, 1], [2], [3, 3, 3], [4], [1, 1]]
'''

nums = [1, 1, 2, 3, 3, 3, 4, 1, 1]
outp = []
i= 0

while i < len(nums):
    j = i
    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
        j += 1
    outp.append(nums[i:j+1])
    i = j + 1

print(outp)