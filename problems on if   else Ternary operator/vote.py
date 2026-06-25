#program to check whether a person is eligible to vote based on age using the if..else operator.
#Ex-6
a=float(input("ENTER U R AGE:"))

res= "U R Eligible" if a>=18   else "ZERO is not considered here give any +ve value" if a==0 else "U  R Not Eligible "

print("Entered Age is {} That is {}".format(a,res))

