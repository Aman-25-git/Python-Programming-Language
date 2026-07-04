#Program on Pyth Retrival from Python Word By using Break statement
#Ex-2
s="Python"
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("This is else block in While loop")
print("*"*50)
#my requirement is to get pyth form s
i=0
while(i<len(s)):
    if(s[i]=='o'):
        break
    print(s[i],end="")
    i=i+1
else:
    print("This is else block in while loop")
print()
print("*"*50)