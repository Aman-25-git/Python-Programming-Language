#program for accepting List of Names and print there length
n=int(input("Enter how many names want to enter in list:"))
if(n<=0):
    print("Enter valid number --tryagain")
else:
    lst=[]
    for i in range(1,n+1):
        val=(input("Enter {} Name :".format(i)))
        lst.append(val)
    else:
        print("List of names: ",lst,)
        for vals in lst:
            print("{} ---->{}".format(vals,len(vals)))
