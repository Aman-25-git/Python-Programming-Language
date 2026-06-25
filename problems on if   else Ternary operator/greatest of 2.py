#program on greatest of two numbers by if..else ternary operator in python
#Ex-1
a=float(input("Enter an Numerical value:"))
b=float(input("Enter another Numerical value:"))
res= a if a>b else b if b>a else "Both the values are equal"
print("Greatest of ({},{}):{}".format(a,b,res))
