#Program on Pyton Retrival from Python Word By without using continue statement
#Ex-1
s="Python"
for ch in s:
    print(ch)
else:
    print("This is else block in for loop")
print("*"*50)
#my requirement is to get pyth form s
for ch in s:
    if(ch=='h'):pass
    else:
        print(ch,end="")
else:
    print()
    print("This is else block in for loop")
print()
print("*"*50)