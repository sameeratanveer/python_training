def reverse_string(s):
    current_index = len(s)-1
    while current_index >= 0:
        yield s[current_index]
        current_index -= 1

for char in reverse_string("Hello"):
    print(char)