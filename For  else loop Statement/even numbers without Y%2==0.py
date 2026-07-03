#Program to print  Even Numbers from 1 to N by using For..else loop and without using y%2==0
#Ex-4
n=int(input("Enter a Number to Print Even numbers:"))
if(n<=0):
    print("*" * 50)
    print("Entered Number is invalid --try again")
    print("*" * 50)
else:
    print("*"*50)
    print("The Even Numbers from 2 TO {} are below".format(n))
    print("*"*50)
    for y in range(2,n+1,2):
        print("\t{}".format(y))
        y=y+2
    else:
        print("*"*50)
print("Program Execution Is Completed  \n\t\t\t\t\t--Thankyou For Using This Program")
print("*"*50)