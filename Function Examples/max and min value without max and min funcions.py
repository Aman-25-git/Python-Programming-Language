#program on finding max,min value for list of vales and without using max() and min()
#Ex-8
def lst():
    n=int(input("Enter the how many values u want to enter into list: "))
    if(n<=0):
        return []
    else:
        lst=[]
        for val in range(1,n+1):
           i=float(input("Enter {} value to list:".format(val)))
           lst.append(i)
    return lst


def Findmax(lst):
    if(len(lst)==0):
        print("List is empty")
    else:
        val=lst[0]
        for i in lst[1:]:
            if i>val:
                val=i
        else:
            print("Max value is:",val)

def Findmin(lst):
    if (len(lst) == 0):
        print("List is empty")
    else:
        val = lst[0]
        for i in lst[1:]:
            if i < val:
                val = i
        else:
            print("Min value is:", val)

#main program
lsts=lst()
Findmax(lsts)
Findmin(lsts)