#Program for Demonstrating globals()
#In This Program we have Same Names for Local and Global Variables
#GlobalsFunEx1.py
a=10
b=20
c=30
d=40   # Here a,b,c,d are Called global variables
def  sums():
	a=100
	b=200
	c=300
	d=400  # Here x,y,z,k  are Called local variables
	res=a+b+c+d+globals()['a']+globals().get('b')+globals()['c']+globals()['d']
	print("Result=",res)

#Main Program
sums()