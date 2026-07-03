#program for Finding product of N Natural Nums
n=int(input("Enter how many values u want product:"))
if(n<=0):
    print("invalid input")
else:
    print("-" * 50)
    print("Product of First {} Natural Nums".format(n))
    print("-" * 50)
    p=1
    for i in range(1,n+1):
        p=p*i
    else:
        print("Product of n natural numbers are:{}".format(p))