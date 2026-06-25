#program to find the absolute value of a number using the if..else operator.
#Ex-10       absolute value of a number is always positive or zero
a=float(input("Enter a value:"))

res= a*-1 if a<=0  else a

print("Absolute value of {} is {}".format(a,res))