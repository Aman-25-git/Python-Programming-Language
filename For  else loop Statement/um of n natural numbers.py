#program for Finding sum of N Natural Nums
n=int(input("Enter how many values u want sum:"))
if(n<=0):
    print("invalid input")
else:
    print("-" * 50)
    print("Sum of First {} Natural Nums".format(n))
    print("-" * 50)
    s=0
    for i in range(1,n+1):
        s=s+i
    else:
        print("sum of n natural numbers are:{}".format(s))