#Program for Demonstrating globals()
#In This Program we have Different Names for Local and Global Variables
#GlobalsFunEx1.py
a=10
b=20
c=30
d=40   # Here a,b,c,d are Called global variables
def  sums():
	x=100
	y=200
	z=300
	f=400  # Here x,y,z,k  are Called local variables
	res=x+y+z+f+a+b+c+d
	print("Result=",res)

#Main Program
sums()