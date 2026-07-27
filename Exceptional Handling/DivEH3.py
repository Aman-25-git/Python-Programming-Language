#Program to Division of two numbers
#DivEH3.py
try:
	print("\t\tProgram Execution Started")
	a=input("Enter a value:")
	b=input("Enter b value:")
	x=int(a)#Exception generation stmt ValueError
	y=int(b)#Exception generation stmt ValueError
	z=x/y #Exception generation stmt ZeroDivisionError
except (ZeroDivisionError,ValueError):
	print("\t\tDon't Enter Zero's as Denominator")
	print("\t\tDon't Enter allnums,str,special symbols only digits are allowed!!!")

else:
	print("\tA value is {}".format(x))
	print("\tB value is {}".format(y))
	print("\tDiv({},{})={}".format(x,y,z))
finally:
	print("\t\tProgram Execution Completed")
