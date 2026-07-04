#program to implement given number is prime or not a prime number
#Ex-5
n=int(input("Enter any number:"))
if(n<=1):
    print("{} is Invalid Input".format(n))# prime starts form 2
else:
    res=True
    for i in range(2,n):
        if(n%i==0):
            res=False
            break
    if(res):
        print("{} is a Prime Number".format(n))
    else:
        print("{} is not a Prime Number".format(n))
