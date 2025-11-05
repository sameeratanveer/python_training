'''
You have two lists — names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78].
Use comprehension to create a dict {name: score} but only include students who scored >80.
'''
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78, 50]
s = zip(names,scores)
print(list(s))
student_marks = {name:score for name, score  in zip(names,scores) if score>80}
print(student_marks)
