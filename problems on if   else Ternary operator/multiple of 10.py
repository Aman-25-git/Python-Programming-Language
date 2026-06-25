#program to check whether a given number is a multiple of 10 using the if..else operator.
#Ex-25
a=int(input("Enter the number:"))

res="Multiple of 10" if a%10==0 else "Not Multiple of 10"

print("Entered number is {} that is {}".format(a,res))