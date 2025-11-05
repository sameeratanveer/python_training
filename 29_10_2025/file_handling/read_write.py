'''
Create a todo.txt file.
Write 3 tasks initially.
Reopen the same file in read mode and display them as a numbered list.
'''
tasks = ["Watch TV", "Eat", "Sleep"]
with open("todo.txt", 'w+') as f:
    f.write('\n'.join(tasks))
    print("Reading the tasks!")
    f.seek(0)
    for task_num, task in enumerate(f.readlines(), 1):
        print(task_num, task)