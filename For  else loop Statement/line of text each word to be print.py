#program to print each word from the line of text
#Ex-12 home work
words=input("Enter a word/line of text:")
nw=0
x=words.split()
print("*"*50)
for val in x:
    nw=nw+1
    print("{}".format(val))

else:
    print("*"*56)
    print("Number of words={}".format(nw))
    print("*"*56)



