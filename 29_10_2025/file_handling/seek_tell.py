'''
Read the first 10 characters of a file, print current pointer position, move it back to start, and print first line again.
'''

with open("quotes.txt", "r") as f:
    print(f"Reading first 10 characters of a file: {f.read(10)}")
    print(f"Current Pointer position: {f.tell()}")
    f.seek(0)
    print(f"Reading first line again after moving back to first position: {f.readline()}")

