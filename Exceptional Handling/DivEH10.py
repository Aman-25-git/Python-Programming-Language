#Program for Demonstrating Exceptrion Occurence
#DivEH10.py
try:
	print("Program Execution Started")
	a=input("\tEnter First Value:")  # 10
	b=input("\tEnter Second Value:") # 2
	x=int(a)  #  exception generated statement--ValueError
	y=int(b) #  exception generated statement--ValueError
	z=x/y  #  exception generated statement--ZeroDivisionError
	#New Statements
	s="PYTHON"
	print(s[3])
except ZeroDivisionError,ValueError,IndexError:
	print("\tDON'T ENTER ZERO FOR DEN....")
	print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
	print("\tCHECK THE INDEX")
except Exception: #generic except block
	print("\tOOOOOOOPs Some thing went Wrong!!!")
else:
		print("-------------------else Block----------------------")
		print("\tFirst Value={}".format(x))
		print("\tSecond Value={}".format(y))
		print("\tDiv={}".format(z))
finally:
	print("-------------------finally Block----------------------")
	print("Program Execution Ended")
