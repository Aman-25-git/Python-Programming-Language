#Program for Demonstrating the Concept of Closure
#Ex-3
def grandparent(gpassets=100):#Outer Function
	print("Grand Parent Property={}".format(gpassets))
	def grandchild(gcp):  # inner function---Closure
		totprop=gpassets+gcp
		print("\tgrandchild()--Grand Parent Property:{}  Child Property:{}   totprop:{}".format(gpassets,gcp,totprop))
	for gcp in range(1000,1011):
		grandchild(gcp)


#Main Program
grandparent()