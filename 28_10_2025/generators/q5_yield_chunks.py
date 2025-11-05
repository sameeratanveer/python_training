'''
Create a generator chunk_reader(iterable, chunk_size) that yields chunks (lists) of elements from an iterable.
'''

iterable = [1, 2, 3, 4, 5, 6, 7]
chunk_size = 3

def chunk_reader(iterable, chunk_size):
    current_element = 0
    while current_element < len(iterable):
        yield iterable[current_element:current_element+chunk_size]
        current_element += chunk_size

for chunks in chunk_reader(iterable, chunk_size):
    print(chunks)