#Program for Demonstrating Exceptrion Occurence
#DivEH8.py
try:
	print("Program Execution Started")
	a=input("\tEnter First Value:")  # 10
	b=input("\tEnter Second Value:") # 2
	x=int(a)  #  exception generated statement--ValueError
	y=int(b) #  exception generated statement--ValueError
	z=x/y  #  exception generated statement--ZeroDivisionError
	#New Statements
	s="PYTHON"
	print(s[12])
except Exception : # generic except block
	print("\tOOOOOOOPs Some thing went Wrong!!!")
else:
		print("-------------------else Block----------------------")
		print("\tFirst Value={}".format(x))
		print("\tSecond Value={}".format(y))
		print("\tDiv={}".format(z))
finally:
	print("-------------------finally Block----------------------")
	print("Program Execution Ended")

