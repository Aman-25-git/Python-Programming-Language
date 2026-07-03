#Program for Finding the Sum of N Natural Nums
#Ex-10
n=int(input("Enter How Many Natual Number Sum u want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    s=0
    # Here s is Called Additive Identity--It is used for accumulating sum of Currently generated values by the Loop
    for i in range(1,n+1):
        print("\t{}".format(i))
        s=s+i
    else:
        print("Sum=",s)
