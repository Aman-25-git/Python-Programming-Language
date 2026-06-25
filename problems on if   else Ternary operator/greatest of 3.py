#program to find the largest of three numbers using nested if..else operators.
#Ex-9
a=float(input("Enter your first number: "))
b=float(input("Enter your second number: "))
c=float(input("Enter your third number: "))

res= a if a>=b and a>=c else b if b>a and b>=c else c if c>a and c>b else "Both are Equal" if (a,b,c)==(a,b,c) else c

print("Greastest of ({},{},{}):{}".format(a,b,c,res))