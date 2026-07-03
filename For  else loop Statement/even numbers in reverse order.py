#Program to print  Even Numbers from N to 1 by using For..else loop and without using y%2==0 and that too in reverse order
#Ex-5
n=int(input("Enter a Number to Print Even numbers in reverse order:"))
if(n<=0):
    print("*" * 50)
    print("Entered Number is invalid --try again")
    print("*" * 50)
else:
    print("*"*50)
    print("The Even Numbers from {} TO 2 are below".format(n))
    print("*"*50)
    for i in range(2,n+1,2):
        print("\t{}".format(i))
    else:
        print("*"*50)
print("Program Execution Is Completed  \n\t\t\t\t\t--Thankyou For Using This Program")
print("*"*50)