#program to find the absolute difference between two numbers using the if..else operator.
#Ex-11       absolute value of a number is always positive or zero
a=float(input("Enter a value:"))
b=float(input("Enter b value:"))

res= (a-b)*-1 if (a-b)<0  else (a-b)

print("Absolute difference of {},{} is {}".format(a,b,res))