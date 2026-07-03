#Program to print Multiplication table by using For..else loop
#Ex-6
n=int(input("Enter a Number to Print  Multiplication table:"))
if(n<=0):
    print("*" * 50)
    print("Entered Number is invalid --try again")
    print("*" * 50)
else:
    print("*"*50)
    print("The Multiplication table for {} is below".format(n))
    print("*"*50)
    for y in range(1,11):
        print("\t{} X {} = {}".format(n,y,n*y))

    else:
        print("*"*50)
print("Program Execution Is Completed  \n\t\t\t\t\t--Thankyou For Using This Program")
print("*"*50)