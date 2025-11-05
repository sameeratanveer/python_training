'''
Given a dictionary of student marks, create another dict with grades (e.g. if marks ≥ 90 → 'A', else if ≥ 75 → 'B', etc.) using dictionary comprehension.
'''
student_marks = {'stud1':90, 'stud2':28, 'stud3':66, 'stud4':88, 'stud5':46}
student_grade = {student: ('A' if marks>=90  else 'B' if marks>= 75  else 'C' if marks>=50 else 'F') for student,marks in student_marks.items()}
print(student_grade)