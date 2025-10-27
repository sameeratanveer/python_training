import time

start_time = time.time()
for i in range(1000000):
    pass
end_time = time.time()
print(f'Time taken for for loop to 100000 iterations is: {end_time-start_time}')

start_time = time.time()
i = 0
while i < 1000000:
    i = i +1
end_time = time.time()
print(f'Time taken for while loop to 100000 iterations is: {end_time-start_time}')