#PROGRAM FOR ACCEPTING A LINE OF TEXT AND DISPLAY EVERY CHAR
#Ex-7
word=input("Enter a word/line of text:")
print("*"*50)
print("By using While loop +ve Indices in forward direction")
i=0
while(i<len(word)):
    print("\t{}".format(word[i]))
    i=i+1
print("*"*50)

print("By using While loop -ve Indices in forward direction")
i=-len(word)
while(i<=-1):
    print("\t{}".format(word[i]))
    i=i+1
print("*"*50)

print("By using While loop +ve Indices in Backward direction")
i=len(word)-1
while(i>=0):
    print("\t{}".format(word[i]))
    i=i-1
print("*"*50)

print("By using While loop -ve Indices in Backward direction")
i=-1
while(i>=-len(word)):
    print("\t{}".format(word[i]))
    i=i-1
print("*"*50)
print("Program Execution Is Completed  \n\t\t\t\t\t--Thankyou For Using This Program")
print("*"*50)