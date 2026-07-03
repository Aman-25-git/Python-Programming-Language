#Program for Finding the Sum of N Natural Nums
#Ex-8
n=int(input("Enter How Many Natual Number Sum u want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    s=0
    # Here s is Called Additive Identity--It is used for accumulating sum of Currently generated values by the Loop
    i=1
    while i<=n:
        print("\t{}".format(i))
        s=s+i
        i=i+1
    else:
        print("Sum=",s)
