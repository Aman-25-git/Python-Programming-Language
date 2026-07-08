#Program for accepting List of Numerical values
# and Get Separately + Vals and -VE VCals
#Ex-3
n=int(input("Enter How Many Numbers U want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=[] # Create an empty List
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
    else:
        print("List of values=",lst)# [10.0, -20.0, 30.0, -40.0, 50.0, -60.0]
        #Code for Getting +VE
        pslist=[] # create empty list
        for val in lst:
            if(val<=0):
                continue
            pslist.append(val)
        else:
            print("List of +VE Values=",pslist)
            # Code for Getting +VE
            nslist=[]
            for val in lst:
                if(val>=0):
                    continue
                nslist.append(val)
            else:
                print("List of -VE Values=",nslist)
 