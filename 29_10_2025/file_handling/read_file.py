'''
Create a text file named quotes.txt with at least 5 lines.
Write a program to:
Read and print the entire file content.
Print the first 3 characters.
Print each line with line numbers.
'''

file = open('quotes.txt', 'x')
lines = ['Create a text file named quotes.txt with at least 5 lines.', 'Write a program to:', 'Read and print the entire file content.', 'Print the first 3 characters.', 'Print each line with line numbers.']
for line in lines:
    file.write(line+'\n')
file.close()

with open('quotes.txt', 'r') as f:
    print(f"Entire file content: ")
    print(f.read())
    print()
    f.seek(0)
    print("First 3 characters: ")
    print(f.read(3))
    print()
    f.seek(0)
    print("Each line with line numbers: ")
    for index, line in enumerate(f.readlines()):
        print(index, line)
print("Done!")