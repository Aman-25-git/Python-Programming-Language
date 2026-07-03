#program for accepting a Number and Find Its Digits Sum
n=int(input("Enter how many values u want sum:"))
if(n<=0):
    print("invalid input")
else:
    s=0
    while(n>0):
        d=n%10
        s=s+d
        n=n//10
    else:
        print("Sum_digits are:{}".format(s))