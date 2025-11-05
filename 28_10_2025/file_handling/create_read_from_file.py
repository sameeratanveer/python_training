'''
Create a text file with 5 lines and read:
Entire content at once
Only the first two lines
All lines in a list and print their count
'''

# writes to file
file_object = open('text.txt', 'w')
file_object.write("Hello world!\nNice to meet you\nWelcome!")
file_object.close()

# reads from file.
file_object = open('text.txt', 'r')
print("Reads the entire content at once.")
print(file_object.read())
file_object.close()
print()
file_object = open('text.txt', 'r')
print("Reads only the first two lines")
file_content_list = file_object.readlines()
print(file_content_list)
print(f"1st line: {file_content_list[0]}")
print(f"2nd line: {file_content_list[1]}")
print("All lines in a list and their count")
for line_num, line in enumerate(file_content_list):
    print(f"{line_num}. {line}")
print(f"Total lines: {len(file_content_list)}")
file_object.close()