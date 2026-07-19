#program to define KeywordvariableLengthArgs
#Ex-3
def info(sno,sname,mm,em,cname): # Function Def-1
	print(sno,sname,mm,em,cname)
info(sno=10,sname="RS",mm=56,em=70,cname="PSF") # Function Call-1 with 5 Keyword Arguments
def info(tno,tname,sub1,sub2):  # Function Def-2
	print(tno,tname,sub1,sub2)
info(tno=100,tname="TR",sub1="PYTHON",sub2="Numpy")# Function Call-2 with 4 Keyword Arguments
def info(cid,cname,hb):  # Function Def-3
	print(cid,cname,hb)
info(cid=1000,cname="JH",hb="Drawing") # Function Call-3 with 3 Keyword Arguments

#Limitation:
#If we have 1000 Similar Function Calls with Keyword Variable Length args then we must define 1000 Function Definitions
#Which is one of the Time Consuming Process.
#To Over this Process, we define ONE Function Definition, Irrespectriable Length argsive of  N-Similar Function Calls with
#Keyword Va by using the concept of  KEY WORD VARIABLE  LENGTH ARGUMENTS.