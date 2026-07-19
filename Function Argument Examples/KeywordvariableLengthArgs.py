#program to define KeywordvariableLengthArgs
#Ex-1
def info(sno,sname,mm,em,cname):
	print(sno,sname,mm,em,cname)
def einfo(tno,tname,sub1,sub2):
	print(tno,tname,sub1,sub2)
def cifo(cid,cname,hb):
	print(cid,cname,hb)
#Main Program
info(sno=10,sname="RS",mm=56,em=70,cname="PSF") # Function Call-1 with 5 Keyword Arguments
einfo(tno=100,tname="TR",sub1="PYTHON",sub2="Numpy")# Function Call-2 with 4 Keyword Arguments
cifo(cid=1000,cname="JH",hb="Drawing") # Function Call-3 with 3 Keyword Arguments


#In This we have Different Function Calls with Different Names and we have corresponding Different Function Def. so that Program will execute  Successfully. But Every Function Name is an Object and It takes Separate Memory Space.
#Here we have 3 Different Function Names and They take 3 Different Memory spaces. This is One of the Limitation
