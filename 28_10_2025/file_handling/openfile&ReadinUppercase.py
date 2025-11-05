'''
Open the same file and print every line in uppercase.
'''

with open('text.txt', 'r') as f:
    all_content = f.read()
    print(all_content.upper())
    # for char in all_content:
    #     print(char.upper(), end='')
