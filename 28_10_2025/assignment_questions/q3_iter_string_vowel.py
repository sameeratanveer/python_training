'''
Create a custom iterator class that iterates over a string and returns only vowels.
'''

class VowelReturn:
    def __init__(self, s):
        self.s = s
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < len(self.s):
            char = self.s[self.current]
            self.current += 1
            if char.lower() in 'aeiou':
                return char
        raise StopIteration

for vowel in VowelReturn('Hello'):
    print(vowel)

