#program on smallest of two numbers by if..else ternary operator in python
#Ex-2
a=float(input("Enter an Numerical value:"))
b=float(input("Enter another Numerical value:"))
res= a if a<b else b if b<a else "Both the values are equal"
print("Smallest of ({},{}):{}".format(a,b,res))
