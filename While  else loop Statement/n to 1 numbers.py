#Program to print N to 1 Natural numbers by using while..else loop
#Ex-2
n=int(input("Enter a Number to Print that many Natural numbers in Reverse order: "))
if(n<=0):
    print("*" * 50)
    print("Entered Number is invalid --try again")
    print("*" * 50)
else:
    print("*"*50)
    print("The Natural Numbers from {} TO 1 are below".format(n))
    print("*"*50)
    while(n>=1):
        print("\t{}".format(n))
        n=n-1
    else:
        print("*"*50)
print("Program Execution Is Completed  \n\t\t\t\t\t--Thankyou For Using This Program")
print("*"*50)