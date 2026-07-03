#PROGRAM FOR ACCEPTING A LINE OF TEXT AND DISPLAY EVERY CHAR
#Ex-7
word=input("Enter a word/line of text:")
print("*"*50)
print("By using For loop +ve Indices in forward direction")
print("*"*50)
for i in range(0,len(word)):
    print("\t{}".format(word[i]))
print("*"*50)

print("By using For loop -ve Indices in forward direction")
print("*"*50)
for i in range(0,len(word)-1+1):
    print("\t{}".format(word[i]))
print("*"*50)

print("By using For loop +ve Indices in Backward direction")
print("*"*50)
for i in range(len(word)-1,-1,-1):
    print("\t{}".format(word[i]))
print("*"*50)

print("By using For loop -ve Indices in Backward direction")
print("*"*50)
for i in range(-1,-len(word)-1,-1):
    print("\t{}".format(word[i]))
print("*"*50)
print("Program Execution Is Completed  \n\t\t\t\t\t--Thankyou For Using This Program")
print("*"*50)