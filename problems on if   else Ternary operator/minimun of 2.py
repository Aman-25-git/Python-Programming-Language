#program to find the minimum among two entered numbers using the if..else operator.
#Ex-24
a=float(input("Enter an Numerical value:"))
b=float(input("Enter another Numerical value:"))
res= a if a<b else b if b<a else "Both the values are equal"
print("Minimum of ({},{}):{}".format(a,b,res))
