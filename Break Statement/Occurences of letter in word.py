#program on Occurences of letter in a word
#Ex-8
word=input("Enter a word:")
d={}
for ch in word:
    if (ch not in d):
        d[ch]=1
    elif (ch in d):
        d[ch]=d[ch]+1
else:
    for i,j in d.items():
        print("{}-->{}".format(i,j))
