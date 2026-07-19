#Program for accepting a List of Values and Get Its Reverse
#without using extended Slicing and reverse()
# Ex-11
def readvals():
    n=int(input("Enter How Many Number of Elements:"))
    if(n<=0):
        return [] # returning empty list
    else:
        lst=[]
        for i in range(1,n+1):
            val=float(input("Enter {} Value:".format(i)))
            lst.append(val)
    return lst
def AmanReverse():
    vals=readvals()
    if (len(vals) == 0):
        print("List is Empty--Can't Reversse")
    else:
        print("Original List=", vals)
        l=0
        r=len(vals)-1
        while(l<r):
            vals[l],vals[r]=vals[r],vals[l]
            l=l+1
            r=r-1
        else:
            print("Reversed list is:",vals )

#Main program
AmanReverse()