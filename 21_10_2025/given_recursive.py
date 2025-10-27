'''
1.
write a program to get factorial of a number using recursion
'''



def recursive_factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * recursive_factorial(num-1)
print(recursive_factorial(5))

'''
2. Write a recursive function to reverse a string.
'''

def recursive_reverse_string(s, char):
    if char < 0:
        return ''
    else:
        return s[char] + recursive_reverse_string(s, char-1)
print(recursive_reverse_string('string', len('string')-1))

'''
3.
Write a recursive function that generates all subsets (the power set) of a given list of elements.
'''
def recursive_all_subsets(nums):
    if not nums:
        return [[]]
    first = nums[0]
    rest = recursive_all_subsets(nums[1:])
    return rest + [[first] + subset for subset in rest]

print(recursive_all_subsets([1,2,3]))

'''
4.
Write a recursive function to generate all permutations of a given string.'''
def permute(s):
    if len(s) == 1:
        return [s]  # only one permutation
    result = []
    for i in range(len(s)):
        # take the current character
        current = s[i]
        # remaining characters
        remaining = s[:i] + s[i+1:]
        # recurse on remaining
        for p in permute(remaining):
            result.append(current + p)
    return result
print(permute("ABC"))

'''
1. 
You are building a billing system where you need a function `calculate_total(price, quantity)` that returns the total price. How would you design the function to accept only positional arguments?
'''
# def total_price(price, quantity, /):
#     return price * quantity
# print(total_price(10, 2))
# print(calculate_total(price=10, quantity=20)) # error because cant use keyword.

'''
2.2. In a video game, players can choose their character's weapon. If no weapon is selected, the default should be "Sword". 
- Write a function `choose_weapon(player_name, weapon="Sword")`.  
- What happens if a player does not specify the weapon?
'''

# def choose_weapon(player_name, weapon='sword'):
#     print(f'Name: {player_name} chosen weapon: {weapon}')
# choose_weapon('sam','gun')
# choose_weapon('sam')


