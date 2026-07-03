#program for accepting List of Values and Find  Max Element
n=int(input("Enter how many values want to enter in list:"))
if(n<=0):
    print("Enter valid number --tryagain")
else:
    lst=[]
    s=0
    for i in range(1,n+1):
        val=float(input("Enter {} value :".format(i)))
        s=s+i
        lst.append(val)
    else:

        print("List of values are:",lst)
        print("Sum of list is:",sum(lst))
        print("Avg of list is:",(sum(lst)/len(lst)))

        #our own code for sum
        print("List of values are:", lst)
        print("Sum of list is:",s)
        print("Avg of list is:", ( s / len(lst)))

        #code for max value
        maxi=lst[0]
        for i in lst[1:]:
            if i>maxi:
                maxi=i
        else:
            print("Maximum value is:",maxi)
        # code for min value home work
        mani = lst[0]
        for i in lst[1:]:
            if i < mani:
                mani = i
        else:
            print("Minimum value is:", mani)