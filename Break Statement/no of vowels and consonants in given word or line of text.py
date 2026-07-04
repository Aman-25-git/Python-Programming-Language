#program on finding no of vowels and consonants in given word or line of text without spaces in a word
#Ex-10
word=input("Enter a word/line of text:")
d={}
for ch in word:
    if (not ch.isspace()):
        if (ch not in d):
            d[ch]=1

        elif (ch in d):
            d[ch]=d[ch]+1
else:
    vowels=0
    cons=0
    for i in word:
        if i in "aeiouAEIOU":
            vowels=vowels+1
        else:
            cons=cons+1
    print("*"*50)
    print("OCCURENCE OF LETTERS IN  WORD:")
    print("*"*50)
    for i,j in d.items():
        print("{}-->{}".format(i,j))
    print("*"*50)
    print("vowels are {}\nconsonants are {}".format(vowels, cons))
    print("*"*50)
print()
print("-"*50)