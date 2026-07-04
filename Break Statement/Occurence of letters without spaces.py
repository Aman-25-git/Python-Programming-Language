#program on Occurences of letter without spaces in a word
#Ex-9
word=input("Enter a word:")
d={}
for ch in word:
    if (not ch.isspace()):
        if (ch not in d):
            d[ch]=1
        elif (ch in d):
            d[ch]=d[ch]+1
else:
    for i,j in d.items():
        print("{}-->{}".format(i,j))
