#Program to Division of two numbers
#DivEH5.py
try:
	print("\t\tProgram Execution Started")
	a=input("Enter a value:")
	b=input("Enter b value:")
	x=int(a)#Exception generation stmt ValueError
	y=int(b)#Exception generation stmt ValueError
	z=x/y #Exception generation stmt ZeroDivisionError
except :
	print("Oops some thing went wrong!!!")
else:
	print("\tA value is {}".format(x))
	print("\tB value is {}".format(y))
	print("\tDiv({},{})={}".format(x,y,z))
finally:
	print("\t\tProgram Execution Completed")
