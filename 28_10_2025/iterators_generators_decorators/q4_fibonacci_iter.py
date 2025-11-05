
class Fibonnaci:
    def __init__(self, n):
        self.n = n
        self.first = 0
        self.second = 1
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index == 0 and self.current_index < self.n:
            self.current_index += 1
            return self.first
        elif self.current_index == 1 and self.current_index < self.n:
            self.current_index += 1
            return self.second
        elif self.current_index < self.n:
            current = self.first + self.second
            self.first = self.second
            self.second = current
            self.current_index += 1
            return current
        else:
            raise StopIteration

for num in Fibonnaci(8):
    print(num)