#program to determine whether a temperature indicates a hot day or a cool day using the if..else operator.
#Ex-21
a=float(input("Enter temperature of day:"))

res= "HOT DAY" if a>=35 else "COOL DAY "

print("Entered Temperature  is {} degree That is {}".format(a,res))

