'''
Q6. Reverse Each Word in Sentence
s = "Python is powerful"
Expected Output: "nohtyP si lufrewop"
'''

s = "Python is powerful"
outp = ' '.join([word[::-1] for word in s.split()])
print(outp)