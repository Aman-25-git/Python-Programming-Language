#program for accepting List of Names
n=int(input("Enter how many names want to enter in list:"))
if(n<=0):
    print("Enter valid number --tryagain")
else:
    lst=[]
    s=0
    for i in range(1,n+1):
        val=(input("Enter {} Name :".format(i)))
        s=s+i
        lst.append(val)
    else:
        print("List of names:",lst)
        print(s)