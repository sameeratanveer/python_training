'''
Create a list of words longer than 3 letters from a given sentence.
'''

list_words = [word for word in 'I am is Hello No worry'.split(' ') if len(word) > 3]
print(list_words)