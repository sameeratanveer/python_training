'''
Extract all vowels from a string into a list.
'''
vowels = [character for character in 'bilvantis technologies' if character.lower() in 'aeiou']
print(vowels)

vowels = [character if character.lower() in 'aeiou' else 'No' for character in 'bilvantis Technologies']
print(vowels)
