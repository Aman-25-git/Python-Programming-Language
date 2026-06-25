#program to check whether a number is positive or negative using the if..else operator.
#Ex-4 and 5
a=float(input("Enter any  Number:"))

res= "+ve number" if a>=1 else "ZERO is not a +ve or -ve" if a==0 else "-ve number"

print("Entered number is {} That is {}".format(a,res))

