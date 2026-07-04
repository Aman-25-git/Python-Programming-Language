#Program on Miss Retrival from MISSISSIPPI Word By using Break statement
#Ex-3
s="MISSISSIPPI"
for ch in s:
    print(ch)
else:
    print("This is else block in for loop")
print("*"*50)
#my requirement is to get Miss form s
icrt=0
for ch in s:
    if(ch=='I'):
        icrt=icrt+1
        if(icrt==2):
            break
    print(ch,end="")
else:
    print("This is else block in for loop")
print()
print("*"*50)