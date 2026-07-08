#Program on Pyton Retrival from Python Word By using continue statement
#Ex-1
s="Python"
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("This is else block in for loop")
print("*"*50)
#my requirement is to get pyth form s
i=0
while(i<len(s)):
    if(s[i]=='h') or (s[i]=="y"):
        i=i+1
        continue
    print(s[i],end="")
    i = i + 1
else:

    print()
    print("This is else block in for loop")
print()
print("*"*50)