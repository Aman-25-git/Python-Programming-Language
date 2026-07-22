#Program Showing The Insurance policy Yearly wise Bonus and Policy amount and Maturity Amount after 15 Years
#ClosureEx6.py
def  licpolicy(sumassured=500000): # Outer Function/Enclosing Function
	bonus=8 # # here bonus' is called Local Variable of licpolicy() and global to paypremium()--nonlocal variable
	def paypremium(yearno,pamt=25000):  # Inner Function--Closure---Enclosed Function
				nonlocal bonus
				totamtamt=sumassured+pamt+(sumassured*bonus/100)
				print("\t Year: {}  Sum Assured: {} Premium Amount:{}  Bonus:{} Totamt:{}".format(yearno,sumassured,pamt,bonus,totamtamt))
				bonus=bonus+1
	for i in range(1,16):
		paypremium(i)
#Main Program
licpolicy()
