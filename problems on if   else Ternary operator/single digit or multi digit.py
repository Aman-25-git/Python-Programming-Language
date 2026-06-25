#program to determine whether a number is a single-digit number or a multi-digit number using the if..else operator.
#Ex-18
a=(input("Enter Numeric value:"))

res="Sigle-Digit Number" if len(a)==1 else "Multi-Digit Number"

print("Entered number is {} that is {}".format(a,res))