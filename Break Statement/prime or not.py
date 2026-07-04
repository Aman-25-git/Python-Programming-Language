#program to implement given number is prime or not a prime number
#Ex-4
n=int(input("Enter any number:"))
if(n<=1):
    print("{} is Invalid Input".format(n))# prime starts form 2
else:
    res="PRIME NUMBER"
    for i in range(2,n):
        if(n%i==0):
            res="NOT A PRIME NUMBER"
            break
    print("{} is {}".format(n,res))


