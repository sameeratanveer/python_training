'''
Read a file data.txt, count how many times each word appears,
and write the frequency dict to a new file frequency.json.
Use:
Dictionary comprehension
json.dump()
Handle FileNotFoundError, PermissionError, IOError
'''

try:
    with open("data.txt", "r") as f:
        content = f.read()
        content = content.split(' ')
        content = [word for sentence in content for word in sentence.split()]
        print(type(content))
except FileNotFoundError:
    print("File not found!")