# Open a file and print the longest word present in it.
length=[]
words=[]
with open("data.txt","r") as t:
    content=t.readlines()
    for i in content:
        for j in i.strip("\n").split(" "):
            words.append(j)
            length.append(len(j))
    print(words,length)
    max_length=max(length)
    index=length.index(max_length)
    print(f"The word is {words[index]}")