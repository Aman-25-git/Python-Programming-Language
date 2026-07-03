#program for accepting a Line of Text and Find Length of Each word
word=input("Enter word /text of line:")
line=word.split()
d={}
for words in line:
    d[words]=len(words)
else:
    for i,j in d.items():
        print("{}-->{}".format(i,j))

