#program on Arithmetic operators using multi line assignment
a=float(input("Enter a value of a:"))
b=float(input("Enter a value of b:"))
ap,sp,mp,dp,fdp,mdp,pp=a+b,a-b,a*b,a/b,a//b,a%b,a**b
print("Sum({},{})={}".format(a,b,ap))
print("Difference({},{})={}".format(a,b,sp))
print("Product({},{})={}".format(a,b,mp))
print("Division({},{})={}".format(a,b,dp))
print("FloorDivision({},{})={}".format(a,b,fdp))
print("Modulodiv({},{})={}".format(a,b,mdp))
print("Pow({},{})={}".format(a,b,pp))