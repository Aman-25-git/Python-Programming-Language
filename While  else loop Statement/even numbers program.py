#Program to print  Even Numbers from 1 to N by using while..else loop
#Ex-3
n=int(input("Enter a Number to Print Even numbers:"))
if(n<=0):
    print("*" * 50)
    print("Entered Number is invalid --try again")
    print("*" * 50)
else:
    print("*"*50)
    print("The Even Numbers from 1 TO {} are below".format(n))
    print("*"*50)
    y=1
    while(n>=y):
        if(y%2==0):
            print("\t{}".format(y))
        y=y+1
    else:
        print("*"*50)
print("Program Execution Is Completed  \n\t\t\t\t\t--Thankyou For Using This Program")
print("*"*50)