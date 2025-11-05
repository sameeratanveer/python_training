'''
Create a list of colors and:
Convert it to an iterator using iter().
Use next() manually to print elements until StopIteration occurs (handle it with try-except).
'''

class ColorIter:
    def __init__(self, colors):
        self.colors = colors
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            current_element = self.colors[self.index]
            self.index += 1
            return current_element
        except:
            raise StopIteration

colors = ['Red', 'Blue', 'Green']
coloriter = ColorIter(colors)
for color in coloriter:
    print(color)