'''
Q1. Remove Duplicates but Keep Order
nums = [4, 5, 4, 6, 5, 7, 4]
Expected Output: [4, 5, 6, 7]
'''

nums = [4, 5, 4, 6, 5, 7, 4]
outp = list(set(nums))
outp.sort()
print(outp)
